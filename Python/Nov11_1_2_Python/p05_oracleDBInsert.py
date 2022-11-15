# -*- coding:utf-8 -*-
from cx_Oracle import connect

#1 . DB 연결
con = connect("babypolarbear/78910@203.252.32.74:1521/xe")

# 3.data확보!
# 로부스타 / 아라비카 /리베리카
# 원두당 커피 3-4개씩 
n = input("커피 이름 : ")
p = int(input("커피 가격 : "))
b = input("원두 이름 : ")


# 4. sql문 작성
#    Java : ?, ?
#    MyBatis : #{멤버변수명}
#    Python : 완성된 sql문을 사용!
#        sql문 끝나고나서 ;(세미콜론) 넣지 않는다!!
sql = "insert into nov11_coffee values(nov11_coffee_seq.nextval, '%s', '%d', '%s')" % (n,p,b)


# 5. DB관련 작업 (sql문을 서버로 전송, 실행, 결과 받기) : 총괄객체
#    Java : PreparedStatement (pstmt)
#    Python : cursor()
cur = con.cursor()

#6. 수행 (sql문을 서버로 전송, 실행, 결과 받기)
cur.execute(sql)

#7. 결과 처리
if cur.rowcount == 1: # 방금 작업 때문에 영향을 받은 행 수가 하나면...
    print("Success!") # 성공
    con.commit()      # commit을 해야 서버에 실제로 반영 O



print(sql)



# 2. DB 종료
con.close()