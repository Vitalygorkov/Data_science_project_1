import sqlite3

conn = sqlite3.connect('base.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS assets(
        assetsid INT,
        name TEXT PRIMARY KEY,
        descr TEXT,
        price_1_day_year INT,
        price INT,
        change INT);''')
print("Table created successfully")

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