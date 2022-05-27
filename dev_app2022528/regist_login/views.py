from django.shortcuts import render, redirect
from django.utils import timezone
from .models import User
from .forms import RegistUser
import random

def login(request):
    count = 0
    random_num = []

    today = str(timezone.now()).split('-')
    context = {
        'year' : today[0],
        'month' : today[1],
    }
    if request.method == 'POST':
        #POSTの読み込み
        user_login = request.POST
        user_email_or_nickname = user_login['mail_or_nickname']
        user_password = user_login['password']

        #全探査♡
        users_information = User.objects.all()
        for user in users_information:
            if (user.e_mail == user_email_or_nickname or user.name == user_email_or_nickname) and user.password == user_password:
                count = random.randint(10000,100000)
                random_num.append(count)
        
        if count == random_num[0]:
            print(count)
            return redirect(to='/main/')
        elif count == 0:
            return redirect(to='/')
    
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