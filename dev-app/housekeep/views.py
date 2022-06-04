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
    sessions = Session.objects.all()
    for session in sessions:
        user_name = session.name

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
    
    items = Billing.objects.filter(user_name = user_name).order_by('created_date')
    now_data = datetime.datetime.now()
    month = now_data.month
    all_info = []
    day_cost_list = []
    for item in items:
        date_info = item.created_date
        month_info = (date_info.split('-'))[1]
        if month_info == month:
            day_cost_list.append((date_info.split('-'))[2])
            day_cost_list.append(item.cost)
            all_info.append(day_cost_list)
            day_cost_list = []
    context = {
        'test': 'test',
        'nums' : sessions,
        'items' : items,
    }



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