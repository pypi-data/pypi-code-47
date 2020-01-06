import requests
import json
import pandas as pd
from pytz import timezone

class WebData:
    baseUrl = ""
    token = ""
    verify = True
    loginInfo = {}

    def __init__(self, username, password, url = "https://webdata.sulfilogger.com/"):
        self.baseUrl = url
        self.loginInfo = {"username": username, "password": password}
    
    def login(self):
        if(self.token == ""):
            headers = {"Content-Type":"application/json"}
            response = requests.post(self.baseUrl + "api/v1/login", verify=self.verify, data=json.dumps(self.loginInfo), headers=headers)
            self.token = str(response.content, 'utf-8').strip('\"')
    
    def getAvailableSites(self):
        self.login()
        headers = {"Authorization":"Bearer " + self.token}
        nameList=[]
        response = {}
        response = requests.get(self.baseUrl + 'api/v1/Sites', verify=self.verify, headers=headers)
        jsonText=response.json()
        for i in range(len(jsonText)):
            nameList.append(jsonText[i]['name'])
        return nameList

    def getLastData(self,sid):
        self.login()
        headers = {"Authorization":"Bearer " + self.token}
        response = requests.get(self.baseUrl + "api/v1/Sites/" + sid + "/Measurements/latest?unit=mg/L&allowNegative=false", verify=self.verify, headers=headers)
        return response.json()

    def getDataFromPeriod(self, sid, timeStart, timeEnd, unit = "mg/L", interval = '1min'):
        self.login()
        try:
            headers = {"Authorization":"Bearer " + self.token}
            timeStart = timeStart.replace('+','%2B')
            timeEnd = timeEnd.replace('+','%2B')
            response = requests.get(self.baseUrl + "api/v1/Sites/" + sid + "/Measurements?unit=" + unit + "&interval=" + interval + "&from=" + timeStart + "&until=" + timeEnd, verify=self.verify, headers=headers)
            data = response.json()
        except:
            data = []

        if(data == []):
            df = pd.DataFrame()
        else:
            # convert data object to an array with an array constructor
            # first pick the time from the first series
            temp = dict()
            temp['datetime'] = [data[0]['data'][index][0] for index in range(len(data[1]['data']))]

            # then append all series
            for serie in range(len(data)):
                temp[f"{data[serie]['name']} {data[serie]['unit']}"] = [data[serie]['data'][index][1] for index in range(len(data[serie]['data']))]

            # store values in a pandes dataframe and set datetime from the first series as index
            df=pd.DataFrame(temp)
            df['datetime']=pd.to_datetime(df['datetime'], unit='ms')
            df.datetime = df.datetime.dt.tz_localize('UTC').dt.tz_convert(timezone('Europe/Copenhagen'))
            df.set_index(df['datetime'],inplace=True)
            del df[df.keys()[0]]
        return df

if __name__ == '__main__':
    webData = WebData(username ="username", password= "password")
    webData.login()
    sites = webData.getAvailableSites()
    print(sites)
    data=webData.getDataFromPeriod(sites[0], '2019-09-25T00:00:00+02:00','2019-10-05T00:00:00+02:00', "mg/L", "1hr")
    print(data)