import requests
import json


def getAddressByIp(ip):
    if not isinstance(ip, str) and not isinstance(ip, unicode):
        raise ValueError('ipaddress must be str')
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query={}&resource_id=6006'.format(ip)
    try:
        html = requests.get(url=url, headers=headers).text
        data = json.loads(html)
    except Exception as e:
        print repr(e)
        return 'time error'
    return data


def getSampleAddressByIp(ip):
    data = getAddressByIp(ip)
    if isinstance(data, dict):
        try:
            data = data['data'][0]['location']
        except:
            return 'time error'
    return data


def getUserAgent():
    return 'Mozilla/5.0'


# if __name__ == '__main__':
#     print getSampleAddressByIp('140.143.11.163')
