# 그 파일 불러와서
# 검색어, 가게명, lng, lat
# 한 줄씩 읽어서
# , 기준으로 나눈 후
# 빈 벡터에다가 넣고
# 데이터프레임 만들기!

library(tidyverse)
library(dplyr)

locResult <- readLines("C:/Users/user/Desktop/python/test/location/locData.csv", encoding = "UTF-8")
locResult

locResult <- strsplit(locResult, ",")
locResult
cate = c()
name = c()
lng = c()
lat = c()

for (l in locResult){
  cate[length(cate) + 1] = l[1]
  name[length(name) + 1] = l[2]
  lng[length(lng) + 1] = l[3]
  lat[length(lat) + 1] = l[4]
}

cate

locDF = data.frame(cate=cate,name=name,lng=lng,lat=lat)
locDF
############################################################################################
library(ggplot2)
library(ggmap)
library(devtools)
#install.packages("devtools")
#AIzaSyAcisUlNxIQXAwFvEVIGBubj9IPHpZsVsU
register_google(key="AIzaSyAcisUlNxIQXAwFvEVIGBubj9IPHpZsVsU")

#y = 37.394776
#x = 127.11116

m <- get_map(location= c(lon=127.11116, lat=37.394776), zoom=16,
             maptype = "satellite")
ggmap(m)

View(locDF)
# 받아온 데이터를 활용 -> scatter(카테고리마다 색 다르게)
ggmap(m) + geom_point(data = locDF,aes(x=lng,y=lat,color=cate))
#2차원(2d) 밀도(density)를 보여주는 heatmap
# ..level.. : 레벨(level)이 높을수록 더 진하게 (밀도가 높을 수록)
# polygon : 다각형, bins : 선 간격격

s <- stat_density_2d(data= locDF,
                     aes(x=lng,y=lat,fill=..level..,alpha=..level..),
                     geom='polygon', bins= 30)
ggmap(m) + s + scale_fill_gradient(low="#FFC19E", high="#F15F5F")





