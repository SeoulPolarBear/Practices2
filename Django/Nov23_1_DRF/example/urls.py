from django.urls import path, include
from .views import HelloAPI
from example.views import fruitsAPI
from example.views import fruitAPI

urlpatterns = [
    path('hello/', HelloAPI),
    path('fruits/', fruitsAPI),
    path('fruits/<int:f_no>/', fruitAPI),
    ]