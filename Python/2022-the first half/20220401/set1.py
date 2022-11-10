# s1 = set([1,2,3])
# print(s1)
# print(type(s1))

# s2 = set('hello')

# print(s2)

# s11= set([1,2,3,4,5,6])
# s12 =set([4,5,6,7,8,9])
# print(s11 & s12)
# print(s11.intersection(s12))
# print(s11|s12)
# print(s11.union(s12))
# print(s11 - s12)
# print(s11.difference(s12))

# s12.add(19)# 1개 요소 추가
# print(s12)
# s12.update([1,2,3])#list 형태로 전달
# s12.remove(19);print(s12)#argument는 삭제할 value 값이다.

# new1_s1 = tuple(s1)
# new2_s1 = list(s1)
# print(new1_s1);print(new2_s1)
# new2_s1.append(4)
# new2_s1.append(10)
# s3 = set(new2_s1)
# print(s3)
# #set의 최대 장점은 list나 투플 등에 존재하는 중복값을 없애는 용도로 사용할 수 있단느 것이다.
# print("length s3 is %d"%len(s3))

s13 = set([1,2,3,4,5,6])
s14 = set([4,5,6])

print('subset ',s13.issubset(s14))# s13이 s14의 부분집합인지 확인
print('subset ',s14.issubset(s13))# s13이 s14의 부분집합인지 확인

print("subset", s13.issuperset(s14))#s13이 s14의 전체집합인지 확인
print("subset", s14.issuperset(s13))#s14이 s13의 전체집합인지 확인

if(True&True):
    print("참입니다.")
    
bool_test = True

print(bool_test)
print(type(bool_test))