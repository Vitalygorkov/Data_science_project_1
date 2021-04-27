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

assetsid = '1'
name = 'BTC'
descr = 'its description'
price_1_day_year = 28951
price = 54200
change = price/price_1_day_year*100


assets = (assetsid, name, descr, price_1_day_year, price, change)
conn.execute("INSERT INTO assets VALUES(?, ?, ?, ?, ?, ?);", assets)
conn.commit()
conn.close()