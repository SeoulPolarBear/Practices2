from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
# 1. 아래 주어진 url과 인증키를 이용하여 서울시의 전통시장 현황 정보를 HTTP통신을 통해 받아
# console창에 찍고 그 정보를 xml 파일에 넣은 후 해당하는 코드를 캡쳐하시오.
#
# URL : http://openapi.seoul.go.kr:8088/sample/xml/ListTraditionalMarket/1/330/
# API KEY : 인증키
# 전통 시장 XML 파싱 
hc = HTTPConnection("openapi.seoul.go.kr:8088")
#인증키
hc.request("GET", "/인증키/xml/ListTraditionalMarket/1/330/")

resbody = hc.getresponse().read()
resbody.decode()

#2. 받아온 xml 정보 중 자치구명, 전통시장명, 위도, 경도에 해당하는 정보만을 정제하여 
#csv파일로 만드는 코드를 작성하고 캡쳐하시오.
file = open("C:/Users/user/Desktop/python/test/traditionalMarket.csv","w",encoding="UTF-8")
file.write("자치구명, 전통시장명, 위도, 경도\n")
for data in fromstring(resbody).iter("row"):
    result = f"{data.find('GUNAME').text},"
    result += f"{data.find('M_NAME').text},"
    result += f"{data.find('LAT').text},"
    result += f"{data.find('LNG').text}\n"
    file.write(result)

print("내보내기 성공")
file.close()



