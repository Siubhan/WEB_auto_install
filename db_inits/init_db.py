init_db = '''
    DROP TABLE IF EXISTS client;
    CREATE TABLE client(
        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname VARCHAR(100),
        phone VARCHAR(11) UNIQUE,
        is_partner boolean,
        discount INTEGER DEFAULT 0
    );
    
    DROP TABLE IF EXISTS client_cars;
    CREATE TABLE client_cars(
        client_car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        model_id INTEGER,
        FOREIGN KEY (client_id)  REFERENCES client(client_id) ON DELETE CASCADE,
        FOREIGN KEY (model_id)  REFERENCES car_models(model_id) ON DELETE CASCADE        
    );
        
    DROP TABLE IF EXISTS car_brands;
    CREATE TABLE car_brands(
        brand_id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand_name VARCHAR(100)
        );
    
    DROP TABLE IF EXISTS car_models;
    CREATE TABLE car_models(
        model_id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand_id INTEGER,
        model_name VARCHAR(100),
        model_year INTEGER,
        FOREIGN KEY (brand_id)  REFERENCES car_brands(brand_id) ON DELETE CASCADE
    );
    
    DROP TABLE IF EXISTS specialist;
    CREATE TABLE specialist(
        specialist_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname VARCHAR(100),
        phone VARCHAR(11) UNIQUE
    );
    
    DROP TABLE IF EXISTS box;
    CREATE TABLE box(
        box_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        specialist_id INTEGER,
        address VARCHAR(150),
        FOREIGN KEY (specialist_id)  REFERENCES specialist(specialist_id) ON DELETE CASCADE
    );
    
    DROP TABLE IF EXISTS type_device;
    CREATE TABLE type_device(
        type_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100),
        price_mount DECIMAL(9,2)
    );
    
    DROP TABLE IF EXISTS devices;
    CREATE TABLE devices(
        device_id INTEGER PRIMARY KEY AUTOINCREMENT,
        type_id INTEGER,
        name VARCHAR(100),
        price DECIMAL(9,2),
        availble INTEGER,
        producer VARCHAR(30),
        FOREIGN KEY (type_id)  REFERENCES type_device(type_id) ON DELETE CASCADE
    );
    
    DROP TABLE IF EXISTS equipment;
    CREATE TABLE equipment(
        equipment_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        device_id INTEGER,
        mount_id INTEGER,
        serial_number VARCHAR(60) UNIQUE,
        is_to_mount boolean,
        FOREIGN KEY (device_id)  REFERENCES devices(device_id) ON DELETE CASCADE,
        FOREIGN KEY (mount_id)  REFERENCES mount(mount_id) ON DELETE CASCADE
    );

    DROP TABLE IF EXISTS status;
    CREATE TABLE status(
        status_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR(80)
    );
    
    DROP TABLE IF EXISTS history_mount;
    CREATE TABLE history_mount(
        history_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        mount_id INTEGER,
        status_id INTEGER,
        time_update TIME,
        FOREIGN KEY (mount_id)  REFERENCES mount(mount_id) ON DELETE CASCADE
    );
    
    DROP TABLE IF EXISTS mount;
    CREATE TABLE mount(
        mount_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        client_car_id INTEGER,
        schedule_id INT,
        time_mount TIME,
        date_mount TIME,
        status_id INTEGER,
        FOREIGN KEY (status_id) REFERENCES status(status_id) ON DELETE CASCADE,
        FOREIGN KEY (schedule_id)  REFERENCES work_schedule(schedule_id) ON DELETE CASCADE,
        FOREIGN KEY (client_car_id)  REFERENCES client_cars(client_car_id) ON DELETE CASCADE
    );
    
    DROP TABLE IF EXISTS work_schedule;
    CREATE TABLE work_schedule(
    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    box_id INTEGER,
    date_mount DATE,
    hour_work_from INTEGER,
    hour_work_to INTEGER,
    FOREIGN KEY (box_id)  REFERENCES box(box_id) ON DELETE CASCADE
    );
'''
