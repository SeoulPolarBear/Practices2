from cx_Oracle import connect

#OracleDB와 연동이 되는 Java : instantClient에 있는 ojdbc8.jar
#OracleDB와 연동이 되는 Python : cx_Oracle.py(가 instantClient를 사용)

#기본적으로 python에는 OracleDB 연결 기능이 없어요...
#cx_Oracle.py -> ojdbc8.jar를 사용
#시작 -> CMD -> pip install cx_oracle
# pip list -> 잘 설치 됐나 확인

#sqlplus로 접속할 때 사용하는 주소
#    sqlplus [ID]/[PW]@[IP Address]:[PORT]/[SID]


try:
    c = connect("[ID]/[PW]@[IP Address]:[PORT]/[SID]")
    print("Success!")
except Exception as e:
    print(e)

c.close()
    
    
    
    
    
    