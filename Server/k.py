from konlpy.tag import Okt
import pymysql.cursors

def fetch_purchase_count(l):
    conn = pymysql.connect(host='localhost', user='cmc9595', password='myungchul123', db= 'BREC', charset='utf8mb4')

    sql = "SELECT * FROM pvector;"

    try:
        with conn.cursor() as curs:
            curs.execute(sql)
            result = curs.fetchall()
            for row in result:
                l.append([row[0], row[1]])

    except:
        pass

    finally:
        conn.close()

    return l

def fetch_keywords(l):
    conn = pymysql.connect(host='localhost', user='cmc9595', password='myungchul123', db= 'BREC', charset='utf8mb4')

    sql = "SELECT * FROM bvector;"

    try :
        with conn.cursor() as curs:
            curs.execute(sql)
            result = curs.fetchall()

            for row in result:
                s1=[]
                s1.append(str(row[0]))

                words = row[1].split(", ")
                s2=[]
                for w in words:
                    s2.append(w.strip())
                s1.append(s2)
                l.append(s1)
    finally :
        conn.close()

    return l

def get_title_by_purchase_count(l, user_words, p): # input booklist, user_keyword, output one title
    tlist=[]
    for b in l:
        title = b[0]
        keyword = b[1]

        res = set(keyword) & set(user_words)

        if len(res) > 0:
            tlist.append([len(res), title]) # kyo-set num, title
    tlist = sorted(tlist, reverse=True) # sort

    try:
        text = tlist[0][1]
    except:
        text = "no book"
    return text

def sentence_to_nouns(s):
    okt = Okt()
    return okt.nouns(s)
#print(okt.morphs("내이름은 천명철, 매너리즘에 빠진 천재다."))
#print(okt.nouns("내이름은 천명철, 매너리즘에 빠진 천재다."))
#print(okt.nouns(" 이순신, 임잰왜란, 거북선 왜군 선조대왕"))

#user = input().split(" ")
#print(user)


if __name__ == '__main__':

    okt = Okt()

    user_words = input().split(" ")
    print("My Input", end=" : ")
    for w in user_words:
        print(w , end=' ')
    print()

    l=[]

    l = fetch_keywords(l)
    p = fetch_purchase_count(l)
    res = get_title_by_purchase_count(l, user_words, p)
    print(res)






