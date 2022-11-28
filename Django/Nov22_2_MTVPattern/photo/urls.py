#photo 앱에 대한 url을 작성할 것이기 때문에
# photo 폴더 안에 urls.py 만들기
from django.urls import path
from . import views

urlpatterns = [
    #views.py에 있는 photo_list 함수를 불러냈고,
    # photo/photo_list.html과 렌더링을 했음
    path('', views.photo_list, name ="photo_list"),
    # 여기서 pk라는 이름의 정수형 변수가 들어갈 자리를 의미(유일하게 데이터를 구분할 수 있음)
    path('photo/<int:pk>', views.photo_detail, name ="photo_detail"),
    
    path('photo/new/', views.photo_post, name ="photo_post"),
    path('photo/<int:pk>/edit', views.photo_edit, name ="photo_edit"),
    path('photo/<int:pk>/delete', views.photo_delete, name ="photo_delete"),
]