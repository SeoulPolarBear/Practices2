#라이브러리 설치
# Data Frame을 위한 전처리, 조작을 쉽고 빠르게 해줄 수 있는 패키지
#dplyr
install.packages("dplyr") # 이 컴퓨터에 영구적으로 설치를 한 상황
library(dplyr)            # python의 import한 개념, 필요할때마다 써야
#########################################################################
a = 1
#print(a)
a

# 화살표 기호: <- / alt + -
b <- 2
b

k <- a + 3
k

#할당
# 함수 c()를 통해서 백터를 생성할 수 있고,
# 콜론( : ) , 쉼표 (,) 를 활용해서 연속된 데이터를 표현할 수 있음


a <- c(11,22,33,44)
b = c("a","b","c","d")
a
b

#list
li1 <- list(x=1, c('cat', 'dog'), z=sum)
li1

li2 <- list(aa=a,bb=b)
li2

# data.frame : 열의 묶음으로 list만들기
mydata = as.data.frame(li2)
mydata

DF <- data.frame(c1=c(1,2,3,4,5), c2=c('ㄱ','ㄴ','ㄷ','ㄹ','ㅁ'))
DF

# $으로 변수를 선택
DF$c1
DF$c2

# sum()
sum(a) # a <- c(11,22,33,44) 다 더해줌

#paste() : 나열된 요소들을 이어 붙여서 하나의 결과값을 내보내는 함수
paste(2,4,6,8)
paste("I am", "a", "boy")
paste("오늘 밤 10시", "치킨 각!")
length(paste(2,4,6,8))


# rep : 반복
paste(rep('a', 7))
length(paste(rep('a', 7))) # 결과 7이 나온다.

#sep : seperate
paste(1,2,3,4, sep="-")
#######################################################################
LETTERS #"A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "O" "P" "Q"
#"R" "S" "T" "U" "V" "W" "X" "Y" "Z"
#반복문 / 조건문
# LETTERS 활용해서 한글자씩 뜯어내는데,
# 그 값이 W라면 ㅋㅋ 출력 나머지는 그 글자 출력

for (i in LETTERS) {
  if(i == "W"){
    print("ㅋㅋ")
  }else{
    print(i)
  }
  
}

# R에서는 인덱스가 1부터 시작을 합니다!!! ***
LETTERS[8]
LETTERS[2:5] # 2~5번째 값
LETTERS[-1] # 1번째 값 빼고 나머지 전부다
LETTERS[c(1,3,5)] # 1,3,5번째 값
#####################################################################
# 1 ~ 10번까지 출력
x <- c(1:10)
x
# 7을 10번 방복 출력
y <- rep(7,10)
y
# 1~ 10사이 숫자를 2씩 증가해서 출력
# range(1,11,2) : python
z <- seq(1,10,2)
z
######################################################################

# data.frame
myData <- data.frame(
  x = c(1,3,5,7,9),
  y = c(2,4,6,8,10)
)
myData

head(myData)

myData[1,] # 1행 전부
myData[,1] # 1열 전부
myData[1] # x(첫 행)를 출력

# 3, 5 행 -> 출력 -> 2열 빼고 (3,5행의 1열만 출력)
myData[c(3,5),-2]
myData[c(3,5),1]
#######################################################################
vt <- c(1:10)
vt

# str(갹체) : 데이터 구조를 확인
str(vt)

# as : 변수의 데이터 타입을 ~~로 취급하겠다.
vt1 <- as.integer(vt)
str(vt1)
vt2 <- as.numeric(vt)
str(vt2)

# integer : 말 그대로 정수만 저장
# numeric : integer를 포함한 모든 수를 저장

# Summary(변수) : 변수의 구성요소를 요약
#   숫자인 경우 : 
#       최소, 최대, 중간, 평균 값
#       1st Qu. /3rd Qu. (분위수 1분위(1/4), 3분위(3/4))
#       Median을 중심으로 1 Qu.와 3 Qu. 사이에 값들이 몰려있다.
summary(vt2)
#   문자인 경우 : 
#       class를 보여주고, 데이터가 총 몇 개인지 보여줌
vt3 <- as.character(vt)
str(vt3)
summary(vt3)
#######################################################################
# is : 변수가 ~~가 맞는지 아닌지 판단해줘라 (논리)
is.integer(vt3)
is.character(vt3)
######################################################################
# csv파일 불러오기
movie <- read.csv("C:/Users/user/Desktop/python/test/crawling/movies.csv")
movie

install.packages("data.table")
library(data.table)

movie2 <- fread("C:/Users/user/Desktop/python/test/crawling/movies.csv")
movie2

#tidyverse:
#   다양한 패키지를 포함하고 있는 메타 패키지
#   이 패키지를 다를 수 있게 된다면...중급 R 데이터 분석가 수준...
install.packages("tidyverse")
library(tidyverse)

tibble(movie2) #상위에 있는 10개 데이터 -> detail하게...

# %>% : 파이프연산자 (ctrl + shift + m)
#   html : table > tr > td
#   pipe operator : table %>% tr %>% td
movie2 %>% tibble() # 즉, tibble(movie2)랑 똑같은 기능 linux랑 비슷하군

head(movie2) # 상위 6개
View(movie2) # dataframe 처럼 나온다.
names(movie2) # 열에 대한 정보

nrow(movie2) # 행의 개수
ncol(movie2) # 열의 개수
dim(movie2) # 행과열의 개수








