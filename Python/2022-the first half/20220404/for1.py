# #for 문 구조
# #for i in <collection>


# # 인자 in 리스트 의 개념
# q = [10, 20, 30]
# w = {70, 80, 90, 90}
# e = {"name": 'Lee', "city": "Seoul", "grade": "A"}
# r = (10, 12, 14)

# print(15 in q)
# print(90 in w)
# print(12 not in r)
# print("name" in e)  # key 검색
# print("seoul" in e.values())  # value 검색

# test_list = ['one','two','three']

# for i in test_list:#초기값, 끝값, 스탭을 리스트에서 가져온다. 단지 우리가 쓰지 않을 뿐 i는 리스트의 값들을 하나하나 가져와서 출력해 준다.
#     print(i)
    
# print(range(10))
# print(list(range(10)))
# for v1 in range(10): # 0~9 9까지 표현
#     print("v1 is :", v1)
# print()
# for v1 in range(10):
#     print(1)
# print()
# for v2 in range(1,11): #1~10
#     print("v2 is :", v2)
# print()

# for v3 in range(1,11,2):#1~10 2
#     print("v3 is : ", v3)
# print()


# sum1 = 0 #초기화보다는 id 즉 객체를 생성해주는 과정이 필요하다. 그에 필요한 0일 뿐이다.
# for v in range(1,1001):
#     sum1 += v # sum1 = sum1 + v / #sum1 -=v #sum1 = sum-v

# print("1~1000 sum is : %d"%sum1)

# names = ["Kim", "Park", "Cho", "Son", "Lim", "Lee"]

# for name in names:
#     print("You are", name)


#continue

# marks = [90,25,67,45,80]
# number = 0
# for mark in marks:
#     if mark < 60:
#         continue
#     print("%d번 학생 축하합니다. %d로 합격입니다."%(number,mark))
    
for i in range(2,10):
    for j in range(1,10):
        print('%d*%d ='%(i,j),i*j, end = " ")#개행을 막기 위해서 end 사용 sep(/)는 ,으로 구분된 곳에서 / 구분 end 마지막 부분에 넣고 개행 대신 " "을 넣는다. end의 default가 \n이라는 소리
    print(" ")#개행을 하기 위해서 사용
    
#iterable자료형 반복, 파이썬에서 Iterables 라고 하는 것은 반복하는 객체를 의미
#문자열, 리스트, 튜플, 집합, 사전
#iterable 리턴함수 : range, reversed, enumerate, filter. map, zip

#예제1
#문자열도 시퀀스 형이기 때문에 Iterable 하기 때문에 사용 가능
word = "beautiful"
for s in word:
    print("word : ", s)
    
#예제 4

my_info = {
    "name" : "Lim",
    "Age" : 27,
    "City" : "Seoul"
}

for key in my_info:#key만 가져온다.
    print( key,":",key)
    
for key in my_info:#key에는 key 값만 저장된다.
    print(key, ":", my_info.get(key))#이를 통해 value를 가져온다. 즉, key와 value 같이 사용 가능
    
for val in my_info.values():#val에 vlaue자체를 가져와도 된다.
    print(val)
    
#예제5
name = 'FineApplE'

for n in name:
    if n.isupper():# isupper는 대문자이면 True 아니면 false // 반대로 islower는 소문자면 True 아니면 False
        print(n)#대문자면 출력
    else:
        print(n.upper())#소문자이면 대문자로 바꿔서 출력

for n in name:
    if n.islower():#위에와 그대로 결과가 나온다.
        print(n.upper())
    else:
        print(n)        
        
        
        
numbers = [14, 3, 4, 7, 10, 24, 2, 34, 5 ,6 , 1 , 21]
for num in numbers:
    if num == 34:
        print("Found : 34!")
        break
    else:
        print("Not found : ", num)
        
It = ["1",2,5, True, 4.3, complex(4)]

for v in It:
    if type(v) is bool:
        continue
    print("current type : ", type(v))


n = 10

while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print("n == 5여서 while문이 종료 되었습니다.")#while문의 조건이 이외의 사항이 벌어졌으므로 else를 통해서 while문이 종료되었다는 것을 알려준다.
    #즉, 여려개의 elif라고 생각하자
    

numbers = [14, 3, 4, 7, 10, 24, 2, 35, 5 ,6 , 1 , 21]
for num in numbers:
    if num == 34:
        print("Found : 34!")
        break
else:
    print("Not found  34...")# 즉 while, for문의 else는 조건문을 다 돌았는데도 값이 없을 경우 마무리할 때 사용한다.
    #예 34를 찾고 있는데 34가 numbers에 없어서 for문의 조건식을 못 맞춰서 else문을 시행하게 되었다.
    
    


            
