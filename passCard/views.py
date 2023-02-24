from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("<p>hello world！</p>")

def GetAllPassCard(request):
    return