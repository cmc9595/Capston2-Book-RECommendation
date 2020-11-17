from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from multiprocessing import Pool, Manager

category = {"소설-한국소설"     : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0101&mallGb=KOR&orderClick=JAR",
            "소설-영미소설"     : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0103&mallGb=KOR&orderClick=JAR",
            "소설-일본소설"     : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0105&mallGb=KOR&orderClick=JAR",
            "소설-중국소설"     : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0107&mallGb=KOR&orderClick=JAR",
            "소설-러시아소설"   : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0109&mallGb=KOR&orderClick=JAR",
            "소설-프랑스소설"   : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0111&mallGb=KOR&orderClick=JAR",
            "소설-독일소설"     : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0112&mallGb=KOR&orderClick=JAR",
            "소설-북유럽소설"   : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0115&mallGb=KOR&orderClick=JAR",
            "소설-그외유럽소설" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0116&mallGb=KOR&orderClick=JAR",
            "소설-기타나라소설"     : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0117&mallGb=KOR&orderClick=JAR",
            "소설-청소년소설"  : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0118&mallGb=KOR&orderClick=JAR", #2개뿐;
            "소설-고전소설/문학선" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0121&mallGb=KOR&orderClick=JAR",
            "소설-세계문학전집"    : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0124&mallGb=KOR&orderClick=JAR",
            "소설-라이트노벨" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0126&mallGb=KOR&orderClick=JAR",
            "소설-장르소" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0128&mallGb=KOR&orderClick=JAR",

            "시/에세이-한국시" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0301&mallGb=KOR&orderClick=JAR",
            "시/에세이-해외시" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0302&mallGb=KOR&orderClick=JAR",
            "시/에세이-테마에세이" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0304&mallGb=KOR&orderClick=JAR",
            "시/에세이-나라별 에세이" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0307&mallGb=KOR&orderClick=JAR",
            "시/에세이-인물/자전적에세이" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0311&mallGb=KOR&orderClick=JAR",
            "시/에세이-청소년 시/에세이" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0317&mallGb=KOR&orderClick=JAR",
            "시/에세이-시/에세이문고" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0319&mallGb=KOR&orderClick=JAR",

            "인문-인문학일반" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0501&mallGb=KOR&orderClick=sgc",
            "인문-심리학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0503&mallGb=KOR&orderClick=JAR",
            "인문-교육학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0505&mallGb=KOR&orderClick=JAR",
            "인문-유아교육" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0507&mallGb=KOR&orderClick=JAR",
            "인문-특수교육" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0509&mallGb=KOR&orderClick=JAR",
            "인문-임용고시" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0511&mallGb=KOR&orderClick=JAR",
            "인문-철학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0513&mallGb=KOR&orderClick=JAR",
            "인문-문학이론" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0515&mallGb=KOR&orderClick=JAR",
            "인문-한국문학론" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0517&mallGb=KOR&orderClick=JAR",
            "인문-영미문학론" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0519&mallGb=KOR&orderClick=JAR",
            "인문-중국문학론" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0520&mallGb=KOR&orderClick=JAR",
            "인문-세계문학론" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0521&mallGb=KOR&orderClick=JAR",
            "인문-언어학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0523&mallGb=KOR&orderClick=JAR",
            "인문-독서/글쓰기" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0525&mallGb=KOR&orderClick=JAR",
            "인문-문헌정보학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0527&mallGb=KOR&orderClick=JAR",
            "인문-역학/사주" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0529&mallGb=KOR&orderClick=JAR",
            "인문-대학교재" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0532&mallGb=KOR&orderClick=JAR",
            "인문-인문교양총서" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0533&mallGb=KOR&orderClick=JAR",
            "인문-인문고전총서" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0535&mallGb=KOR&orderClick=JAR",
            "인문-방송통신대교재" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0551&mallGb=KOR&orderClick=JAR",

            "가정/육아-결혼/가정" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0701&mallGb=KOR&orderClick=JAR",
            "가정/육아-임신/출산" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0703&mallGb=KOR&orderClick=JAR",
            "가정/육아-육아" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0704&mallGb=KOR&orderClick=JAR",
            "가정/육아-자녀교육" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0705&mallGb=KOR&orderClick=JAR",
            "가정/육아-살림의지혜" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0707&mallGb=KOR&orderClick=JAR",
            "가정/육아-홈인테리어" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0709&mallGb=KOR&orderClick=JAR",

            "요리-요리일반" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0801&mallGb=KOR&orderClick=JAR",
            "요리-요리에세이" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0802&mallGb=KOR&orderClick=JAR",
            "요리-테마별요리" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0803&mallGb=KOR&orderClick=JAR",
            "요리-베이킹/간식" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0805&mallGb=KOR&orderClick=JAR",
            "요리-계절요리" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0807&mallGb=KOR&orderClick=JAR",
            "요리-재료별요리" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0809&mallGb=KOR&orderClick=JAR",
            "요리-나라별요리" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0811&mallGb=KOR&orderClick=JAR",
            "요리-생활요리" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0813&mallGb=KOR&orderClick=JAR",
            "요리-전문요리" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0815&mallGb=KOR&orderClick=JAR",
            "요리-와인/커피/음료" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0817&mallGb=KOR&orderClick=JAR",
            "요리-요리수험서" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0819&mallGb=KOR&orderClick=JAR",

            "건강-건강일반" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0901&mallGb=KOR&orderClick=JAR",
            "건강-뇌건강" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0903&mallGb=KOR&orderClick=JAR",
            "건강-한방치료" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0905&mallGb=KOR&orderClick=JAR",
            "건강-자연건강" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0907&mallGb=KOR&orderClick=JAR",
            "건강-건강식사" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0908&mallGb=KOR&orderClick=JAR",
            "건강-질병치료/예방" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0909&mallGb=KOR&orderClick=JAR",
            "건강-다이어트" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0911&mallGb=KOR&orderClick=JAR",
            "건강-운동/트레이닝" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0913&mallGb=KOR&orderClick=JAR",
            "건강-피부관리/메이크업" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0915&mallGb=KOR&orderClick=JAR",
            "건강-건강문고" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=0920&mallGb=KOR&orderClick=JAR",
            
            "취미/실용/스포츠-가정원예" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1101&mallGb=KOR&orderClick=JAR",
            "취미/실용/스포츠-홈인테리어/수납" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1102&mallGb=KOR&orderClick=JAR",
            "취미/실용/스포츠-생활공예/DIY" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1103&mallGb=KOR&orderClick=JAR",
            "취미/실용/스포츠-살림의지혜" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1104&mallGb=KOR&orderClick=JAR",
            "취미/실용/스포츠-반려동물" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1105&mallGb=KOR&orderClick=JAR",
            "취미/실용/스포츠-등산/낚시" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1107&mallGb=KOR&orderClick=JAR",
            "취미/실용/스포츠-바둑/골프" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1109&mallGb=KOR&orderClick=JAR",
            "취미/실용/스포츠-무술" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1113&mallGb=KOR&orderClick=JAR",
            "취미/실용/스포츠-스포츠" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1115&mallGb=KOR&orderClick=JAR",
            "취미/실용/스포츠-레크레이션/게임" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1117&mallGb=KOR&orderClick=JAR",
            "취미/실용/스포츠-퀴즈/퍼즐/스도쿠" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1118&mallGb=KOR&orderClick=JAR",
            "취미/실용/스포츠-무용" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1119&mallGb=KOR&orderClick=JAR",
            "취미/실용/스포츠-체육" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1121&mallGb=KOR&orderClick=JAR",
            "취미/실용/스포츠-취미일반" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1124&mallGb=KOR&orderClick=JAR",
            "취미/실용/스포츠-취미관련상품" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1125&mallGb=KOR&orderClick=JAR",
            "취미/실용/스포츠-대학교재" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1130&mallGb=KOR&orderClick=JAR",

            "경제/경영-경영일반" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1301&mallGb=KOR&orderClick=JAR",
            "경제/경영-경영이론" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1303&mallGb=KOR&orderClick=JAR",
            "경제/경영-경영관리" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1305&mallGb=KOR&orderClick=JAR",
            "경제/경영-경영전략" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1307&mallGb=KOR&orderClick=JAR",
            "경제/경영-경제일반" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1309&mallGb=KOR&orderClick=JAR",
            "경제/경영-경제이론" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1311&mallGb=KOR&orderClick=JAR",
            "경제/경영-경제실무" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1313&mallGb=KOR&orderClick=JAR",
            "경제/경영-각국경제" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1315&mallGb=KOR&orderClick=JAR",
            "경제/경영-세무/회계" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1316&mallGb=KOR&orderClick=JAR",
            "경제/경영-마케팅/광고/고객" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1319&mallGb=KOR&orderClick=JAR",
            "경제/경영-유통/창업" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1321&mallGb=KOR&orderClick=JAR",
            "경제/경영-재테크/금융" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1323&mallGb=KOR&orderClick=JAR",
            "경제/경영-무용/운송" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1325&mallGb=KOR&orderClick=JAR",
            "경제/경영-관광/호텔" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1327&mallGb=KOR&orderClick=JAR",
            "경제/경영-경제/경영문고" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1329&mallGb=KOR&orderClick=JAR",
            "경제/경영-대학교재" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1331&mallGb=KOR&orderClick=JAR",

            "자기계발-성공/처세" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1501&mallGb=KOR&orderClick=JAR",
            "자기계발-자기능력계발" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1503&mallGb=KOR&orderClick=JAR",
            "자기계발-비즈니스능력계발" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1505&mallGb=KOR&orderClick=JAR",
            "자기계발-인간관계" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1506&mallGb=KOR&orderClick=JAR",
            "자기계발-화술/협상" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1507&mallGb=KOR&orderClick=JAR",
            "자기계발-청소년자기계발" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1508&mallGb=KOR&orderClick=JAR",
            "자기계발-오디오북" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1509&mallGb=KOR&orderClick=JAR",
            "자기계발-전자책단말기/전자기기" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1519&mallGb=KOR&orderClick=JAR",

            "정치/사회-정치/외교" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1701&mallGb=KOR&orderClick=JAR",
            "정치/사회-행정/정책" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1703&mallGb=KOR&orderClick=JAR",
            "정치/사회-국방/군사" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1705&mallGb=KOR&orderClick=JAR",
            "정치/사회-법학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1707&mallGb=KOR&orderClick=JAR",
            "정치/사회-사회학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1709&mallGb=KOR&orderClick=JAR",
            "정치/사회-사회문제/복지" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1711&mallGb=KOR&orderClick=JAR",
            "정치/사회-언론/신문/방송" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1713&mallGb=KOR&orderClick=JAR",
            "정치/사회-정치/사회문고" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1715&mallGb=KOR&orderClick=JAR",
            "정치/사회-대학교재" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1717&mallGb=KOR&orderClick=JAR",
            "정치/사회-정부간행물" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1720&mallGb=KOR&orderClick=JAR",

            "역사/문화-역사일반" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1901&mallGb=KOR&orderClick=JAR",
            "역사/문화-세계사" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1903&mallGb=KOR&orderClick=JAR",
            "역사/문화-서양사" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1905&mallGb=KOR&orderClick=JAR",
            "역사/문화-동양사" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1907&mallGb=KOR&orderClick=JAR",
            "역사/문화-한국사" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1909&mallGb=KOR&orderClick=JAR",
            "역사/문화-신화" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1911&mallGb=KOR&orderClick=JAR",
            "역사/문화-민속학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1912&mallGb=KOR&orderClick=JAR",
            "역사/문화-문화일반" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1913&mallGb=KOR&orderClick=JAR",
            "역사/문화-문화사" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1915&mallGb=KOR&orderClick=JAR",
            "역사/문화-역사인물" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1917&mallGb=KOR&orderClick=JAR",
            "역사/문화-역사기행" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1918&mallGb=KOR&orderClick=JAR",
            "역사/문화-청소년 역사" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1919&mallGb=KOR&orderClick=JAR",
            "역사/문화-지리학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1920&mallGb=KOR&orderClick=JAR",
            "역사/문화-대학교재" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=1921&mallGb=KOR&orderClick=JAR",

            "종교-종교일반" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2101&mallGb=KOR&orderClick=JAR",
            "종교-기독교(개신교)" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2103&mallGb=KOR&orderClick=JAR",
            "종교-가톨릭" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2105&mallGb=KOR&orderClick=JAR",
            "종교-불교" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2107&mallGb=KOR&orderClick=JAR",
            "종교-그외종교" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2109&mallGb=KOR&orderClick=JAR",
            "종교-CD/TAPE/악보" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2111&mallGb=KOR&orderClick=JAR",

            "예술/대중문화-예술일반" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2301&mallGb=KOR&orderClick=JAR",
            "예술/대중문화-미술" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2303&mallGb=KOR&orderClick=JAR",
            "예술/대중문화-만화/애니메이션" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2305&mallGb=KOR&orderClick=JAR",
            "예술/대중문화-디자인/색채" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2307&mallGb=KOR&orderClick=JAR",
            "예술/대중문화-패션/의류" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2309&mallGb=KOR&orderClick=JAR",
            "예술/대중문화-음악" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2313&mallGb=KOR&orderClick=JAR",
            "예술/대중문화-사진/영상" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2315&mallGb=KOR&orderClick=JAR",
            "예술/대중문화-연극" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2317&mallGb=KOR&orderClick=JAR",
            "예술/대중문화-영화" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2319&mallGb=KOR&orderClick=JAR",
            "예술/대중문화-예술기행" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2320&mallGb=KOR&orderClick=JAR",
            "예술/대중문화-예술문고" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2321&mallGb=KOR&orderClick=JAR",
            "예술/대중문화-청소년예술" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2325&mallGb=KOR&orderClick=JAR",
            "예술/대중문화-대학교재" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2327&mallGb=KOR&orderClick=JAR",

            "중/고등참고서-고등학교 출판사별" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2501&mallGb=KOR&orderClick=JAR",
            "중/고등참고서-고등학교 과목별" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2503&mallGb=KOR&orderClick=JAR",
            "중/고등참고서-중학교 출판사별" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2505&mallGb=KOR&orderClick=JAR",
            "중/고등참고서-중학교 학년별" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2509&mallGb=KOR&orderClick=JAR",
            "중/고등참고서-예비중학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2513&mallGb=KOR&orderClick=JAR",
            "중/고등참고서-중간고사(중등)" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2515&mallGb=KOR&orderClick=JAR",
            "중/고등참고서-기말고사(중등)" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2517&mallGb=KOR&orderClick=JAR",
            #"중/고등참고서-EBS 중학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2521&mallGb=KOR&orderClick=JAR",
            #"중/고등참고서-EBS 고등" : "",
            "중/고등참고서-강남구청 인터넷교재" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2523&mallGb=KOR&orderClick=JAR",
            "중/고등참고서-중고등경시/올림피아드" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2524&mallGb=KOR&orderClick=JAR",
            "중/고등참고서-특목고대비교재" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2525&mallGb=KOR&orderClick=JAR",
            "중/고등참고서-NEAT(국가영어능력평가)" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2526&mallGb=KOR&orderClick=JAR",
            "중/고등참고서-영어/수학일반/한자" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2527&mallGb=KOR&orderClick=JAR",
            "중/고등참고서-논술/면접대비" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2529&mallGb=KOR&orderClick=JAR",
            "중/고등참고서-중고학습문학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2531&mallGb=KOR&orderClick=JAR",
            "중/고등참고서-검정고시" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2533&mallGb=KOR&orderClick=JAR",
            "중/고등참고서-공부방법/진" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2535&mallGb=KOR&orderClick=JAR",

            "기술/공학-건축/인테리어" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2601&mallGb=KOR&orderClick=JAR",
            "기술/공학-토목/건설" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2603&mallGb=KOR&orderClick=JAR",
            "기술/공학-환경/소방/도시/조경" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2605&mallGb=KOR&orderClick=JAR",
            "기술/공학-자동차/운전" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2607&mallGb=KOR&orderClick=JAR",
            "기술/공학-운전면허" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2608&mallGb=KOR&orderClick=JAR",
            "기술/공학-공학일반" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2609&mallGb=KOR&orderClick=JAR",
            "기술/공학-금속/재료" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2611&mallGb=KOR&orderClick=JAR",
            "기술/공학-기계/역학/항공" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2613&mallGb=KOR&orderClick=JAR",
            "기술/공학-전기/전자" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2615&mallGb=KOR&orderClick=JAR",
            "기술/공학-농수산/축산" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2617&mallGb=KOR&orderClick=JAR",
            "기술/공학-생활과학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2619&mallGb=KOR&orderClick=JAR",
            "기술/공학-의학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2621&mallGb=KOR&orderClick=JAR",
            "기술/공학-대학교재" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2623&mallGb=KOR&orderClick=JAR",

            "외국어-영어일반" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2701&mallGb=KOR&orderClick=JAR",
            "외국어-영어회화/청취" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2703&mallGb=KOR&orderClick=JAR",
            "외국어-비즈니스영어" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2705&mallGb=KOR&orderClick=JAR",
            "외국어-영어문법/독해/작문" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2707&mallGb=KOR&orderClick=JAR",
            "외국어-영어문고" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2709&mallGb=KOR&orderClick=JAR",
            "외국어-영어수입교재" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2711&mallGb=KOR&orderClick=JAR",
            "외국어-방송영어교재" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2715&mallGb=KOR&orderClick=JAR",
            "외국어-수험영어" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2717&mallGb=KOR&orderClick=JAR",
            "외국어-유학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2719&mallGb=KOR&orderClick=JAR",
            "외국어-번역/통역" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2721&mallGb=KOR&orderClick=JAR",
            "외국어-일본어일반" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2723&mallGb=KOR&orderClick=JAR",
            "외국어-일본어회화" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2725&mallGb=KOR&orderClick=JAR",
            "외국어-일본어문법/작문" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2727&mallGb=KOR&orderClick=JAR",
            "외국어-일본어능력시험/JPT" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2729&mallGb=KOR&orderClick=JAR",
            "외국어-중국어일반" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2733&mallGb=KOR&orderClick=JAR",
            "외국어-중국어회화" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2735&mallGb=KOR&orderClick=JAR",
            "외국어-중국어문법/독해" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2737&mallGb=KOR&orderClick=JAR",
            "외국어-HSK/중국어시험" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2739&mallGb=KOR&orderClick=JAR",
            "외국어-중국원서" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2740&mallGb=KOR&orderClick=JAR",
            "외국어-독일어" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2741&mallGb=KOR&orderClick=JAR",
            "외국어-프랑스어" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2743&mallGb=KOR&orderClick=JAR",
            "외국어-기타외국어" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2745&mallGb=KOR&orderClick=JAR",
            "외국어-어학사전" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2747&mallGb=KOR&orderClick=JAR",
            "외국어-대학교재" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2750&mallGb=KOR&orderClick=JAR",

            "과학-과학이론" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2901&mallGb=KOR&orderClick=JAR",
            "과학-도감" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2903&mallGb=KOR&orderClick=JAR",
            "과학-교양과학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2905&mallGb=KOR&orderClick=JAR",
            "과학-수학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2907&mallGb=KOR&orderClick=JAR",
            "과학-물리학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2909&mallGb=KOR&orderClick=JAR",
            "과학-화학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2911&mallGb=KOR&orderClick=JAR",
            "과학-생물학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2913&mallGb=KOR&orderClick=JAR",
            "과학-지구과학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2915&mallGb=KOR&orderClick=JAR",
            "과학-천문학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2917&mallGb=KOR&orderClick=JAR",
            "과학-청소년 교양과학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2918&mallGb=KOR&orderClick=JAR",
            "과학-과학문고" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2919&mallGb=KOR&orderClick=JAR",
            "과학-대학교재" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2921&mallGb=KOR&orderClick=JAR",
            "과학-초과학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=2923&mallGb=KOR&orderClick=JAR",

            "취업/수험서-취업" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3101&mallGb=KOR&orderClick=JAR",
            "취업/수험서-공무원 과목별" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3102&mallGb=KOR&orderClick=JAR",
            "취업/수험서-공무원 직군별" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3104&mallGb=KOR&orderClick=JAR",
            "취업/수험서-인적성/직무능력" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3105&mallGb=KOR&orderClick=JAR",
            "취업/수험서-공인중개사/주택관리사" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3106&mallGb=KOR&orderClick=JAR",
            "취업/수험서-고시" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3108&mallGb=KOR&orderClick=JAR",
            "취업/수험서-전문직자격증" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3110&mallGb=KOR&orderClick=JAR",
            "취업/수험서-국가자격증" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3112&mallGb=KOR&orderClick=JAR",
            "취업/수험서-경제/금융/회계자격증" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3114&mallGb=KOR&orderClick=JAR",
            "취업/수험서-편입/독학사" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3116&mallGb=KOR&orderClick=JAR",
            "취업/수험서-한자능력시" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3130&mallGb=KOR&orderClick=JAR",

            "여행-국내여행" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3201&mallGb=KOR&orderClick=JAR",
            "여행-해외여행" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3203&mallGb=KOR&orderClick=JAR",
            "여행-여행에세이" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3204&mallGb=KOR&orderClick=JAR",
            "여행-테마여행" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3205&mallGb=KOR&orderClick=JAR",
            "여행-인기지역" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3206&mallGb=KOR&orderClick=JAR",
            "여행-지도" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3214&mallGb=KOR&orderClick=JAR",

            "컴퓨터/IT-컴퓨터공학" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3301&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-IT일반" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3302&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-컴퓨터입문/활용" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3303&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-전산통계/해석" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3305&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-OS" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3307&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-네트워크" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3309&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-보안/해킹" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3310&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-데이터베이스" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3311&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-개발방법론" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3312&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-게임" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3313&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-웹프로그래밍" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3314&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-프로그래밍 언어" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3315&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-모바일프로그래밍" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3316&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-OA/사무자동화" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3317&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-웹사이트" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3319&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-그래픽" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3321&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-멀티미디어" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3323&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-CAD" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3325&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-자격증/수험서" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3328&mallGb=KOR&orderClick=JAR",
            "컴퓨터/IT-대학교재" : "http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3329&mallGb=KOR&orderClick=JAR"
            
            }

options = Options()
'''
options.add_argument('headless') # headless 모드 설정
options.add_argument("start-maximized")
options.add_argument("disable-gpu") 
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

# 속도 향상을 위한 옵션 해제
prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2,
                                                    'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2,
                                                    'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2,
                                                    'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
options.add_experimental_option('prefs', prefs)
'''


#driver.set_window_size(1024, 600)

#category 들어가지는지 확인 - 20.11.07 문제없음
'''
for key, val in category.items():
    url = val
    try:
        driver.get(url)
        driver.back()
        print(key)
    except:
        print("Error : " + key)
'''
#manager = Manager()
#booklist = manager.list()
booklist=[]
booknum = 1


#driver.get("http://google.com")
#driver.implicitly_wait(5) #solve unable to locate element issue, refer to : https://codechacha.com/ko/selenium-explicit-implicit-wait/

#driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@name="HiddenActionFrame"]')) #iframe 진입 (필요 x)
#driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="wrapper"]')) div진입은 불가
#1페이지  > : //*[@id="eventPaging"]/div/a
#2페이지~ < : //*[@id="eventPaging"]/div/a[1]
#         > : //*[@id="eventPaging"]/div/a[2]
#끝페이지 < : //*[@id="eventPaging"]/div/a

def crawl(url):
#for key, val in category.items():
    #global booklist
    global booknum
    #url = val

    path = "C:\\Users\cmc9595\AppData\Local\Programs\Python\chromedriver_86.exe"
    driver = webdriver.Chrome(path, options=options)
    driver.implicitly_wait(5)
    driver.get(url)

    for i in range(1, 16): #1~15페이지
        for j in range(1, 40, 2): #1~20번
            try: 
                driver.find_element_by_xpath('//*[@id="prd_list_type1"]/li['+ str(j) +']/div/div[1]/div[2]/div[1]/a/strong').click() #TITLE CLICK
                title = driver.find_element_by_css_selector('div.box_detail_point > h1.title > strong') #TITLE
                print(title.text, end=" : ")
                
                
                try: 
                    keyword=[]
                    li = driver.find_elements_by_css_selector('div.book_keyword > a') #KEYWORD
                    
                    for a in li:
                        print(a.text, end=" ")
                        keyword.append(a.text)
                    print()

                    info=[]
                    info.append(title.text)
                    info.append(keyword)
                    #booklist.append(info) #ADD TO BOOKLIST
                         
                except:
                    print("Keyword Error")
                
                driver.back()
            except:
                print("bookNum < 20 Error" + "(" + str(j//2) + ")")
                break
        
        #페이지 넘김
        if i==1: #첫 페이지가 끝이면 종료
            try:
                #driver.find_element_by_xpath('//*[@id="eventPaging"]/div/a').click()
                driver.find_element_by_xpath('//*[@id="eventPaging"]/div/a').send_keys(Keys.ENTER)
                print("page"+str(i))
            except:
                print("end:page"+str(i))
                break
        else: #나머지페이지에선 > 있으면누르고 없으면 종료
            try:
                #driver.find_element_by_xpath('//*[@id="eventPaging"]/div/a[2]').click()
                driver.find_element_by_xpath('//*[@id="eventPaging"]/div/a[2]').send_keys(Keys.ENTER)
                print("page"+str(i))
            except:
                print("Category end : page"+str(i))
                break

if __name__ == '__main__':
    
    l = [category['여행-인기지역'], category['컴퓨터/IT-대학교재']]
    l1=[]
    l2=[]
    pool = Pool(processes=2)
    pool.map(crawl, l)
    #crawl(category['컴퓨터/IT-개발방법론'])

    print("total count : " + str(len(booklist)))
    
    f = open("C:\\Users\\cmc9595\\Desktop\\booklist.txt", "w")
    f.write("total count : " + str(len(booklist)))
    f.close()


#//*[@id="iframeResult"]
#/html/body/iframe

#/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/form/ul/li[1]/div/div[1]/div[2]/div[1]/a/strong
#/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/form/ul/li[3]/div/div[1]/div[2]/div[1]/a/strong
#//*[@id="wrapper"]
