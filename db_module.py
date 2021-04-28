import sqlite3

class Group(object):
    """docstring"""

    def __init__(self, name, description, marketcap):
        """Constructor"""
        self.name = name
        self.description = description
        self.marketcap = marketcap

class Asset(object):
    """docstring"""

    def __init__(self, name, description, marketcap, price):
        """Constructor"""
        self.name = name
        self.description = description
        self.marketcap = marketcap
        self.price = price

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

group_id = None
name_group = 'Сryptocurrencies'
descr_group = 'Cryptocurrencies, DEFI, tokens, etc.'
price_1_day_year_group = 28951
price_group = 54200
change_group = price_group/price_1_day_year_group*100

group1 = (group_id, name_group, descr_group, price_1_day_year_group, price_group, change_group)
conn.execute("INSERT INTO groups VALUES(?, ?, ?, ?, ?, ?);", group1)
conn.commit()

group_id = None
name_group = 'Currencies'
descr_group = 'Currencies, USD, EUR, RUB, etc.'
price_1_day_year_group = 28951
price_group = 54200
change_group = price_group/price_1_day_year_group*100


group1 = (group_id, name_group, descr_group, price_1_day_year_group, price_group, change_group)
conn.execute("INSERT INTO groups VALUES(?, ?, ?, ?, ?, ?);", group1)
conn.commit()

BTC = Asset('BTC', 'This is the first cryptocurrency, the leader in capitalization and digital gold', 1020169351771, 54300,)

print(BTC.name, BTC.price)

asset_id = None
name_asset = 'BTC'
descr_asset = 'its description'
price_1_day_year_asset = 28951
price_asset = 54200
change_asset = price_asset/price_1_day_year_asset*100

# asset1 = (asset_id, name_asset, descr_asset, price_1_day_year_asset, price_asset, change_asset)
# conn.execute("INSERT INTO assets VALUES(?, ?, ?, ?, ?, ?);", asset1)
# conn.commit()

asset1 = (asset_id, name_asset, descr_asset, price_1_day_year_asset, price_asset, change_asset)
conn.execute("INSERT INTO assets VALUES(?, ?, ?, ?, ?, ?);", asset1)
conn.commit()

conn.close()