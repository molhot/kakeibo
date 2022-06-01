from django.shortcuts import render, redirect
from .models import Billing, Session
from .forms import SpendingBilling
import datetime

# Create your views here.
def main(request):
    sessions = Session.objects.all()
    for session in sessions:
        id = session.session_num
    return redirect('housekeeping',id)

def housekeeping(request, id):
    session = Session.objects.all()
    context = {
        'test': 'test',
        'nums' : session,
    }

    if request.method == 'POST':
        data = request.POST
        sub_session = Session.objects.filter(session_num = id)
        for session in sub_session:
            user_name = session.name
        #一意に決まります#
        created_date = data['create_date']
        cost = data['cost']
        category = data['category']
        detail = data['detail']
        Billing.objects.create(
            user_name = user_name,
            created_date = created_date,
            cost = cost,
            category = category,
            detail = detail,
        )

    return render(request, 'housekeep/housekeep.html', context)

def logout(request, id):
    Session.objects.all().delete()
    return render(request, 'housekeep/logout.html')

def regist_bill(request, id):
    form = SpendingBilling()
    context = {
        'form' : form
    }
    return render(request, 'housekeep/regist_bill.html', context)

def regist_wait(request,id):

    if request.method == 'POST':
        data = request.POST
        sub_session = Session.objects.all()
        for session in sub_session:
            user_name = session.name
        #一意に決まります#
        created_date = data['created_date']
        cost = data['cost']
        category = data['category']
        detail = data['detail']
        Billing.objects.create(
            user_name = user_name,
            created_date = created_date,
            cost = cost,
            category = category,
            detail = detail,
        )

    sub_session = Session.objects.all()
    for session in sub_session:
        id = session.session_num
    return redirect('housekeeping',id)