import pymysql.cursors

def create_table():

    conn = pymysql.connect(host=HOST,
            user=USER,
            password=PW,
            db=bvector,
            charset='utf8mb4')
    sql='''
        CREATE TABLE test(

        id varchar(10) not null primary key,
        pw varchar(10) not null,
        time TIMESTAMP comment 
        )
        '''

    try:
        with conn.cursur() as cursor:
            cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()


