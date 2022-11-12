# 람다 함수 정의 방법

#lambda 매개변수 : 결과


#ex 2)

lambda a: a-1


(lambda a:a-1)(10) # 인터프리터 환경에서는 일회성으로 지금처럼 쓸수 있다.

9

first_lambda = lambda a: a-1 # 람다 함수를 재활용 하기 위해서는 반드시 객체가 선언되어 야 한다.

first_lambda(10)



# if문 사용한 람다 함수 사용


def is_positive_number(a):

    if a > 0:

        return True

    else:

        return False

is_positive_number(-2)

False



# 변형

lambda a: True if a > 0 else False



lambda a: True if a > 0 else False(-2)
#   lambda 매개변수 1, 매개변수 2, ... : 결과 (인자값)
#다만 이렇게 선언만 하면 재활용이 불가능 하다.

False



is_positive_number = lambda a: True if a > 0 else False
#람다함수는 객체를 선언해야 유지가 되므로 재활용할 때는 다음과 같이 객체를 선언해줘야 한다.

print(is_positive_number(-2))

for i in range(1,10):
    if i % 3 == 0:
        print("짝")
    else:
        print(i)

print(list(map(lambda x :"짝" if x % 3 == 0 else x,range(1,10))))#map은 반복할 때 사용한다.
#즉, 이 코드는 range(1,10)을 x값에 전달해서 반복하게 된다.

#map(함수, 입력값) 다만 이건 객체로만 반환되기 때문에 id만 존재하고 자료형이 존재하지 않기 때문에 자료형변환을 해줘야한다.

myList = [lambda a,b : a+b, lambda a,b: a*b]#각각 id가 다르다
myList = [lambda a,b : a+b, lambda a,b: a*b]
print(myList)
print(myList[0])
print(myList[1])
print(myList[0](3,4))
print(myList[1](3,4))