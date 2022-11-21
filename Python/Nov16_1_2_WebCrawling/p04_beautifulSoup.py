# cmd -> pip install bs4
# pip list
from bs4 import BeautifulSoup

htmlEX = '''
<html>
<head>
<meta charset="UTF-8">
<title>우리는 bs4로 Web Crawling을 할거에요!</title>
</head>
<body>
<h1>다들 식사 후라 졸리시겠지만</h1>
<h1>다들 식사 후라 졸리시겠지만2</h1>
<h2>조금 더 힘내주세요!</h2>
<p><b>BeautifulSoup</b></p>
<p>Python에서 Crawling할 때 유용하게 사용할 수 있는 Library
<a href="#">구글</a>
<a href="#">네이버</a>
<a href="#">유튜브</a>
</p>
<p>How to use bs4</p>
</body>
</html>
'''

#bs4 초기화
#html.parser : HTML 문법 규칙에 따른 문자열, 해당 문법을 바탕으로
#                단어의 의미나 구조를 분석하는 프로그램
soup = BeautifulSoup(htmlEX, 'html.parser')

print(type(soup))
print(soup)

# 코드 예쁘게 정리하기 - prettify
#print(soup.prettify())

#title부분 찾기
title = soup.html.head.title
print(type(title))
print(title)

#<class 'bs4.element.NavigableString'>
print(type(title.string))
print(title.string)
#<class 'str'>
print(type(title.text))
print(title.text)
print('-------------------------------------------------------------------------')

#h1태그
h1 = soup.html.body.h1
print(h1.string)
print(h1.text)
print('-------------------------------------------------------------------------')

#p태그
p1 = soup.html.body.p
print(p1.string)
print(p1.text) # 처음 나오는 p tag만 가져온다.
print('-------------------------------------------------------------------------')

# next_sibling : 동일한 레벨 상의 다음요소를 불러올 수 있는 기능(tag 기준 (x))
#        <-> previous_sibling
# 태그와 태그사이에 개행이 있는 경우, 엔터처리로 취급함...! -> 태그 요소로 인식을 함
p2 = p1.next_sibling.next_sibling
print(p2)
print(p2.text)



















