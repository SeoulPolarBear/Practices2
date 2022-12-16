# -*- coding:utf-8 -*-
#${인증키}
from http.client import HTTPSConnection
from json import loads
from urllib.parse import quote

y = 37.394776
x = 127.11116

# 위의 좌표를 기준으로 반경 5km이내에 있는
# 검색 결과에 대한
# 검색어, 업체명, 경도, 위도 값을
# ,를 기준으로 
# csv파일에 저장
search = input("검색하고 싶은것을 입력하세요 : ")
search2 = quote(search)
h ={"Authorization" : "KakaoAK ${인증키}"}
hc = HTTPSConnection("dapi.kakao.com")
hc.request("GET", 
            f"/v2/local/search/keyword.json?query={search2}&x={x}&y={y}&radius=5000", 
            headers = h)
res = hc.getresponse().read().decode()
#print(res)
res= loads(res)
print(res)

with open("C:/Users/user/Desktop/python/test/location/locData.csv", "a", encoding="UTF-8") as f:
    for l in res["documents"]:
        f.write(f"{search},{l['place_name']},{l['x']},{l['y']}\n")
print("성공")




