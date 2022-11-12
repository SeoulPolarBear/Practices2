class person: #클래스의 정의
    name = "Default name"#멤버 변수, 클래스 변수
    
    def Print(self):#멤버 메소드
        print("my name is {0}".format(self.name))
        
p1 = person() # 인스턴스 객체 선언
p2 = person() # 인스턴스 객체 선언
p1.Print()

print(person.name) #클래스 변수 호출 방법 class 명.클래스 변수
# Default name

print("p1`s name : ", p1.name)
print()
print("p2`s name : ", p2.name)
# p1`s name :  Default name

# p2`s name :  Default name



p1.name = "파린이" #p1인스턴스 name 속성 변경 인스턴스 변수라고 할 수 있다.
print("p1`s name : ", p1.name)
print()
print("p2`s name : ", p2.name)
# p1`s name :  파린이

# p2`s name :  Default name
print("=" * 10)

person.title = "New title"
print(dir(person))
print(person.title)
print(p1.title)
print(p2.title)
p1.age = 20
print(dir(p1))
print("p1`s age : ", p1.age)
#print("p2`s age : ", p2.age) #p1에만 age가 추가 되었으므로 p2에서는 사용할 수 없다.
print(p2.title)#person에서 title을 추가 해서 p2에도 반영 되었다.

#person : name, title
#p1 : age, name, title
#p2 : name, title
#즉, 클래스, 인스턴스 변수는 클래스 내에 안 넣어도 코드상에서 추가가 가능하다.
#그리고 클래스에 반영된 것은 인스턴스에도 즉시 반영 된다.




