import pandas


def get_boxes(conn):
    # Получить всех клиентов
    return pandas.read_sql(
        '''SELECT box_id, address FROM box''', conn)


def get_schedule(conn):
    return pandas.read_sql(
        '''SELECT 
            schedule_id, box_id, schedule_date, work_hour, is_free 
            FROM work_schedule
        ''', conn)


def get_schedule_box(conn, box_id):
    return pandas.read_sql(
        f'''SELECT 
            schedule_id, box_id, schedule_date, work_hour, is_free 
            FROM work_schedule
            Where box_id = {box_id}
        ''', conn)


def get_dates(conn):
    return pandas.read_sql(
        '''SELECT 
            distinct schedule_date 
            FROM work_schedule
        ''', conn)


def enroll_install(conn, time_id, client_id, equipment):
    cur = conn.cursor()
    sched_id = time_id['id']

    # ! В будущем запись осуществлять на указанную машину! !!!
    car_id = pandas.read_sql(
        f'''SELECT client_car_id 
        FROM client_cars 
        WHERE client_id ={client_id} LIMIT 1''', conn
    )

    car_id = int(car_id.loc[0, 'client_car_id'])
    # print(car_id)

    update_shed = f'''
        UPDATE work_schedule
        SET is_free = false
        WHERE schedule_id = {sched_id}
    '''
    cur.executescript(update_shed)
    conn.commit()

    insert_mount = '''
        INSERT INTO
        mount(client_car_id, schedule_id, status_id)
        values(:client_car_id, :schedule_id, :status_id)
    '''
    cur.execute(insert_mount,
                {'client_car_id': car_id,
                 'schedule_id': time_id['id'],
                 'status_id': 1})
    conn.commit()

    mount_id = cur.lastrowid
    insert_equip = '''
        INSERT INTO
        equipment(device_id, mount_id, quantity,is_to_mount)
        values(:device_id, :mount_id, :quantity, :is_to_mount)
    '''

    for equip in equipment:
        cur.execute(insert_equip,
                    {'device_id': equip['Артикул'],
                     'mount_id': mount_id,
                     'quantity': equip['Количество'],
                     'is_to_mount': 1})

    conn.commit()
    cur.close()
