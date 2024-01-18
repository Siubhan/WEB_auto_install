import pandas


def get_all_sales(conn):
    return pandas.read_sql(
        '''SELECT 
        mount_id, model_name || ' ' || model_year as car, address,
        date_mount, time_mount, s.name 
         FROM mount
         inner join client_cars cc on cc.client_car_id = mount.client_car_id
         inner join car_models cm on cm.model_id = cc.model_id
         inner join work_schedule ws on ws.schedule_id = mount.schedule_id
         inner join box b on b.box_id = ws.box_id
         inner join status s on s.status_id = mount.status_id
         WHERE mount.status_id = 4''', conn)


def get_all_statuses(conn):
    return pandas.read_sql(
        '''SELECT status_id,name 
         FROM status
         WHERE status_id > 3''', conn)
