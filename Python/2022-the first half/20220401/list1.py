import copy

#List indexing

# lista = []
# listb = list()

# print(lista)
# print(type(lista))
# print(type(listb))
# print(listb)

# listc = ["Life", 'is', 'too','short']
# print(listc)

# listd = [1, 2, 'hello','python']
# print(listd)

# liste = list([1,2, ["Life",'is', 1]])#list함수의 argument는 list이다
# print(liste)
# print(type(liste[2]))

# listf = ['Life', 'is', 'too', 'short']
# print(listf[-2])

# listg = list([1,2, ["Life",'is', 3]])
# print(listg[2][0])
# print(listg[2][1])
# print(listg[2][2])

# listh = [1,2,3,['a','b','c',['list', 'is']]]
# print(listh[-1][-1][-1])







#list slicing

# listi = [1,2,3,4,5]
# print(listi[0:2])
# print(listi[2:])
# listj = [1,2,3,['a','b','c'],4,5]
# print(listj[0:4])
# print(listj[3][0:4])
# print(listj[3][0:2])

# #list sum

# print(listi + listj)

# #list multi

# print(listi*2)





#list update
listk = [4,5,6]
listk[2] = 7
print(listk[2])

print(listk[1:2])
listk[1:2] = ['a', 'b', 'c']
print(listk[1:2])

listl = [1, 'a', 'b', 'c', 4]
print(listl)
listl[0] = ['a1','a2','a3']
print(listl[0])
print(listl)

#delete list element #1 - slicing
listl[0:1] = []
print()

#delete list element #2 - del
del listl[0:1]
del listl[0]

# listl.append(6)
# print(listl)
# listm = [1,2,5,3,4]
# listn = ['a','b','z','c','d']
# listm.sort()
# listn.sort()
# print(listm);print(listn)

# listm.reverse()
# listn.reverse()
# print(listm);print(listn)
# listm.sort()
# listm.reverse()
# print(listm)
# print(listm[::-1])




listo = [1,2,3]
#list.insert(INDEX,VALUE)//INDEX에 있던 기존 값 부터 뒤로 밀려나게 된다.
listo.insert(0,4)
print(listo)
listo.insert(1,'z')
print(listo)

listp = [1,2,3]
listp =listp*2
#listp.remove(value)# 처음 나오는 value값만 지워진다.
# listp.remove(3)
# print(listp)

# print(listp.pop())
# print(listp)
# print(listp.index(2))
# print(listp.count(2))
# listp = listp + [8,9]
# print(listp)


# #extend와 append의 차이
# listp.extend([4,5])
# #[1,2,3,4,5]
# listp.append([1,2])
# #[1,2,3,[1,2]]
# print(listp)



# x = [1,2,3,4,5]
# y = x
# y[2] = 0
# print(x)
# print(y)
# print(id(x))
# print(id(y))

# a = [5,6,7,8,9]
# b = a.copy()
# b[2] = 0
# print(a)
# print(b)
# print(id(a))
# print(id(b))



# c = [[1,2], [3,4,5]]
# d = copy.deepcopy(c)# import copy 이때 copy는 모듈로 따지고 보면 copy.py에 있는 deepcopy() 함수를 사용했다고 보면 된다.
# d[0][0] = 0
# print(c)
# print(d)
# print(id(c))
# print(id(d))

list_1 = [1,2,3,(1,2,3)]
print(list_1)

list2 = [10,2,30,4,9]
list2.sort(reverse=True)#역순으로 정렬하는 방법
print(list2)