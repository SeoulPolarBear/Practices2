# -*- coding:utf-8 -*-
#https://openapi.naver.com/v1/search/shop.xml
from http.client import HTTPConnection, HTTPSConnection
import urllib.request
from xml.etree.ElementTree import fromstring

def cut(t):
    t = t.replace("<b>", "").replace("</b>", "")
    return t

#상품명 : 입력
# xml 파싱해서
# 문서의 제목 / 최저가 / 브랜드 / 대분류 카테고리 정보를 출력
client_id = "Rest API Key"
client_secret = "Secret API Key"
Myquery = input("검색할 단어를 입력해주세요. : ")
encText = urllib.parse.quote(Myquery)

request = urllib.request.Request(url = "https://openapi.naver.com/v1/search/shop.xml?query=" + encText, method="GET")
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode == 200):
    response_body = response.read()
    #print(response_body.decode('utf-8'))
else:
    print("Error Code: " + rescode)

fish = fromstring(response_body)
items = fish.iter("item")
for f in items:
    #print(type(f.find("title")))  # <DOM 객체> ElementTree이거
    print(cut(f.find("title").text)) 
    #print(type(f.find("lprice").text)) # String
    print(f.find("lprice").text)
    print(f.find("brand").text)
    print(f.find("category1").text)
    print(f.find("category2").text)
    print(f.find("category3").text)
    print(f.find("category4").text)
    print("----------------------------------------------------------------")
###############################################################################################
hc = HTTPSConnection("openapi.naver.com")
# 요청 header 처리
h = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret
    }

hc.request("GET", "/v1/search/shop.xml?query=" + encText,headers=h)

#http통신해서 -> 응답결과가 콘솔에 나오게
resBody = hc.getresponse().read()
resBody.decode()

# XML Parsing
# DOM객체 여러개 찾기 : getiterator("태그명") / iter("태그명")
# DOM객체 하나 찾기 : .find("태그명")

for p in fromstring(resBody).iter("item"):
    print(cut(p.find("title").text)) 
    print(p.find("lprice").text)
    print(p.find("brand").text)
    print(p.find("category1").text)
    print(p.find("category2").text)
    print(p.find("category3").text)
    print(p.find("category4").text)
    print("----------------------------------------------------------------")

















