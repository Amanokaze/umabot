from db import connect_db, close_db

def query_skill_data(message):
    conn, cursor = connect_db()

    with open('data/skill.sql', 'r') as f:
        sql = f.read()
        real_message = '%' + message + '%'
        cursor.execute(sql, (real_message, ))
        result = cursor.fetchall()

    close_db(conn, cursor)
    return result
