import datetime

from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import date
from .models import Controllers, OneWire, Rele
from .utils import getStatus, chartPoints


def listener(request):
    controllers = Controllers.objects.all().filter(id=request.GET.get('contr')[-1:]).values()
    title = controllers[0]['contr_name']
    address = controllers[0]['contr_addr']
    password = controllers[0]['contr_passwd']

    laurent = getStatus(address, password)

    controllerId = Controllers.objects.get(id=request.GET.get('contr')[-1:])

    def addData(num, channel):
        currData = []
        for key, val in laurent[num].items():
            currData.append(
                OneWire(onewire_contr=controllerId, onewire_name=key, onewire_value=val, onewire_channel=channel))
        channelX = OneWire.objects.bulk_create(currData)

    if len(laurent[1]) > 0:
        addData(1, 'A')
    if len(laurent[2]) > 0:
        addData(2, 'B')

    currData = []
    i = 1
    for row in laurent[0]:
        currData.append(Rele(rele_contr=controllerId, rele_num=i, rele_satus=int(row)))
        i += 1
    channelX = Rele.objects.bulk_create(currData)

    return HttpResponse(laurent)


def index(request):
    controllers = Controllers.objects.all().values()
    title = 'Выбор склада'
    return render(request, 'index.html', {'controllers': controllers, 'title': title})


def storage(request):
    controllerID = request.GET.get('contr')[8:]
    controller = Controllers.objects.all().filter(id=controllerID).values()
    address = controller[0]['contr_addr']
    password = controller[0]['contr_passwd']
    title = controller[0]['contr_name'] + ' - ' + address
    laurent = getStatus(address, password)
    if laurent != 'Fail':
        return render(request, 'storage.html', {'title': title, 'reles': laurent[0], 'address': address,
                                                'password': password, 'channelA': laurent[1], 'channelB': laurent[1]})
    else:
        return HttpResponse(f'Fail-{controller[0]["contr_name"]}')



def ownTemp(request):
    return render(request, 'owtemp.html')


def refreshData(request):
    address = request.GET.get('addr')
    password = request.GET.get('passwd')
    laurent = getStatus(address, password)
    return render(request, 'owtemp.html', {'reles': laurent[0], 'channelA': laurent[1], 'channelB': laurent[2]})


def keyPress(request):
    address = request.GET.get('addr')
    password = request.GET.get('passwd')
    rele = request.GET.get('rele')[6:]

    if request.GET.get('rele') != 'allOff':
        url = f'http://{address}/cmd.cgi?psw={password}&cmd=REL,{rele},2'
    else:
        url = f'http://{address}/cmd.cgi?psw={password}&cmd=REL,ALL,0000'

    try:
        reqStr = requests.get(url, timeout=2).status_code
    except:
        reqStr = 'Fail'

    return HttpResponse(reqStr)


def chart(request):
    controllerID = request.GET.get('contr')
    dateNow = datetime.datetime.now()
    datePrev = dateNow - datetime.timedelta(days=1)
    owTemp = OneWire.objects.filter(onewire_time__range=[datePrev, dateNow]).filter(onewire_contr=controllerID).values()
    chartPoints(owTemp)
    return HttpResponse(owTemp)
