# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# Numpy
#     cmd -> pip install Numpy

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size =50).get_name()
plt.rc("font", family=fontName)

#matplotlib에서는 일반적으로 Numpy에 있는 Array를 이용
#Numpy를 사용하지 않더라도, 모든 시퀀스는 내부적으로 Array로 변환을 해서 사용

yData = np.array([12,31,1,2]) #Numpy의 Array를 사용
xData = [1,2,3,4]             #Numpy를 사용하지 않아도 내부적으로 변환

# 기본
# plt.plot(yData) # plot : 선그래프를 의미한다.
# plt.show()

# x, y
# plt.plot(xData,yData) # x축 에는 xData, y축에는 yData가 축이되어 선 그래프가 그려진다.
# plt.show()

# 축
# plt.plot(xData, yData)
# plt.xlabel("x축")
# plt.ylabel("y축")
# plt.axis([0, 10, 0, 50]) # [xmin, xmax, ymin, ymax]를 나타낸다. => 
                         # 즉, (x,y) => [0,10], [0,50]인 평면에 선 그래프가 그려진다.

# title
# plt.plot(xData, yData)
# f = {"fontsize" : 15, "fontweight" : "light"} # blod, light, ultralight, ...
# plt.title("ㅋㅋ", loc="left")
# plt.title("ㅎㅎ", loc="center")
# plt.title("제목", loc="right", fontdict=f)
# plt.show()

#style
# plt.plot(xData, yData, "c-.h")
# plt.show()

# 색/ 선의 모양/ 마커의 모양

# 색
#    B : blue / g : green / r : red / y : yellow / k : black / w : white / c : cyan

# 선의 모양 -> edge
#    ':' : 점선
#    '-' : 실선
#    '--' : dashed line
#    '-.' : 실선 + 점선

# 마커의 모양 => node
#    '.' : 점
#    'o' : 동그라미
#    'v' : 아래삼각형
#    '^' : 위 삼각형
#    '<' , '>' : 삼각형 왼쪽, 오른쪽
#    's' : squre(사각형)
#    'p' : 오각형
#    'h' : 육각형
#    '*' : 별
#    '+' : + 모양
#    'x' : x 모양
#    '*' : 별
#    '*' : 별

# plt.plot(xData,yData,color="#A566FF", linestyle="--", marker="+", linewidth=5, markersize=10)
# plt.plot(xData,yData,color="#A566FF", linestyle="-.", marker="*", linewidth=5, markersize=10)
# plt.show()

# grid(격자)
# plt.plot(xData,yData)
# plt.grid(axis="both", color="#ABCDEF", linestyle="-.")
# plt.show()

#눈금
# plt.plot(xData,yData)
# plt.xticks(xData,["일","이","삼","사"])
# plt.yticks(np.arange(0,41,10), ["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ"])
# plt.tick_params(axis="x", direction="inout", length=10, pad=15, color="r", labelsize=20, labelcolor="#F15F5F")
# #                    x,y,both    in,out,inout
# plt.show()

# # 선
# plt.plot(xData,yData)
# plt.hlines(31,1,2,color="r", linestyles="--")   # 실제 y값, xmin, xmax (즉, 상수 함수 y = 31 x는 (1,2)을 표현)
# plt.vlines(1,31,12,color="r", linestyles="--")  # 실제 x값, ymin, ymax (즉, 상수 함수 x = 1 y는 (12,31)을 표현)
# plt.show()

#선 여러개
# yData = np.array([12,31,1,2]) #Numpy의 Array를 사용
# xData = [1,2,3,4]             #Numpy를 사용하지 않아도 내부적으로 변환
# yData2 = [5,66,1,10]
# plt.plot(xData,yData, "r-")
# plt.plot(xData,yData2, "g:")
# plt.legend(["빨강(data1) data", "초록(data2) data"])
# plt.show()

#선 여러개2 (y축을 나눠서)
yData2 = [500,600,100,1000]

x1 = plt.subplot()
p1 = x1.plot(xData, yData, "r-")
x1.set_xlabel("X축")
x1.set_ylabel("Y축")

x2=x1.twinx()
p2=x2.plot(xData,yData2,"g:")
x2.set_ylabel("Y축2")
x1.legend(p1 + p2, ["Red", "Green"])
plt.show()











































































