#-*- coding:utf-8 -*-

# for (int i=0; ...)        : X
# for (int ii : i)            : O (Java의 for-each문에 해당하는 반복문)

l = [123,45,6,78,910]
for ll in l:
    print(ll)
print()

# ㅋ을 10번 출력
for _ in range(10):
    print("ㅋ", end = " ")
print()
# 1 ~ 20까지의 숫자 중에서 홀수만 출력
for i in range(1,20,2): # for (int zz = 1; zz < 21; zz += 2)
    print(i)
print()
########################################################################################
# while문 : 0
while True:
    y = int(input("y : "))
    if y % 2 == 0:
        print("짝수")
        break

# do{}while문 : X
########################################################################################
# enumerate : 반복문을 사용할 때 몇 번 반복되었는지 확인이 필요할 때 사용
#                (인덱스, 값) 형태의 tuple 형태로 return
ll = ["컴퓨터", "모니터", "마우스", "키보드"]
for i, v in enumerate(ll):
    print(i + 1, v, end = " / ") 
    
score = [10, 54, 56, 70, 70, 87, 65, 99, 91, 88]
# 1등학생은 몇 번째에 ? / 점수는 몇점인지 ? 출력
print()
result = [0,0];
print("1번")
for i, v in enumerate(score):
    if v == max(score):
        print(i, v)
print("2번")
for i, v in enumerate(score):
    if v > result[1] :
        result[0] = i 
        result[1] = v
print(result)

        























