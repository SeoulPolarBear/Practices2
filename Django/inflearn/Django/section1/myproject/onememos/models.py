from django.db import models

# Create your models here.
# 클래스를 작성 하는 것 모델을 만드는 것

#1) 데이터 모델
# 클래스로 코드를 작성할 때 PK는 자동으로 할당하므로 궅이 적어줄 필요가 없다.
# idx(정수형) x
# memo_text(문자형) o
# published_date(날짜형) o

class Memo(models.Model):
    memo_text = models.CharField(max_length=250) # 200자 이하 같이 제한이 있는 것을 사용할 때 쓰는 함수
    memo_text2 = models.TextField()
    published_date=models.DateTimeField(auto_now_add=True) # 현재 시간을 저장한다.

# class의 getter이다. 즉 admin 서버에서 DB 조작할 때 text를 보이게 해줄 수 있다.  
    def __str__(self):
        return self.memo_text
    
#2) 작성후 -> 반영을 위해서 -> Admin사이트에 반영 -> admin.py 열고 추가 작성.