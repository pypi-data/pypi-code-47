from datetime import datetime, timedelta
from pymongo import MongoClient
from bson.objectid import ObjectId

class Datalake:
    def __init__(self, usr, pwd, channel):

        self.client = MongoClient('mongodb://13.232.47.177:27017/datalake', username=usr, password=pwd)
        
        channel = channel.replace('/', '').lower()
        print('Working on collection: ' + channel)
        self.collection = self.client.datalake[channel]

    def insert(self, geospace, obj):
        data = {
            'geospace': geospace,
            'item': obj
        }
        return self.collection.insert(data)
    
    # past: 60 mins
    # start: 2019/12/23 00:00:00
    def get(self, query, start='', end='', past=60):
        if isinstance(query, ObjectId):
            return self.collection.find_one({
                '_id': query
            })
        elif isinstance(query, dict):
            if start != '' and end != '':
                start_date = ObjectId.from_datetime(datetime.strptime(start, '%Y/%m/%d %H:%M:%S').astimezone())
                end_date = ObjectId.from_datetime(datetime.strptime(end, '%Y/%m/%d %H:%M:%S').astimezone())
                query['_id'] = {
                    '$gte': start_date,
                    '$lte': end_date
                }
                return self.collection.find(query)
            elif start != '':
                print('this')
                start_date = ObjectId.from_datetime(datetime.strptime(start, '%Y/%m/%d %H:%M:%S').astimezone())
                query['_id'] = {
                    '$gte': start_date
                }
                return self.collection.find(query)
            elif end != '':
                end_date = ObjectId.from_datetime(datetime.strptime(end, '%Y/%m/%d %H:%M:%S').astimezone())
                query['_id'] = {
                    '$lte': end_date
                }
                return self.collection.find(query)
            else:
                date = datetime.utcnow() - timedelta(minutes=past) 
                start_date = ObjectId.from_datetime(date)
                query['_id'] = {
                    '$gte': start_date
                }
                return self.collection.find(query)
        raise Exception

