import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from http.client import HTTPConnection
from json import loads

# http://openAPI.seoul.go.kr:8088/(인증키)/json/RealtimeCityAir/1/25/
#(인증키)

#서북권, 도심권, 동남권,...의 미세먼지 / 초미세먼지
#    각각 평균 값을 bar 그래프로 표현(누적합)

hc = HTTPConnection("openAPI.seoul.go.kr:8088")
hc.request("GET", "/(인증키)/json/RealtimeCityAir/1/25/")
resbody = hc.getresponse().read().decode()
print(resbody)
resbody = loads(resbody)

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size =50).get_name()
plt.rc("font", family=fontName)
#===============================================================================================
#내 풀이

# ~권 파악
MSRRGN_NM_set = set()
for r in resbody["RealtimeCityAir"]["row"]:
    MSRRGN_NM_set.add(r["MSRRGN_NM"])


MSRRGN_NM_list = list(MSRRGN_NM_set)
print(MSRRGN_NM_list)

# ~권의 index에 맞게 합계 값을 넣어준다.
# 각 인덱스에 맞게 추가해 준다.
# 각 지역의 미세먼지 농도, 초미서먼지, 개수 농도 값을 넣어주는 list
air_list = [[0]*3 for _ in range(5)]
for r in resbody["RealtimeCityAir"]["row"]:
    MSRRGN_NM_list_index = MSRRGN_NM_list.index(r["MSRRGN_NM"])
    air_list[MSRRGN_NM_list_index][0] += r["PM10"]
    air_list[MSRRGN_NM_list_index][1] += r["PM25"]
    air_list[MSRRGN_NM_list_index][2] += 1
    #print(MSRRGN_NM_list_index)

# 평균 구하기
avg_pm10_list = []
avg_pm25_list = []
for pm in air_list:
    avg_pm10_list.append(pm[0] / pm[2])
    avg_pm25_list.append(pm[1] / pm[2])
    
p1 = plt.bar(MSRRGN_NM_list, avg_pm10_list, color="#3FAB76", linewidth= 5, edgecolor="pink")
p2 = plt.bar(MSRRGN_NM_list, avg_pm25_list, color="#FA563B", bottom=avg_pm10_list,linewidth= 5, edgecolor="skyblue")
plt.legend((p1[0], p2[0]), ('pm10', 'pm25'), fontsize=15)
plt.show()

#===============================================================================================
#강사님 풀이

where, pm10, pm25 = None, None, None

whereDict={}
pm10Dict={}
pm25Dict={}

for r in resbody["RealtimeCityAir"]["row"]:
    where = r["MSRRGN_NM"]
    pm10 = float(r["PM10"])
    pm25 = float(r["PM25"])

    # 다음과 같이 key값은 그대로 사용해도 된다.
    if where in pm10Dict:
        pm10Dict[where] += pm10
        pm25Dict[where] += pm25
        whereDict[where] += 1
    else:
        pm10Dict[where] = pm10
        pm25Dict[where] = pm25
        whereDict[where] = 1

names =[]
pm10s = []
pm25s = []
for k, v in whereDict.items():
    names.append(k)
    pm10s.append(pm10Dict[k] / v)
    pm25s.append(pm25Dict[k] / v)
    

p1 = plt.bar(names, pm10s, color="#3FAB76", linewidth= 5, edgecolor="pink")
p2 = plt.bar(names, pm25s, color="#FA563B", bottom = pm10s,linewidth= 5, edgecolor="skyblue")
plt.legend((p1[0], p2[0]), ('pm10', 'pm25'), fontsize=15)
plt.show()


    





