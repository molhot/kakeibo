from django.shortcuts import render, redirect
from .models import Session

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
    return render(request, 'housekeep/housekeep.html', context)

def logout(request, id):
    Session.objects.all().delete()
    return render(request, 'housekeep/logout.html')