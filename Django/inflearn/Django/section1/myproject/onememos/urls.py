from django.urls import path

from . import views
#default : localhost:8000/onememos/
urlpatterns = [
    path('', views.main, name = 'index'), # (router, view function) -> default IP : localhost:8000/onememos/
    path('createMemo/',views.createMemo),
]