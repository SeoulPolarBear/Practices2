#-*- coding:utf-8 -*-

#조건문 : 흐름 제어

if True :
    print("와~ 조건문~")

if False:
    print("안나옴~~")
##################################################################################
# 우선순위(산술, 관계, 논리)
# 산술 > 관계 > 논리
print(10 + 2 > 8 + 3) # 산술이 관계보다 앞서서 => 12 > 11
print(10 + 2 * 2 > 8 + 3 * 2) # 14 > 14
print(((10 + 2) > 3) and (6 + 4 == 10))
##################################################################################
# 놀이동산 >> A : 성인, 150이상 (값은 입력받아서)
# 입력시에 -> 탑승 가능 or 탑승 불가 출력
# answer = "1";
# while True:
    # person_adult,  person_height = input("성인 (y or n)/ 키 입력 :").split(" ")
    # person_height = float(person_height)
    # if person_adult == "y" and person_height >= 150:
        # print("탑승가능합니다.")
    # else:
        # print("탑승불가합니다.")
    # answer = input("그만 묻고 싶으시면 0을 입력해 주세요. : ")
    # if answer == "0":
        # break
    
##################################################################################
# 다중 조건문
# Java : if - else if - else
# Python : if - elif - else

# 점수 입력 -> 80점 이상은 'A'
# 점수 입력 -> 70점 이상은 'B'
# 점수 입력 -> 60점 이상은 'C'
# 점수 입력 -> 나머지는    'D'


# while True:
    # score = int(input("점수를 입력하세요.:"))
    # result = [];
    # print("학점 : ", end = "")
    # if score >= 80:
        # result.append("A")
    # elif score >= 70:
        # result.append("B")
    # elif score >= 60:
        # result.append("C")
    # else:
        # result.append("D")
        #
    # if "D" in result:
        # print("재시험")
        #
    # else:
        # print("통과")
        # break
    
##################################################################################
# switch-case : 없음

# in, not in
abc = {"name": "polarbear", "age": 19, "phone": "010-1111-2222"}
print("name" in abc.keys())
print("name" in abc)
print("height" not in abc)
print(19 in abc.values())
print(20 not in abc.values())
    














