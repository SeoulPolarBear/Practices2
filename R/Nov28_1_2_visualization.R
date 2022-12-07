install.packages("readxl")


library(tidyverse)
library(dplyr)
library(readxl)

# 데이터 가져오기
xlData = read_excel("C:/Users/user/Desktop/R/sample/screening_clinic.xls")
xlData

# 필요한 데이터는 시도, 시군구, 의료기관명, 주소만 필요해서
# 그 정보들만 추출해서 새로운 변수에 담기
# 변수명(컬럼명)이 한글이라서 데이터 분석중에 오류가 발생할 수 있음
# 영어로 변수명을 변경하기
names(xlData)

screening_clinic <- xlData %>% 
              select(city = 시도,`city county` = 시군구, `medical institution`= 의료기관명,addr = 주소)
screening_clinic
names(screening_clinic) <- c("state", "city", "name", "addr")

# 빈도 분석하기
screening_clinic %>% 
  group_by(state) %>% 
    summarise(n = n())

table(screening_clinic$state)
barplot(table(screening_clinic$state))
# 시도 중에 서울시 데이터를 추출해서... -> 시도 이름이 서울인 것만 새로운 변수에 담기
sc_seoul <- screening_clinic %>% 
              filter(state == '서울')

seoul_data <- screening_clinic[screening_clinic$state == "서울",]

sc_seoul
seoul_data

head(seoul_data)
nrow(seoul_data)

# 지도 시각화하기
install.packages("ggmap")

library(ggmap)

register_google(key="인증키")

# mutate_geocode() 함수는 데이터프레임의 컬럼명으로 주소가 있는 열을 기준으로
# 여러 주소의 경도, 위도 데이터를 한번에 가져올 수 있음

# mutate_geocode(data = 데이터프레임명, location = 주소가 적힌 변수명, source='google')
seoul_data <- mutate_geocode(data = seoul_data, location = addr, source='google')
View(seoul_data)

# 결측치 제거
is.na(seoul_data) # na가 있는 위치에 TRUE 표시가 됨
# na.omit() 함수를 사용해서 na가 포함된 행을 제거 함
seoul_data <- na.omit(seoul_data)
View(seoul_data)

# 서울시 지도 시각화 하기 (산점도)
seoul_map <- get_googlemap('서울', maptype = 'roadmap', zoom = 11)
ggmap(seoul_map)+
  geom_point(data = seoul_data, aes(x=lon,y=lat, color = name,size=3))
  
# 마커로 위치 표시하고 위치 이름 넣기
  
# get_googlemap()의 marker 옵션은 데이터프레임 형태의 위도, 경도 데이터를 지정해줘야 함
seoul_data_marker <- data.frame(seoul_data$lon, seoul_data$lat)
View(seoul_data_marker)
seoul_map <- get_googlemap('서울', maptype = 'roadmap', zoom = 11, markers = seoul_data_marker)
ggmap(seoul_map) +
  geom_text(data = seoul_data, aes(x=lon,y=lat), size=3, label = seoul_data$name)
