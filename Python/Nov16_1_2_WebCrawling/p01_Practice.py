# xml, json => 대기업들이 제공하는 데이터, 공공기관에서 제공하는 데이터
import urllib.request as req

# 웹 크롤링(Web Crawling) / 웹 스크래핑(Web Scrapping)
#    : 웹 페이지에 널려있는 데이터들을 프로그래밍적으로 추출하는 것
# 웹은 개발자들이 어떠한 정형화 되어있는 형태로 관리 -> 규칙이 생기기 마련
#    -> 그 규칙을 분석해서 원하는 정보들만 뽑아오는 작업
# 웹 크롤링 자체가 불법은 아님...! => 불법으로 간주되는 경우도 있습니다.
#    => 조심해서 사용!

# url - 이미지
img = "아무 이미지의 링크 주소"
html = "https://www.youtube.com"

# 다운받을 경로
path1 = "C:/Users/user/Desktop/python/test/crawling/meerkat.jpg"
path2 = "C:/Users/user/Desktop/python/test/crawling/youtube.html"

try:
    f1, h1 = req.urlretrieve(img, path1) # urlretrieve : 다운받을 파일 및 저장정보를 retrieve(검색)한다.
    f2, h2 = req.urlretrieve(html, path2)
except Exception as e:
    print(e)
    print("실패")
else:
    #정상적으로 실행되었을 경우
    # Header 정보를 출력 : 개발자 도구 -> Network -> Header
    print(h1)
    print("---------------------------------------------------------------------------------")
    print(h2)

#다운로드 파일 정보
print(f"이미지 정보 : {f1}")
print(f"파일 정보 : {f2}")

print("성공 !")
    
    
    
    
    
    
    