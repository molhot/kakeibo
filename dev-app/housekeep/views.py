from django.shortcuts import render, redirect
from .models import Billing, Session
from .forms import SpendingBilling
import matplotlib.pyplot as plt
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
        print(date_info)
        print("check")
        month_info = date_info.month
        if month_info == month:
            day_cost_list.append(date_info.day)
            day_cost_list.append(item.cost)
            all_info.append(day_cost_list)
            day_cost_list = []
    print(all_info)
    if(month_info == 2 or month_info == 4 or month_info == 6 or month_info == 9 or month_info == 11):
        graph_day = [i for i in range(1,31)]
        cost_day = [0 for i in range(1,31)]
    else:
        graph_day = [i for i in range(1,32)]
        cost_day = [0 for i in range(1,32)]
    i = 0
    while(i != len(all_info) - 1):
        month_info_any = all_info[i][0]
        cost_day[month_info_any - 1] = cost_day[month_info_any - 1] + all_info[i][1]
        i = i + 1
    print(graph_day)
    print(cost_day)
    plt.plot(graph_day, cost_day)
    plt.savefig('figure.png')
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