#
# # str
# s = "Can`t tuna kkk"
# print(s)
# print(s[0])
# print(s[0:6])       # (0번째 부터 (6-1)번째까지의 문자열)
# print(s[2:10:2])    # (2번째 부터 (10-1)번째까지의 문자열을 2칸씩 건너서 출력)
# print("---------------------------------------------------------------------------------")
#
# # List : 리스트 (순서 O, 중복 O, 수정 O, 삭제 O)
# a = [123, 4, 56, 789, 1011]
# print(a, type(a))
# print(a[0])
# print(a[0:3])
# print(a[0::2])
# print(a[:-1]) # 뒤에서 첫번째
#
# print(len(a))       #요소의 갯수
# a.append(1234)      #끝에 요소 추가
# a.insert(2, 1235)   #중간에 요소 추가
#
# print(a)
# a[4] = 7788
# print(a)
# del a[0]
# print(a)
#
# a.sort()            #오름차순
# print(a)
# a.sort(reverse=True)#내림차순
# print(a)

print("---------------------------------------------------------------------------------")

# Tuple : 튜플 (순서 O, 중복 O, 수정 x, 삭제 x)
tuple1 = ("1","2","3")
print(tuple1)
# del tuple1[0]    #삭제 안 됨
# tuple1[0] = 'c'  #수정 안 됨

t = (1,2,3,4,5,4,4,4)
print(t)
print(t.index(5))   # index안의 요소가 있는 위치를 반환
# index안의 요소가 튜플안에 몇 개가 있는지 그 갯수를 반환
print(t.count(4))

a1, b1 = 20, 10
print(a1, b1)
a1, b1 = b1, a1 #튜플에 넣어서 서로의 값 바꾸기
print(a1, b1)

x,y,z = 10, 20, 30
x,y,z = z,x,y
print(x,y,z)

print("---------------------------------------------------------------------------------")

# Set : 집합 (순서 X, 중복 X, 수정 X, 삭제 O)
s = {"ㅋ", "ㅋ","ㄹ", "ㅃ", "ㅃ"}
print(len(s))
s = list(s)
print(s)
print("---------------------------------------------------------------------------------")

# Dict : 딕셔너리(= map) (순서 X, 중복 X, 수정 O, 삭제 O) - MongoDB / ElasticSearch
d = {"name" : "곽두팔", 13 : 12}
print(type(d))

print(d["name"])
print(d[13])

print("---------------------------------------------------------------------------------")
# Range
r = range(10)       # (0 ~ 9)까지의 범위
r = range(2, 10)    # (2~ 9)까지의 범위
r = range(2, 10, 3) # (2~ 9)까지, 3칸씩
print(r, type(r))

# 0 ~ 9까지 있는 list
r2 = range(10)
r2 = list(r2)
print(r2, type(r2))

# 1~ 20까지 홀수만 있는 list 출력
print(list(range(1,20,2)))
print([2*i + 1 for i in range(10)])











