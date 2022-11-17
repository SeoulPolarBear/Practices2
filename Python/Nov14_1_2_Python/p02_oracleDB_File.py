# -*- coding:utf-8 -*-
from cx_Oracle import connect
import csv

# DB연결 -> 커피 이름, 가격, 원두 정보 -> .csv파일로 생성(,를 기준으로)
# ex) 이름,가격,원두
#     이름,가격,원두
#     ...
try:
    con = connect("[ID]/[PW]@[IP Address]:[PORT]/[SID]")
    sql = "select c_name, c_price, c_bean from nov11_coffee order by c_price"
    cur = con.cursor()
    cur.execute(sql)
    #newline ='' 없으면 한줄씩 띄워서 저장이 되고 있으면 하나의 enter를 기준으로 저장이 된다.
    # 아메리카노,4000,아라비카
    
    # 아메리카노,4000,리베리카
    
    # 아메리카노,4000,로부스타
    
    # 아메리카노,4000,아라비카
    # 아메리카노,4000,리베리카
    # 아메리카노,4000,로부스타

    file = open("C:/Users/user/Desktop/python/test/coffee.csv","a",newline ='',encoding = "UTF-8") 
    wr = csv.writer(file)
    for c,p,b in cur:
        wr.writerow([c,p,b])
        file.write(f"{c},{p},{b} \n")
except Exception as e:
    print(e)
    
file.close()
con.close()
print("\nEND")








