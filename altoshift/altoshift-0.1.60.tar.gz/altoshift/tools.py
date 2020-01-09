import os
import re
import json
import pandas as pd
from pandas.io.json import json_normalize

class Tools(object):
    def __init__(self):
        super(Tools, self).__init__()
        
    def writeToCsv(self,fname,df,sep='\t'):
        df.to_csv(fname, sep=sep, encoding='utf-8')
    
    def writeToJson(self,fname,df):
        df.to_json(fname, orient='records', lines=False)

    def readMysqltoJson(self,query,con):
        df = pd.read_sql(query, con=con)
        result = df.to_json(orient='records', lines=False)
        result = json.loads(result.decode('latin-1'))
        return result

    def readXlsToJson(self,file):
        df = pd.read_excel(file)
        result = df.to_json(orient='records', lines=False)
        result = json.loads(result.decode('latin-1'))
        return result

    def readCsvToJson(self,file,xdelimiter='\t'):
        df = pd.read_csv(file,delimiter=xdelimiter)
        result = df.to_json(orient='records', lines=False)
        result = json.loads(result.decode('latin-1'))
        return result

    def cleanHTMLforJson(self,dt,xfilter=[]):
        df = dt.filter(xfilter) if xfilter else dt
        df = json_normalize(dt)
        for cfilter in xfilter:
            df[cfilter]=re.sub(r'<.+?>','',str(df[cfilter]))
        return df

    def filterJson(self,dt,xfilter=None):
        df = pd.DataFrame(dt)
        df = df.filter(xfilter) if xfilter else df
        result = df.to_json(orient='records', lines=False)
        result = json.loads(result.decode('latin-1'))
        return result

    def dataSlicer(self, source, every=500):
        step = (len(source)/every+1)
        return [source[i::step] for i in range(step)]

    def altoReader(self,file):
        if(os.path.isfile(file) == False):
            print('File not found')
            return False
        
        if(file.lower().endswith('.csv')):
            datas = self.readCsvToJson(file)
        elif(file.lower().endswith('.tsv')):
            datas = self.readCsvToJson(file,'\t')
        elif(file.lower().endswith('.xlsx')):
            datas = self.readXlsToJson(file)
        else:
            print('not supported file')
        return datas

    def altoOptimizer(self,fname,df2):
        df1 = pd.DataFrame()
        if(os.path.isfile(fname)):
            df1 = pd.DataFrame(self.readCsvToJson(fname))
        if not(df1.empty):
            merged = df1.merge(df2, indicator=True, how='outer')
            data = merged[merged['_merge'] == 'right_only']
        else:
            data = df2
        self.writeToCsv(fname,df2)
        result = data.to_json(orient='records', lines=False)
        result = json.loads(result.decode('latin-1'))
        return result
    
    def categoryGenerator(self, dt, categoryLabel=None, categorySplit='|', excludeCategory=[]):
        categoryIdx = 0
        categories = {}
        for row in dt:
            if(categoryLabel == None):
                ctRow = row
            elif(categoryLabel not in row):
                print('Please specify the correct category label | ex : categoryGenerator(dt, categoryLabel="category"')
                break
            else:
                ctRow = row[categoryLabel]
    #           Validate row
            if(type(ctRow) in [str,unicode]):
                ct = [str(c) for c in ctRow.split(categorySplit)]
            elif(type(ctRow) == dict):
                print('%s |Please specify the category label | ex : categoryGenerator(dt, categoryLabel="category")' % (type(row)))
                break
            else:
                ct = []
            for idx,c in enumerate(ct):
                if (c in excludeCategory):
                    continue
                elif(c not in categories):
                    if(idx != 0):
                        parentId = str(categories[ct[idx-1]]['catId'])
                    else:
                        parentId = '0'
                    categories[c] = {'name':c, 'count':1, 'parentCatId':str(parentId), 'catId':str(categoryIdx), 'description':''}
                    categoryIdx+=1
                else:
                    categories[c]['count'] += 1
        return categories

    def categoryMap(self, dt, categories, categoryLabel=None, categorySplit='|'):
        for i,row in enumerate(dt): 
            if(categoryLabel == None):
                ctRow = row
            else:
                ctRow = row[categoryLabel]
            ctRow = ctRow.split(categorySplit)
            ctids = [categories[c]['catId'] for c in ctRow]
            dt[i]['categoryIds'] = ctids
        return dt
    
if(__name__ == "__main__"):
    print('Believe in Future.')
