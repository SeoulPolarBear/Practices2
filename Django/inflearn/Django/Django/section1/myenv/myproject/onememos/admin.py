from django.contrib import admin
from onememos.models import Memo

# Register your models here.
admin.site.register(Memo) 
# 만든 model을 admin 사이트에 등록을 해야 admin에서 인식을 하기 때문에 등록을 해야 한다.
# 이제 CMD에서 등록 된 것을 반영하기 위해서 migrate를 해줘야 한다.
# 그 전에 선행으로 2가지를 수행햐야 한다.
# 1) 환경설정이 들어있는 myproject가 최상위 폴더이다.
# settings.py에 Apps을 등록 해줘야 한다. Installed_Apps=[]에기에 추가를 해줘야 한다.
# 2) App폴더 내에 migrations 폴더에 init을 추가 하기 위해 section\myproject 폴더에서 
# py manage.py makemigrations를 실행해줘야 한다.
# make migrations를 함으로써 db를 이행할 폴더를 만드는 것이다.
# 3) 그 다음에 프로젝트에서 migrate를 하면 된다.
