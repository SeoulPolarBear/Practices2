# -*- coding:utf-8 -*-
from cx_Oracle import connect

# Table 데이터 -> 번호값 제외한 모든 데이터 -> CSV 파일에 담는 작업

con = connect("[ID]/[PW]@[IP Address]:[PORT]/[SID]")
cur = con.cursor()
sql = "select * from nov18_map order by m_id"
cur.execute(sql)
with open("C:/Users/user/Desktop/python/test/pizza.csv", "w", encoding ="UTF-8") as f:
    f.write("장소, 번호, 경도, 위도\n")
    for _,place,phone,long,lat in cur:
        f.write(f"{place},")
        f.write(f"{phone},")
        f.write(f"{long},")
        f.write(f"{lat}\n")
    print("파일 출력 성공")    
f.close()    
con.close()