from django.shortcuts import render

# Create your views here.
def main(request):
    context = {
        'test': 'test',
    }
    return render(request, 'housekeep/housekeep.html', context)