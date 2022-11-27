#방금 만든 csv파일 불러와서
# -> 연월에 맞춰서 -> 유임승차인원, 무임승차인원, 유임하차인원, 무임하차인원
# -> 선 그래프 그리기!
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

with open("C:/Users/user/Desktop/python/test/subway/subway.csv", "r", encoding="UTF-8") as f:
    subway = f.read()
    #print(type(subway))
    #print(subway)
    #먼저 일단 /n을 통해서 각각 낱개의 정보로 나눈 list
    subways = subway.split("\n")
    for i in range(len(subways)):
        subways[i]= subways[i].split(",")
    #print(subways)
    USE_MON = set()
    PAY_RIDE_NUM = {}
    FREE_RIDE_NUM = {}
    PAY_ALIGHT_NUM = {}
    FREE_ALIGHT_NUM = {}
    for subway_info in subways:
        #print(subway_info) 
        if subway_info[0] in USE_MON:
            PAY_RIDE_NUM[subway_info[0]] += float(subway_info[3])
            FREE_RIDE_NUM[subway_info[0]] += float(subway_info[4])
            PAY_ALIGHT_NUM[subway_info[0]] += float(subway_info[5])
            FREE_ALIGHT_NUM[subway_info[0]] += float(subway_info[6])
        else:
            if subway_info[0] == "":
                break
            PAY_RIDE_NUM[subway_info[0]] = float(subway_info[3])
            FREE_RIDE_NUM[subway_info[0]] = float(subway_info[4])
            PAY_ALIGHT_NUM[subway_info[0]] = float(subway_info[5])
            FREE_ALIGHT_NUM[subway_info[0]] = float(subway_info[6])
            USE_MON.add(subway_info[0])
    #print(PAY_RIDE_NUM)
    #[['201501', '4호선', '삼각지', '138257.0', '178987.0', '32268.0', '36116.0'], 
f.close()

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size =50).get_name()
plt.rc("font", family=fontName)
#x1 = subplot()
p1 = plt.plot(PAY_RIDE_NUM.keys(), PAY_RIDE_NUM.values(), color="r", linestyle="-", marker=".", linewidth=8, markersize=5)
#x2 = x1.twin()
p2= plt.plot(FREE_RIDE_NUM.keys(),FREE_RIDE_NUM.values(),color="g", linestyle="-", marker=".", linewidth=6, markersize=5)
#x3 = x2.twin()
p3= plt.plot(PAY_ALIGHT_NUM.keys(),PAY_ALIGHT_NUM.values(),color="b", linestyle="-", marker=".", linewidth=4, markersize=5)
#x4 = x3.twin()
p4= plt.plot(FREE_ALIGHT_NUM.keys(),FREE_ALIGHT_NUM.values(),color="y", linestyle="-", marker=".", linewidth=2, markersize=5)
plt.legend(p1 + p2 + p3 + p4, ["유임승차인원", "무임승차인원","유임하차인원", "무임하차인원"])
plt.xticks(rotation=90)
plt.show()








