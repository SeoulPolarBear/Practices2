# -*- coding:utf-8 -*-
from cx_Oracle import connect
from datetime import datetime

#메뉴만들기(함수)
#1. 학생 등록 / 2. 강의장 조회 / 3. 학생 조회 / 4. 학생정보를 파일로 내보내기
#0. 종료

def menu():
    print("1. 학생 등록")
    print("2. 강의장 조회")
    print("3. 학생 조회")
    print("4. 학생정보를 파일로 내보내기")
    print("0. 종료")
    print("---------------------------------------------------")
    num = int(input("다음 중 원하는 번호를 입력하세요. :"))
    print("---------------------------------------------------")
    return num

#1. 학생 등록
def insertStudent():
    con = connect("[ID]/[PW]@[IP Address]:[PORT]/[SID]")
    try:
        cur = con.cursor()
    
        s_name = input("학생이름 : ")
        s_birthday = input("학생 생일(xxxxxxxx) :")
        s_lh_no = input("강의장 (번호만 적을 것) :")
        s_mid_exam = input("중간 점수 :")
        s_final_exam = input("기말 점수 : ")
        print("------------------------------------------------------------------")
        #print(s_birthday)
        sql_s_insert ="insert into nov15_student values(nov15_student_seq.nextval,"
        sql_s_insert +=f"'{s_name}',"
        sql_s_insert +=f"to_date('{s_birthday}','yyyymmdd'),"
        sql_s_insert +=f"{s_lh_no},"
        sql_s_insert +=f"{s_mid_exam},"
        sql_s_insert +=f"{s_final_exam})"
        cur.execute(sql_s_insert)
        if cur.rowcount == 1:
            print("등록 성공")
            print("==================================================================")
            con.commit()
    except Exception as e:
        print(e)
    con.close() 
    
#2. 강의장 조회 
def getLectureHall():
    con = connect("[ID]/[PW]@[IP Address]:[PORT]/[SID]")
    try:
        cur = con.cursor()
        
        lecture_num = input("강의장 번호를 입력하세요 : ")
        sql_l_select =f"select * from nov15_lecture_hall where lh_no = {lecture_num}"
        cur.execute(sql_l_select)
        #print(cur)
        for r in cur:
            #print(r)
            print(f"{r[0]} 강의장 - {r[1]}")
        print("============================================================")
    except Exception as e:
        print(e)  
    con.close() 
        
#3. 학생 조회 
def getStudentbyName():
    con = connect("[ID]/[PW]@[IP Address]:[PORT]/[SID]")
    try:
        cur = con.cursor()
        
        s_name = input("이름을 입력하세요 : ")
        print("------------------------------------------------------------------")
        sql_l_select =f"select * from nov15_student where s_name = '{s_name}'"
        cur.execute(sql_l_select)
        for no,name,birthday,lh_no,mid_exam,final_exam in cur:
            print(f"번호 : {no}")
            print(f"이름 : {name}")
            s_birthday2 = datetime.strftime(birthday, '%Y-%m-%d')
            s_birthday3 = datetime.strftime(birthday, '%A')
            print(f"생년월일 : {s_birthday2}, {s_birthday3}")
            now = datetime.today()
            #print(type(birthday))
            age = now.year - birthday.year + 1
            print(f"나이 : {age}세")
            print(f"강의장 : {lh_no} 강의장")
            print(f"중간 점수 : {mid_exam} 점")
            print(f"기말 점수 : {final_exam} 점")
            print(f"평균 점수 : 평균 {(mid_exam + final_exam)/2 : .2f} 점")
            print("============================================================")
            
    except Exception as e:
        print(e)
    con.close()
#4. 학생정보를 파일로 내보내기
def writeFileStudent():
    con = connect("[ID]/[PW]@[IP Address]:[PORT]/[SID]")
    try:
        cur = con.cursor()
        print("------------------------------------------------------------------")
        sql_l_select =f"select * from nov15_student order by s_name"
        cur.execute(sql_l_select)
        file = open("C:/Users/user/Desktop/python/test/student.csv", "w", encoding="UTF-8",newline="")
        file.write("이름, 생년월일, 나이, 강의장, 중간 점수, 기말 점수, 평균 점수\n")
        for _,name,birthday,lh_no,mid_exam,final_exam in cur:
            s_birthday2 = datetime.strftime(birthday, '%Y-%m-%d')
            s_birthday3 = datetime.strftime(birthday, '%A')
            now = datetime.today()
            age = now.year - birthday.year + 1
            result = f"{name},{s_birthday2} {s_birthday3},{age}, {lh_no} 강의장,{mid_exam} 점"
            result += f",{final_exam} 점,{(mid_exam + final_exam)/2 : .2f} 점\n"
            file.write(result)
        print("내보내기 성공")
        print("============================================================")
        
    except Exception as e:
        print(e)
    file.close()
    con.close()
#0. 종료
def BeStop(num):
    return False if num == 0 else True

# 강의장 조회 : 1강의장 - 7층 복도 오른쪽
# 학생 조회 : 이름, 생년월일(연-월-일)(+요일), 나이, 몇 강의장,
#                중간고사점수, 기말고사점수, 평균 점수

#파일로 내보내기(학생의 전체 정보 다 csv 파일로)
