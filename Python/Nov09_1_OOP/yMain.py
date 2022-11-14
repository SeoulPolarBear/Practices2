#-*- coding:utf-8 -*-
import random

def welcome():
    name = input("이름을 입력해유. : ")
    print(f"{name} 어서와유")
# 숫자야구 (3자리) (함수) (각 자릿수의 숫자는 중복 X)
# 012~ 987 중에 랜덤한 숫자가 정답
def computer():
    com = set()
    com2 = []
    while len(com) < 3:
        com.add(random.randint(0, 9))
    for _ in range(3):
        com2.append(com.pop())
    print("컴퓨터가 모든 숫자를 골랐써유.")
    return com2

# 유저가 입력 -> 자릿수와 값까지 같으면 S, 자릿수는 다른데 값이 같으면 B
def challenge():
    print("==============================================================")
    while True:   
        user = list(map(int,input("1 2 3 처럼 띄워쓰기로 구별해서 입력해여 빨리혀. :").split(" ")))
        if len(set(user)) < 3:
            print("다시 입력혀")
        else:
            break
    return user

# S가 3개 나오면 정답! -> 종료
def check(com, user):
    ball ,strike = 0, 0
    for i,v in enumerate(user):
        com_check = set([com[(i + 1) % 3], com[(i + 2) % 3]])
        if v == com[i]:
            strike += 1
        elif v in com_check:
            ball += 1
        else:
            pass
    return ball, strike

def result(com):
    strike = 0
    count = 1
    input_list = []
    while strike != 3:
        user = challenge()
        input_list.append(user)
        ball, strike = check(com, user)
        print(input_list)
        print("---------------------------------------------------------------")
        print(f"{count}회전", end = " ")
        if strike == 3:
            print("...아따 정답이유!")
            break
        else:
            print(f"...에라이 {strike} strike {ball} ball 이네.")
            count += 1
        
            
######################################################################################
welcome()
com = computer()
result(com)


















