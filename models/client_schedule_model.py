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
