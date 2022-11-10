# # if CONDITION:
# #     STATEMENT
# #     STATEMENT
# #     STATEMENT
# money = False   
# if money == True:
#     print("if 문 내부 문장 실행")
    
# print("프로그램 종료")

# money = True
# if money ==True:
#     print(" if문 내부 문장 실행")
# else:
#     print(" elsee문 내부 문장 실행")
    

# money = 10000

# if money > 10000:
#     print("만원 있습니다.")
# elif money < 10000:
#     print("돈이 부족합니다.")
# else:
#     print("딱 만원이 있습니다.")
    

print("가위 바위 보 입력 : ")#이렇게 설정하면 개행 때문에 아래 입력해야한다. 
choice = input("가위 바위 보 입력 : ")#사용자의 입력을 받을 수 있는 함수 type은 str로 받는다.
#input의 처음 인자값은 prompt를 인자로 갖는다.

#choice = int(input("숫자를 입력하시오 : "))#숫자로 변환시키고 싶을 때

print(choice)
print(type(choice))

if choice == "가위":
    print("%s를 입력하셨네요."%choice)
elif choice == "바위":
    print("%s를 입력하셨네요."%choice)
elif choice == "보":
    print("%s를 입력하셨네요."%choice)
else:
    print("잘못 입력하셨습니다.")