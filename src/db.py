import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def connect_db():
    conn = sqlite3.connect(os.path.join(BASE_DIR, 'umabot', 'data', 'master.db'))
    cursor = conn.cursor()
    return conn, cursor

def close_db(conn, cursor):
    cursor.close()
    conn.close()

