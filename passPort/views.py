import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from passPort.models import passPort


# Create your views here.
def hello(request):
    return HttpResponse("<p>hello world！</p>")
# @csrf_exempt
def GetAllPassPort(request):
    result = {"resCode": '200', "message": 'success', "data": []}
    passPortAll = passPort.objects.all()
    serial_data = serializers.serialize('python',passPortAll)
    data = []
    for i in serial_data:
        j = i['fields']
        j['id'] = i['pk']
        data.append(j)
    result['data'] = data
    return JsonResponse(result, headers={'Access-Control-Allow-Origin':'*'})

def AddPassPort(request):
    result = {"resCode": '200', "message": 'success', "data": []}
    data = request.GET.dict()
    passport = passPort.objects.create(**data)
    serial_data = serializers.serialize('python', [passport])
    serial_data = serial_data[0]
    id = serial_data['pk']
    serial_data = serial_data['fields']
    serial_data['id'] = id
    result['data'] = serial_data
    return JsonResponse(result)

def UpdatePassPort(request):
    result = {"resCode": '200', "message": 'success', "data": []}
    data = request.GET.dict()
    id = data['id']
    passport = passPort.objects.filter(id=id).update(**data)
    serial_data = serializers.serialize('python', [passport])
    serial_data = serial_data[0]
    id = serial_data['pk']
    serial_data = serial_data['fields']
    serial_data['id'] = id
    result['data'] = serial_data
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
    serial_data = serializers.serialize('python', data)
    data = []
    for i in serial_data:
        j = i['fields']
        j['id'] = i['pk']
        data.append(j)
    result['data'] = data
    return JsonResponse(result)


