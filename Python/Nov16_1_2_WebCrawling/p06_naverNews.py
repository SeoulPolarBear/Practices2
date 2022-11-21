#https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EC%9D%B8
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup

# 검색어 입력했을 때,
# 관련 뉴스 내용 5page까지의 뉴스 제목들을 콘솔에 출력

q = quote(input("검색 : "))
for page in range(1,42,10):
    url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + q
    url += "&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews=0&office_type=0"
    url += f"&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={page}"
    response = requests.get(url)
    
    if response.status_code == 200:
        #print(response.status_code)
        html = response.text
        #print(html)
        soup = BeautifulSoup(html, 'html.parser')
        #print(soup)
        titles = soup.select('.news_tit')
        
        
        #ui.list_new > li> div > div > a
        print("============================================================================================")
        print(f"{(page//10) + 1}page")
        for title in titles:
            # title = u.select('li#sp_nws1.bx > div.news_wrap.api_ani_send > div.news_area > a.news_tit')
            print(title.get_text())
            print("-----------------------------------------------------------------------")
            
        
    else:
        print(response.status_code)
print("============================================================================================")
        