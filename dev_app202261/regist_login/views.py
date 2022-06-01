from urllib.parse import urlencode
from django.shortcuts import render, redirect
from django.utils import timezone
from housekeep.models import Session
from housekeep.urls import app_name
from .models import User
from .forms import RegistUser
import random
from django.urls import reverse
from housekeep.views import main

def login(request):
    random_num = []
    count = 0

    today = str(timezone.now()).split('-')
    context = {
        'year' : today[0],
        'month' : today[1],
        'count' : count,
    }
    if request.method == 'POST':
        #POSTの読み込み
        user_login = request.POST
        user_email_or_nickname = user_login['mail_or_nickname']
        user_password = user_login['password']

        #全探査
        users_information = User.objects.all()
        for user in users_information:
            if (user.e_mail == user_email_or_nickname or user.name == user_email_or_nickname) and user.password == user_password:
                count = random.randint(10000,100000)
                random_num.append(count)
            else:
                random_num.append(count)
        
        if count == random_num[0] and count != 0:
            print(count)
            sub_info = User.objects.filter(e_mail = user_email_or_nickname)
            if 'sub_info' not in locals():
                sub_info = User.objects.filter(name = user_email_or_nickname)
            print(sub_info)
            for sub_info in sub_info:
                name = sub_info.name
            Session.objects.all().delete()
            Session.objects.create(
                session_num = count,
                name = name,
            )
            return redirect('main/')
        elif count == 0:
            count = count + 1
            context = {
                'year' : today[0],
                'month' : today[1],
                'count': count,
            }
            return render(request, 'regist_login/login.html', context)
    
    return render(request, 'regist_login/login.html', context)

def regist(request):
    user = User.objects.all()
    form = RegistUser()
    context = {
        'users':user,
        'form':form,
    }

    if request.method == 'POST':
        user_data = request.POST
        e_mail = user_data['mail']
        password = user_data['password']
        name = user_data['name']

        User.objects.create(
            e_mail = e_mail,
            password = password,
            name = name,
        )

        return redirect(to='/regist/')

    return render(request, 'regist_login/regist.html', context)