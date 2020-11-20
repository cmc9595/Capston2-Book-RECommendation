import pymysql.cursors

def drop_table():

    conn = pymysql.connect(host='localhost', user='cmc9595', password='myungchul123', db='bvector', charset='utf8mb4')

    sql = 'DROP TABLE bvector'

    try:
        with conn.cursor() as curs:
            curs.execute(sql)
        conn.commit()
    finally:
        conn.close()


drop_table()
