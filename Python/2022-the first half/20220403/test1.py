tup1 = (1,2,'a','b',(11,12,13))
print(tup1)

#tup1[0]=1000
print(tup1[0])
print(tup1[2:])

list3_tup1 = list(tup1)
print(type(list3_tup1))
list3_tup1.extend(['a1','a2','a3'])
print(list3_tup1)
print(id(tup1))# 튜플을 list로 바꾸면 id가 바뀌고 다시 tuple로 바꾸면 id가 바뀐다. 그 이유는 tuple은 수정이 불가하므로 id도 새로 만들어 줘야한다.
tup1 = tuple(list3_tup1)
print(id(tup1))

tup2 = (1,2,3)
tup3 = (4,5)
print(id(tup2))
#1541304746304
tup2 = tup2 + tup3#마찬가지로 tuple은 변경이 불가하므로 새로운 tup2를 만들어서 id를 부여하게 했다
print(tup2)
print(id(tup2))
#1541304742272


#======================================================================================

dic1 ={'key' : 111, 123 : 'abc'}
dic1['key'] = 'good'
print(dic1['key']) 
print(dic1.get(123))

print(dic1.keys())
print(dic1.values())
print(dic1.items())

