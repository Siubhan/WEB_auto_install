fill_script = '''
    INSERT INTO client(fullname, phone, is_partner)  VALUES
    ('Иванов М.С.', '79990000000', true),
    ('Петров Ф.С.', '79990000001', false),
    ('Федоров П.Р.', '79990000002', false),
    ('Абрамова А.А.', '79990000003', true),
    ('Самарин С.С.', '79990000004', false),
    
    ('Туполев И.Д.', '79990000005', false),
    ('Баранов П.В.', '79990000006', false),
    ('Шевцова А.Р.', '79990000007', true),
    ('Белых К.Д.', '79990000008', false),
    ('Садиев С.И.', '79990000009', false),
    
    ('Астахов И.И.', '79990000010', false),
    ('Борисов В.В.', '79990000011', true),
    ('Тощаков П.С.', '79990000012', false),
    ('Солиева К.П.', '79990000013', true),
    ('Левченко А.Г.', '79990000014', false),
    
    ('Хованец Г.П.', '79990000015', false),
    ('Тихомиров Т.М.', '79990000016', false),
    ('Дворников М.А.', '79990000017', false),
    ('Жидкова Р.Л.', '79990000018', false),
    ('Бондаренко С.С.', '79990000019', false),
    
    ('Кошар А.В.', '79990000020', false),
    ('Маликов И.И.', '79140000004', false),
    ('Серый И.И.', '79140000005', false),
    ('Ольха И.И.', '79140000006', false),
    ('Валец И.И.', '79140000007', false),
    
    ('Кот И.И.', '79140000008', false),
    ('Прим И.И.', '79140000009', false),
    ('Левин И.И.', '79140000010', false),
    ('Косарь И.И.', '79140000011', false),
    ('Лык И.И.', '79140000012', false),
    
    ('Филер И.И.', '79140000013', true),
    ('Тур И.И.', '79140000014', false),
    ('Пак И.И.', '79140000015', false),
    ('Янов И.И.', '79140000016', false),
    ('Лесник И.И.', '79140000017', true),
    
    ('Остырь И.И.', '79140000018', false),
    ('Януш И.И.', '79140000019', false),
    ('Остырь И.И.', '79140000099', false),
    ('Кек И.И.', '79140000022', false),
    ('Чоба И.И.', '79140000024', false),
    
    ('Свак И.И.', '79140000025', false),
    ('Фролов И.И.', '79140000026', false),
    ('Остов И.И.', '79140000035', false),
    ('Права И.И.', '79140000053', false),
    ('Лева И.И.', '79140000043', false);
    
    INSERT INTO specialist(fullname, phone)  VALUES
    ('Иванов И.И.', '79140000000'),
    ('Симонов И.И.', '79140000001');
    
    INSERT INTO box(specialist_id, address)  VALUES
    (1, 'г. Владивосток, ул. -'),
    (2, 'г. Находка, ул. -');
    
    INSERT INTO type_device(name, price_mount) VALUES 
    ('Автосигнализация', 1000),
    ('Иммобилайзер', 1000),
    ('GPS трекер', 1200),
    ('Парковочный радар', 1500),
    ('Видеорегистратор', 500),
    ('Доводчики дверей', 2000),
    ('Камера', 700),
    ('Прочее', 1000);
    
    INSERT INTO devices(name, price, availble, producer, type_id)  VALUES
    ('Автосигнализация EUROSEC GN7C', 12000, 300,'Литва',1),
    ('Иммобилайзер Skybrake DD5 5211', 7000, 100,'Литва',1),
    ('Иммобилайзер Skybrake DD5 (5201)', 9000, 50,'Литва',1),
    ('Иммобилайзер Skybrake DD5 Bike', 9500, 20,'Литва',1),
    ('Автосигнализация EUROSEC GN7C.HUPS', 10000, 210,'Литва',1),
    
    ('Автосигнализация EUROSEC GSW-CAN_GP', 9500, 70,'Литва',1),
    ('Автосигнализация GN8', 15000, 90,'Литва',1),
    ('Иммобилайзер IMB5', 7000, 15,'Литва',2),
    ('GPS-трекер DSF10', 7500, 20,'Литва',3),
    ('GPS-трекер DSF22', 8000, 25,'Литва',3),
    
    ('GPS-маяк DSM4', 8500, 30,'Литва',3),
    ('Парковочный радар HPS-4083', 10500, 15,'Литва',4),
    ('Парковочный радар HPS-4073', 10300, 20,'Литва',4),
    ('Парковочный радар HPS-4003', 10100, 21,'Литва',4),
    ('OBD BLOCK', 10500, 10,'Россия',8),
    
    ('CONTOUR', 11500, 15,'Россия',8),
    ('KEYLESS BLOCK', 10000, 20,'Россия',8),
    ('CANREADER2', 10000, 30,'Литва',8),
    ('IGLA 251', 16000, 35,'Россия',2),
    ('IGLA 231', 14000, 40,'Россия',2),
    
    ('IGLA 220', 13000, 45,'Россия',2),
    ('IGLA 200', 12000, 50,'Россия',2),
    ('IGLA 240', 15000, 40,'Россия',2),
    ('IGLA 271', 17000, 35,'Россия',2),
    ('IGLA 281', 18000, 35,'Россия',2);
    
    INSERT INTO devices(type_id, name, price, availble, producer)  VALUES
    (1, 'Pandora DXL 3970', 1200.50, 10, 'Россия'),
    (2, 'StarLine A93', 950.75, 15, 'Россия'),
    (3, 'GPS Tracker TK103', 1300.00, 8, 'Китай'),
    (4, 'Steel Mate PTS400M7', 1800.25, 5, 'Китай'),
    (5, 'BlackVue DR900S-2CH', 600.90, 20, 'Южная Корея'),
    (6, 'Soft-Top Comfort', 2500.00, 3, 'Германия'),
    (7, 'Xiaomi 70mai Dash Cam Pro', 850.30, 12, 'Китай'),
    (8, 'Thinkware Q800 Pro', 1100.50, 18, 'Южная Корея'),
    (1, 'Sher-Khan Logicar 5', 1050.25, 7, 'Россия'),
    (2, 'Pandect IS-750', 1400.75, 14, 'Россия'),

    (3, 'Coban GPS303-F', 1600.00, 10, 'Китай'),
    (4, 'Steel Mate PTS800EX', 2000.25, 5, 'Китай'),
    (5, 'BlackVue DR750S-2CH', 700.90, 20, 'Южная Корея'),
    (6, 'Soft-Top Comfort Plus', 2800.00, 3, 'Германия'),
    (7, 'Xiaomi 70mai A800', 950.30, 12, 'Китай'),
    (8, 'Thinkware U1000', 1200.50, 18, 'Южная Корея'),
    (1, 'Sher-Khan Magicar 7', 1000.25, 7, 'Россия'),
    (2, 'Pandect IS-770', 1300.75, 14, 'Россия'),
    (3, 'Coban GPS303-G', 1400.00, 10, 'Китай'),
    (4, 'Steel Mate PTS810EX', 1900.25, 5, 'Китай'),

    (5, 'BlackVue DR590W-2CH', 650.90, 20, 'Южная Корея'),
    (6, 'Soft-Top Comfort Pro', 2600.00, 3, 'Германия'),
    (7, 'Xiaomi 70mai A500', 900.30, 12, 'Китай'),
    (8, 'Thinkware F800 Pro', 1150.50, 18, 'Южная Корея'),
    (1, 'Sher-Khan Magicar 8', 1100.25, 7, 'Россия'),
    (2, 'Pandect IS-780', 1500.75, 14, 'Россия'),
    (3, 'Coban GPS306', 1700.00, 10, 'Китай'),
    (4, 'Steel Mate PTS820EX', 2200.25, 5, 'Китай'),

    (5, 'BlackVue DR900X-2CH', 750.90, 20, 'Южная Корея'),
    (6, 'Soft-Top Comfort Ultra', 3000.00, 3, 'Германия'),
    (7, 'Xiaomi 70mai A300', 1000.30, 12, 'Китай'),
    (8, 'Thinkware M1', 1250.50, 18, 'Южная Корея'),
    (1, 'Sher-Khan Magicar 9', 1200.25, 7, 'Россия'),
    (2, 'Pandect IS-790', 1600.75, 14, 'Россия'),
    (3, 'Coban GPS304-B', 1800.00, 10, 'Китай'),
    (4, 'Steel Mate PTS830EX', 2300.25, 5, 'Китай'),
    (5, 'BlackVue DR750-2CH LTE', 800.90, 20, 'Южная Корея'),
    (6, 'Soft-Top Comfort Elite', 3200.00, 3, 'Германия'),
    
    (7, 'Xiaomi 70mai A400', 1050.30, 12, 'Китай'),
    (8, 'Thinkware QX800', 1300.50, 18, 'Южная Корея'),
    (1, 'Sher-Khan Magicar 10', 1250.25, 7, 'Россия'),
    (2, 'Pandect IS-800', 1700.75, 14, 'Россия'),
    (3, 'Coban GPS305', 1900.00, 10, 'Китай'),
    (4, 'Steel Mate PTS840EX', 2400.25, 5, 'Китай'),
    (5, 'BlackVue DR590-2CH', 850.90, 20, 'Южная Корея'),
    (6, 'Soft-Top Premium', 3500.00, 3, 'Германия'),
    (7, 'Xiaomi 70mai A600', 1100.30, 12, 'Китай'),
    
    (8, 'Thinkware F200', 1350.50, 18, 'Южная Корея'),
    (1, 'Sher-Khan Magicar 11', 1300.25, 7, 'Россия'),
    (2, 'Pandect IS-810', 1800.75, 14, 'Россия'),
    (3, 'Coban GPS307', 2000.00, 10, 'Китай'),
    (4, 'Steel Mate PTS850EX', 2500.25, 5, 'Китай'),
    (5, 'BlackVue DR750X-2CH', 900.90, 20, 'Южная Корея'),
    (6, 'Soft-Top Supreme', 3800.00, 3, 'Германия'),
    (7, 'Xiaomi 70mai A700', 1150.30, 12, 'Китай'),
    (8, 'Thinkware F100', 1400.50, 18, 'Южная Корея'),
    (1, 'Sher-Khan Magicar 12', 1350.25, 7, 'Россия'),
    
    (2, 'Pandect IS-820', 1900.75, 14, 'Россия'),
    (3, 'Coban GPS308', 2100.00, 10, 'Китай'),
    (4, 'Steel Mate PTS860EX', 2600.25, 5, 'Китай'),
    (5, 'BlackVue DR750-1CH', 950.90, 20, 'Южная Корея'),
    (6, 'Soft-Top Master', 4000.00, 3, 'Германия'),
    (7, 'Xiaomi 70mai A800S', 1200.30, 12, 'Китай'),
    (8, 'Thinkware F70', 1450.50, 18, 'Южная Корея'),
    (1, 'Sher-Khan Magicar 13', 1400.25, 7, 'Россия'),
    (2, 'Pandect IS-830', 2000.75, 14, 'Россия'),
    (3, 'Coban GPS309', 2200.00, 10, 'Китай'),
    
    (4, 'Steel Mate PTS870EX', 2700.25, 5, 'Китай'),
    (5, 'BlackVue DR590-1CH', 1000.90, 20, 'Южная Корея'),
    (6, 'Soft-Top Classic', 4200.00, 3, 'Германия'),
    (7, 'Xiaomi 70mai A900', 1250.30, 12, 'Китай'),
    (8, 'Thinkware F50', 1500.50, 18, 'Южная Корея'),
    (1, 'Sher-Khan Magicar 14', 1450.25, 7, 'Россия'),
    (2, 'Pandect IS-840', 2100.75, 14, 'Россия'),
    (3, 'Coban GPS310', 2300.00, 10, 'Китай'),
    (4, 'Steel Mate PTS880EX', 2800.25, 5, 'Китай'),
    (5, 'BlackVue DR900-1CH', 1050.90, 20, 'Южная Корея');
    
    INSERT INTO status(name) VALUES 
    ('Записан'),
    ('Принят в работу'),
    ('Выполнен');
'''

fill_cars = '''
INSERT INTO car_brands (brand_name) VALUES
    ('Tesla'),
    ('Toyota'),
    ('Ford'),
    ('Honda'),
    ('BMW'),
    ('Chevrolet'),
    ('Audi'),
    ('Nissan'),
    ('Mercedes-Benz'),
    ('Volkswagen'),
    ('Porsche'),
    ('Mazda'),
    ('Subaru'),
    ('Kia'),
    ('Hyundai'),
    ('Lexus'),
    ('Acura'),
    ('Infiniti'),
    ('Jaguar'),
    ('Land Rover');
-- Add more brands as needed;

INSERT INTO car_models (brand_id, model_name, model_year) VALUES
    (1, 'Model X', 2022),
    (1, 'Model Y', 2023),
    (2, 'Sedan', 2021),
    (2, 'SUV', 2022),
    (2, 'Civic', 2022),
    (2, 'Accord', 2023),
    (2, 'Camry', 2021),
    (3, 'Mustang', 2022),
    (3, 'Explorer', 2023),
    (1, 'Model S', 2022),
    (1, 'Model 3', 2023),
    (1, 'Model Y', 2022),
    (5, 'X5', 2021),
    (5, 'X3', 2022),
    (11, '911', 2022),
    (11, 'Cayenne', 2023),
    (12, 'MX-5', 2022),
    (12, 'CX-5', 2021),
    (3, 'Impreza', 2022),
    (3, 'Outback', 2023),
    (14, 'Sportage', 2021),
    (14, 'Seltos', 2022),
    (15, 'Elantra', 2023),
    (15, 'Santa Fe', 2022),
    (17, 'MDX', 2022),
    (17, 'RDX', 2021),
    (16, 'Q50', 2023),
    (16, 'QX60', 2022),
    (17, 'XE', 2022),
    (19, 'F-PACE', 2021),
    (18, 'Range Rover Sport', 2023),
    (18, 'Discovery', 2022), 
    (18, 'Defender', 2022),
    (19, 'CT4', 2023),
    (19, 'CT5', 2022),
    (20, 'Q60', 2021),
    (20, 'QX50', 2022),
    (11, 'Macan', 2023),
    (11, 'Panamera', 2022),
    (12, 'CX-9', 2021),
    (12, 'CX-30', 2022),
    (13, 'Forester', 2023),
    (13, 'Legacy', 2022),
    (14, 'Sorento', 2021),
    (14, 'Telluride', 2022),
    (15, 'Sonata', 2023),
    (14, 'K5', 2022),
    (18, 'QX80', 2021),
    (18, 'QX55', 2022),
    (9, 'E-Class', 2023),
    (9, 'GLC', 2022),
    (11, '718 Cayman', 2021),
    (11, 'Taycan', 2022),
    (12, 'MX-3', 2023),
    (12, 'CX-3', 2022),
    (13, 'Legacy', 2021),
    (13, 'Outback', 2022),
    (14, 'Telluride', 2023),
    (14, 'Seltos', 2022),
    (15, 'Kona', 2021),
    (15, 'Palisade', 2022),
    (16, 'LS', 2023),
    (16, 'RX', 2022),
    (17, 'ILX', 2021),
    (17, 'RDX', 2022),
    (18, 'QX60', 2023),
    (18, 'Armada', 2022),
    (19, 'CLA-Class', 2021),
    (19, 'GLA-Class', 2022),
    (20, 'Discovery Sport', 2023),
    (20, 'Range Rover Velar', 2022),
    (1, 'Model X', 2021),
    (1, 'Model 3', 2022),
    (2, 'Camry', 2023),
    (2, 'Corolla', 2022),
    (3, 'F-150', 2021),
    (3, 'Escape', 2022),
    (4, 'Accord', 2023),
    (4, 'Pilot', 2022),
    (5, 'X5', 2021),
    (5, 'X1', 2022),
    (6, 'Civic', 2023),
    (6, 'CR-V', 2022),
    (7, 'Silverado', 2021),
    (7, 'Malibu', 2022),
    (8, 'A4', 2023),
    (8, 'Q5', 2022),
    (9, 'Altima', 2021),
    (9, 'Rogue', 2022),
    (10, 'C-Class', 2023),
    (10, 'GLB-Class', 2022),
    (11, 'Cayenne', 2021),
    (11, '911 Turbo', 2022),
    (12, 'MX-30', 2023),
    (12, 'CX-30', 2022),
    (13, 'Impreza', 2021),
    (13, 'Forester', 2022),
    (14, 'Soul', 2023),
    (14, 'Sportage', 2022),
    (15, 'Elantra', 2021),
    (15, 'Tucson', 2022);

'''


fill_client_cars = '''
-- Insert data into client_cars
INSERT INTO client_cars (client_id, model_id) VALUES
    (1, 1),
    (2, 5),
    (3, 9),
    (4, 15),
    (5, 20),
    (6, 26),
    (7, 32),
    (7, 32),
    (1, 1),
    (3, 5),
    (3, 9),
    (24, 15),
    (25, 20),
    (26, 26),
    (27, 32),
    (3, 37),
    (1, 43),
    (10, 48),
    (11, 2),
    (12, 7),
    (13, 13),
    (14, 18),
    (15, 24),
    (16, 29),
    (17, 35),
    (18, 40),
    (19, 45),
    (20, 3),
    (21, 8),
    (22, 14),
    (23, 19),
    (24, 25),
    (25, 30),
    (26, 36),
    (27, 41),
    (28, 46),
    (29, 4),
    (30, 10),
    (31, 16),
    (32, 21),
    (33, 27),
    (34, 33),
    (35, 38),
    (36, 44),
    (37, 49),
    (38, 6),
    (39, 12),
    (40, 17);
'''