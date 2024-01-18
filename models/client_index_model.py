import pandas


def get_clients(conn):
    # Получить всех клиентов
    return pandas.read_sql(
        '''SELECT * FROM client''', conn)


def get_catalog(conn):
    # Получить каталог
    return pandas.read_sql(
        '''SELECT 
        device_id, td.name, devices.name, price, availble, producer, price_mount 
        FROM devices inner join type_device td on td.type_id = devices.type_id
        ''', conn)


def get_products(conn, item):
    # Получить похожие
    return pandas.read_sql(
        '''SELECT 
        device_id, td.name, devices.name, price, availble, producer, price_mount 
        FROM devices inner join type_device td on td.type_id = devices.type_id
        where lower(devices.name) like :item''', conn, params={"item": "%" + item.lower() + "%"})


def get_filtred(conn, prod, prod_type):
    if not prod:
        script = f'''SELECT 
        device_id, td.name, devices.name, price, availble, producer, price_mount 
        FROM devices inner join type_device td on td.type_id = devices.type_id
        where td.name {prod_type}'''
    elif not prod_type:
        script = f'''SELECT 
        device_id, td.name, devices.name, price, availble, producer, price_mount 
        FROM devices inner join type_device td on td.type_id = devices.type_id
        where producer {prod}'''
    else:
        script = f'''SELECT 
                device_id, td.name, devices.name, price, availble, producer, price_mount 
                FROM devices inner join type_device td on td.type_id = devices.type_id
                where td.name {prod_type} and producer {prod}'''
    # Получить фильтрованные
    return pandas.read_sql(
        script,
        conn)


def get_filters_producer(conn):
    # Получить список производителей
    return pandas.read_sql(
        '''SELECT distinct producer FROM devices
        ''', conn
    )


def get_filters_type(conn):
    # Получить список типов устройств
    return pandas.read_sql(
        '''SELECT name FROM type_device
        ''', conn
    )


def create_new_client(conn, name, phone, partner):
    # Добавить нового клиента
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO client(fullname, phone, is_partner)
        VALUES (:fullname, :phone, :is_partner)
    """, {"fullname": name, "phone": phone, "is_partner": partner})

    conn.commit()

    return cur.lastrowid


def insert_systems(conn, client_id, systems):
    cur = conn.cursor()
    # from datetime import datetime
    # cur_date = datetime.now().strftime('%d.%m.%Y')

    car_id = pandas.read_sql(
        f'''SELECT client_car_id 
        FROM client_cars 
        WHERE client_id ={client_id} LIMIT 1''', conn
    )

    car_id = car_id.loc[0, 'client_car_id']

    cur.execute(f"""
        INSERT INTO mount(status_id,client_car_id)
        VALUES (2,{car_id})
    """)

    mount_id = cur.lastrowid

    conn.commit()
    for car_system in systems:
        cur.execute(f"""
            INSERT INTO equipment(device_id, quantity, mount_id, is_to_mount)
            VALUES ({car_system['Артикул']},{car_system['Количество']},{mount_id},{0})
        """)
        conn.commit()
