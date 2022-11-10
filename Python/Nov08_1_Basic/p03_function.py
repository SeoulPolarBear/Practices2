#-*- coding:utf-8 -*-

# function(함수)
# def 함수명(파라미터명):
#    code

def test():
    print("배부른 polarbear")
#################################################################################
def test2():    # :을 썼으면 그 다음줄에는 반드시 들여쓰기를 해야!
    pass        # :뒤에 코드 적을 것이 없을 때, 자리채워주라는 의미

# 정수 2개를 넣으면 그 합을 '출력'하는 함수
def printHab(a = 5, b = 8): #호출할 때 값을 안 넣어주면 파라미터의 값을 기본값으로 사용
    print(a + b)

# 정수 3개를 넣으면 그 합을 '출력'하는 함수
# def printHab(a,b,c): # overloading이 안 됨 -> 모든 함수명이 다 달라야...
    # print(a + b + c)
def printHab2(a,b,c): # overloading이 안 됨 -> 모든 함수명이 다 달라야...
    print(a + b + c)
    
# 정수 2개를 넣으면 그 합을 '구하는' 함수
def getHab(a, b):
    return a + b 
    
def sum2(a, b):
    print(a + b)
    
sum2((lambda a, b : a + b) (10 , 20), (lambda a, b : a + b) (10, 43))
sum2(1, 2)
printHab()
printHab2(1, 2, 3)
print(getHab(1, 2))
    
# 정수 2개를 넣으면 사칙연산 결과를 '구하는' 함수
def cal(num1, num2):
    dict_cal = {}
    dict_cal["+"] = num1 + num2
    dict_cal["-" ] = num1 - num2
    dict_cal["*"] = num1 * num2
    dict_cal["/"] = num1 / num2
    return dict_cal
num1, num2 = list(map(int,(input("정수 2개 띄워쓰기로 입력 : ").split(" "))))

def calc (a, b):
    
    '''
        설명서...
        이 설명서는 1743년 부터 시작 됨 
        주석 아님 문자열 임
    '''
    
    
    q = a + b
    w = a - b
    m = a * b
    k = a / b
    return (q,w,m,k)

print(calc(num1,num2))
print(cal(num1, num2))

# 아래와 같이 _을 이용하면 안 가져 올 수도 있다.
u,i,_,p = calc(20,10)
print(u,i,p)
help(calc)
help(print)
###########################################################################################    










