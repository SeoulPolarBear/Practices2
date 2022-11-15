#42008a8c8e7402a3fc9d3b1a7df8fee9
#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
from http.client import HTTPSConnection
from json import loads

#도시 이름 : 입력(영어)
#응답 내용 출력까지
# 요청파라미터 추가 O
API_key = "API_key"
city_name = input("검색하실 도시이름을 영어로 입력하세요. :")
lang= "kr"
hc = HTTPSConnection("api.openweathermap.org")
hc.request("GET", f"/data/2.5/weather?q={city_name}&appid={API_key}&lang={lang}")

res = hc.getresponse()
resBody = res.read()
resBody.decode()

weatherData = loads(resBody) # JS -> Python 역할을 한다.

#날씨 / 기온 / 체감기온 / 습도 / 바람 속도
#데이터를 콘솔창에 출력
# Dict / list 잘 확인하면서

#날씨
print("날씨 :", weatherData["weather"][0]["main"])
print("날씨 :", weatherData["weather"][0]["description"])

#기온
print("기온 :", weatherData["main"]["temp"])

#체감기온
print("체감기온 :", weatherData["main"]["feels_like"])

#습도
print("습도 :", weatherData["main"]["humidity"])

#바람 속도
print("바람 속도 :", weatherData["wind"]["speed"])























