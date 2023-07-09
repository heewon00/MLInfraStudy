from django import forms
from .models import Mymodel

# forms는 사용자로부터 데이터를 수집하고 유효성을 검사하는 웹 폼을 생성하고 처리하는 데 사용
# models는 데이터베이스와 상호작용하여 데이터의 구조를 정의하고 데이터를 저장하고 조회하는데 사용

class MyForm(forms.ModelForm):
    class Meta:
        model = Mymodel
        fields = "__all__"