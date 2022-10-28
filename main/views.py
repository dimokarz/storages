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

    if len(laurent[1]) > 0:
        currData = []
        for key, val in laurent[1].items():
            currData.append(OneWire(onewire_contr=controllerId, onewire_name=key, onewire_value=val, onewire_channel='A'))
        channelA = OneWire.objects.bulk_create(currData)

    if len(laurent[2]) > 0:
        currData = []
        for key, val in laurent[1].items():
            currData.append(OneWire(onewire_contr=controllerId, onewire_name=key, onewire_value=val, onewire_channel='B'))
        channelB = OneWire.objects.bulk_create(currData)

    return HttpResponse(laurent)
