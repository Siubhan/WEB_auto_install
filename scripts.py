# два запроса на выборку для связанных таблиц с условиями и сортировкой;
# два запроса с группировкой и групповыми функциями;
# два запроса со вложенными запросами или табличными выражениями;
# два запроса корректировки данных (обновление, добавление, удаление и пр)

select_1 = '''
    SELECT fullname, phone, cb.brand_name, cm.model_name 
    FROM client 
    inner join client_cars using(client_id)
    inner join car_models cm on client_cars.model_id = cm.model_id
    inner join car_brands cb on cb.brand_id = cm.brand_id
    WHERE fullname LIKE '%ва%' order by fullname DESC;
'''

select_2 = '''
    SELECT brand_name || ' ' || model_name AS car, model_year
    FROM car_models 
    inner join car_brands using(brand_id)
    WHERE model_year between 2015 and 2020;
'''

group_1 = '''
    SELECT count(*) as count_cars, brand_name || ' ' || model_name AS car
    FROM client_cars 
    inner join car_models cm on client_cars.model_id = cm.model_id
    inner join car_brands cb on cb.brand_id = cm.brand_id
    GROUP BY client_cars.model_id;
'''

group_2 = '''
    SELECT type_device.name as type_device, round(avg(price+type_device.price_mount),2) AS average_price
    FROM devices 
    inner join type_device on devices.type_id = type_device.type_id
    GROUP BY type_device.name; 
'''

complex_1 = '''
    WITH 
      cars AS
        (SELECT 
        c.fullname || ' ' || c.phone as owner, 
        group_concat(brand_name || ' ' || model_name || ' ' ||  model_year) as car, 
        count(client_car_id) as quantity
        FROM client_cars
        inner join car_models cm on client_cars.model_id = cm.model_id
        inner join client c on client_cars.client_id = c.client_id 
        inner join car_brands cb on cb.brand_id = cm.brand_id
        group by client_cars.client_id)
    SELECT * FROM cars where quantity > 1;
'''

complex_2 = '''
    WITH 
      rests AS
        (SELECT 
        devices.name,  
        availble,
        td.name as type
        FROM devices
        inner join type_device td on td.type_id = devices.type_id)
    SELECT * FROM rests where availble < 10 and type like '%ер';
'''

edit_1 = '''
    UPDATE client SET discount = 15 where is_partner = 1;
'''

edit_3 = '''
    UPDATE devices SET price = price * 10 where device_id > 25;
'''

edit_2 = '''
INSERT INTO car_models (brand_id, model_name, model_year) VALUES    
    (1, 'Model X', 2015),
    (1, 'Model S', 2014),
    (2, 'Camry', 2016),
    (2, 'Corolla', 2017),
    (3, 'F-150', 2018),
    (3, 'Escape', 2019),
    (4, 'Civic', 2020),
    (4, 'CR-V', 2020),
    (5, 'X5', 2018),
    (5, '3 Series', 2019),
    (6, '911', 2020),
    (6, 'Cayenne', 2020),
    (7, 'A3', 2016),
    (7, 'Q5', 2017),
    (8, 'Altima', 2018),
    (8, 'Rogue', 2019),
    (9, 'E-Class', 2020),
    (9, 'GLC', 2020),
    (10, 'Golf', 2016),
    (10, 'Tiguan', 2017),
    (11, 'Panamera', 2018),
    (11, 'Macan', 2019),
    (12, 'CX-5', 2020),
    (12, 'Mazda3', 2020),
    (13, 'Outback', 2016),
    (13, 'Impreza', 2017),
    (14, 'Optima', 2018),
    (14, 'Soul', 2019),
    (15, 'Elantra', 2020),
    (15, 'Santa Fe', 2020),
    (16, 'RX', 2016),
    (16, 'IS', 2017),
    (17, 'TLX', 2018),
    (17, 'RDX', 2019),
    (18, 'QX50', 2020),
    (18, 'Q60', 2020),
    (19, 'F-Type', 2016),
    (19, 'XF', 2017),
    (20, 'Discovery Sport', 2018),
    (20, 'Range Rover Evoque', 2019);
'''
