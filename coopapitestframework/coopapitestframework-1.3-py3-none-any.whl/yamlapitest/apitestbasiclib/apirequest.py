# coding:utf-8

import ast

# import atApiBasicLibrary.log as logger
import requests

def getPostInterfaceResponse(url,reqbody,headers):
    '''
    【功能】根据接口uri、请求body、请求headers请求post接口
    【参数】url:被请求的接口全路径
            reqbody:请求参数，字典类型
            headers:请求头参数，字典类型
    【返回】包含：请求响应码status_code,响应头信息headers,响应体body
    '''
    # logger.info("getInterfaceResponse.reqbody=%s" % reqbody,html=True,also_console=True)
    try:
        resp = requests.post(url,json=reqbody,headers=headers)
        respdict = {}
        respdict['status_code'] = resp.status_code
        respdict['headers'] = resp.headers
        respdict['body'] = resp.text
        return respdict
    except requests.exceptions.RequestException as e:
        # logger.error("getInterfaceResponse异常：%s" % e)
        raise AssertionError('getInterfaceResponse异常:%s' % e)

def http_post_response_body(url,reqbody,headers):
    '''
    【功能】根据接口uri、请求body、请求headers请求post接口
    【参数】url:被请求的接口全路径
            reqbody:请求参数，字典类型
            headers:请求头参数，字典类型
    【返回】响应体body
    '''
    # logger.info("url="+url,html=True,also_console=True)
    # logger.info("getInterfaceResponse.reqbody=%s" % reqbody,html=True,also_console=True)
    try:
        if reqbody is {}:
            resp = requests.post(url,headers=headers)
        else:
            resp = requests.post(url,json=reqbody,headers=headers)

        return resp
    except requests.exceptions.RequestException as e:
        # logger.error("getInterfaceResponse异常：%s" % e)
        return None
        raise AssertionError('getInterfaceResponse异常:%s' % e)

def http_put_response_body(url, headers=None, json=None):
    # logger.info("url=" + url, html=True, also_console=True)
    if url is None:
        # logger.error("url参数是None!",False)
        raise AssertionError("url参数是None")
    try:
        if headers is None:
            headers = {}
        headers.update({'Content-Type': 'application/json;charset=UTF-8'})
        if json is None:
            response = requests.put(url, headers=headers)
        else:
            # body = json.dumps(json)
            response = requests.put(url,headers=headers, json=json)
        return response.text
    except requests.exceptions.RequestException as e:
        # logger.error('发送请求失败，原因：%s' % e)
        raise AssertionError('发送请求失败，原因：%s' % e)

def http_delete_response_body(url,params=None,headers=None):
    if url is None:
        # logger.error("uri参数是None!",False)
        raise AssertionError("uri参数是None")
    try:
        response = requests.delete(url, headers=headers, params=params)
        return response.text
    except requests.exceptions.RequestException as e:
        # logger.error('发送请求失败，原因：%s' % e)
        raise AssertionError('发送请求失败，原因：%s' % e)

def http_get_response_body(url,params=None,headers=None,timeout=None):
    '''
       【功能】处理GET方式的接口请求
       【参数】url:接口地址
               params:请求参数，字典类型
               headers:请求头信息，字典类型
               timeout:请求超时时间
       【返回】响应Body,即response.text
       '''
    # logger.info('url='+url,html=True,also_console=True)
    if url is None:
        # logger.error("url参数是None!", False)
        raise AssertionError("url参数是None")
    try:
        response = requests.get(url, headers=headers, params=params, timeout=timeout)
        return response
    except requests.exceptions.RequestException as e:
        # logger.error('发送请求失败，原因：%s' % e)
        raise AssertionError('发送请求失败，原因：%s' % e)


def getxforcesaastoken(url,reqbody,headers):
    '''
    【功能】根据接口uri、请求body、请求headers请求登录接口
    【参数】url:被请求的接口全路径
            reqbody:请求参数，字典类型
            headers:请求头参数，字典类型
    【返回】token,string类型
    '''
    # logger.info("getInterfaceResponse.reqbody=%s" % reqbody,html=True,also_console=True)
    try:
        resp = requests.post(url,json=reqbody,headers=headers)
        xforcesaastoken = (eval(resp.text)).get('data').get('xforce-saas-token')
        return xforcesaastoken
    except requests.exceptions.RequestException as e:
        # logger.error("getInterfaceResponse异常：%s" % e)
        raise AssertionError('getInterfaceResponse异常:%s' % e)

def gettoken(url,reqbody,headers):
    '''
    【功能】根据接口uri、请求body、请求headers请求登录接口
    【参数】url:被请求的接口全路径
            reqbody:请求参数，字典类型
            headers:请求头参数，字典类型
    【返回】token,string类型
    '''
    # logger.info("getInterfaceResponse.reqbody=%s" % reqbody,html=True,also_console=True)
    try:
        resp = requests.post(url,json=reqbody,headers=headers)
        # respheader = resp.headers['Set-Cookie']
        # token = re.search(r'xforce-saas-token=(.*)',respheader).group(0).split(';')[0].split('=')[1]
        token = (ast.literal_eval(resp.text))['token']
        return token
    except requests.exceptions.RequestException as e:
        # logger.error("getInterfaceResponse异常：%s" % e)
        raise AssertionError('getInterfaceResponse异常:%s' % e)
#
# if __name__=='__main__':
#     st = 'aaaid'
#     ste = st.replace("id","112233")
#     print(ste)