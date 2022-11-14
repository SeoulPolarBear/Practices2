# -*- coding:utf-8 -*-

class Book():
    # def __init__(self):
        # print("기본 생성자 - 책 생성")
    
    # 생성자 : 객체가 메모리상에 만들어질 때 호출하는 메소드
    # overloading 안되니 -> 생성자를 하나만!
    def __init__(self, title, price):
        print("오버로딩 된 생성자!!!")
        self.title = title      # 보통은 이렇게 생성자에서 멤버변수를 만들어서 결정
        self.price = price
    
    def printInfo(self):
        print(self.title,self.price)
        
    def __del__(self):
        print("책삭제")

####################################################################################
# 사람 클래스 : 이름, 나이 / 그 속성들 출력하는 기능 / 생성자, 소멸자
# Garbage Collection : 그 객체를 가리키는 변수가 없게 되면 Heap영역을 자동으로 정리
class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def showInfo(self):
        print(self.name, self.age)
    
    def __del__(self):
        print("종료")
        
        
####################################################################################
#b1 = Book()
b2 = Book("원피스", 7000)
b2.printInfo()
####################################################################################
h1 = person("Lim",20)
h1.showInfo()
print("==========================")
h2 = person("Kim",20)
h2.showInfo()
print("==========================")
h3 = h1 
h3.showInfo()

# h1과 h3는 같은 Id이기 때문에 같이 한번에 사라진다.
# h1이 없어졌다고 하더라도 h3가 객체의 id를 가지고 있기 때문에 소멸자가 발동이 안 된다.
h1=None
# h3이 없어졌다고 하더라도 h3가 객체의 id를 가지고 있기 마지막 객체이므로 소멸자가 발동 된다.
h3=None

















