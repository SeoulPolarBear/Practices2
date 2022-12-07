library(dplyr)
library(tidyverse)

# 데이터 전처리(Data Preprocessing)
# 주어진 원래 데이터를 그대로 사용하기보다, 원하는 형태로 변형해서 분석하는 경우
# 비슷한 말로... 데이터 가공(Data manipulation), 데이터 핸들링(Data Handling),
# 데이터 클리닝(Data Cleaning) , ...
# 성별, 사는 지역, 흡연 여부, ...-> 문자를 숫자형태로 변형해서 분석하는 것!
#   => 이게 전처리!

bike <- read.csv("C:/Users/user/Desktop/R/sample/bike.csv") %>% 
  tibble() # 상위 10개 보여주고 data.frame으로 보여줌
# names(bike) 
# View(bike)

# "자전거번호","대여일시","대여.대여소번호", "대여.대여소명","대여거치대",     
# "반납일시","반납대여소번호","반납대여소명","반납거치대","이용시간",       
# "이용거리"

bike <- bike %>% 
  rename(bikeNo = "자전거번호",
         br_dt = "대여일시",
         br_no = "대여.대여소번호", 
         br_nm = "대여.대여소명",
         br_std = "대여거치대",     
         re_dt = "반납일시",
         re_no = "반납대여소번호",
         re_nm = "반납대여소명",
         re_std = "반납거치대",
         ride_time = "이용시간",       
         ride_dist = "이용거리")
View(bike)

# 대여.대여소명 어디가 가장 많이 이용되었는지 조회(대여.대여소명 / 빈도수)
bike %>% 
  count(br_nm, sort=T) # 빈도수 기준으로 내림차순

# 반납대여소명 / 어디가 가장 많이 반납되었는지 조회
bike %>% 
  count(re_nm, sort=T)
# 쓸모없는 변수의 열은 제외 (자전거번호, 대여거치대, 반납거치대)
#1
bike <- bike %>% 
  select(-1,-5,-9)
#2
bike <- bike %>% 
  select(-c(bikeNo,br_std,re_std))

bike

# 이용거리가 10m이하인 곳 제외(데이터 : m 단위)
bike<-bike %>% 
  filter(ride_dist > 10)

# 이용시간이 1분이하면 제외(데이터 : 분 단위)
bike<-bike %>% 
  filter(ride_time > 1)

# 이용거리, 이용시간에 대한 통계 수치 조회(최소, 중앙, 평균, 최대)
bike %>% 
  summarise(
    min_ride=min(ride_dist),
    min_time=min(ride_time),
    median_ride=median(ride_dist),
    median_time=median(ride_time),
    mean_ride=mean(ride_dist),
    mean_time=mean(ride_time),
    max_ride=max(ride_dist),
    max_time=max(ride_time)
            )

# 대여.대여소명, 반납대여소명 빈도수가 많은대로 내림차순 -> 상위 30개만 출력
#1
bike %>% 
  count(br_nm,re_nm, sort=T) %>% head(30)
#2
bike %>% 
  count(br_nm,re_nm, sort=T) %>% 
  print(n=30)
#===========================================================================================
install.packages("ISOweek")
install.packages("lubridate") # 날짜.시간데이터를 다루는 패키지

library(ISOweek)
library(lubridate)

View(bike)
 bike <- bike %>% 
   #mutate() 함수는 기본적으로 dataframe 자료형에 새롭게 파생되는 열(컬럼)을 만드는 함수
   mutate(wk = paste0(br_dt %>% isoweek(), '주차'), # paste0 concat이랑 같은 쓰임새이다.
          yoil = br_dt %>% lubridate::wday(label = T), # 요일 (일 ~ 토) 
          date = br_dt %>% substr(1,10),
          hour = br_dt %>% substr(12,13)) %>% 
   select(-c(br_no,re_no))
View(bike) 

# 일자별 자전거 이용량(건수)을 bar 그래프로 표현 -> 주차별로 그래프색 다르게
# (echart4r)

library(echarts4r)

bike %>% 
  group_by(wk,date) %>% 
  summarise(n=n(), .groups="drop_last") %>% 
  #.group = "drop_last" : group_by()의 상태를 summarise 이후에
  # 유지할 것인지, 삭제할 것인지에 대한 옵션
  e_chart(date) %>% 
  e_bar(n,barwidth=15) %>% 
  e_tooltip(trigger = c("axis"))






































  











