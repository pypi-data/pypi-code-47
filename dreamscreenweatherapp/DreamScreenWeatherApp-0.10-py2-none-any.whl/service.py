import os
import socket
import sys
import time
import json
import re
import requests
from flask import Flask, render_template, request, redirect, url_for, abort, session
from subprocess import call
from bs4 import BeautifulSoup
from datetime import datetime
import logging

logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)s:%(message)s', level=logging.DEBUG)
logging.info('DreamScreen Weather App service startup')

_ROOT = os.path.abspath(os.path.dirname(__file__))

def get_data(path):
    return os.path.join(_ROOT, path)

logging.debug(_ROOT)
# global section
app = Flask(__name__, instance_relative_config=False)
app.debug=True
app.config.from_pyfile('instance/weatherservice-config.py')
logging.debug(app.config)
#app.config.from_envvar('WEATHERSERVICE-CONFIG', silent=True)
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

log_dir='/var/log/dreamscreen/'
stationId='KNYSTATE9'
stationId='KNYNEWYO1249'

# map of icons to weather string
with open(get_data('etc/weather_map.json'), 'r') as map_data:
    icon = json.load(map_data)
    logging.debug(icon)
 
# global weather data response holder 
wdata = {}

def getIconKey():
    writeLog("Getting icon key")
    source_url = 'https://api.weather.com/v3/wx/forecast/daily/5day?postalKey=10308:US&units=e&language=en-US&format=json&apiKey=2008eda92fe1478c88eda92fe1378ca1'
    r = requests.get(source_url)
    data = r.json()
    currentWeather = data['daypart'][0]['wxPhraseLong'][0]  # returns a String, offset in daypart
    if currentWeather is None:
       currentWeather = data['daypart'][0]['wxPhraseLong'][1]  # returns a String, offset in daypart

    iconKey = 10  #unknown
    if currentWeather in icon:
       iconKey = icon[ currentWeather]
       writeLog('mapped %s to icon #: %d' % (currentWeather,iconKey) )
    else:
       writeLog('** DID NOT MAP %s to icon' % (currentWeather) )
    return iconKey


# url end-point handlers
@app.route('/getLiveWeatherRSS.aspx', methods=['POST','GET'])
def api_getLiveWeatherRSS():
#    now=datetime.now().strftime("%m/%d/%y %H:%M:%S %p")
#    now=datetime.now().strftime("%h %-d, %Y %-I:%M%p")
    now=datetime.now().strftime("%-m/%-d/%Y %-I:%M%p")

    writeLog("Getting Live Weather Data, current conditions.")
    mode='live'
    source_url = 'https://api.weather.com/v2/pws/observations/current?stationId=' + stationId + '&format=json&units=e&apiKey=2008eda92fe1478c88eda92fe1378ca1'
    r = requests.get(source_url)
    data = r.json()
    writeLog(data)
    obs=data['observations'][0]['imperial']
    loc=data['observations'][0]
    writeLog(loc)
    iconLive = getIconKey()
    return render_template('getLiveWeatherApi.html', obs = obs, iconLive = iconLive,  weburl = source_url, loc = loc, now = now)

# forecast is called After liveWeather 
@app.route('/getForecastRSS.aspx', methods=['POST','GET'])
def getForecastRSS():
    logging.info('Getting Forecast weather data via API')
    writeLog('Getting Forecast weather data via API')
    find_key = 'forecast'
    source_url = 'https://api.weather.com/v3/wx/forecast/daily/5day?postalKey=10308:US&units=e&language=en-US&format=json&apiKey=2008eda92fe1478c88eda92fe1378ca1'
    r = requests.get(source_url)
    data = r.json()
    writeLog(data)
    forecasts=[]
    mode='forecast'

    loc={ 'city': 'Staten Island', 'state': 'NY', 'zip': '10308'}   #data['response']['features']

    for i in range(0, 5):
        fc = {}
        fc['tempMax'] = str(data['temperatureMax'][i])
 	fc['tempMin'] = str(data['temperatureMin'][i])
	#fc['short_prediction'] = data['narrative'][i]
	fc['short_prediction'] = data['daypart'][0]['wxPhraseLong'][i*2]  # offset in daypart
	fc['weather_quickie'] = data['daypart'][0]['wxPhraseShort'][i*2]  # offset in daypart
        fc['date'] = {} 
	fc['date']['weekday'] = data['dayOfWeek'][i]
	fc['date']['weekday_short'] = data['dayOfWeek'][i]

        if fc['short_prediction'] is None:
           fc['short_prediction'] = data['daypart'][0]['wxPhraseLong'][i*2+1]  # returns a String, offset in daypart

	fc['icon'] = 10  #unknown
	if fc['short_prediction'] in icon:
	   fc['icon'] = icon[ fc['short_prediction'] ]
	   writeLog('mapped %s to icon #: %d' % (fc['short_prediction'],fc['icon']) )
	else:
	   writeLog('** DID NOT MAP %s to icon' % (fc['short_prediction']) )
        
        icon.setdefault(fc['short_prediction'],  10)
        forecasts.append(fc)    
     
    writeLog('Forecast data block:')
    writeLog(forecasts)

    now=datetime.now().strftime("%m/%d/%y %H:%M:%S %p")
    return render_template('getForecastApi.html', loc = loc, forecasts = forecasts, icon = icon, now = now)

@app.route('/getLocationsXML.aspx', methods=['POST','GET'])
def getLocationsXML():
    mode='locations'
    key = request.args.get('SearchString')
    obj = { 'primary_city' : app.config['CITY'], 'state' : app.config['STATE'], 'country': app.config['COUNTRY'], 'zip': app.config['ZIPCODE'] }
    writeLog(key)
    return render_template('getLocationsXML.html', loc = obj)

@app.route('/verify', methods=['POST','GET'])
def verify():
    global wdata
    logging.info('verifying setup')
    mode='verify'
    logging.info(app.config['QUERY_URL'])
    wdata = getWeatherData(app.config['QUERY_URL'])
    writeLog(wdata)
    loc=wdata['response']['location']
    obs=wdata['current_observation']
    date=obs['date']
    writeLog(mode)
    return render_template('verify.html', obs = obs, date = date, loc = loc)

def writeRequestParams(mode):
    #log_dir = app.instance_path
    with open(log_dir + '' + mode + "." + session['id'] + '.params','w') as f:
        for p in request.args:
            f.write('%s = %s\n' % (p, request.args.get(p))) 

def writeLog(mode):
    #log_dir = app.instance_path
    now = time.strftime("%Y-%m-%d-%H:%M:%S")
    with open(log_dir + 'DreamScreenWeatherApp.log', 'a') as f:
        f.write('%s %s\n' % (now,  mode))

if __name__ == '__main__':
    if socket.gethostname() == 'ubuntu':
        app.run(host='0.0.0.0',  port=8080)
    else:
        app.run(host='0.0.0.0', port=8880)

