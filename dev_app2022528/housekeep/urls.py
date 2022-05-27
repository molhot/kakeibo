from django.urls import path
from . import views

app_name = 'housekeep'
urlpatterns = [
        path('', views.main, name='housekeep'), 
]