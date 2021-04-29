import sqlite3
from sqlite3 import Error




def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn



def select_all_assets(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM assets")

    rows = cur.fetchall()

    for row in rows:
        print(row)

conn = create_connection('base.db')

select_all_assets(conn)