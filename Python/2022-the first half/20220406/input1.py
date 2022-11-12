for i in range(10):#이건 interpreter로 입력해야 결과값을 볼 수 있다.
    result = input("Enter your Name")#값을 입력받으면 무조건 string으로 받는다. prompt이기 때문이다.
    grade = input("Enter your grade")
    company = input("Enter your company")
    break
    
print(result);print(grade);print(company)
print(type(result));print(type(grade));print(type(company))
    
name = input("Enter Your Name : ")
grade = input("Enter Your Grade : ")
company = input("Enter Your Company name : ")

print(name, grade, company)

# 예제2
number = input("Enter number : ")
name = input("Enter name : ")

#print("type of number", type(number))
print("type of number", type(number), number * 3)    # 기본 타입(str)
print("type of number", type(number), int(number) * 3)   # 위라인과 결과 비교필요
print("type of nanme", type(name))

# 예제3(계산)
first_number = int(input("Enter number1 : "))
second_number = int(input("Enter number2 : "))

total = first_number + second_number
print("first_number + second_number : ", total)


print("FirstName -{0}, LastName-{1}".format(input("Enter first name:"), input("Enter last Name: ")))
    
    
    