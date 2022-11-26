# -*- coding:utf-8 -*-

sss = ["ㅋㅋㅋ", "ㅁㅁㅁ", "ㅂㅂㅂ", "ㅎㅎㅎ", "ㅋㅋㅋ", "ㄹㄹㄹ"]
for s in sss:
    # 찾는 문자열이 존재하는 경우 : 그 문자열이 있는 인덱스 값을 리턴
    # 찾는 문자열이 존재하지 않는 경우 : -1 리턴
    print(s.find("ㅋㅋ"))

# 조조(맹덕), 유비(현덕), 손권(중모)
# 책을 훑어보면서... -> 위의 인물들이 몇 번 언급되는지 카운팅하기!
# 인물, 언급횟수 의 형태로 -> CSV파일에 저장

person = ["조조","맹덕","유비","현덕","손권","중모"]
counts = [0 for _ in range(6)]

for i in range(1,10):
    file = open(f"C:/Users/user/Desktop/python/ThreeKingdoms/ThreeKingdoms0{i}.txt", "r", encoding ="UTF-8")
    book = file.read()
    for j in range(6):
        book_split = book.split(person[j])
        counts[j] += len(book_split) - 1
    file.close()

file = open(f"C:/Users/user/Desktop/python/ThreeKingdoms/ThreeKingdoms10.txt", "r", encoding ="UTF-8")
book = file.read()
for m in range(6):
    book_split = book.split(person[m])
    counts[m] += len(book_split) - 1
file.close()

file2 = open("C:/Users/user/Desktop/python/ThreeKingdoms/ThreeKingdoms_count.txt", "w", encoding ="UTF-8")
file2.write("인물, 언급 횟수\n")
for k in range(0,6,2):
    file2.write(f"{person[k]}({person[k+1]}),")
    file2.write(f"{counts[k] + counts[k+1]}\n")
file2.close()
print("일단 됨")
#===============================================================================================================================
fileName = None
line, word = None, None

wc ={"조조" : 0, "유비" : 0, "손권" : 0}
for i in range(1,11):
    fileName = f"C:/Users/user/Desktop/python/ThreeKingdoms/ThreeKingdoms%02d.txt" % i
    with open(fileName, "r", encoding="utf-8") as f:
        for line in f.readlines():
            print()
            line = line.replace("\n", "")
            line = line.split(" ")
            for word in line:
                if word.find("조조") != -1 or word.find("맹덕") != -1:
                    wc["조조"] += 1
                elif word.find("유비") != -1 or word.find("현덕") != -1:
                    wc["유비"] += 1
                elif word.find("손권") != -1 or word.find("중모") != -1:
                    wc["손권"] += 1

with open("C:/Users/user/Desktop/python/ThreeKingdoms/ThreeKingdoms_count2.txt", "w", encoding ="UTF-8") as f:
    for k, v in wc.items():
        f.write(f"{k}, {v}\n")
print("끝!")


    
    
    
    