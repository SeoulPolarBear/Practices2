# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

#카카오톡 내용 txt파일 정제
# ㅋ : ? , ㅎ : ?, ㅠ : ? ,... -> pie 차트로 나타내보기!
# 7월, 8월, 9월,10월, 11월, skkukdp, 비대면, 2022년, n, 안녕하세요, 오후, 오전, 판교, 사진
word = {"1일" : 0, "2일" : 0, "3일" : 0, "4일" : 0, "5일" : 0,  "6일" : 0, "7" : 0, "8" : 0, 
         "9" : 0, "10" : 0, "11" : 0, "2022" : 0,"n" : 0,"skkukdp" : 0}
#======================================================================================================
#1번 방법
with open("C:/Users/user/Desktop/python/KakaoTalkChats.txt", "r", encoding="utf-8") as f:
    txets = f.read()
    for k in word.keys():
        word[k] = len(txets.split(k)) - 1
    f.close()
fontfile = "C:/windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname = fontfile, size = 50).get_name()
plt.rc("font", family=fontName)

# pie 차트
c =['#FFFF33', '#FF00FF', '#FFCCFF', '#FFCC99', '#FF0000', '#CCFF33', 
    '#990000', '#9966FF', '#00FF66', '#33FFFF', '#3366FF', '#663300', '#CC00CC', '#9999FF']

plt.pie(list(word.values()), labels = list(word.keys()), colors=c, shadow=True,
        explode=(0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.5,0.5))
plt.title("KakaoTalk")
plt.show()
#=======================================================================================================
#2번 방법
with open("C:/Users/user/Desktop/python/KakaoTalkChats.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.replace("\n","").split(":")
        if len(line) == 2:
            for w in line[-1]:
                print(w) # 대화 내용을 한글자씩 쪼갬
                if w in word.keys():
                    word[w] += 1
                    
fontfile = "C:/windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname = fontfile, size = 50).get_name()
plt.rc("font", family=fontName)

w = {'width': 0.7, 'edgecolor': 'pink','linewidth': 5}

# pie 차트
c =['#FFFF33', '#FF00FF', '#FFCCFF', '#FFCC99', '#FF0000', '#CCFF33', 
    '#990000', '#9966FF', '#00FF66', '#33FFFF', '#3366FF', '#663300', '#CC00CC', '#9999FF']

plt.pie(list(word.values()), labels = list(word.keys()),autopct="%.2f%%" ,wedgeprops=w)
plt.title("카톡 단어 사용량")
plt.show()
    
    













