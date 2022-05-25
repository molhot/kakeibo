from django.shortcuts import render, redirect
from django.utils import timezone

def login(request):
    today = str(timezone.now()).split('-')
    context = {
        'year' : today[0],
        'month' : today[1],
    }
    return render(request, 'regist_login/login.html', context)