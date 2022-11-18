# -*- coding:utf-8 -*-
from cx_Oracle import connect

# DB에 있는 미세먼지 데이터 -> csv에 저장

con = connect("[ID]/[PW]@[IP Address]:[PORT]/[SID]")

cur = con.cursor()
sql = "select * from nov15_seoulAir order by sa_no"
cur.execute(sql)

file = open("C:/Users/user/Desktop/python/test/seoulAir.csv", "a", newline ="", encoding = "UTF-8")


file.write("번호, 지역, 미세먼지, 초미세먼지\n")
for no, msrste_nm, pm10, pm25 in cur:
    file.write(f"{no}, {msrste_nm}, {pm10}, {pm25}\n")
    
    
print("csv 등록 완료")
file.close()
con.close()
    
