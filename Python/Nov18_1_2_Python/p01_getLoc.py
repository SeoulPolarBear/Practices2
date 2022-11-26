# -*- coding:utf-8 -*-
#(인증키)
#3d!4d
from http.client import HTTPSConnection
from urllib.parse import quote
from json import loads
from cx_Oracle import connect

#검색어를 입력 
#            -> 위도 / 경도 지정 x 127.11116 y 37.394776
#            ->반경 1km내에 있는
#            ->검색어에 대한 위치 정보
#
#            -> 장소명(업체명), 전화번호, 경도, 위도
#            -> DB에 저장
#            -> 전화번호 : 없는 부분은 '-'으로 대체
#            -> 경도, 위도 : 소수점 6자리까지
q = quote(input("원하는 검색어를 입력하세요. : "))
x ="127.11116" # 경도
y = "37.394776" # 위도
radius = 1000
category_group_code = "FD6"
h ={"Authorization" : "KakaoAK ${인증키}"}
hc = HTTPSConnection("dapi.kakao.com")
hc.request("GET", 
            f"/v2/local/search/keyword.json?query={q}&category_group_code={category_group_code}&x={x}&y={y}&radius={radius}", 
            headers = h)
res = hc.getresponse().read().decode()
#print(res)
res= loads(res)
print(res)

con = connect("babypolarbear/78910@203.252.32.74:1521/xe")
cur = con.cursor()
for d in res["documents"]:
    # if d['phone'] == "":
        # d['phone'] = "-"
    sql=f"insert into nov18_map values(nov18_map_seq.nextval,'{d['place_name']}',"
    sql += f"nvl('{d['phone']}','-'),{d['x']},{d['y']})"
    cur.execute(sql)
if cur.rowcount >= 1:
    print("등록 성공")
    con.commit()
con.close()
hc.close()















































