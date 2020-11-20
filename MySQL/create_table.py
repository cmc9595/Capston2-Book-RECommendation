import pymysql.cursors

def create_table():

    conn = pymysql.connect(host='localhost', user='cmc9595', password='myungchul123', db= 'bvector', charset='utf8mb4')

    sql = '''
            CREATE TABLE bvector(
				title varchar(100) not null,
				keywords varchar(100)
            )
            '''

    try:
        with conn.cursor() as curs:
            curs.execute(sql)
        conn.commit()
    finally:
        conn.close()


def insert_table(sql):

    conn = pymysql.connect(host='localhost', user='cmc9595', password='myungchul123', db= 'bvector', charset='utf8mb4')

    try:
        with conn.cursor() as curs:
            curs.execute(sql)
        conn.commit()
    finally:
        conn.close()


if __name__ == '__main__':
    create_table()

    f = open("result.txt", "r", encoding='cp949')

    count=0

    while True :
        line = f.readline().strip('\n')
        if not line : break
        line = line.split(" : ")
        title = line[0].strip('')
        try :
            keyword = line[1].strip()
        except:
            print("no kw")
            keyword =""

        if title.find('"')>=0:
            sql = "INSERT INTO bvector (title, keywords) VALUES ('" + str(title)+ "', '" + str(keyword) + "')"
        else:
            sql = 'INSERT INTO bvector (title, keywords) VALUES ("' + str(title)+ '", "' + str(keyword) + '")'


        tmp = "Oh \"my\"my god"
        g = "oh my god"

        #print(count)
        insert_table(sql)

    f.close()




