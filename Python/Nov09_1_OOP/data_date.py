# -*- coding:utf-8 -*-
from datetime import datetime, date


#현재시간 날짜
# datetime 두번째 _없는거 불러오면 된다.
now = datetime.today()
print(now)

# 특정 시간 날짜
yesterday = datetime(2022, 11, 8)
print(yesterday)
print(type(yesterday))
print(yesterday.year)
print(type(yesterday.year))
print(yesterday.month)
print(yesterday.day)

#생일을 입력받아서 나이를 계산해주는 프로그램(출력)

def MyAge():
    list_age = list(map(int, input("생년월일 입력하세요 ex)1999-01-01 : ").split("-")))
    return list_age

def nowAbout():   
    list_now2 = []
    list_now2.append(datetime.today().year)
    list_now2.append(datetime.today().month)
    list_now2.append(datetime.today().day)
    return list_now2

def CalAge(list_age, list_now2):
    age = list_now2[0] - list_age[0] + 1
    age_man = list_now2[0] - list_age[0]
    if list_age[1] >= list_now2[1]:
        age_man -= 1
    elif list_age[2] >= list_now2[2]:
        age_man -= 1
    return age, age_man
        
birthday = "1999/01/01"
# strptime : str -> datetime
bd = datetime.strptime(birthday, "%Y/%m/%d")
print(bd)
# strftime : datetime -> str
bd = datetime.strftime(bd, "%A")
print(bd)

print(CalAge(MyAge(), nowAbout()))
#########################################################################
#Pattern
# %Y : 연도 4자리 / %y : 연도 뒤에 2자리
# %m : 월 / %d : 일 / %H : 시간 (24시간) / %I : 시간(12시간) / %p : AM, PM
# %M : 분 / %S : 초 / %a : 요일 (짧게 / 'Wed') / %A : 요일(길게 / 'Wednesday')
##########################################################################
# 특정 날짜를 연/월/일 형태로 입력 받아서 -> 일/월 형태의 문자열로 출력
def changeDate():
    now3 = input("xxxx/xx/xx형태로 날짜를 입력해 주세요. : ")
    print(type(now3))
    now3 = datetime.strptime(now3,"%Y/%m/%d")
    print(type(now3))
    now3 = datetime.strftime(now3,"%d/%m")
    print(type(now3))
    print(now3)
    
changeDate()











































