#https://kin.naver.com/search/list.naver?query=
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup

q = quote(input("검색어 : "))

url = f"https://kin.naver.com/search/list.naver?query={q}"

# cmd -> pip install requests
# requests : 간단하게 HTTP 요청을 하기위해서 사용하는 모듈
response = requests.get(url) # get() : GET방식 요청
print(response.status_code)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    # select_one을 사용할 경우 : 문서의 처음부터 찾게 되며,
    #                            가장 처음에 만나는 해당 selector를 호출함
    ul = soup.select_one('ul.basic1')
    #print(ul)
    # #s_content > div.section > ul > li:nth-child(1) > dl > dt > a
    # select을 사용할 경우 : 해당하는 selector들의 모든 내용이 List에 담긴다.
    # > : 하위에 있는 selector들 전부다!
    titles = ul.select('li > dl > dt > a')
    
    for title in titles:
        #print(title.text)
        print(title.get_text())
else:
    print(response.status_code)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    