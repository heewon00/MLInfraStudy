from django.contrib import admin
from . import models
# Register your models here.
# 추가한 모델을 admin page에 등록
admin.site.register(models.Mymodel)