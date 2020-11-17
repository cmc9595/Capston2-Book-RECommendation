from collections import Counter

f = open("C:\\Users\\cmc9595\\Desktop\\b.txt", "r")

wlist=[]
while True :
    line = f.readline().strip('\n')
    if not line : break

    line = line.split(":")

    try :
        words = line[1].split(",")
        for word in words:
            wlist.append(word.strip())
    except:
        print("no kw")



count = Counter(wlist)
common = count.most_common(1000)
for c in common:
    print(c)

print("총 단어 개수 : " + str(len(wlist)))
wlist = set(wlist)
print("단어 종류 수 : " + str(len(wlist)))
f.close()