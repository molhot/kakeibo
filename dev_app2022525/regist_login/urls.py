from django.urls import path
from . import views
app_name = 'regist_login'
urlpatterns = [
        path('', views.login, name='login'), 
        ]

