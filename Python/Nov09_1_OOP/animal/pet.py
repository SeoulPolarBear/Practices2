'''
Created on 2022. 11. 9.

@author: user
'''

#강아지 클래스 ->생성자에 이름,나이 = 구 속성 추가 기능

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printInfo(self):
        print(self.age)
        print(self.name)
        

if __name__ == "__main__":
    # 여기서 야생돌물 불러와서 -> 객체 만들어서 출력하는 기능까지
    #oMain3에서 실행
    from animal.wild import wild
    w = wild("낑", "토낑", 2)
    w.printInfo()
