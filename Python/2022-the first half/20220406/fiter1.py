#사용방법 : filter(함수, 순서가 있는 자료형)
#사용이유 : 기존 리스트에서 조건을 만족하는 요소만 뽑고 싶을 때

def func(x):
    return x<0


animals = ['cat','tiger','dog','bird','monkey']
result = []

for i in animals:
    if len(i) <= 3:
        result.append(i)
print(result)

def word_check(x):
    return len(x) <=3

result = list(filter(word_check,animals))
print(result)

list(filter(lambda x : len(x)<=3,animals))# len(x)<=3인 경우만 출력하겠다.
#list(filter(lambda x : x if len(x)<=3,animals))# 다음과 같은 경우이다.

str1 = "hobby abcd"
result = list( filter( lambda i: str1[i] == "b", range(len(str1))))
# str[i] = b인 str[i]들을 찾아라 즉, 결국 i가 인자이면 range를 사용해야 한다.
print("find character result = ", result)


