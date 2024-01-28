import os
import pandas as pd
from db import connect_db, close_db

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def query_text_data(txt, filename):
    conn, cursor = connect_db()

    with open(os.path.join(BASE_DIR, 'umabot', 'data', filename), 'r') as f:
        sql = f.read()
        real_message = '%' + txt + '%'
        cursor.execute(sql, (real_message, ))
        result = cursor.fetchall()
        
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame(result, columns=columns)

    close_db(conn, cursor)
    return df

def query_2ea_text_data(txt1, txt2, filename):
    conn, cursor = connect_db()

    with open(os.path.join(BASE_DIR, 'umabot', 'data', filename), 'r') as f:
        sql = f.read()
        real_message1 = '%' + txt1 + '%'
        real_message2 = '%' + txt2 + '%'
        cursor.execute(sql, (real_message1, real_message2))
        result = cursor.fetchall()
        
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame(result, columns=columns)

    close_db(conn, cursor)
    return df


def query_id_data(id, filename):
    conn, cursor = connect_db()

    with open(os.path.join(BASE_DIR, 'umabot', 'data', filename), 'r') as f:
        sql = f.read()
        cursor.execute(sql, (id, ))
        result = cursor.fetchall()
        
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame(result, columns=columns)

    close_db(conn, cursor)
    return df

def query_2ea_id_data(id1, id2, filename):
    conn, cursor = connect_db()

    with open(os.path.join(BASE_DIR, 'umabot', 'data', filename), 'r') as f:
        sql = f.read()
        cursor.execute(sql, (id1, id2))
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