# -*- coding:utf-8 -*-

class Avengers:
    def __init__(self, realName):
        self.realName = realName
    
    def attack(self):
        print("무찐 공격!")
    
    def printInfo(self):
        print(self.realName)
#############################################################################
class Human:
    def __init__(self, age):
        self.age = age
        
    def eat(self):
        print("쩝쩝박사")
    
    def attack(self):
        print("데미지 1짜리 발차기")
    
    def printInfo(self):
        print(self.age)
        
#############################################################################
# Java : 다중상속 - X (interface로 흉내만 냄)
# Python : 다중상속 - O
#        상속받는게 중복되면(ex: attack) -> 먼저 상속받은거를 불러옴(Avengers의 attack)
#        -> Human의 attack을 불러오고 싶다면 -> 직접 입력해야 한다.
class Ironman(Avengers, Human):
    def __init__(self, realName, age):
        Avengers.__init__(self, realName)
        Human.__init__(self, age)
    
    def attack(self):
        Avengers.attack(self)
        Human.attack(self)
    
    def eat(self):
        Human.eat(self)
    
    def printInfo(self):
        Avengers.printInfo(self)
        Human.printInfo(self)
        

#######################################################################################
if __name__ == "__main__":
    i = Ironman("토니스타크", 40)
    i.attack()
    i.eat()
    i.printInfo()
        










