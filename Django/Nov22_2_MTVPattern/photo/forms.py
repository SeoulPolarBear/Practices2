from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        # Photo를 가지고 왔으므로 model에 그대로 적용되서 굳이 input을 넣어줄 필요가 없게 된다.
        model = Photo
        fields = (
            'title',
            'author',
            'image',
            'description',
            'price',
            )
        
# Django의 ModelForm이라는 것을 상속받아 위의 필드값을 입력으로 받는 PhotoForm 클래스를 생성