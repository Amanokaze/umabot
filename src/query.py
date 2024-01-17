import os
from db import connect_db, close_db

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def query_skill_data(message):
    conn, cursor = connect_db()

    with open(os.path.join(BASE_DIR, 'umabot', 'data', 'skill.sql'), 'r') as f:
        sql = f.read()
        real_message = '%' + message + '%'
        cursor.execute(sql, (real_message, ))
        result = cursor.fetchall()

    close_db(conn, cursor)
    return result
