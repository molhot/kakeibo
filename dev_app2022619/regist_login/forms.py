from django import forms
from .models import User

class RegistUser(forms.Form):
    mail = forms.EmailField(label="メールアドレス")
    password = forms.CharField(label="パスワード",min_length=8)
    name = forms.CharField(label="あだ名",min_length=8)