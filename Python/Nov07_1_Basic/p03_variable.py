# -*- coding:utf-8 -*-


# 변수 (Variable)
# Java : 값을 표현하기 위해서 최적의 자료형을 개발자가 직접 선정
#            -> 메모리 사용량이 최적화
#        자료형 변수명 = 값;
#        int a = 10;

# Python : Python이 알아서 자료형을 선정
#            '자료형'이라는 것 자체를 공부할 필요가 딱히 없음 -> 개발자가 편함
#            자동으로 선정하는 시간 : 메모리 사용량 최적화 컨트롤이 불가능...!
#            기본형이 없고, 다 참조형 >> 메모리의 사용량이 많음
#            변수명 = 값    (세미콜론 X)

a = 10
b = a
print(a)
print(type(a))
print(id(a))
print(id(b))

# Java 버전 값 바꾸기
# int b = 10;
# b = 20;
print("##############################################################################")
a = 20; # 새로운 객체 만들기, 기존에 있던 값은 Garbage Collection 날아감!
print(a)
print(type(a))
print(id(a))
print("##############################################################################")
a = "ㅎ"; # 새로운 객체 만들기, 기존에 있던 값은 Garbage Collection 날아감!
print(a)
print(type(a))
print(id(a))
print("##############################################################################")


# Python의 data type(자료형)
p_str = "polarbear"     #str : 문자열
print(p_str, type(p_str))
p_int = 10              # int : 정수
print(p_int, type(p_int))
p_float = 1.234         # float : 실수
print(p_float, type(p_float))
p_bool = True           # boolean : 논리(True, False)
print(p_bool, type(p_bool))
p_list = [p_str, p_int, p_float] # list : 리스트
print(p_list, type(p_list))

p_dict = {
    'name' : "polarbear",
    "age" : 100,
    }# dict : 사전(dictionary)
print(p_dict, type(p_dict))

p_set = {3,6,7} # set : 집합
print(p_set, type(p_set))

p_tuple = (5,6,7) # tuple(튜플)
p_tuple = 5,6,7
print(p_tuple,type(p_tuple))
##########################################################################################################
#형 변환(Type Casting)
print("############################")
d = 1
print(type(d))
d = str(d)
print(type(d))
e = False
e = int(e)      # False = 0 / True = 1
##########################################################################################################
# 키모드 입력 받기 (keyboard input)
ki = input("키 : ")
print(ki, type(ki))   #input으로 가져오면 기본적으로 str이기 때문에
            # 정수, 실수는 형 변환이 필요함
            
ki = float(ki)
print(ki, type(ki))

ki2 = float(input("몸무게"))
print(ki2, type(ki2))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            



















