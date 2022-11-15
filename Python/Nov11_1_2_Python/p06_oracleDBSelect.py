from cx_Oracle import connect

#r각각의 커피 이름, 가격, 원두 정보 가격 오름차순으로 정렬해서 출력
#    (select 결과가 cur에 들어가게 됨)

con = connect("[ID]/[PW]@[IP Address]:[PORT]/[SID]")

#sql문 작성
sql = "select c_name, c_price, c_bean from nov11_coffee order by c_price"

# DB관련 총괄 객체 / sql 수행 결과(select문 결과 객체)
cur = con.cursor() 

#sql문 수행 
cur.execute(sql) # 수행하면 select의 결과가 cur에 tuple로 들어가게됨

# for c in cur:
    # print(c, type(c))
    
for n, p, b in cur:
    print(n, p, b)
    print("------------------------------------------------")
    
con.close()
    