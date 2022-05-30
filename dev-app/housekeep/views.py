from django.shortcuts import render
from .models import Session

# Create your views here.
def main(request):
    session = Session.objects.all()
    context = {
        'test': 'test',
        'nums' : session,
    }
    return render(request, 'housekeep/housekeep.html', context)

def logout(request):
    Session.objects.all().delete()
    return render(request, 'housekeep/logout.html')