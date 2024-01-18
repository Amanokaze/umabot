import os
import pandas as pd
from db import connect_db, close_db

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def query_skill_data(message):
    conn, cursor = connect_db()

    with open(os.path.join(BASE_DIR, 'umabot', 'data', 'skill.sql'), 'r') as f:
        sql = f.read()
        real_message = '%' + message + '%'
        cursor.execute(sql, (real_message, ))
        result = cursor.fetchall()
        
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame(result, columns=columns)

    close_db(conn, cursor)
    return df

def query_skill_condition_data(skill_id):
    conn, cursor = connect_db()

    with open(os.path.join(BASE_DIR, 'umabot', 'data', 'skill_condition.sql'), 'r') as f:
        sql = f.read()
        cursor.execute(sql, (skill_id, ))
        result = cursor.fetchall()
        
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame(result, columns=columns)

    close_db(conn, cursor)
    return df

def query_skill_icon():
    conn, cursor = connect_db()

    sql = "select distinct icon_id from skill_data order by icon_id asc"
    cursor.execute(sql)
    result = cursor.fetchall()

    close_db(conn, cursor)
    return result