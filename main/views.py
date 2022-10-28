from django.shortcuts import render
from django.http import HttpResponse
from .models import Controllers, OneWire, Rele
from .utils import getStatus


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
        print(row)
        currData.append(Rele(rele_contr=controllerId, rele_num=i, rele_satus=int(row)))
        i += 1
    channelX = Rele.objects.bulk_create(currData)

    return HttpResponse(laurent)
