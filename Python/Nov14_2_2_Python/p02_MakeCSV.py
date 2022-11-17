# -*- coding:utf-8 -*-
from cx_Oracle import connect

con = connect("[ID]/[PW]@[IP Address]:[PORT]/[SID]")
sql = "select * from nov14_weather order by w_no"
cur = con.cursor()
cur.execute(sql)
file = open("C:/Users/user/Desktop/python/test/weather.csv", "a",newline ='',encoding="UTF-8")
file.write("번호,시간,기온,최고기온,최저기온\n")
for n,h,t,max,min in cur:
    file.write(f"{n},{h},{t},{max},{min}\n")

print("잘들어갔습니다.")
file.close()
con.close()

