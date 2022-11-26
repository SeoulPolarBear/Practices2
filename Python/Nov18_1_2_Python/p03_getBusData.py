#http://openapi.seoul.go.kr:8088/(인증키)/xml/CardBusStatisticsServiceNew/1/5/20151101/
#(인증키)
#2017 ~ 2021년 5년치 데이터를...
#연,월,일,노선 번호, 정류장명(역명),승차총승객수, 하차총승객수
#연도별로 csv파일에 저장
from http.client import HTTPConnection
from json import loads
import datetime

#정류장명(역명) -> 혹시 ,가 들어가있을수도 있으니
#                -> ,를 .로 바꿔서 저장
# 인원수 관련 -> 정수형태로 저장
authKey =(인증키)
hc = HTTPConnection("openapi.seoul.go.kr:8088")
now = datetime.datetime.today()
years = 2022

with open(f"C:/Users/user/Desktop/python/test/bus{years}.csv", "w", encoding="UTF-8") as f:
    for m in range(1,13):
        for d in range(1,32):
            for start in range(1,39000,1000):
                url = "/%s/json/CardBusStatisticsServiceNew/" % authKey
                url += "%d/%d/%d%02d%02d/" %(start,start + 999,years,m,d)
                hc.request("GET", url)
            
                res = hc.getresponse().read().decode()
                # 다음과 같이 decode를 한 결과는 string인 상태이다.
                # 따라서 다음과 같이 if로 확인만 해주면 된다. 
                # if "CardBusStatisticsServiceNew" in res:
                    # pass
                    
                res = loads(res)
                #print(res)
            
                if "CardBusStatisticsServiceNew" not in res.keys():
                    pass
                else:
                    for r in res["CardBusStatisticsServiceNew"]["row"]:
                        
                        f.write(f"{r['USE_DT'][:4]},{r['USE_DT'][4:6]},{r['USE_DT'][6:]},")
                        f.write(f"{r['BUS_ROUTE_NO'].replace(',','.')},")
                        f.write(f"{r['BUS_STA_NM'].replace(',','.')},")
                        f.write(f"{r['RIDE_PASGR_NUM']:.0f},")
                        f.write(f"{r['ALIGHT_PASGR_NUM']:.0f}\n")
            print(years, m, d)                
    print("파일 출력 완료")
    f.close()
hc.close()
     
    