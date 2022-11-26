#Python의 시각화를 위한 library - matplotlib

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

name = []
count = []
with open("C:/Users/user/Desktop/python/ThreeKingdoms/ThreeKingdoms_count2.txt", "r", encoding ="UTF-8") as f:
    for line in f.readlines():
        line = line.replace("\n", "").split(",")
        name.append(line[0])
        count.append(int(line[1]))
        
fontfile = "C:/windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname = fontfile, size = 50).get_name()
plt.rc("font", family=fontName)

#막대그래프 - 절대적인 값 비교 : bar
# c = ['yellow', '#B2CCFF', '#FFA7A7']
# plt.bar(name, count, width=0.4, color=c)
# plt.title('Three Kingdoms')
# plt.xlabel('name')
# plt.ylabel('count')
# plt.xticks(range(len(name)), name) # 눈금 설정
# plt.ylim(0, 10000)
# plt.show()

#파이차트(pie)- 절대적인 값 비교 : bar
c = ['yellow', '#52CCFA', '#1FA7A7']
plt.pie(count,labels = name, colors=c,shadow=True, explode=(0.01,0.01,0.01))
#explode : 각 항목이 원점에서 튀어나는 정도
plt.title('Three Kingdoms')
plt.show()








