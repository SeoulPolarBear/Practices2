#기상청 data
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 각 시간별 기온(temp)과 습도(reh)를 선으로 표현하시오

#http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4113565000
hc = HTTPConnection("www.kma.go.kr")
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=4113565000")
resbody = hc.getresponse().read().decode()
#print(resbody)
temp_list = []
reh_list = []
time_list = []

temp_list2 = []
reh_list2 = []
time_list2 = []

for d in fromstring(resbody).iter("data"):
    temp_list.append(float(d.find("temp").text))
    reh_list.append(float(d.find("reh").text))
    time_list.append(float(d.find("hour").text))
indexes =range(len(time_list))  
    
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size =50).get_name()
plt.rc("font", family=fontName)

plt.plot(temp_list,reh_list, color="#ABCDEF", linestyle="-", marker=".", linewidth=2, markersize=5)
plt.xlabel("기온")
plt.ylabel("습도")
plt.show()

#선 여러개2 (y축을 나눠서)
x1 = plt.subplot()
p1 = x1.plot(time_list, temp_list, color="r", linestyle="-", marker=".", linewidth=2, markersize=5)
# x1.xticks(time_list, [i for i in range(1,25)])
x1.set_xlabel("X축")
x1.set_ylabel("온도")

x2=x1.twinx()
p2=x2.plot(time_list,reh_list,color="g", linestyle="-", marker=".", linewidth=2, markersize=5)
x2.set_ylabel("습도")
x1.legend(p1 + p2, ["Red", "Green"])

plt.xticks(indexes, time_list)
plt.show()

#눈금
# plt.plot(xData,yData)
# plt.xticks(xData,["일","이","삼","사"])
# plt.yticks(np.arange(0,41,10), ["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ"])
# plt.tick_params(axis="x", direction="inout", length=10, pad=15, color="r", labelsize=20, labelcolor="#F15F5F")
# #                    x,y,both    in,out,inout
# plt.show()

    
