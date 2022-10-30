import requests


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
