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

    def __init__(self, name, description, marketcap, price, price_1_day_year_asset):
        """Constructor"""
        self.name = name
        self.description = description
        self.marketcap = marketcap
        self.price = price
        self.price_1_day_year_asset = price_1_day_year_asset

conn = sqlite3.connect('base.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS groups(
        name TEXT PRIMARY KEY,
        descr TEXT,
        marketcap INT);''')
print("Table groups created successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS assets(
        name TEXT  PRIMARY KEY,  
        descr TEXT,
        price INT,
        price_1_day_year INT,
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

Cryptocurrencies = Group('Сryptocurrencies', 'Cryptocurrencies.. etc.', 100)
Currencies = Group('Currencies', 'Currencies, USD, EUR, RUB, etc.', 300)
Cryptocurrencies_tuple = (Cryptocurrencies.name, Cryptocurrencies.description, Cryptocurrencies.marketcap,)
Currencies_tuple = (Currencies.name, Currencies.description, Currencies.marketcap,)
try:
    conn.execute("INSERT INTO groups VALUES(?, ?, ?);", Cryptocurrencies_tuple)
    conn.commit()
except Exception as e:
    print(e, 'This entry already exists')

try:
    conn.execute("INSERT INTO groups VALUES(?, ?, ?);", Currencies_tuple)
    conn.commit()
except Exception as e:
    print(e, 'This entry already exists')


BTC = Asset('BTC', 'This is the first cryptocurrency, the leader in capitalization and digital gold', 1020169351771, 54300, 28951)

print(BTC.name, BTC.price, BTC.price_1_day_year_asset, str((BTC.price-BTC.price_1_day_year_asset)/BTC.price_1_day_year_asset*100)+'%' )

# asset_id = None
name_asset = 'BTC'
descr_asset = 'its description'
price_1_day_year_asset = 28951
price_asset = 54200
change_asset = price_asset/price_1_day_year_asset*100

# asset1 = (asset_id, name_asset, descr_asset, price_1_day_year_asset, price_asset, change_asset)
# conn.execute("INSERT INTO assets VALUES(?, ?, ?, ?, ?, ?);", asset1)
# conn.commit()

asset1 = (name_asset, descr_asset, price_1_day_year_asset, price_asset, change_asset)
try:
    conn.execute("INSERT INTO assets VALUES(?, ?, ?, ?, ?);", asset1)
    conn.commit()
except Exception as e:
    print(e, 'This entry already exists')

conn.close()