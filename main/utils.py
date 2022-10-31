import datetime
import time
import requests


### Данные датчиков
def getStatus(address, password):
    url = f'http://{address}/json_sensor.cgi?psw={password}'
    try:
        request = requests.get(url, timeout=2)
        rele = request.json()['rele']
        channelA = {}
        channelB = {}
        for row in request.json()['owi_temp']:
            if row[0] == 'A':
                channelA[row[2]] = row[3]
            elif row[0] == 'B':
                channelB[row[2]] = row[3]
        return [rele, channelA, channelB]
    except:
        return 'Fail'


def chartPoints(owTemp, channel):
    currDate = ''
    firstRun = True
    pointsCurr = {}
    labels = []
    pointsLst = []
    for tmp in owTemp:
        if tmp['onewire_channel'] == channel:
            if firstRun:
                labels.append(tmp['onewire_name'])
            chkDate = tmp['onewire_time'].strftime('%Y-%m-%d %H:%M')
            if chkDate != currDate and currDate != '':
                pointsLst.append(pointsCurr)
                firstRun = False
                pointsCurr = {}
            if chkDate != currDate:
                pointsCurr['Date'] = chkDate
                currDate = chkDate
            pointsCurr[tmp['onewire_name']] = tmp['onewire_value']

    return [labels, pointsLst]
