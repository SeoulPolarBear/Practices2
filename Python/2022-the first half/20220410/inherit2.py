# from unicodedata import name


# class Person:
#     def __init__(self,name, phoneNumber):
#         self.name = name
#         self.phoneNumber = phoneNumber
        
#     def Print(self):
#         print("")
        
# # class Student(Person):
# #     def __init__(self,name, phoneNumber,subject,studentID):
# #         self.name = name
# #         self.phoneNumber = phoneNumber
# #         self.Subject = subject
# #         self.StudentID =studentID
        
# class Student(Person):
#     def __init__(self,name, phoneNumber,subject,studentID):
#         super().__init__(name, phoneNumber)
#         self.Subject = subject
#         self.StudentID =studentID
        
#     def Print(self):
#         super().Print()# 다음과 같이 함수도 super를 통해서 상속할 수있다. 
        
# print(issubclass(Person, Student))
# print(issubclass(Student, Person))

# c = Student(1,2,3,4)
# print(c.name)

# class SelfTest:
#     def func1(): # self가 없으면 클래스 메소드 즉, 클래스의 변수와 마찬가지로 인스턴스를 거치지 않고 출력되어야 한다.
#         print('Func1 called')
#     def func2(self):#self는 인스턴스를 요구를 한다. 따라서 f = SelfTest()로 인스턴스 객체를 생성했으면 반드시 self를 써 줘야한다.
#         print('Func2 called')
        
# f = SelfTest()
# print(dir(f))
# print(dir(f))
# print(id(f))
# f.func1()#오류 self 가 없기 때문에 인스턴스에 적용을 할 수가 없다.
# SelfTest.func1()
# SelfTest.func2()#오류 self가 있기 때문에 인스턴스가 아니여서

# f.func2()


class Unit:
    count = 0#instance에서 접근가능 즉, instance가 공통적으로 사용하는 속성이라고 볼 수 있다.
    def __init__(self, name, hp, shield, damage):
        self.name = name
        self.__hp = hp# 비공개 속성 : 클래스 안에서만 접근 가능한 속성
        #이걸 name mangling이라한다.
        #_hp로 설정하면 _Unit_hp로 바뀐다.
        self.shield = shield
        self.damage = damage
        Unit.count +=1 #클래스 속성은 self가 아닌 "클래스 이름, 클래스속성명"
        print(f"[{self.name}](이)가 생성되었습니다.")
    
    def __str__(self):
        return f"[{self.name}] 체력 : {self.__hp} 쉴드 : {self.shield} 공격력 : {self.damage}"
    
    
    def hit(self, damage):
        #방어막 변경
        if self.shield >= damage:
            self.shield -= damage
            damage = 0
        else:
            damage -=self.shield
            self.shield = 0
        
        #더이상 shield가 방어를 못하게 되었을 때
        #체력 변경
        if damage > 0:
            if self.__hp > damage:
                self.__hp -= damage
            else:
                self.__hp = 0  
    
    
    @classmethod  #클래스 속성에 접근하는 메서드 print는 아래에서 확인하자
    def print_count(cls):#즉, cls가 self 같은 역할을 한다.
        print(f"생성된 유닛 개수 : [{cls.count}]")      



probe = Unit("프로브",20,20,5)#생성시 [프로브](이)가 생성되었습니다. 출력
zealot = Unit("프로브",100,60,16)
dragoon = Unit("프로브",100,80,20)
print(probe)#다음과 같이 객체를 print할 때 __str__ 메소드가 있으면 __str__의 return 값을 반환한다.
print(zealot)
print(dragoon)
print(probe.count)#count는 클래스 자체에서 생성했기 때문에 인스턴스도 사용할 수 있다.
print(Unit.count)
probe.__hp =9999#private이기 때문에 메소드를 통해서만 수정이 가능하다.
print(probe)

#probe._Unit_hp =9999#mangling 할 시 이렇게 입력하면 변환은 가능하다.

probe.hit(30)
print(probe)
probe.hit(30)
print(probe)

Unit.print_count()
        