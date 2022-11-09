# -*- coding:utf-8 -*-

# Java vs Python
# Java : 컴퓨터 활용 효율적 -> 규칙의 언어 -> perfect한 객체지향언어
#        명확하고, 혼란스럽지 않은 코드
#        코드가 길어진다.

# Python : 사람이 쓰기 편하게 -> 자유의 언어 -> hybrid한 객체지향언어
#        코드가 짧다
#        코드가 길어지면... 헷갈릴 여지가 있음!
####################################################################################################
# 기본적인 출력 방식

print('WA! 파이썬!')
print('WA! 월요일!') # enter 기능 포함 O
print()

# seperator
print('내', '일', '월', '화', '수', '목', '금', '토', sep="        ")

# 여러분의 메일주소 출력
# 전화번호 출력
print("xxxx@xxxx.com", "010-xxxx-xxxx", sep = "    ", end = "    /    ")
print("xxxx", "xxxx.com", sep = "@", end = "    /    ")
print("010", "xxxx","xxxx", sep = "-")

# end
print('파이썬이', end=' ')
print('본격적으로', end=' ')
print('시작되었습니다.')
print()

#출력 형식(format)
print('{} and {}'.format('1번','2번'))
print('{1} and {0} and {0}'.format('1번','2번'))
print("{p1} is {p2}".format(p1 ="Life", p2="Egg"))

#%d, %f, %s
# System.out.printf("%d",123);
print("%d" % 123)
print("%.2f"% 123.2352642)

#10이라는 값을 0번째에, 11.1111111111111이라는 값을 1번째에 소수점 둘째자리까지 출력
print("%d %.2f" % (10, 11.1111111111111))
print("{0:d}, {1:.2f}".format(10,11.11111111))











