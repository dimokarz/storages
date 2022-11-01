import datetime
import time
import requests


### Данные датчиков
def getStatus(address, password):
    url = f'http://{address}/json_sensor.cgi?psw={password}'
    lineColors = ['#FF0000', '#FFA500', '#FFFF00', '#008000', '#0000FF', '#000080',
                  '#808080', '#800000', '#00FFFF', '#2F4F4F']
    try:
        request = requests.get(url, timeout=2)
        rele = request.json()['rele']
        channelA = {}
        channelB = {}
        a = 0
        b = 0
        for row in request.json()['owi_temp']:
            if row[0] == 'A':
                channelA[row[2]] = [row[3], lineColors[a]]
                a += 1
            elif row[0] == 'B':
                channelB[row[2]] = [row[3], lineColors[b]]
                b += 1
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
