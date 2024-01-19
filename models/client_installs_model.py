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
         WHERE cc.client_id = {client_id} AND is_to_mount = false
         GROUP BY mount.mount_id'''

    return pandas.read_sql(script, conn)


def get_client_installs(conn, client_id):
    # Получить все УСТАНОВКИ клиента
    return pandas.read_sql(
        f'''SELECT
        mount.mount_id, cb.brand_name || ' ' || cm.model_name || ' ' || cm.model_year as car, group_concat(d.name) as devices, b.address,
        w.schedule_date, w.work_hour, s.name as status
         FROM mount
         inner join work_schedule w on mount.schedule_id = w.schedule_id
         inner join box b on b.box_id = w.box_id
         inner join client_cars cc on cc.client_car_id = mount.client_car_id
         inner join car_models cm on cm.model_id = cc.model_id
         inner join car_brands cb on cb.brand_id = cm.brand_id
         inner join equipment e on mount.mount_id = e.mount_id
         inner join devices d on d.device_id = e.device_id
         inner join status s on s.status_id = mount.status_id
         WHERE cc.client_id = {client_id} AND is_to_mount = true
         GROUP BY mount.mount_id''', conn)
