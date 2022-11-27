# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

xData = np.array([1,2,3,4])
yData = np.array([12,31,7,17])
yData2 = np.array([1,51,23,10])

c=["#FFB2D9","#AAB2D9","#FFBBAA","#123456"]

# plt.bar(xData, yData, width=0.5, edgecolor="#659031", linewidth= 5, color =c)
# plt.show()

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size =50).get_name()
plt.rc("font", family=fontName)

#여러 항목
# plt.bar(xData, yData, color="#AB23C9", width=0.3, align="edge")# xData기준으로 오른쪽으로 0.3
# plt.bar(xData, yData2, color="#1C32BA", width=-0.3, align="edge")# xData기준으로 왼쪽으로 0.3
# # data에 -(음수)를 붙이면 바로 위의 그래프의 옆으로 이동하게
# plt.bar(xData - 0.3, yData2, color="#654321", width=-0.3, align="edge")
# plt.show()

# 누적합
plt.bar(xData, yData, color="#B5B2FA")
plt.bar(xData, yData2, color="#25B2FC", bottom=yData) # bottom=yData는 bar 아래에 yData가 있다는 뜻
plt.show()



