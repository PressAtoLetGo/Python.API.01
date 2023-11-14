-- Apaga as tabelas caso existam.
DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS owner;

-- Cria a tabela 'owner'.
CREATE TABLE owner (
    owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    owner_name TEXT,
    owner_email TEXT,
    owner_password TEXT,
    owner_birth DATE,
    owner_status TEXT DEFAULT 'on',
    owner_field1 TEXT,
    owner_field2 TEXT
);

-- Popular a tabela 'owner' com dados 'fake'.
INSERT INTO owner 
	(owner_date, owner_name, owner_email, owner_password, owner_birth)
VALUES
	('2023-09-28 10:11:12', 'Joca da Silva', 'joca@silva.com', '123', '1988-12-14'),
    ('2022-05-18 09:23:45', 'John Doe', 'john.doe@email.com', 'pass123', '1990-05-21'),
    ('2019-08-27 14:56:32', 'Jane Smith', 'jane.smith@email.com', 'pass456', '1985-08-17'),
    ('2014-03-15 18:42:21', 'Bob Johnson', 'bob.johnson@email.com', 'pass789', '1992-03-09'),
    ('2023-11-02 22:11:33', 'Alice Brown', 'alice.brown@email.com', 'passabc', '1988-11-30'),
    ('2017-07-09 07:34:52', 'Charlie Wilson', 'charlie.wilson@email.com', 'passxyz', '1995-07-04');

-- Cria a tabela 'item'.
CREATE TABLE item (
	item_id INTEGER PRIMARY KEY AUTOINCREMENT,
	item_date DATETIME DEFAULT CURRENT_TIMESTAMP,
	item_name TEXT,
	item_description TEXT,
	item_location TEXT,
	item_owner INTEGER,
	item_status TEXT DEFAULT 'on',
	item_field1 TEXT,
	item_field2 TEXT,
	FOREIGN KEY (item_owner) REFERENCES owner (owner_id)
);

-- Popular a tabela 'item' com dados 'fake'.
INSERT INTO item 
	(item_date, item_name, item_description, item_location, item_owner)
VALUES
    ('2022-05-18 09:23:45', 'Item1', 'Description for Item1', 'Location1', 1),
    ('2019-08-27 14:56:32', 'Item2', 'Description for Item2', 'Location2', 2),
    ('2021-03-15 18:42:21', 'Item3', 'Description for Item3', 'Location3', 3),
    ('2021-11-02 22:11:33', 'Item4', 'Description for Item4', 'Location4', 4),
    ('2020-07-09 07:34:52', 'Item5', 'Description for Item5', 'Location5', 5),
    ('2023-02-24 13:17:04', 'Item6', 'Description for Item6', 'Location6', 6);