# # t1 = ()
# # print(t1)
# # print(type(t1))
# # t2 = ('1','b','c')
# # print(t2)

# # t3 = (1,2,3)
# # print(t3)
# # t4 = 1,2,3
# # print(t4)
# from pyrsistent import immutable


# t5 = ('a', 'b', ('ab','cd'))
# print(t5[2])
# #t5[2] = 'c'
# t6 = list(t5)
# print(t6)
# print(type(t6[2]))
# #immutable(불변)
# print(t6)
# del t6[2]
# print(t6)

# #del t5 # tuple 삭제 방법
# print(t5[0:1])


#팩킹 언패킹




#(x1, x2, x3, x4) = t 각 객체당 하나씩 필요하다

# 언팩킹
(x1, x2, x3, x4) = ('foo', 'bar', 'baz', 'qux')
print(type(x1), type(x2), type(x3), type(x4))#전부 str로 나온다
print(x1, x2, x3, x4)


#팩킹
t2 =1, 2, 3      # t2 = (1, 2, 3)   
t3 = 4,         #여기도 t3 = (4,) 와 같다


#언팩킹 이때는 tuple이 아니므로 수정 가능
#x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6 
x5 = 9

print(t2)
print(type(t2))
print(type(x4),type(x5),type(x6))
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)


