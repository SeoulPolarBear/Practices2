# -*- coding:utf-8 -*-
#
# # 정수 2개 입력 받아서, 사칙연산에 대한 결과와 
# # 앞의 수를 뒤의 수로 나눴을 때의 나머지 값을 출력
#
# a = int(input("피연산자 1 : "))
# b = int(input("피연산자 2 : "))
#
# print(f"a + b  = {a + b}")
# print("a - b  = {}".format(a - b))
# print("a * b  = %d" % (a * b))
# #나누기
# print("a / b  = {0:.2f}".format(a / b))
# # 몫 구하기
# print("a // b = {0}".format(a // b))
# print(f"a % b = {a % b}")
#
# # 거듭 제곱
# x = 6
# y = 4
# g = x ** y 
# print(g)
#
# z = "ㅋㅋㅋ"
# #h = x + z 
# #print(h) # 숫자 + 문자열 -> 불가능!
# h = str(x) + z # 문자열 결합
# print(h)
#
# i = x * z
# print(i) # 숫자 * 문자열 -> 문자열 반복
#
# ##############################################################
# x = 3
# x += 3
# print(x)
#
# #x++ # 존재하지 않습니다.
#
# j = x > 10
# print(j)
#
# # && : and, || : or
# k = (x > 10) and y < 3
# print(k)
#
# # ! : not
# l = not k
# print(l)
#
# # m : x가 5이상 ~ 10 이하 : True / 아니면 False 출력
# m = True if 5 <= x and x <= 10 else False
# print(m)
# ######################################################################
# # 3항 연산자
# # Python에는 있다고 하는 사람도 있고, 없다고 하는 사람도 있음...
# # [참일때의 값] if [조건식] else [거짓일 때의 값]
# m = True if 5 <= x and x <= 10 else False
# print(m)

# 정수를 하나 입력받아서 -> 그게 짝수면 '짝수', 홀수면 '홀수' 출력
x1 = int(input("정수를 입력하세요 : "))
print("짝수" if x1 % 2 == 0 else "홀수");




































