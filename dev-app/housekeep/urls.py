from django.urls import path
from . import views

app_name = 'housekeeping'
urlpatterns = [
        path('', views.main, name='housekeep'), 
        path('logout/', views.logout, name='logoutpage'),
]