from datetime import datetime, timedelta
from pymongo import MongoClient
from bson.objectid import ObjectId

class Datalake:
    def __init__(self, usr, pwd, channel):

        self.client = MongoClient('mongodb://datalake.pravah.io:27017/datalake', username=usr, password=pwd)
        
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
    def get(self, query={}, start='', end='', past_hours=0, past_minutes=1, past_seconds=0):
        if isinstance(query, ObjectId):
            return self.collection.find_one({
                '_id': query
            })
        elif isinstance(query, dict):
            self.get_query_for_time_bound(query, start, end, past_hours, past_minutes, past_seconds)
            print(query)
            return self.collection.find(query)

    def aggregate(self, group_by='', push={}, pipeline=[], match={}, start='', end='', past_hours=0, past_minutes=1, past_seconds=0):
        
        final_agg = []

        """ { "$group": {
                "_id": '$' + group_by,
                "all": { "$push": push } 
            }} """

        """ for k, v in push.items():
                group[k] = {
                    "$push": '$' + v
                } """

        self.get_query_for_time_bound(match, start, end, past_hours, past_minutes, past_seconds)
        if bool(match):
            final_agg.append({
                "$match": match
            })
        final_agg = final_agg + pipeline

        return self.collection.aggregate(final_agg)

    def get_query_for_time_bound(self, query, start, end, past_hours, past_minutes, past_seconds):
        if start != '' and end != '':
            start_date = ObjectId.from_datetime(datetime.strptime(start, '%Y/%m/%d %H:%M:%S').astimezone())
            end_date = ObjectId.from_datetime(datetime.strptime(end, '%Y/%m/%d %H:%M:%S').astimezone())
            query['_id'] = {
                '$gte': start_date,
                '$lte': end_date
            }
        elif start != '':
            print('this')
            start_date = ObjectId.from_datetime(datetime.strptime(start, '%Y/%m/%d %H:%M:%S').astimezone())
            query['_id'] = {
                '$gte': start_date
            }
        elif end != '':
            end_date = ObjectId.from_datetime(datetime.strptime(end, '%Y/%m/%d %H:%M:%S').astimezone())
            query['_id'] = {
                '$lte': end_date
            }
        else:
            date = datetime.utcnow() - timedelta(hours=past_hours, minutes=past_minutes, seconds=past_seconds) 
            start_date = ObjectId.from_datetime(date)
            query['_id'] = {
                '$gte': start_date
            }
        return query

