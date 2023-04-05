"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#urlpatterns 정리
#   -슬래시(/)는 기봊거으로 장고가 알아서 하기는 하지만 특별한 경우가 아니라면, 슬래시를 붙히도록하자.
#   -urlpatterns 배열의 마지막단은, 콤마를 생략해도 되고 붙혀도 된다.
#   -서버 구동시 변화가 감지되면 자동으로 리로더.
#   -잘못된 코드로 오류가 나면 서버 구동이 자동적으로 감지하고 에러를 낸다. 수정되면 다시 재구동을 한다.
#   -초기화면 views.index할 필요는 없다. 즉, views.main으로 설정해도 되지만 확실한 매칭이 필요하다.
urlpatterns = [
    path('onememos/', include('onememos.urls')), # routes
    path('admin/', admin.site.urls),
    ]
