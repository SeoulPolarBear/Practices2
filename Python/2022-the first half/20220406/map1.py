# #map(함수 이름, 입력(인자)값들)
# #map(Function function, Arg arg)
# #map(함수 리스트도 가능하다, 입력값)


# def multi(x):
#     return x*x
# for i in range(1,11):
#     print(multi(i))


# list(map(multi,range(1,11)))    

# print(list(map(lambda x: x*x,range(1,11))))
# print(list(map(lambda x: x**2 if x%2 == 0 else x+x,range(1,11))))

# list1 = [1,2,3,4]
# print(list(map(lambda x: x**2 if x%2 == 0 else x+x,list1)))
# #print(list(map(lambda x,y: x**2 if x%2 == 0 else x+y,2,2)))#이건 굳이 할 필요가 없어서 오류 즉, list나 range 값이 반복문에 씌이는 것을 입력값으로 넣어야 한다.

# list2 = ["1","2","3","4","5"]# int의 형변환을 map을 이용해서 활용
# print(list(map(int, list2)))

# in1 =[1,3,5,7]
# in2 = [2,4,6,8]
# print(list(map(lambda x,y : x**y, in1, in2)))
# lambdaList = [lambda x,y : x+y,lambda x,y : x-y,lambda x,y : x*y,lambda x,y : x/y]#즉, 객체를 만들어서 사용했다!!!! 

# print(list(map(lambdaList[0], in1,in2)))
# print(list(map(lambdaList[1], in1,in2)))
# print(list(map(lambdaList[2], in1,in2)))
# print(list(map(lambdaList[3], in1,in2)))


a = "     test     "
print(a)
print(a.strip())#default : 공백을 지워준다.
b = ["   hi       ","       hello        "," world "]
for i in b:
    print(i.strip())
    
print(list(map(lambda i : i.strip(),b)))
print(set(map(lambda i : i.strip(),b)))
print(tuple(map(lambda i : i.strip(),b)))


itemz = 'test'
items = ["       로지텍 마우스      ", " 앱솔 키보드     "]


print(len(itemz))
print(len(items))
for i in range(len(items)):
    items[i] = items[i].strip()
print(items)


#map으로 변환
#ist 수정<--------------------------------이 방법은 출력시 리스트 자체를 수정하게 된다.
items =list(map(lambda x : items[x].strip(),range(len(items))))
print(items)

#출력시 형변환  <--------------------------이 방법은 출력시 형변환을 하는 것으로 원본 수정이 일어나지 않는다.
items_after = list(map(lambda x : x.strip(),items))




