# -*- coding:utf-8 -*-
from wordcloud.wordcloud import WordCloud

# wordcloud
#     cmd -> pip install wordcloud

with open("C:/Users/user/Desktop/python/KakaoTalkChats.txt", "r", encoding="utf-8") as f:
    txt = f.readlines()

wc = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf", background_color="black", max_font_size=200, width=1200, height=1200)
cloud = wc.generate(str(txt))
wc.to_file("C:/Users/user/Desktop/python/KakaoTalkChats.jpg")
print("성공 !")











