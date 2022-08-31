from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('hello im your buyer')


def login(request):
    return render(request,'facebook.html')
