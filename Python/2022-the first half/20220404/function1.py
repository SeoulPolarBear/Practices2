# # def printHello():
# #     print("Hello")
    
# # printHello()

# # def printHello(a):
# #     print(a)
    
# # def printHellodict(a):
# #     print(list(a.values()))

# # tuple1 = (1,2,(3,1))
# # dict = {"name" : 1233}
# # set1 = ([1,2,3])
# # printHello(dict)
# # printHello(set1)
# # printHello(tuple1)
# # printHellodict(dict)


# # #1.  함수의 기본 형태
# # # 정의하기
# # # def function_name(parameter):      #def 는 define 의 약자. 정의하다
# # #     code #명령 블록

# # # 호출하기
# # # 함수이름()  # function_name()
# # #ex)
# # def printHello():
# # 	print("Hello")

# # printHello()

# # def printHello2(a):
# # 	print(a)
# # printHello2("Hello2")



# # #2.  매개변수가 있는 함수
# # # 정의하기
# # # def 함수이름(매개변수1, 매개변수2):
# # #	명령블록
# # # 호출하기
# # #함수이름(인자1,인자2)
# # #ex)
# # def sum(a, b):
# #     print(a + b)

# # sum(3, 4)

# # #3.  반환값이 있는 함수
# # # 정의하기
# # # def 함수이름():
# # #	명령블록
# # #	return 반환값
# # # 호출하기
# # # 함수이름()
# # #ex)
# # import random
# # def getRandomNumber():
# #     number = random.randint(1,10)
# #     return number

# # print(getRandomNumber())


# # #4.  매개변수와 반환값이 있는 함수 
# # # 정의하기
# # # def 함수 이름(매개변수1, 매개변수2):
# # #	령블록
# # #	return 반환값
# # # 호출하기
# # # 함수이름(인자1, 인자2)
# # #ex)
# # def add(a, b):
# #     result = a + b
# #     return result

# # print(add(5,6))


# # #1. 위치 매개변수
# # # sum(3,4) 
# # #def sum(x,y)

# # #2. 기본 매개변수(default 값이 존재하는 매개변수)

# # #매개 변수가 받을 기본값을 미리 선언하는 것
#예시 1
# # def post_info(title, content = '내용 없음'):
# #     print('제목', title)
# #     print('내용', content)
# # post_info("출석 체크합니다.")# 다음과 같이 이미 함수에 parameter가 지정이 되어있으니까 하나만 인자값에 넣어주면 된다.
# #즉, 함수에 이미 지정이 되어있으므로 굳이 호출시 생각할 필요가 없다.
# #다음과 같이 parameter는 2개인데 호출시 parameter를 1개만 출력해도 작동이 된다. title에만 인자값이 들어갔다.

#예시 2
# # sum(x = 3, y = 4) def sum(y,x)
# # 함수 호출
# def post_info(content='없어요',title='여자친구 만드는 방법'):  # 인자값을 매개변수에 각각 매핑하여 전달 순서와 상관없이 인자를 넣어준다.
#     print("제목 : ", title)
#     print("내용 : ", content) #default 값을 주기 떄문에 기본 매개 변수
    
# post_info()


# #3. 키워드 매개변수
# def post_info(content,title):  # 인자값을 매개변수에 각각 매핑하여 전달 순서와 상관없이 인자를 넣어준다.
#     print("제목 : ", title)
#     print("내용 : ", content)

# post_info(content = "없어요", title = "여자친구 만드는 방법")


# #함수 정의 위치 가변 매개 변수
# def print_fruits(*args):
#     for arg in args:
#         print(arg, end = " ")
#     print(" ")
        
# print_fruits('apple', 'orange', 'mango')

# #함수 호출 2
# def comment_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key} : {value}')

# comment_info(name = '파린아', content = '쉽다.')

# #매개 변수 작성 순서
# #위치 - 기본 - 위치 가변 - 키워드(기본) - 키워드 가변

# #비교 
# #오류 
# def post_info(*tags, title, content):
#     print(f'제목 : {title}')
#     print(f'내용 : {content}')
#     print(f'태그 : {tags}')
    
#     post_info('#파이썬','#함수','파이썬 함수 정리!', '다양한 매개변수')

# #정상
# def post_info(title, content, *tags):
#     print(f'제목 : {title}')
#     print(f'내용 : {content}')
#     print(f'태그 : {tags}')
    
#     post_info('파이썬 함수 정리!', '다양한 매개변수','#파이썬','#함수')
    


#전체 다 넣어보기
def post_info(title, content ="기본 매개변수", *tags, test, **dicts):
    print(f'제목 : {title}')
    print(f'내용 : {content}')
    print(f'태그 : {tags}')
    print(f'기본 키워드 : {test}')
    # print(f'기본 키워드 : {text2}')
    # print(f'기본 키워드 : {text3}')
    print(f'딕셔너리 : {dicts}')
    
post_info('위치 매개변수', '위치','가변','매개','변수',  test= "test" , fru = "키워드", man = "가변", woman = "매개변수")
#post_info('위치 매개변수', '위치','가변','매개','변수',  test= "test" , {"fru" : "키워드", "man" : "가변", "woman" : "매개변수"}) 불가능 하다.
    
    # def post_info(title, content ="기본 매개변수", *tags, text, text2, text3,**dicts):
    # print(f'제목 : {title}')
    # print(f'내용 : {content}')
    # print(f'태그 : {tags}')
    # print(f'기본 키워드 : {text}')
    # print(f'기본 키워드 : {text2}')
    # print(f'기본 키워드 : {text3}')
    # print(f'딕셔너리 : {dicts}')
    
    # post_info('위치 매개변수', '위치','가변','매개','변수', text = "기본", text2="키워드", text3 = "매개 변수", 123 = "키워드", 124 = "가변", 125 = "매개변수")
    
    

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3    # 다운 리턴  언팩킹을 이용하면 리턴값이 여러개일 수 있다.

w = func_mul(10) # 이것이 패킹 튜플로 받겠다.
x, y, z = func_mul(10)   #  이것이 언패킹 각각 int로 받게 된다.
#x, y, z = (100, 200, 300)

print(type(x)) #int
print(x, y ,z)#이건 그냥 한번에 출력 print(x);print(y);print(z);

def fun_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

x, y, z = func_mul(10)   # 결국 투플을 받아서 언패킹 하므로 이것도 가능하다.

q = fun_mul2(20)

print(type(q),q,list(q))

def fun_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3] 

q = fun_mul2(20)

print(type(q),q,list(q))



def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1' : 'y1', 'v2' : 'y2', 'v3' : 'y3'}
    #return {v1='y1', v2='y2', v3='y3'} 이건 불가능 하다.
d = func_mul3(30)

#print(type(d), d)
print(type(d), d, d.get('v2'), d.items(), d.keys(), d.values())
#print(d.values())
    

