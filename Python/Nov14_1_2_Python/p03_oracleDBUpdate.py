# -*- coding:utf-8 -*-
from cx_Oracle import connect

# input 2개 : 원두 이름 검색 / 숫자를 입력
# 검색한 원두를 사용하는 커피의 가격을 => 입력한 숫자만큼 가격을 인상

bean = input("원두 이름을 검색하세요 : ")
price = int(input("인상 가격을 입력하세요 : "))

try:
    con = connect("[ID]/[PW]@[IP Address]:[PORT]/[SID]")
    sql = "update nov11_coffee set c_price = c_price + %d where c_bean = '%s' " % (price, bean)
    cur = con.cursor()
    cur.execute(sql)
        
    if cur.rowcount >= 1:
        print("가격 인상 성공")
        con.commit()
   
except Exception as e:
    print(e)

con.close()