from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render

from passPort.models import passPort


# Create your views here.
def hello(request):
    return HttpResponse("<p>hello world！</p>")

def GetAllPassPort(request):
    result = {"resCode": '200', "message": 'success', "data": []}
    passPortAll = passPort.objects.all()
    result['data'] = serializers.serialize('python',passPortAll)
    return JsonResponse(result)

def AddPassPort(request):
    result = {"resCode": '200', "message": 'success', "data": []}
    data = request.GET.dict()
    passport = passPort.objects.create(**data)
    result['data'] = serializers.serialize('python',passport)
    return JsonResponse(result)

def UpdatePassPort(request):
    result = {"resCode": '200', "message": 'success', "data": []}
    data = request.GET.dict()
    id = data['id']
    passport = passPort.objects.filter(id=id).update(**data)
    result['data'] = serializers.serialize('python', passport)
    return JsonResponse(result)

def DeletePassPort(request):
    id = request.GET.get('id')
    passport = passPort.objects.filter(id=id).delete()
    return HttpResponse(status=200)

def Search(request):
    name = request.GET.get('name','')
    number = request.GET.get('number','')
    result = {"resCode": '200', "message": 'success', "data": []}
    if name is None and number is None:
        return HttpResponseBadRequest()
    data = None
    print(name)
    if name is not None:
        print(name)
        data = passPort.objects.filter(name=name)
    else:
        data = passPort.objects.filter(number=number)
    if data is None:
        return HttpResponseBadRequest()
    result['data'] = serializers.serialize('python', data)
    return JsonResponse(result)


