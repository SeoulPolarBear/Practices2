# 파일로부터 데이터를 읽어와서 프로그램에서 활용하기 위함
# 프로그램에서 만든 데이터를 파일 형태로 저장하기 위함

# 파일 열기 -> 작업(읽기, 쓰기) -> 파일 닫기 (필수!)

# .txt / .csv 파일( 데이터를 다루는 작업)

#1. 파일에 내용 쓰기(write) 
#폴더는 미리 만들어놔야 함 / 파일은 존재하지 않아도 실행시에 파일을 만들어줌
# w : 덮어쓰기 모드
# file = open("C:/Users/user/Desktop/python/test/test.txt", "w", encoding="UTF-8")
# file.write("조금만 지나면 점심시간 ^-^ 근데 메뉴는 샐러드 ㅠ-ㅠ")
# print("완료!")
# file.close()

#2. 파일에 내용을 추가(append)
file = open("C:/Users/user/Desktop/python/test/test.txt", "a", encoding="UTF-8")
file.write("\n그런데 말입니다... \n 이따 저녁에 회식인데요? \n Wa!!!!!!!!!!!!!")
print("완료")
file.close()

#3. 파일 읽어오기 (read)
file = open("C:/Users/user/Desktop/python/test/test.txt", "r", encoding="UTF-8")

# 3-1 파일 전체 일기
# data = file.read()
# print(data)
# file.close()

# 3-2 파일을 한줄한줄 읽기
while True: # 내가 가져온 파일의 내용이 언제 끝날지 모르기 때문에 True
    data = file.readline() # 한줄을 읽어옴
    print(data, end = "")
    #readline의 결과가 공백인 상황(파일의 맨 마지막 줄까지 끝난 상황)
    if data == "":
        break # 종료해라
file.close()








