import json

import requests
from ipware.ip import get_ip
from requests import Response
from xmltodict import parse


# Определение города по ip
def get_city(request):
    city = request.session.get('city')
    region = request.session.get('region')
    if city or region:
        return {'city': city, 'region': region}
    else:
        # Стучим в ipgeobase
        try:
            response = requests.get('http://ipgeobase.ru:7020/geo?ip=' + str(get_ip(request)), timeout=5)
        except Exception as e:
            response = Response()
            response.status_code = 404
        if response.status_code == requests.codes.ok:
            response.encoding = 'cp1251'
            text = response.text.encode('utf-8').replace('windows-1251', 'utf-8')
            ip = parse(text)
            try:
                city = ip['ip-answer']['ip']['city']
                region = ip['ip-answer']['ip']['region']
            except:
                city = None
                region = None
            if city:
                request.session['city'] = city
                request.session['region'] = region
                request.session.modified = True
            return {'city': city, 'region': region}
        else:
            # Пробуем стучаться в sypexgeo
            try:
                response = requests.get('http://api.sypexgeo.net/json/' + str(get_ip(request)), timeout=5)
            except Exception as e:
                response = Response()
                response.status_code = 404
            if response.status_code == requests.codes.ok:
                text = response.text
                ip = json.loads(text)
                try:
                    city = ip['city']['name_ru']
                    region = ip['region']['name_ru']
                except:
                    city = None
                    region = None
                if city:
                    request.session['city'] = city
                    request.session['region'] = region
                    request.session.modified = True
                return {'city': city, 'region': region}
            else:
                return {'city': None, 'region': None}
