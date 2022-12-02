#시험 관련한 데이터 자료 불러오기
library(tidyverse)
library(dplyr)

exam <- read.csv("C:/Users/user/Desktop/R/sample/exams.csv")
exam
#################################################################################
# 열을 기준으로 하는 함수들
#################################################################################

# data의 빈도를 나타내는 / 조사하는 함수
# table(), n(), count()

# table() : data의 종류별 개수가 몇 개인지 파악
# table(data.frame이름$변수명)
table(exam$`race/ethnicity`)

# n() : dplyr 패키지 안에 있는 함수
# group_by() 함수에 연결이 되어있는 summarise()함수 내부에 포함
# table()과는 다르게 세로로 출력
# data.frame명 %>% group_by(변수명) %>% summarise(표시할 변수명 =n())
exam %>% 
  group_by(`race/ethnicity`) %>% 
  summarise(n=n())

#count() : dplyr 패키지 안에 있는 함수
#count(data.frame명, 변수명)
count(exam, `race/ethnicity`)
##############################################################################
# mean(평균) vs median(중앙값)
# 중앙값 : data들의 중심이 되는 위치를 가리키는 값 >> [대표값]이라고도 부름

# 대부분은 mean(평균)으로 계산을 함
# 경우에 따라서는 median(중앙값)이 더 정확할 때가 있음
#   => data가 너무 크거나, 너무 작거나하는 극단적인 값들이 많은 경우
#   => 어느 한쪽으로 데이터가 치우쳐져 있는 경우

# 그룹별로 인원이 몇 명있는지, 읽기시험 점수의 평균값, 중앙값 출력

exam %>% 
  group_by(`race/ethnicity`) %>% 
  summarise(
    n=n(),
    mean = mean(`reading score`),
    median = median(`reading score`))
#################################################################################
# 행을 기준으로 하는 함수들
#################################################################################

# slice() : index에 의한 행 선택
# 특정한 행을 선택하거나, 제거 가능
# 양수(+) : 해당하는 행을 선택
# 음수(-) : 해당한느 행을 제거

# 5 ~ 10번째 행
exam %>% slice(5:10)

# 101 ~ 1000행 제거
exam %>% slice(-101:-1000)
exam %>% slice(-(101:1000))

# 성별, 그룹으로 묶어서 6~10번째 정보
#     -> 수학점수 최대값, 읽기 점수 최소값, 쓰기점수 평균값을 출력

exam %>% 
  group_by(gender,`race/ethnicity`) %>% 
    slice(6:10) %>% 
      summarise(math_max = max(`math score`),
                reading_min = min(`reading score`),
                writing_mean = mean(`writing score`),
                )

# 마지막 행만 보고싶다 => n() 함수
exam %>% slice(n())

# slice_head() : data.frame 처음
# slice_tail() : data.frame 마지막
# 행의 개수 지정 : n = 개수 (n=10)
# 행의 비율 지정 : prop = 비율(prop=0.1)
exam %>% slice_head(n=10)
exam %>% slice_tail(prop=0.3) # 하위 30% 보고 싶을 때때

insurance <- read.csv("C:/Users/user/Desktop/R/sample/insurance.csv")
insurance

#slice_sample() : 랜덤으로 행 선택
# n, prop 통해서 개수나 비율을 설정할 수 있음
insurance %>% slice_sample(n=5)
insurance %>% slice_sample(prop = 0.3)

# slice_max() : 특정변수가 가장 클 때 => 가장 큰 순서대로 보여준다.
# slice_min() : 특정변수가 가장 작을 때
insurance %>% slice_max(bmi, n=10)
insurance %>% slice_min(charges, prop = 0.3)
###############################################################################
# arrange() : 특정 변수를 기준으로 행을 재배열
# 기본값은 오름차순
insurance %>% arrange(bmi)

# exam 쓰기시험 오름차순, 쓰기시험 점수가 같으면 -> 읽기점수 내림차순 정렬
exam %>% arrange(`writing score`, desc(`reading score`))

# 성별, 교육 등급을 그룹화해서, 수학점수의 평균값 지표를 -> 내림차순으로 정렬
View(exam)
exam %>% 
  group_by(gender, p) %>% 
    summarise(mean_math = mean(`math score`)) %>% 
      arrange(desc(mean_math))
################################################################################
exams <- exam %>% 
  select(`math score`,`reading score`,`writing score`)
View(exams)

# distinct() : 중복없는 유일한 값 추출

exams %>% 
  distinct(`math score`)

exams %>% 
  head(12) %>% 
  distinct(`writing score`, .keep_all = T)
# .keep_all = T(TRUE) : 모든 열을 유지해서 보여줌, 이 옵션을 쓰지 않으면 
# 지정한 열만 보여줌
###############################################################################
library(ggplot2)
# aes(aesthetic)은 그래프의 미적부분을 지정하는 속성
# 아래 코드을 실행하면, 축이랑 바탕만 그려지고...
# 실제 그래프는 다음줄에다가 그래프 그리는 함수를 추가해줘야!!
ggplot(data = exam, aes(x=math.score, y = reading.score, color=gender))

# 산점도 (Scatter Plot)
exam %>% 
  ggplot(aes(math.score,reading.score,color=gender)) +
  # + 로 ggplot과 geom_point를 연결
  # pipe( %>% ) 대신에 + 를 사용한다고 생각하면...
  geom_point() +
  scale_color_brewer(palette = "Set1")
  # scale_color_manual은 직접 색을 정한다.
# scale_color_grey는 색을 흑백으로 시각화
# scale_color_brewer는 누군가가 이미 만들어 놓은 palette 자료 값과 색을 대응시킴

# 색상 조합 참고
RColorBrewer::display.brewer.all()

# 선그래프
exam %>% 
  ggplot(aes(math.score,reading.score,color=gender)) +
  geom_line()

# 막대 그래프
exam %>% 
  ggplot(aes(gender)) + 
  geom_bar(fill = "orange") # bar는 빈도수를 나타낼 때 사용한다.

exam %>% 
  group_by(gender) %>%
  summarise(n = n(),
            m = mean(math.score)) %>% 
  ggplot(aes(gender,m)) + 
  geom_col(fill = "royalblue") # col은 평균값을 나타낼 때 사용한다.

exam %>% 
  group_by(gender, race.ethnicity) %>% 
  summarise(n=n(),
            m=mean(reading.score)) %>%
  ggplot(aes(gender, m, fill=race.ethnicity)) + # x축, y축, color
  geom_col(position = "dodge") # dodge : 복수의 데이터를 독립적인 막대그래프로 표현 
            

# 히스토그램
exam %>% 
  ggplot(aes(writing.score, fill=gender)) + 
  geom_histogram(position = 'identity', alpha = 0.5)
  # identity : y축 값은 높이를 데이터의 기반으로 전해줄 때 사용
  # alpha : 투명도도


# 상자그래프(Boxplot)
exam %>% 
  ggplot(aes(race.ethnicity, math.score, fill=gender)) + 
  geom_boxplot()

exam %>% 
  ggplot(aes(race.ethnicity, math.score, fill=gender)) + 
  geom_boxplot() + 
  coord_flip() # 축 반전

# 열 지도(heatmap)
exam %>% 
  group_by(race.ethnicity, parental.level.of.education) %>% 
  summarise(n=n(),
            r=mean(reading.score)) %>%
  ggplot(aes(race.ethnicity,parental.level.of.education, fill=n)) +
  scale_fill_gradient(low='yellow', high='red') + 
  geom_tile()




