# -*- coding:utf-8 -*-
import json
import urllib

import oss2
import requests

from MyOSSException import MyOSSException


class MyOSS:
    tokenServer = "https://fstoken.ipaylinks.com"
    duration = 3600
    accessKey = ""
    rawToken = {}

    def __init__(self, accessKey):
        self.accessKey = accessKey

    '''
        获取OSSClient,需要先初始化stsToken
    '''
    def getOSSClient(self):
        if not self.rawToken:
            raise MyOSSException('Need to call init first!')
        # 字典
        stsToken = self.rawToken['stsToken']
        # 字典
        credentials = stsToken['Credentials']
        accessKeyId = credentials['AccessKeyId']
        AccessKeySecret = credentials['AccessKeySecret']
        securityToken = credentials['SecurityToken']
        endpoint = self.rawToken['endpoint']
        bucketName = self.rawToken['bucket']
        # 使用临时token中的认证信息初始化StsAuth实例
        auth = oss2.StsAuth(accessKeyId, AccessKeySecret, securityToken)

        # 使用StsAuth实例初始化存储空间
        bucket = oss2.Bucket(auth, endpoint, bucketName)
        return bucket

    '''
    此处duration没有使用，默认60秒
    '''
    def init(self, subPath, duration):
        params = urllib.parse.urlencode({'cmd': 'getToken', 'subPath': subPath, 'duration': duration, 'accessKey': self.accessKey})
        # headers = {'Content-type': 'application/x-www-form-urlencoded;charset=utf-8', 'Accept': 'text/plain'}
        self.rawToken = self.postToServer(params)
        return self.rawToken

    '''
    请求FileServerToken获取签名URL
    '''
    def signURL(self, originalURL, duration):
        params = urllib.parse.urlencode({'cmd': 'signURL', 'url': originalURL, 'duration': duration, 'accessKey': self.accessKey})
        token = self.postToServer(params)
        return token['url']

    '''
    请求FileServerToken获取sts临时授权
    '''
    def postToServer(self, params):
        # headers = {'Content-type': 'application/x-www-form-urlencoded;charset=utf-8', 'Accept': 'text/plain'}
        headers = {'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'}
        response = requests.post(self.tokenServer, params, headers=headers).content.decode("utf-8")
        # 将json字符串转换成字典
        # response_dict = ast.literal_eval(response)
        response_dict = json.loads(response)
        if response_dict['errorCode'] != 0:
            print("postToServer error, errorCode=" + response_dict['errorCode'] + ",msg=" + response_dict['errorMsg'])
            raise MyOSSException("postToServer error, errorCode=" + response_dict['errorCode'])
        return response_dict['data']

# if __name__ == '__main__':
    # myOss = MyOSS('debug_mps_123456')
    # automationTest = myOss.init('automationTest', 3600)
