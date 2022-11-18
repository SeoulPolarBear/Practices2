#http://openAPI.seoul.go.kr:8088/(인증키)/json/RealtimeCityAir/1/25/
#인증키

from http.client import HTTPConnection
from cx_Oracle import connect
from json import load, loads

#요청해서
#데이터들 가지고 parsing
hc = HTTPConnection("openAPI.seoul.go.kr:8088")
hc.request("GET", "/(인증키)/json/RealtimeCityAir/1/25/")
resBody = hc.getresponse().read()
resBody.decode()

SeoulAir = loads(resBody)


# 구 이름, 미세먼지, 초미세먼지의 정보를 DB에 담아주세요!
con = connect("[ID]/[PW]@[IP Address]:[PORT]/[SID]")
cur = con.cursor()

for r in SeoulAir["RealtimeCityAir"]["row"]:
    sql = "insert into nov15_seoulAir values(nov15_seoulAir_seq.nextval,"
    sql += f"'{r['MSRSTE_NM']}',"
    sql += f"{r['PM10']},"
    sql += f"{r['PM25']}"
    sql += ")"
    cur.execute(sql)
if cur.rowcount >= 1:
    print("등록 완료")
    con.commit()

con.close()






