from django.shortcuts import render, redirect
from django.utils import timezone
from .models import User
from .forms import RegistUser

def login(request):
    today = str(timezone.now()).split('-')
    context = {
        'year' : today[0],
        'month' : today[1],
    }
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