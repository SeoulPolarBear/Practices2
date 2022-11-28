from rest_framework import serializers
from .models import Fruit

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields =['f_no','f_name','f_price','f_explanation']
        
#Serializer
# 사전적 의미로는 직렬화, Django 프로젝트에서 내가 만든 모델로부터 뽑아낸 데이터들을
# JSON타입으로 바꾸는 작업
# Django에서 데이터들은 JSON형태의 포맷이 아닌 파이썬 객체의 형태로 저장이 됨
# API(Application Programming Interface, 응용 프로그램에 사용할 수 있도록)
#    운영체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스)는
#    이런 데이터들을 클라이언트한테 보내주는 역할을 하는데,
#    이 때 어떤 작업도 하지 않고 데이터를 그대로 보내게 된다면
#    클라이언트는 읽지도 못하는 파이썬의 데이터를 받아야 함...
#    이를 위해서, 파이썬 데이터를 읽을 수 있는 문자열(ex:JSON)로 변환하여 보내줘야하고,
#    이렇게 변환하는 작업을 직렬화(Serialize)라고 함

# 반대로, 클라이언트가 데이터를 서버에 보내주는 경우도 있는데, 
# 클라이언트는 API 요청에 의해 데이터를 JSON 문자열 형태로 입력해서 보내줄 것!
# 서버 입장에서는 모델을 통해 저장하려면 데이터가 파이썬 객체의 형태여야 하기 때문에
# 받아낸 데이터를 저장할 수 없음
# 그래서 반대로 JSON형태의 문자열을 파이썬 데이터 객체로 변환하는 작업이 필요한데,
# 이 작업을 역직렬화(Deserialize)라고 함
# 이 시리얼라이저는 직렬화와 역직렬화 기능을 동시에 가지고 있음

# => 클라이언트와 서버 API간의 데이터 양식을 맞춰주는 변환기라고 생각하면...!

# ModelSerializer는 모델의 내용을 기반으로 동작하는 시리얼라이저
#    코드의 중복을 줄일 수 있고, 필드 선언도 모델에서 이미 했으므로
#    시리얼라이저에서는 간단하게 작업을 마칠 수 있음













        
        
        