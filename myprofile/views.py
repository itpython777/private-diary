from django.shortcuts import render

def top(request):
    context = {
        'name': 'たろう',
    }
    return render(request, 'top.html', context)
# Create your views here.
