import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

#CMD -> pip install pandas
#Pandas : 데이터 조작, 분석을 쉽게 하기 위한 모듈(라이브러리)

name_list = ["연월(ex:202211)", "호선명", "지하철역", "유임승차인원", "무임승차인원", "유임하차인원", "무임하차인원"]
df = pd.read_csv("C:/Users/user/Desktop/python/test/subway/subway.csv", names=name_list)

#groupby() : 집단 그룹별로 데이터를 집계 요약,
df2 = df.groupby("연월(ex:202211)").sum()
# plt.plot(range(df2.index.size),df2[])

print(type(df2))
    
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size =50).get_name()
plt.rc("font", family=fontName)

p1 = plt.plot(range(df2.index.size), df2["유임승차인원"], color="r", linestyle="-", marker=".", linewidth=8, markersize=5)
#x2 = x1.twin()
p2= plt.plot(range(df2.index.size),df2["무임승차인원"],color="g", linestyle="-", marker=".", linewidth=6, markersize=5)
#x3 = x2.twin()
p3= plt.plot(range(df2.index.size),df2["유임하차인원"],color="b", linestyle="-", marker=".", linewidth=4, markersize=5)
#x4 = x3.twin()
p4= plt.plot(range(df2.index.size),df2["무임하차인원"],color="y", linestyle="-", marker=".", linewidth=2, markersize=5)
plt.legend(p1 + p2 + p3 + p4, ["유임승차인원", "무임승차인원","유임하차인원", "무임하차인원"])
plt.title("월별 지하철 유무임 승차 정보")
plt.xticks(range(df2.index.size),df2.index,rotation=90)
plt.show()