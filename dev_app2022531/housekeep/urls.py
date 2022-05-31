from django.urls import path
from . import views

app_name = 'housekeeping'
urlpatterns = [
        path('', views.main, name='dummy'), 
        path('show_all/<int:id>/', views.housekeeping, name='housekeeping'),
        path('show_all/<int:id>/logout/', views.logout, name='logoutpage'),
        path('show_all/<int:id>/regist_bill/', views.regist_bill, name='regist_mercandish'),
]