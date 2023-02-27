from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render


# Create your views here.


def uregist(request):
    if request.method == 'GET':
        return HttpResponseBadRequest()
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        User.objects.create_user(username=name, password=password)
        return HttpResponse(status=200)
    return HttpResponseBadRequest()


def ulogin(request):
    if request.method == 'GET':
        return HttpResponseBadRequest()
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        # 验证用户名和密码，通过的话，返回User对象
        user = auth.authenticate(username=name, password=password)
        if user:
            auth.login(request, user)
            return HttpResponse(status=200)
        else:
            return HttpResponseBadRequest()
    return HttpResponseBadRequest()

def ulogout(request):
    if request.method == 'GET':
        auth.logout(request)
    return HttpResponse(status=200)


