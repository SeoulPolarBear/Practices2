# -*- coding:utf-8 -*-

# 3항 연산자
# [참일때의 값] if [조건문] else [거짓일때의 값]
def getWeight():
    weight = float(input("몸무게 : "))
    return weight if weight >= 0 else (-1) * weight

# weight = getWeight()
# print(weight)

# 숫자를 입력했을 때 짝수인지 홀수인지 출력해주는 프로그램 (3항 + f-string)

def OverOrEven():
    num1 = int(input("숫자 : "))
    result = "짝수" if num1 % 2 == 0 else "홀수"
    print(f"{'짝수' if num1 % 2 == 0 else '홀수'}")
    print(f"{result}")

OverOrEven()

# 3항 연산자 중첩
#[참1] if [조건1] else [참2] if [조건2] else ... [거짓]

# 15, 16, 17을 list에 담고
# 리스트 각각의 요소가 2의 배수인지 3의 배수인지, 아니면 둘 다 아닌지를 출력

num_list = [15,16,17]
for v in num_list:
    print("2의 배수") if v % 2 == 0 else print("3의 배수") if v % 3 == 0 else print("둘다 아닙니다.")



