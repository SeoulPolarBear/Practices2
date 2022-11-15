from cx_Oracle import connect

# 원두를 검색해서
# 그 원두를 사용하는 커피의 종류 갯수, 평균가를 출력

con = connect("[ID]/[PW]@[IP Address]:[PORT]/[SID]")

# 검색
b = input("원두 : ")

#sql
sql = "select count(*), avg(c_price) from nov11_coffee "
sql += f"where c_bean = '{b}'"

cur = con.cursor()

cur.execute(sql)

for c, a in cur:
    print(c, a)
    
# 연결 종료
con.close()