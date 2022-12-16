# a match 파일 가지고
# 우리나라 역대 전적 뽑아오기!
# 승,?
# 무,?
# 패,? 의 형태로
# 파일에 저장
record ={"승" : 0, "무" : 0, "패" : 0}
with open("C:/Users/user/Desktop/python/test/amatch/results.csv", "r", encoding="UTF-8") as f:
    try:
        for line in f.readlines():
            line = line.replace("\n","").split(",")
            print(line)
            if line[1] == 'South Korea':
                if int(line[3]) > int(line[4]):
                    record["승"] += 1
                elif int(line[3]) == int(line[4]):
                    record["무"] += 1
                else:
                    record["패"] += 1
            
            elif line[2] == 'South Korea':
                if int(line[3]) < int(line[4]):
                    record["승"] += 1
                elif int(line[3]) == int(line[4]):
                    record["무"] += 1
                else:
                    record["패"] += 1
    except:
        pass
print(record)

for k, v in record.items():
    print(k,v)
    
with open("C:/Users/user/Desktop/python/test/amatch/southkorea.csv", "w", encoding="UTF-8") as f2:
    for k, v in record.items():
        f2.write(f"{k},{v}\n")
print("성공!")
        
                
                
                
                
                
                
                
                 