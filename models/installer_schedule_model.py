import pandas
from datetime import datetime, timedelta
from time import strftime


def get_all_sales(conn):
    return pandas.read_sql(
        '''SELECT 
        c.fullname, c.phone,
        mount_id, model_name || ' ' || model_year as car, address,
        date_mount, time_mount, s.name 
         FROM mount
         inner join client_cars cc on cc.client_car_id = mount.client_car_id
         inner join car_models cm on cm.model_id = cc.model_id
         inner join work_schedule ws on ws.schedule_id = mount.schedule_id
         inner join box b on b.box_id = ws.box_id
         inner join status s on s.status_id = mount.status_id
         inner join client c on c.client_id = cc.client_id
         WHERE mount.status_id = 4''', conn)


def get_all_statuses(conn):
    return pandas.read_sql(
        '''SELECT status_id,name 
         FROM status
         WHERE status_id > 3''', conn)


def create_schedule(conn):
    select_boxes = '''
        SELECT box_id
        FROM box
    '''

    df_boxes = pandas.read_sql(select_boxes, conn)

    insert_work = '''
        INSERT INTO 
        work_schedule(box_id, schedule_date, work_hour) 
        VALUES (:box,:sch_date,:work_hour)
    '''

    now = datetime.now()
    monday = now - timedelta(days=now.weekday())
    saturday = datetime.date(monday + timedelta(days=5))
    monday = datetime.date(monday)

    cur = conn.cursor()
    # cur.execute('''Delete from work_schedule''')

    for index, row in df_boxes.iterrows():
        while monday < saturday:
            for work_time in range(10, 18):
                cur.execute(insert_work,
                            {'box': int(row['box_id']),
                             'sch_date': monday,
                             'work_hour': strftime(str(work_time) + ':00')})
            monday = monday + timedelta(days=1)
        monday = now - timedelta(days=now.weekday())
        monday = datetime.date(monday)

    conn.commit()
    cur.close()



def init_schedule(conn):
    # 0 - mon, 1 - tue, 2 - wen, 3 - thur ...
    if datetime.today().weekday() == 6:
        create_schedule(conn)


def edit_schedule(conn):
    cur = conn.cursor()

    update_work = f'''
        UPDATE work_schedule
        SET is_free = false 
        WHERE DATE(schedule_date) < DATE('now')
    '''

    cur.executescript(update_work)

    conn.commit()
    cur.close()
