# Python 3.6.x 부터 f-string이라고 부르는 포멧팅을 좀 더 쉽게 할 수 있는 방법이 추가됨
# f-string의 모양은 f와 {}만 아시면 됩니다.
# f"문자열 {변수명} 문자열..."의 형태
from datetime import datetime

#좋아하는 음료이름, 마시는 횟수 => 입력 받아서 그 내용을 출력

# drink, count = input("좋아하는 음료와 마시는 횟수를 띄어쓰기로 입력하세요 : ").split(" ") 
#
# print(f"저는 {drink}를(을) 하루에 {count}잔 마십니다.")

# 정리
# 1. 문자열 맨 앞에(따옴표 앞) 'f'를 붙인다.
# 2. 사용하고 싶은 변수, 값을 중괄호 {} 안에 넣는다.
# 3. 예쁘게 출력한다.

# 소수점 반올림 표현
# 기본적으로 % 포멧팅과 거의 유사함
# 하지만 {}를 사용해서 포맷팅 할 때는, 포맷팅하는 값의 자료형에 상관없이 {}를 사용하면 됨

f = 1.125
#f = 1.135
print(f"{f}")           # 1.125    1.135
print(f"{f:.1f}")       # 1.1      1.1
print(f"{f:.2f}")       # 1.2      1.4

# Python의 반올림은 반올림하려는 수가 올림, 내림 했을때
# 동일하게 차이가 나는 경우에는 (5가 기준이 될 때)
# 0, 1, 2만 반올림이 안 됨... (왜지...? 감자...?)

# 문자 정렬
s1 ="left"
result1 = f"/{s1:<10}/"
print(result1)

#가운데 정렬
s2 ="mid"
result2 = f"/{s2:^10}/"
print(result2)

#오른쪽 정렬
s3 ="right"
result3 = f"/{s3:>10}/"
print(result3)

# 중괄호 {}안에 있는 변수 뒤에 콜론(:) 붙인 후
# 왼쪽 정렬 (<) / 오른쪽 정렬 (>) / 가운데 정렬 (^)의 옵션을 넣어서
# 그 후에 자릿수를 알려주는 숫자를 넣어서 정렬 옵션을 완성

# f-string에서 중괄호를 출력...?
num = 10
result4 = f"my age : {{{num}}}"
print(result4)

# 중괄호를 연속해서 2개를 사용하면 ({{}}), 중괄호 자체를 출력할 수 있음
# f-string의 값과 중괄호까지 같이 표현하려면,
# {{{}}}중괄호 3개를 입력하면 num을 변수값으로 인식하게 됨

#f-string과 dict
d = {
        "name" : "polarbear",
        "gender" : "남자",
        "age" : 100
    }

result5 = f"name : {d['name']}, gender : {d['gender']}, age : {d['age']}"
print(result5)

#f-string과 list
n = [100, 200, 300]

# 각 요소를 출력
for v in n:
    print(f"List : {v}")
    
# 기존에 리스트에 접근하는 방법과 동일하게 {}안에 리스트에 대한 접근을 활용하면 됨!
print("----------------------------------------------------------")
num2 =1234567890
print(num2)

#1, 234,567,890
print(f"{num2:,}") # 1000단위씩 , 찍어준다.

date1 = datetime.today()
print(date1)
#연-월-일 -> 요일
print(f"{date1:%Y-%m-%d} is on a {date1:%A}")

























