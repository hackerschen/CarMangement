import os


from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest

from CardManagement.settings import BASE_DIR
from passPort.models import passPort
from django.core.paginator import Paginator
import pandas as pd
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

def GetAPassPort(request):
    result = {"resCode": '200', "message": 'success', "data": []}
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)
    passPortAll = passPort.objects.all()
    paginator = Paginator(passPortAll, limit)
    page_data = paginator.get_page(page)
    serial_data = serializers.serialize('python',page_data)
    data = []
    for i in serial_data:
        j = i['fields']
        j['id'] = i['pk']
        data.append(j)
    result['data'] = data
    return JsonResponse(result, headers={'Access-Control-Allow-Origin':'*'})

def FileAdd(request):
    result = {"resCode": '200', "message": 'success', "data": []}
    received_file = request.FILES.get("upload_file")
    fileName = os.path.join(BASE_DIR, 'temp', received_file)
    saveFile(received_file, fileName)
    total_names = ['number','name','sex','native_place','company_name','save_number','valid_date','brith_date','get_date','out_date','last_date','state']
    df = pd.read_csv(fileName, names=total_names)
    datas = df.to_dict(orient='records')
    for data in datas:
        passPort.objects.create(**data)
    return JsonResponse(result, headers={'Access-Control-Allow-Origin':'*'})

def saveFile(recvived_file, fileName):
    with open(fileName, 'wb') as f:
        f.write(recvived_file.read())

def AddPassPort(request):
    result = {"resCode": '200', "message": 'success', "data": []}
    data = request.GET.dict()
    print('add-data', data)
    passport = passPort.objects.create(**data)
    # serial_data = serializers.serialize('python', [passport])
    # serial_data = serial_data[0]
    # id = serial_data['pk']
    # serial_data = serial_data['fields']
    # serial_data['id'] = id
    # result['data'] = serial_data
    return JsonResponse(result)

def UpdatePassPort(request):
    result = {"resCode": '200', "message": 'success', "data": []}
    data = request.GET.dict()
    # print(request.GET)
    # return HttpResponse(status=200)
    id = data['id']
    passport = passPort.objects.filter(id=id).update(**data)
    # serial_data = serializers.serialize('python', [passport])
    # serial_data = serial_data[0]
    # id = serial_data['pk']
    # serial_data = serial_data['fields']
    # serial_data['id'] = id
    # result['data'] = serial_data
    return JsonResponse(result)

def DeletePassPort(request):
    result = {"resCode": '200'}
    id = request.GET.get('id')
    passport = passPort.objects.filter(id=id).delete()
    return JsonResponse(result)

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


