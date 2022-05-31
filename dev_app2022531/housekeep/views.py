from django.shortcuts import render, redirect
from .models import Session
from .forms import SpendingBilling

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