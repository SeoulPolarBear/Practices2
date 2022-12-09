# A매치 데이터 파일
# mongoDB에 담고,
# 그 데이터를 활용해서
# 우리나라 경기 기준
# ggplot2 bar
# echart bar
library(mongolite)
library(tidyverse)
library(dplyr)
library(ggplot2)
library(ISOweek)
library(lubridate)
library(echarts4r)

amatch <- read.csv("C:/Users/user/Desktop/R/sample/amatch/results.csv") %>% tibble()
amatch

con <- mongolite::mongo(collection= "amatchs", 
                        db="nov29", 
                        url="mongodb://localhost",
                        verbose = TRUE, # 함수 수행시 발생하는 정보들을 자세히 보겠다.
                        options = ssl_options()) # 접속시에 보안 설정

con

con$insert(amatch)
rm(amatch)
korea_amatch_home <- con$find(query='{"home_team":{"$regex":"South Korea"}}')
korea_amatch_away <- con$find(query='{"away_team":{"$regex":"South Korea"}}')

hDF <- data.frame(korea_amatch_home)
aDF <- data.frame(korea_amatch_away)

stat = c()
differ = c()
#Home일때#################################################################################
# 득점
mode(hDF[[4]]) #"integer" => array 처럼 접근할 수 있게 해준다.

typeof(hDF[4]) #"list"
typeof(hDF[1,4]) #"integer" => DataFrame 처럼 접근해야한다.

for(i in 1:nrow(hDF)){ # => 이것처럼 hDF[i,4]이용해서 값을 가져오는것도 가능하다.
  print(hDF[i,4])
}
#nrow(hDF) : 행의 개수
# 1:nrow(hDF) => 1부터 hDF 행의 개수까지
# 만약 i in nrow(hDF) 이렇게 적으면 nrow(hDF)하나만 돌아간다.

for (i in 1:nrow(hDF)){
  getGoal = as.numeric(hDF[[4]][i])
  lostGoal = as.numeric(hDF[[5]][i])
  
  if(getGoal > lostGoal){
    if(getGoal - lostGoal == 1){
      differ[length(differ) + 1] ="1점차"
    }else if(getGoal - lostGoal == 2){
      differ[length(differ) + 1] ="2점차"
    }else if(getGoal - lostGoal == 3){
      differ[length(differ) + 1] ="3점차"
    }else if(getGoal - lostGoal == 4){
      differ[length(differ) + 1] ="4점차"
    }else if(getGoal - lostGoal >= 5){
      differ[length(differ) + 1] ="5점차 이상"
    }
    stat[length(stat) + 1] = "승"
  }else if(getGoal < lostGoal){
    if(getGoal - lostGoal == -1){
      differ[length(differ) + 1] ="1점차"
    }else if(getGoal - lostGoal == -2){
      differ[length(differ) + 1] ="2점차"
    }else if(getGoal - lostGoal == -3){
      differ[length(differ) + 1] ="3점차"
    }else if(getGoal - lostGoal == -4){
      differ[length(differ) + 1] ="4점차"
    }else if(lostGoal - getGoal >= 5){
      differ[length(differ) + 1] ="5점차 이상"
    }
    stat[length(stat) + 1] = "패"
  }
}

for (i in 1:nrow(aDF)){
  getGoal = as.numeric(aDF[[5]][i])
  lostGoal = as.numeric(aDF[[4]][i])
  
  if(getGoal > lostGoal){
    if(getGoal - lostGoal == 1){
      differ[length(differ) + 1] ="1점차"
    }else if(getGoal - lostGoal == 2){
      differ[length(differ) + 1] ="2점차"
    }else if(getGoal - lostGoal == 3){
      differ[length(differ) + 1] ="3점차"
    }else if(getGoal - lostGoal == 4){
      differ[length(differ) + 1] ="4점차"
    }else if(getGoal - lostGoal >= 5){
      differ[length(differ) + 1] ="5점차 이상"
    }
    stat[length(stat) + 1] = "승"
  }else if(getGoal < lostGoal){
    if(getGoal - lostGoal == -1){
      differ[length(differ) + 1] ="1점차"
    }else if(getGoal - lostGoal == -2){
      differ[length(differ) + 1] ="2점차"
    }else if(getGoal - lostGoal == -3){
      differ[length(differ) + 1] ="3점차"
    }else if(getGoal - lostGoal == -4){
      differ[length(differ) + 1] ="4점차"
    }else if(lostGoal - getGoal >= 5){
      differ[length(differ) + 1] ="5점차 이상"
    }
    stat[length(stat) + 1] = "패"
  }
}
goalDF = data.frame(stat,differ)
goalDF

#################################################################################
goalDF %>% 
  group_by(stat,differ) %>% 
  summarise(n=n(), .groups = "drop_last") %>% 
  ggplot(aes(stat, n, fill=differ)) + 
  geom_col(position = position_dodge(0.7), width = 0.5)
  



goalDF %>% 
  group_by(stat,differ) %>% 
    summarise(n=n(), .groups = "drop_last") %>% 
    e_chart(differ) %>% 
    e_bar(n, barwidth=10) %>% 
    e_tooltip(trigger = c("axis")) %>% 
    e_color(c("#ABCDEF","#123456"))
  
  
  
  
  
  

