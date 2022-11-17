# -*- coding:utf-8 -*-
from cx_Oracle import connect

# select 번호순으로 조회 -> 번호를 입력하면 -> 그 데이터가 삭제!
# 999를 입력하게 되면 프로그램이 종료

try:
    con = connect("[ID]/[PW]@[IP Address]:[PORT]/[SID]")
    sql = "select * from nov11_coffee order by c_no"
    cur = con.cursor()
    cur.execute(sql)
    
    for n, name, p, b in cur:
        print(n, name, p, b)
        print("========================================")
    
    num = 0
    
    while num != 999:
        num = int(input("삭제할 커피의 번호를 입력하세요 : "))
        sql2 = "delete from nov11_coffee where c_no = %d " % num 
        cur.execute(sql2)
        
        if cur.rowcount == 1:
            con.commit()
            print("삭제 성공")
        
        
except Exception as e:
    print(e)
    
con.close()
    
