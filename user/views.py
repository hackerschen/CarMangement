from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render


# Create your views here.


def uregist(request):
    if request.method == 'GET':
        # print('get')
        return HttpResponseBadRequest()
    if request.method == 'POST':
        print('post')
        name = request.POST.get('username')
        password = request.POST.get('password')
        # print('name, password', name, password)
        if name is None:
            return HttpResponseBadRequest()
        User.objects.create_user(username=name, password=password)
        return HttpResponse(status=200)
    return HttpResponseBadRequest()


def ulogin(request):
    if request.method == 'GET':
        return HttpResponseBadRequest()
    if request.method == 'POST':
        print('post')
        name = request.POST.get('username')
        password = request.POST.get('password')
        # 验证用户名和密码，通过的话，返回User对象
        print('name, password', name, password)
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


