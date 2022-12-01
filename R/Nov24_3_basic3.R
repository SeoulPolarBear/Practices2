library(data.table)
library(tidyverse)
library(dplyr)

# data불러오기
exam <- fread("C:/Users/user/Desktop/R/sample/exams.csv")
exam

# 관측치 첫 6개
head(exam)

# 관측치 끝 3개
tail(exam, n=3)

#스프레드시트 형식으로 확인
View(exam)

#변수 이름 확인하기
names(exam)

#특정 위치 변수 이름 확인하기
names(exam)[6:8]

#변수명 바꾸기
names(exam)[3:5] = c('p','l','t')

#간단한 변수별 용약
summary(exam)

sum(exam$`math score`) # 수학점수 총합
mean(exam$`math score`) # 수학점수 평균
length(exam$gender)
#######################################################################
head(exam)
exam %>% head()

#dplyr 패키지를 불러오면 파이프연산자를 사용할 수 있음
# 파이프연산자( %>% ) : 체인 연ㅅ나자 / 파이프
# %>% : ctrl + shift + m

exam %>%
  select(gender, `reading score`, 8) %>% head()
# 원하는 열의 이름 혹은 인덱스를 통해서 접근할 수 있다.
########################################################################
insurance = fread("C:/Users/user/Desktop/R/sample/insurance.csv")
insurance


# 3,6,7 열 데이터 조회
insurance %>% 
  select(3,6,7)
# 2~6 열 데이터 조회
insurance[,c(seq(2,6))]
insurance %>% 
  select(2:6)
# smoker, bmi 내용만 조회
insurance %>% 
  select(smoker, bmi)
# smoker, bmi 제외하고 전체 조회
insurance %>% 
  select(-smoker, -bmi)
# 1, 2열 빼고 나머지 조회
insurance %>% 
  select(-1, -2)
# 3열, region 빼고 나머지 조회
insurance %>% 
  select(-3, region)
# 나이, 성별, bmi, 보험비용 조회
insurance %>% 
  select(-4,-5,-6)

insurance %>% 
  select(age,sex,bmi,charges)

insurance %>% 
  select(age:bmi,charges)

insurance %>% 
  select(1:3,charges)
#######################################################################
# select() : 열 추출
# select()에서 사용할 수 있는 기능(함수)
#   -() : 모든 변수를 선택
#   -last_col() : 제일 마지막에 있는 변수 선택
#   -starts_with(값) : 이름이 ~으로 시작하는 변수를 선택
#   -ends_with(값) : 이름이 ~으로 끝나는 변수를 선택
#   -contains(값) : 이름에 ~이 들어있는 변수를 선택

# c로 시작하는 변수의 내용을 조회
insurance %>% 
  select(starts_with("c"))
# n으로 끝나는 변수의 내용을 조회
insurance %>% 
  select(ends_with("n"))
# s가 포함된 변수의 내용을 조회
insurance %>% 
  select(contains("s"))
########################################################################
# ! : 논리 부정(나열된 열의 여집합)
# - : 연산자 (차집합)

# 1, 2, 4번째 변수를 제외한 나머지를 출력
insurance %>% 
  select(!c(1,2,4))
insurance %>% 
  select(-c(1,2,4))
########################################################################
# 특정타입의 변수만 뽑아올 수 있음
insurance %>% 
  select(where(is.numeric)) # 데이터타입이 숫자인거 선택

exam %>% 
  select(where(is.character)) #데이터타입이 문자인거 선택
########################################################################
# filter() : 행 추출
# exam에서 성별이 남자인 사람의 정보 위에서부터 6개
exam %>% 
  filter(gender =="male") %>% 
  head()

# 성별이 여자면서, c그룹에 속하는 사람의 정보 끝에서부터 6개 조회
exam %>% 
  filter(gender =='female') %>%  
    filter(`race/ethnicity` == "group C") %>% 
      tail()

exam %>% 
  filter(gender =='female', `race/ethnicity` == "group C") %>% 
  tail()

#########################################################################
# summarise()
#   평균, 빈도, ... 기본적인 통계 수치를 요약하고 싶을 때 사용

exam %>% 
  summarise(n=n(),max(`math score`)) 
# n() : 빈도 n =n() : n이라는 열로 표현하겠다.

exam %>% 
  summarise(min(`math score`)) 

exam %>% 
  summarise(mean(`math score`)) 

exam %>% 
  summarise(median(`math score`)) 
#######################################################################
# exam의 읽기 시험점수의 최대값
#        쓰기 시험점수의 최대값
#        읽기 시험점수의 평균값
#        쓰기 시험점수의 평균값
# 을 하나로 합쳐서 출력력

exam %>% 
  summarise(n = n(),
            max(`reading score`), 
            max(`writing score`),
            mean(`reading score`),
            mean(`writing score`))

# group_by() : 그룹화
exam %>% 
  group_by(gender) %>% 
  summarise(min(`writing score`),
            max(`reading score`),
            mean(`math score`)
            )

# insurance
# 흡연 여부로 나눠서
# bmi의 최대값
# age의 최소값
# charges의 평균값
# bmi의 중앙값
# 을 하나로 합쳐서 출력
insurance %>% 
  group_by(smoker) %>% 
  summarise(
            n=n(),
            max(bmi),
            min(age),
            mean(charges),
            median(bmi)
  )
######################################################################
#across() : 여러 열을 대상으로 같은 작업을 해야하는 경우
# 모든 숫자형 변수의 평균값을 계산
insurance %>% 
  summarise(across(where(is.numeric),mean))

# 변수명이 b로 시작하는 변수들의 중앙값
insurance %>% 
  summarise(across(starts_with('b'),median))

# 변수명이 age, charges인 변수의 평균값
insurance %>% 
  summarise(across(c(age,charges),median))

# 변수명이 age인 변수의 평균값과 중앙값
insurance %>% 
  summarise(across(age,c(mean = mean,median = median)))




















