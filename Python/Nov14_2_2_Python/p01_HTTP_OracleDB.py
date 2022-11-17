# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring
from cx_Oracle import connect

# 기상청 (주소값 구해서)

# 기상청 XML -> DB에 적재
# 시간대 / 기온 / 최고기온/ 최저기온
try:
    hc = HTTPSConnection("www.kma.go.kr")
    hc.request("GET", "/wid/queryDFSRSS.jsp?zone=1165065100")
    resBody = hc.getresponse().read()
    
    resBody.decode()
    con = connect("[ID]/[PW]@[IP Address]:[PORT]/[SID]")
    cur = con.cursor()
    for f in fromstring(resBody).iter("data"):
        sql = "insert into nov14_weather values("
        sql += f"nov14_weather_seq.nextval, '{f.find('hour').text}'"
        sql += f",'{f.find('temp').text}'"
        sql += f",'{f.find('tmx').text}'"
        sql += f",'{f.find('tmn').text}')"
        #print(sql)
        cur.execute(sql)
        
        # if cur.rowcount == 1:
            # print("입력 성공")
            # con.commit()
    con.commit()

except Exception as e:
    print(e)
con.close()
print("END !")



























