"CardSubwayPayFree"#http://openapi.seoul.go.kr:8088/(인증키)/xml/CardSubwayPayFree/1/5/201501/
#(인증키)
from http.client import HTTPConnection
from json import loads

# 2015 ~ 2021년 월별로 > 하나의 파일(csv)에 저장
# 연월(ex:202211), 호선명, 지하철역, 유임승차인원, 무임승차인원, 유임하차인원, 무임하차인원 # 603
hc = HTTPConnection("openapi.seoul.go.kr:8088")
auth = (인증키)

with open("C:/Users/user/Desktop/python/test/subway/subway.csv", "w", encoding="UTF-8") as f:
    f.write("연월(ex:202211), 호선명, 지하철역, 유임승차인원, 무임승차인원, 유임하차인원, 무임하차인원\n")
    for y in range(2015,2022):
        for m in range(1,13):
            hc.request("GET", f"/{auth}/json/CardSubwayPayFree/1/700/{y}{m:02d}/")
            resbody = hc.getresponse().read().decode()
            subway = loads(resbody)
            # print(subway)
            print(f"{y}{m:02d}")
            for r in subway["CardSubwayPayFree"]["row"]:
                f.write(f"{r['USE_MON']},")
                f.write(f"{r['LINE_NUM']},")
                f.write(f"{r['SUB_STA_NM']},")
                f.write(f"{r['PAY_RIDE_NUM']},")
                f.write(f"{r['FREE_RIDE_NUM']},")
                f.write(f"{r['PAY_ALIGHT_NUM']},")
                f.write(f"{r['FREE_ALIGHT_NUM']}\n")

f.close()
hc.close()
        








