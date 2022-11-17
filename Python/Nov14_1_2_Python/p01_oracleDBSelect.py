# -*- coding:utf-8 -*-
from cx_Oracle import connect

# 커피테이블 활용
# input으로 숫자 2개를 입력 => 가격순(오름차순)으로 정렬해서
#                            => ? ~ ?번째까지의 평균 가격을 출력

min1, max1 =  list(map(int,input("숫자 2개를 띄워쓰기로 입력하세요(작은 수가 앞에 와야 합니다.) : ").split(" ")))

con = connect("[ID]/[PW]@[IP Address]:[PORT]/[SID]")

sql = "select avg(c_price) from "
sql += "(select rownum as num ,c_price from  " 
sql += "(select c_price from nov11_coffee order by c_price)) " 
sql += f"where num between {min1} and {max1}"


cur = con.cursor()

cur.execute(sql)

for c in cur: # cur안에 tuple형태로 결과가 담김
    print(c)
    print(c[0])
    print(type(c))
    
con.close()



