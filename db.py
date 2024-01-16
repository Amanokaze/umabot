import sqlite3

def connect_db():
    conn = sqlite3.connect('data/master.db')
    cursor = conn.cursor()
    return conn, cursor

def close_db(conn, cursor):
    cursor.close()
    conn.close()

