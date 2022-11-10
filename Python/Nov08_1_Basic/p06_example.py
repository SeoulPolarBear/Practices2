# -*- coding:utf-8 -*-
import random


#Java(null) = Python(None)

#가위바위보 -> 한번 질 때까지 -> 총 몇 번 이겼는지 출력
# 가위 : 0, 바위 : 1, 보 : 2
def computer():
    com = random.randint(0, 2)
    print("컴퓨터가 낼 것을 정했습니다.")
    return com

def user():
    user = int(input("가위 : 0, 바위 : 1, 보 : 2  =>  " ))
    if user == 0:
        print("유저가 가위를 냈습니다.")
    elif user == 1:
        print("유저가 바위를 냈습니다.")
    elif user == 2:
        print("유저가 보를 냈습니다.")
    else:
        print("유저가 이상한걸 냅니다.")
    return user
    
def resultPrint(com, user,count):
    result = com - user;
    if result == 0:
        print("비겼습니다.")
        print("====================================================")
        return True, count
    elif result == 1 or result == -2:
        print("졌습니다.")
        print("====================================================")
        return False, count
    elif result == -1 or result == 2: 
        count += 1
        print(f"{count}번이겼습니다.")
        print("====================================================")
        return True, count
    else:
        print("다시 입력하세요")
        print("====================================================")
        return True, count

def game():
    result = True
    count = 0;
    while result:
        result, count = resultPrint(computer(), user() ,count)
    print(f"총 {count}승 게임 끝!")
    print("====================================================")
        
game()
########################################################################################################
handtable = [None, "가위", "바위", "보"]

def printRule():
    print("=================================")
    for i, h in enumerate(handtable):
        if i != 0:
            print("[%d] %s" % (i,h))
    print("==================================")
    
def comFire():
    return random.randint(1, 3)

def userFire():
    print("=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=--==--==-=-=-")
    uh = int(input("뭐 낼 까? :"  ))
    print("=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=--==--==-=-=-")
    if(1 <= uh <= 3):
        return uh
    return userFire()

def printHandle(uhuh, chch):
    print("유저 : %s" % handtable[uhuh])
    print("컴퓨터 : %s" % handtable[chch])
    
def judge(uhuh,chch):
    t = uhuh - chch
    if t == 0:
        print("무승부")
        return 0
    elif t == -1 or t == 2:
        print("패배")
        return 999
    else:
        print("승리")
        return 1

def playGame(uHand, cHand, result, win):
    while True:
        uHand = userFire()
        cHand = comFire()
        printHandle(uHand, cHand)
        result = judge(uHand, cHand)
        if result == 999:
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("종료")
            break
        win += result
    print("%d승으로 종료 !"%win)
########################################################################################################
printRule()
uHand, cHand, result, win = 0,0,0,0
playGame(uHand, cHand, result, win)
    
    
    
    
    
    
    
    
    
