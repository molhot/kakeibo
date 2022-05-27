from django.urls import path,include
from . import views


app_name = 'regist_login'
urlpatterns = [
        path('', views.login, name='login'), 
        path('regist/', views.regist, name='regist'),
        path('main/',include('housekeep.urls')),
]

