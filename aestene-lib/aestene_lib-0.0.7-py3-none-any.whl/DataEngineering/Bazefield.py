import datetime as dt
import json
import re
import requests
import pandas as pd
import numpy as np
import urllib3

from requests.auth import HTTPBasicAuth

from AesLib.DataEngineering import Azure

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def getDatetimeAsString(timeStamp: dt.datetime.timestamp, stringFormat="%Y_%m_%d_%H_%M_%S") -> str:
    timeStampAsDateTime = dt.datetime.fromtimestamp(timeStamp / 1000)
    return timeStampAsDateTime.strftime(stringFormat)

def reduceDataFrameSize(dataFrame) -> pd.DataFrame:
    dataFrame.loc[:, dataFrame.select_dtypes(include=np.float64).columns] \
        = dataFrame.select_dtypes(include=np.float64).astype(np.float32)
    return dataFrame

def getBazefieldAuthenticationFromKeyVault(keyVaultName: str) -> HTTPBasicAuth:
    apiKey = Azure.getSecretFromKeyVault(keyVaultName, secretName='bazefield-api-key')
    return HTTPBasicAuth(apiKey, '')

def getBazefieldHeaders() -> dict:
    headers = {'Content-Type': 'application/json;charset=UTF-8',
               'Accept': 'application/json, text/plain, */*'}
    return headers

def getFullTagListFromBazefield(keyVaultName: str):
    auth = getBazefieldAuthenticationFromKeyVault(keyVaultName)
    tagListUrl = Azure.getSecretFromKeyVault(keyVaultName, secretName='bazefield-tagid-url')
    tagList = requests.get(url=tagListUrl, verify=False, auth=auth)
    return json.loads(tagList.text)

def matchTaglistToRegularExpression(tagList: list, regularExpression: str) -> list:
    tagIds = [t["tagId"] for t in tagList
              if re.match(regularExpression, t["tagName"])]
    return tagIds

def getTransformedTagListFromBazefield(regExStrings: list, keyVaultName: str):
    tagList = getFullTagListFromBazefield(keyVaultName)

    tagIds = []

    for regEx in regExStrings:
        tagIds = tagIds + matchTaglistToRegularExpression(tagList=tagList,
                                                          regularExpression=regEx)

    tagListToDownload = {"tagIds": str(tagIds)[1:-1].replace(" ", "")}

    tagListToDownload['dateTimeFormat'] = "dd-MM-yyyy HH:mm:ss.fff"
    tagListToDownload["calenderUnit"] = "Minute"
    tagListToDownload["useAssetTitle"] = False
    tagListToDownload["useInterval"] = True
    return json.dumps(tagListToDownload)

def prepareDownload(fromTimeStamp: int,
                    keyVaultName: str,
                    aggregates: str,
                    interval: str,
                    regExStrings: list,
                    downloadFileResolution=1000*3600*24):

    fromTimeStampAsString = getDatetimeAsString(fromTimeStamp)
    endTimeStamp = fromTimeStamp + downloadFileResolution

    print("Downloading " + fromTimeStampAsString)

    url = Azure.getSecretFromKeyVault(keyVaultName, secretName='bazefield-data-export-url')
    auth = getBazefieldAuthenticationFromKeyVault(keyVaultName)
    headers = getBazefieldHeaders()
    proxy = {'https': Azure.getSecretFromKeyVault(keyVaultName, secretName='equinor-proxy')}
    data = getTransformedTagListFromBazefield(regExStrings, keyVaultName)

    res = requests.post(url=url.format(fromTimeStamp, endTimeStamp, interval, aggregates),
                        auth=auth,
                        headers=headers,
                        verify=False,
                        proxies=proxy,
                        data=data)

    filename = res.text
    nextTimeStamp = endTimeStamp

    return filename, nextTimeStamp, fromTimeStampAsString

def downloadFile(filename: str, fromTimeStampAsString: str, keyVaultName: str):
    csvName = fromTimeStampAsString + '.csv'
    filename = filename.replace(".txt", "")

    url = Azure.getSecretFromKeyVault(keyVaultName, secretName='bazefield-get-file-url')
    auth = getBazefieldAuthenticationFromKeyVault(keyVaultName)
    proxy = {'https': Azure.getSecretFromKeyVault(keyVaultName, secretName='equinor-proxy')}

    res = requests.get(url=url.format(filename),
                       auth=auth,
                       verify=False,
                       proxies=proxy)

    file = res.content.decode()

    destination = './Data/WithAggregates/'
    filePath = destination + csvName

    with open(filePath, 'w') as f:
        f.write(file)
        print("Finished.")
        print("Downloaded to "+ str(filePath))

    dataFrame = pd.read_csv(filePath, sep=';')
    dataFrame = reduceDataFrameSize(dataFrame)

    dataFrame.to_csv(filePath, sep=';')

    return True


def downloadDataFromBazefieldAsCSV(fromTimeStamp: dt.datetime, 
                                   toTimeStamp: dt.datetime, 
                                   aggregates: str, 
                                   interval: str,
                                   regExStrings: list,
                                   keyVaultName: str):
    fromTimeStampInt = int(fromTimeStamp.timestamp()) * 1000
    toTimeStampInt = int(toTimeStamp.timestamp())

    while True:
        try:
            filename, nextTimeStamp, fromTimeStampAsString = prepareDownload(fromTimeStampInt,
                                                                             keyVaultName,
                                                                             aggregates,
                                                                             interval,
                                                                             regExStrings)
            print('Downloading ' + fromTimeStampAsString)
            print(filename)
            _ = downloadFile(filename, fromTimeStampAsString, keyVaultName)
        except Exception as e:
            print(e)
            fromTimeStampInt = nextTimeStamp
            continue
        
        if dt.datetime.fromtimestamp(nextTimeStamp / 1000) \
           > dt.datetime.fromtimestamp(toTimeStampInt):
            return
        else:
            fromTimeStampInt = nextTimeStamp
