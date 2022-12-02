aResult <- readLines("C:/Users/user/Desktop/python/test/amatch/southkorea.csv",encoding="UTF-8")
aResult

aResult <- strsplit(aResult,",")
aResult # 단어와 카운팅 회수를 분리

record = c() #빈 벡터를 만들어서...
count = c()
for (ar in aResult) {
  # R에서는 인텍스 시작은 1부터 시작이니까... -> 1을 더해주고 시작
  record[length(record) + 1] = ar[1]
  count[length(count) + 1] = as.numeric(ar[2])
}

record
count

aDF <- data.frame(record=record,count=count)
View(aDF)

# count를 기준으로 오름차순으로 정렬
aDF <- aDF[order(aDF$count),]
aDF

barplot(
  aDF$count,
  names.arg = aDF$record,
  main = "대한민국 축구 역대 A매치 전적",
  xlab = "전적",
  ylab = "횟수",
  col=c("red","blue","green")
)

pie(
  aDF$count,
  labels = aDF$record,
  main ="대한민국 축구 역대 A매치 전적",
  col=rainbow(7)
)
















