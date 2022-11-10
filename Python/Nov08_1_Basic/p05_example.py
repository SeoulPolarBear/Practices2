# -*- coding:utf-8 -*-
import random

# UP/DOWN 게임 (함수)
# 유저의 이름을 입력 받고 환영하는 인사를 출력
def welcome():
    name = input("당신의 이름을 입력하세요. : ")
    print(f"{name}을 환영합니다!")
    return name

# (컴퓨터) 1 ~ 100사이의 랜덤한 숫자를 하나 뽑아서
def computer():
    com = random.randint(1,100)
    print("컴퓨터가 값을 골랐습니다.")
    return com
def explainRule():
    print("=======================================")
    print("1~100까지만 입력하세요.")
    print("=======================================")

# 유저에게 정답을 입력하게 했을 때
def challenge():
    user = int(input("값을 입력해 주세요. :"))
    return user;

# 저 범위의 숫자가 아니면 다시 입력하도록
# 입력한 숫자가 정답보다 작으면 'UP', 크면 'DOWN' 출력
# 정답을 맞췄을 때는 몇 번만에 맞췄는지 출력 + 종료
# 정답 기회는 총 10번
def game(com):
    count = 0
    while count < 10:
        answer = challenge();
        if 1 <= answer and answer <= 100 :
            count += 1
            print(f"{count}째 도전이었습니다.")
            if answer == com:
                print(f"정답입니다! {count}만에 맞췄습니다. 정답은 {com}")
                print("=======================================")
                break
            elif answer < com:
                print('UP')
                print("=======================================")
            else:
                print('DOWN')
                print("=======================================")
        else:
            print("다시 입력하세요. : ")
            print("=======================================")
        if count == 10:
            print(f"게임 종료 {count} 횟수 끝났습니다. 당신의 패배")
            print("=======================================")
            
#########################################################################################################
welcome()
explainRule()
game(computer())
        
        







































