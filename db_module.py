import sqlite3

conn = sqlite3.connect('base.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS groups(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        descr TEXT,
        price_1_day_year INT,
        price INT,
        change INT);''')
print("Table groups created successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS assets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,  
        descr TEXT,
        price_1_day_year INT,
        price INT,
        change INT);''')
print("Table assets created successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS assets_groups(
        groups_id INT,
        assets_id INT,
        FOREIGN KEY(groups_id) REFERENCES groups(id),
        FOREIGN KEY(assets_id) REFERENCES assets(id)
        );''')
print("Table assets_groups created successfully")

# conn.close()

group_id = '1'
name_group = 'BTC'
descr_group = 'its description'
price_1_day_year_group = 28951
price_group = 54200
change_group = price_group/price_1_day_year_group*100


group1 = (group_id, name_group, descr_group, price_1_day_year_group, price_group, change_group)
conn.execute("INSERT INTO groups VALUES(?, ?, ?, ?, ?, ?);", group1)
conn.commit()

asset_id = '1'
name_asset = 'BTC'
descr_asset = 'its description'
price_1_day_year_asset = 28951
price_asset = 54200
change_asset = price_asset/price_1_day_year_asset*100

asset1 = (asset_id, name_asset, descr_asset, price_1_day_year_asset, price_asset, change_asset)
conn.execute("INSERT INTO assets VALUES(?, ?, ?, ?, ?, ?);", asset1)
conn.commit()

conn.close()