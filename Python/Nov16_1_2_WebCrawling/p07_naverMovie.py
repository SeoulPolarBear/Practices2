# 크롤링해서 1~10페이지까지의
# 영화제목, 평점, 감상평의 형태로 CSV파일로 저장
import requests
from bs4 import BeautifulSoup

#ex) 동감, 10, 감상평

with open("C:/Users/user/Desktop/python/test/crawling/movies.csv","w", encoding="UTF-8", newline="") as file:
    file.write("title, score, review\n")
    for page in range(1,11):
        url = f"https://movie.naver.com/movie/point/af/list.naver?&page={page}"
        res = requests.get(url)
        
        if res.status_code == 200:
            soup = BeautifulSoup(res.text,'html.parser')
            reviews = soup.select('.title')
            for r in reviews:
                reviews_list = r.get_text().split("\n")
                #print(reviews_list)
                file.write(reviews_list[1] + ",")
                file.write(reviews_list[3].split("- 총 10점 중")[1] + ",")
                file.write(reviews_list[5] + "\n")
                #file.write(f"{file1},{file2},{file3}\n")
        else:
            print(res.status_code)
    print("잘됨")
        