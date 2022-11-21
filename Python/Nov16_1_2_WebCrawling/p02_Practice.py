# 저장 경로 - list 형식으로!

import urllib.request as req
from urllib.error import URLError, HTTPError

pathList = ["C:/Users/user/Desktop/python/test/crawling/redfox.jpg",
"C:/Users/user/Desktop/python/test/crawling/index.html"]

urlList = ["내가 원하는 정보가 있는 site",
           "https://www.google.com" ]

for i, url in enumerate(urlList):#enumerate(인덱스 확인 가능)
    #예외 처리
    try:
        #web의 수신정보를 확인
        res = req.urlopen(url)
        
        #수신받는 내용
        content = res.read()
        print("-------------------------------------------")
        
        #상태정보 중간 확인
        print(f"헤더 정보 : {i, res.info()}")
        print(f"http status : {res.getcode()}")
        
        # 파일 쓰기
        # with : 파일을 열고, 닫는거 같이 해주는 역할
        with open(pathList[i], "wb") as f: # 'b' : binary mode
            f.write(content) 
            
        
        
    except HTTPError as e:
        print("HTTPError Code : ", e.code)
    except URLError as e:
        print("URLError Code : ", e.code)
    else:
        print("------------------------------------------------------------")
        print("성공")
        print("------------------------------------------------------------")
        
        
        
        
        
        
        
        
        
        
