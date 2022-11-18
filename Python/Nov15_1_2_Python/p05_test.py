#1ded9e6d43edfb90edf73a1fe871184c
#3. kakao developers에서 web 검색을 통해 검색어를 입력하면 해당하는 web문서 자료가 나올 수
#있도록 하여 json파일에 옮겨 보기 편하도록 하는 코드를 작성하고 캡쳐하시오.
from http.client import HTTPSConnection
from json import loads
from urllib.parse import quote

search =quote(input("검색하고 싶은것을 입력하세요 : "),encoding="UTF-8")
hc = HTTPSConnection("dapi.kakao.com")
h = {"Authorization" : "KakaoAK ${REST API KEY}"}
hc.request("GET", "/v2/search/web?query=" + search, headers = h)
resbody = hc.getresponse().read()

resbody.decode()
result = loads(resbody)
# 4. JSON으로 연결을 하여 검색한 내용 중 제일 먼저 나온 결과의 title을 console에 찍는 코드를 
#작성하고 캡쳐하시오.
print(result["documents"][0]["title"]
      .replace("\u003c","<")
      .replace("\u003e",">")
      )
print("-------------")
# 5. 검색한 내용에서 bold 처리가 되어 있는 부분을 []로 교체하는 함수를 작성하고 그 함수를 적용하여
#검색한 내용 전체의 title, contents가 나올 수 있도록 코드를 작성하고 캡쳐하시오.
for r in result["documents"]:
    print(r["title"].replace("\u003cb\u003e","[")
      .replace("\u003c/b\u003e","]").replace("\u0026#39;",""))
    print(r["contents"].replace("\u003cb\u003e","[")
      .replace("\u003c/b\u003e","]").replace("\u0026#39;",""))
    print("-------------")











