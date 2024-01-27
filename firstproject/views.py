from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    contex={
        'title': 'this is title',
        'description':'this is description'
    }
    return render(request,'index.html', contex)