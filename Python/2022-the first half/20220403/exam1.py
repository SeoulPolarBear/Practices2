# #1. 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하시오.
# vehicle_number = "100나 1234"

# #방법1
# print(vehicle_number[-4:])
# #방법2
# new_vehicle_number = vehicle_number.split()#100나 1234의 공백을 기준으로 나눈다. 총 index개수가 2개가 된다.
# print(new_vehicle_number[1])



# #2. 아래의 전화번호에서 대시('-')을 제거하고 출력하시오.
# phone = "010-1234-5678"

# #방법1
# print(phone.replace('-',''))

# #참고로 phone[0] = '1'하면 오류가 나온다. str에서는 불가능하기 때문
# #따라서 list로 변경시킨다음에 처리를 해줘야 한다.

      
# #3. 다음 가격을 컴마를 제거하고 숫자로 바꿔보시오.
# price = "13,200"

# #방법1
# new_price=price.replace(',',"")
# new_price=int(new_price)
# print(new_price)



# #4. 다음과 같이 날짜를 표현하는 문자열이 있을 때 년, 월, 일로 나눠 출력하시오.
# date = "2022-04-01"
# #2022년 04월 01일

# #방법1
# print("%s년 %s월 %s일"%(date[:4],date[5:7],date[-2:]))

# #방법2
# print(f'{date[:4]}년 {date[5:7]}월 {date[-2:]}일')



# #5. 슬라이싱을 사용해서 홀수만 출력하시오.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# #방법1
# print(nums[::2])
      


# #6. 다음 문자열에서 '/'로 구분된 이름을 리스트에 저장하시오.
# friends="alice/bob/charlie"

# #방법1
# list_friends = friends.split('/')
# print(list_friends)


# #제어문
# #1.숫자를 입력받아 짝수와 홀수를 구분하는 프로그램을 작성하시오.

# num1 = int(input("숫자를 입력하시오 : "))
# if num1 % 2 == 0:
#     print("{}는 짝수 입니다.".format(num1))
# elif num1 % 2 == 1:
#     print("{}는 홀수 입니다.".format(num1))
# else:
#     print("잘못 입력하셨습니다.")
    
# pocket = ['paper', 'money', 'cellphone']
# # if 'money' in pocket:#이렇게 if문안에 아무것도 하지 않게 하고 싶은 경우 아무것도 넣지 안으면 syntax오류가 발생한다.
# # else:
# #     print("카드를 꺼내라")


# if 'money' not in pocket:#따라서 이렇게 pass를 넣어서 문장을 그냥 넘어갈 수 있게 할 수 있다.
#     pass#즉, pass가 있는 줄에서는 아무것도 하지 않겠다.
# else:
#     print("카드를 꺼내라")

# #AND A AND B : A, B 모두 TRUE인 경우에 TRUE
# #OR  A OR B : A,B 둘 중 하나라도 True이면 True
# #NOT NOT A : 부정연산(True -> False, False -> True)

# number = int(input("숫자 입력 : "))

# if number%2 == 0 and number%3 == 0:
#     print("%d는 2의 배수이면서 3의 배수입니다."%number)
    
treeHit = 0
while treeHit < 10:
    treeHit += 1## 특이하게 증감연산자는 존재하지 않는다. ++, --
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit ==10:
        print("나무가 넘어값니다.")