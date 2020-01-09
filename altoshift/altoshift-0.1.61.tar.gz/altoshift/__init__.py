import re
import os
import json
import time
from tqdm import tqdm
import requests
import altoshift
import pandas as pd
from altoshift.tools import Tools

helper = Tools()

ALTO_SYNC_PATH = '/api/mapping/sync'
ALTO_READ_PATH = '/api/mapping/read'
ALTO_UPSERT_CATEGORY_PATH = '/api/upsert/categories'
ALTO_UPSERT_PATH = '/api/upsert/products'
ALTO_DELETE_PATH = '/api/delete/products'
ALTO_SEARCH_PATH = '/v1/search'

class connect():
    args = {}
    conf = {
        'DEV': False,
        'host': 'https://search.altoshift.com',
        'xEngineId': '5e170781db2bc600759c0a1c',
        'xUserId': '5e1589d81ef4c70058a6b8ad',
        'xToken': 'ca7effded7c27df4274d29e54053b9654df8069cad804bb4a4cceaad',
        'sToken': '5e1589e8db2bc600759c0a1b'
    }

    @classmethod
    def info(self):
        resp = json.dumps(self.conf, indent=2)
        print "=== Configuration ==="
        print resp
        return 
    
    def __init__(self, host='https://api.altoshift.com', xEngineId='', xUserId='',xToken='', sToken='', **kwargs):
        args = kwargs
        if not(args.get('DEV',False)):
            self.conf['host'] = host
            self.conf['xEngineId'] = args.get('engineId',xEngineId)
            self.conf['xUserId'] = args.get('userId',xUserId)
            self.conf['xToken'] = args.get('token',xToken)
            self.conf['sToken'] = args.get('sToken',sToken)
            
        self.headers = {
            'content-type': 'application/json',
            'Accept-Charset': 'UTF-8',
            'x-engine-id': self.conf['xEngineId'],
            'x-user-id': self.conf['xUserId'],
            'x-token': self.conf['xToken']
        }
        self.info()
    

    def requestHandle(self,resp):
        try:
            result =  {'status_code': resp.status_code,
            'response': resp.json() if resp.text else {}}
        except ValueError:
            result =  {'status_code': resp.status_code,
            'response': resp.text}
        return result

    def requestGet(self,**kwargs):
        args = kwargs
        url = args.get('url','')
        headers = args.get('headers','')
        body = args.get('body','')
        resp = requests.get(url,headers=headers)
        result = self.requestHandle(resp)
        return result

    def requestPost(self, **kwargs):
        args = kwargs
        url = args.get('url','')
        headers = args.get('headers','')
        data = args.get('data','')
        resp = requests.post(url,data=json.dumps(data),headers=headers)
        result = self.requestHandle(resp)
        return result

    def mappingSync(self,dt):
        headers = self.headers
        data = {"customFields": dt}
        url = self.conf['host']+ALTO_SYNC_PATH
        return self.requestPost(url=url,headers=headers,data=data)

    def altoReader(self,file):
        datas = helper.altoReader(file)
        return datas
            
    def altoUpsert(self,file):
        datas = self.altoReader(file)
        if(datas):
            resp = self.upsertData(datas)
        return "Finished"

    def upsertItems(self,dt):
        headers = self.headers

        data = {
            "items": dt
        }
        url = self.conf['host']+ALTO_UPSERT_PATH
        resp = self.requestPost(url=url,headers=headers,data=data)
        return resp
    
    def upsertCategories(self,dt):
        headers = self.headers

        data = {
            "categories": dt
        }
        url = self.conf['host']+ALTO_UPSERT_CATEGORY_PATH
        resp = self.requestPost(url=url,headers=headers,data=data)
        return resp

    def deleteItems(self,dt):
        headers = self.headers
        data = {
            "ids": dt
        }
        url = self.conf['host']+ALTO_DELETE_PATH
        return self.requestPost(url=url,headers=headers,data=data)
    
    def mappingRead(self):
        headers = self.headers
        data = {}
        url = self.conf['host']+ALTO_READ_PATH
        result = self.requestGet(url=url,headers=headers)
        return result
        
    def mappingHeader(self):
        resp = self.mappingRead()
        header = []
        for x in resp['response']['mapping']:
            header += [ x['name'] for x in resp['response']['mapping'][x]]
        result = header
        return result

    def getItems(self,query):
        url = result['host']+ALTO_SEARCH_PATH
        url+='?query=%s&token=%s' % (url, result['sToken'])
        return self.requestGet(url=url)
    
    def upsertData(self, dt, generateCategory=False, categoryLabel=None, categorySplit='|', excludeCategory=[], slicePer=500, delay=0.5, excludeAttribute=[]):
        reports = {'count':{
                        'success':0,
                        'fail':0,
                        'error':0
                    },
                    'logs':{
                        'failed':[]
                    }
                  }
        if(generateCategory):
            categories = helper.categoryGenerator(dt, categoryLabel=categoryLabel, categorySplit=categorySplit, excludeCategory=excludeCategory)
            print('=== Upserting Category ===')
            upCategories = list(categories.itervalues())
            upCategories = helper.dataSlicer(upCategories,slicePer)
            for ct in tqdm(upCategories):
                print(self.upsertCategories(ct))
                time.sleep(delay)
            dt = helper.categoryMap(dt, categories, categoryLabel=categoryLabel, categorySplit=categorySplit)
        print('Data attributes : %s' %dt[0].keys())
        dt = [dict((key,value) for key, value in d.iteritems() if key not in excludeAttribute) for d in dt]
        datas = helper.dataSlicer(dt,slicePer)
        print('=== Upserting Data === \n Total data\t: %s \n Slicer (%s)\t: %s (%s) \n Delay upsert\t: %s' % (len(dt),slicePer,len(datas),[len(x) for x in datas],delay))
        for data in tqdm(datas):
            try:
                resp = self.upsertItems(data).get('response',[])
                if(resp.get('success')):
                    resp = resp.get('response',[])
                    reports['count']['success'] += resp.get('inserted',0)
                    reports['count']['fail'] += len(resp.get('failed',[]))
                    reports['logs']['failed'] += (resp.get('failed',[]))
                    time.sleep(delay)
                else:
                    reports['count']['error'] += len(data)
                    reports['logs']['failed'].append(resp)
            except Exception as e:
                resp = e
                reports['logs']['failed'].append(resp)
        print('Upsert Status | Success : %s | Failed : %s | Error : %s' % (reports['count']['success'],reports['count']['fail'],reports['count']['error']))
        return reports

if(__name__ == "__main__"):
    print('Believe in Future.')