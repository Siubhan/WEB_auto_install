init_db = '''
    DROP TABLE IF EXISTS client;
    CREATE TABLE client(
        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname VARCHAR(100),
        phone VARCHAR(11) UNIQUE,
        is_partner boolean,
        discount INTEGER DEFAULT 0
    );
    
    DROP TABLE IF EXISTS specialist;
    CREATE TABLE specialist(
        specialist_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname VARCHAR(100),
        phone VARCHAR(11) UNIQUE,
        price_mount DECIMAL(9,2)
    );
    
    DROP TABLE IF EXISTS devices;
    CREATE TABLE devices(
        device_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100),
        price DECIMAL(9,2),
        availble INTEGER,
        producer VARCHAR(30)
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
    
    DROP TABLE IF EXISTS mount;
    CREATE TABLE mount(
        mount_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        specialist_id INTEGER,
        client_id INTEGER,
        date_mount DATE,
        time_mount TIME,
        FOREIGN KEY (specialist_id, date_mount, time_mount)  REFERENCES spec_schedule(specialist_id, date_mount, time_mount) ON DELETE CASCADE,
        FOREIGN KEY (client_id)  REFERENCES client(client_id) ON DELETE CASCADE
    );
    
    DROP TABLE IF EXISTS spec_schedule;
    CREATE TABLE spec_schedule(
    specialist_id INTEGER,
    date_mount DATE,
    time_mount TIME,
    is_free BOOLEAN,
    CONSTRAINT PK_SCHEDULE PRIMARY KEY (specialist_id, date_mount, time_mount),
    FOREIGN KEY (specialist_id)  REFERENCES specialist(specialist_id) ON DELETE CASCADE
    );
'''
