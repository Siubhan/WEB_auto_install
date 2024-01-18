import pandas


def get_client_purcases(conn, client_id):
    # Получить все ПОКУПКИ клиента
    script = f'''SELECT 
        mount.mount_id, 
        group_concat(d.name || ' - ' ||e.quantity || 'шт.', '; ')  as devices, 
        s.name as status
         FROM mount
         inner join client_cars cc on mount.client_car_id = cc.client_car_id
         inner join equipment e on mount.mount_id = e.mount_id
         inner join devices d on d.device_id = e.device_id
         inner join status s on s.status_id = mount.status_id
         WHERE cc.client_id = {client_id}
         GROUP BY mount.mount_id'''

    return pandas.read_sql(script, conn)


def get_client_installs(conn, client_id):
    # Получить все УСТАНОВКИ клиента
    return pandas.read_sql(
        f'''SELECT
        mount.mount_id, model_name || ' ' || model_year as car, group_concat(d.name) as devices, address,
        date_mount, time_mount, s.name as status
         FROM mount
         inner join client_cars cc on cc.client_car_id = mount.client_car_id
         inner join car_models cm on cm.model_id = cc.model_id
         inner join work_schedule ws on ws.schedule_id = mount.schedule_id
         inner join equipment e on mount.mount_id = e.mount_id
         inner join devices d on d.device_id = e.device_id
         inner join box b on b.box_id = ws.box_id
         inner join status s on s.status_id = mount.status_id
         WHERE cc.client_id = {client_id}
         GROUP BY mount.mount_id''', conn)
