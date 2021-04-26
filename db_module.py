import sqlite3

conn = sqlite3.connect('base.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS assets(
        assetsid INT,
        name TEXT PRIMARY KEY,
        descr TEXT,
        price INT,
        change INT);''')
print("Table created successfully")

conn.close()