class Person:#부모 클래스
    pass
class Bird:
    pass
class Student(Person):# 상속
    pass

p, s, b = Person(), Student(), Bird() #언팩킹을 이용한 선언

print("p is instance of Person: ", isinstance(p,Person))# isinstance(인스턴스 객체, 부모 클래스)
#True
print("s is instance of Person: ", isinstance(s,Person))# isinstance(인스턴스 객체, 부모 클래스)
#True
print("s is instance of Person: ", isinstance(b,Person))# isinstance(인스턴스 객체, 부모 클래스)
#False
#================================================================================================================
print("Bird is instance of Person: ", isinstance(Bird,Person))# isinstance(인스턴스 객체, 부모 클래스)
#False
print("Student is instance of Person: ", isinstance(Student,Person))# isinstance(인스턴스 객체, 부모 클래스)
#False
#이렇게 되면 클래스 끼리 비교가 되는 것이기 때문에 isinstance함수를 쓰는 의미가 없다.



class Calculator:
    def __init__(self):
        self.result = 0#생성자
    def __del__(self):
        print("성공")#소멸자
    
    def add(self,num):
        self.result = num + self.result
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(5))
print(cal2.add(6))
print(cal2.add(7))

class MyClass:
    def __init__(self, value): #생성자 메소드
        self.Value = value
        print("Class is created: Value = ", value)
    
    def __del__(self): # 소멸자 메소드
        print("Class is deleted!")
        
def foo(): #함수 foo 블록안에서만 인스턴스 객체 d가 존재
    d = MyClass(10)
    
foo()
#즉, calculator는 함수가 종료 될 때 소멸자를 호출하는데 
#foo 함수 안에 있는 MyClass는 foo()함수가 끝나면 소멸자를 호출 한다.
# 3
# 7
# 5
# 11
# 18
# Class is created: Value =  10
# Class is deleted!
# 성공
# 성공


