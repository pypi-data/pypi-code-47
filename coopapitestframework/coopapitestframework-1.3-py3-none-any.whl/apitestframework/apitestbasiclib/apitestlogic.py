# coding:utf-8

import json
import logging
from apitestbasiclib import apirequest
from apitestbasiclib.apibasic import replace_var_in_str, replace_var_in_dict
from apitestbasiclib.apirequest import gettoken
from apitestbasiclib.dbutils import excute_sqls, query_result_one, query_rows_count
from apitestbasiclib.filetools import get_env_config
import requests

from apitestbasiclib.jsoncompare import json_comp


def apitest(requstinfo,envname):
    '''
    从配置文件读取登录信息和数据库信息
    通过gettoken()函数获取token
    '''
    log = logging.getLogger('apitest()运行日志')
    env_config = get_env_config('./config/env_config.yaml',envname)
    print('requestinfo=%s'% env_config)
    log.info('requestinfo=%s'% env_config)
    try:
        login_url = env_config['loginUrl'] + env_config['loginPath']
        login_request_body = env_config['loginBody']
        login_header = env_config['headers']
        token = gettoken(login_url,login_request_body,login_header)
        log.info('token=%s'% token)
        print('token=%s'% token)
    except requests.exceptions.RequestException as e:
        log.error("【异常】无法获取token，%s")
        raise AssertionError("无法获取token，%s" % e)

    #获取用例相关数据
    req_url = str(env_config['hostUrl'])+str(requstinfo['api'])
    headers = requstinfo['headers']
    database_setup_sqls = requstinfo['database_setup']['sqls']
    request_body = requstinfo['request_body']
    urlParameters = requstinfo['urlParameters']
    request_method = requstinfo['request_method']
    expected_code = requstinfo['assert']['resp_assert']['expected_code']
    expected_response = requstinfo['assert']['resp_assert']['expected_response']
    db_assert_sqls = requstinfo['assert']['db_assert']['sqls']
    db_assert_expected_rowcount = requstinfo['assert']['db_assert']['expected_rowcount']
    database_teardown_sqls = requstinfo['database_teardown']['sqls']

    '''
    如果字典requstinfo中的database_setup不为空
    则执行初始化语句
    '''
    dbinfo = env_config['dbconfig']
    dbconfig = {}
    dbconfig['host'] = dbinfo['host']
    dbconfig['user'] = dbinfo['user']
    dbconfig['password'] = dbinfo['password']
    dbconfig['db'] = dbinfo['db']
    dbconfig['charset'] = dbinfo['charset']
    if database_setup_sqls:
        try:
            for sql in requstinfo['database_setup']['sqls']:
                excute_sqls(sql,dbconfig)
        except Exception as e:
            log.error('【异常】初始化数据库失败')
            if database_teardown_sqls:
                for sql in database_teardown_sqls:
                    try:
                        excute_sqls(sql, dbconfig)
                    except Exception as e:
                        log.error('【异常】初始化数据库失败后数据库清理异常')
                        raise AssertionError('数据库清理异常')
            raise AssertionError('初始化数据库异常:%s' % e)

    # 将token放入用例请求header中
    headers[headers['token_name']] = token
    # 如果用例数据中mysql_query不为空，则执行其中的sql语句，并把查询的数据替换request_body中的相同名称的变量
    if requstinfo['mysql_query']['sqls']:
        if len(requstinfo['mysql_query']['sqls']) == len(requstinfo['mysql_query']['return_value']):
            query_values = []
            try:
                for sql in requstinfo['mysql_query']['sqls']:
                    ret = query_result_one(sql,dbconfig)
                    if ret:
                        query_values.append(ret)
            # 使用sql查询的值替换request_body中的变量
                if query_values:
                    request_body = json.dumps(request_body)
                    for val in query_values:
                        request_body = replace_var_in_dict(request_body, val)
                    log.info('request_body=%s' % request_body)
                    print('request_body=%s' % request_body)
            except Exception as e:
                log.error('【异常】执行mysql_query中sql语句异常')
                if database_teardown_sqls:
                    for sql in database_teardown_sqls:
                        try:
                            excute_sqls(sql, dbconfig)
                        except Exception as e:
                            log.error('【异常】执行mysql_query中sql语句异常后清理数据异常')
                            raise AssertionError('数据库清理异常')
                raise AssertionError('mysql_query查询数据库异常:%s'% e)
        else:
            if database_teardown_sqls:
                for sql in database_teardown_sqls:
                    try:
                        excute_sqls(sql, dbconfig)
                    except Exception as e:
                        log.error('【异常】return_value和sqls不匹配后清理数据异常')
                        raise AssertionError('数据库清理异常')
            raise AssertionError('return_value和sqls不匹配，请检查用例数据')
    log.info('request_body=%s' % request_body)
    print('request_body=%s' % request_body)

    #如果urlParameters中的sqls和urlPath不为空，则使用sqls查询的值替换urlPath中的变量，如果urlPath中没有变量则不替换，如果sqls为空，则不替换，此处用于DELETE、PUT、GET方法
    urlpath = ''
    if urlParameters:
        if urlParameters['sqls']:
            if urlParameters['urlPath']:
                log.info('处理路径参数')
                print('处理路径参数')
                url_vars = []
                try:
                    for sql in urlParameters['sqls']:
                        ret = query_result_one(sql,dbconfig)
                        if ret:
                            url_vars.append(ret)
                except:
                    log.error('【异常】执行路径参数中的sql异常')
                    if database_teardown_sqls:
                        for sql in database_teardown_sqls:
                            try:
                                excute_sqls(sql, dbconfig)
                            except Exception as e:
                                log.error('【异常】执行路径参数中的sql异常后，清理数据异常')
                                raise AssertionError('数据库清理异常')
                    raise AssertionError('urlParameter数据库查询异常')
                if url_vars:
                    urlpath = urlParameters['urlPath']
                    for val in url_vars:
                        urlpath = replace_var_in_str(urlpath,val)
                    log.info('urlPath=%s' % urlpath)
                    print('urlPath=%s' % urlpath)
    # 判断接口请求类型，GET  POST  INPUT DELETE 并发送请求
    resp = None
    if (request_body is not None) and (not isinstance(request_body,dict)):
        log.info('转换request_body为字典类型')
        print('转换request_body为字典类型')
        request_body = json.loads(request_body)
    if (headers is not None) and (not isinstance(headers,dict)):
        log.info('转换headers为字典类型')
        print('转换headers为字典类型')
        headers = json.loads(headers)
    if (req_url is not None) and (not isinstance(req_url,str)):
        log.info('转换req_url为字符串类型')
        print('转换req_url为字符串类型')
        req_url = str(req_url)
    if request_method == 'POST':
        resp = apirequest.http_post_response_body(url=req_url, reqbody=request_body, headers=headers)
    elif request_method == 'GET':
        req_url = req_url + urlpath
        resp = apirequest.http_get_response_body(url=req_url,headers=headers)
    elif request_method == 'PUT':
        req_url = req_url + urlpath
        resp = apirequest.http_put_response_body(url=req_url, json=request_body, headers=headers)
    elif request_method == 'DELETE':
        req_url = req_url + urlpath
        resp = apirequest.http_delete_response_body(url=req_url,headers=headers)
    log.info('resp=%s' % resp.text)
    print('resp=%s' % resp.text)
    resp_code = resp.status_code
    log.info('status-code=%s' % resp_code)
    print('status-code=%s' % resp_code)
    #断言
    #1、判断响应码是否符合预期
    if expected_code != resp_code:
        if database_teardown_sqls:
            for sql in database_teardown_sqls:
                try:
                    excute_sqls(sql, dbconfig)
                except Exception as e:
                    log.error('【异常】按响应码校验不通过')
                    raise AssertionError('数据库清理异常')
        raise AssertionError('接口请求响应码和预期不一致，expected_code=%s,resp_code=%%'% (expected_code,resp_code))
    #2、判断响应内容是否符合预期
    resp_assert_result = json_comp(resp.text,expected_response)
    log.info('resp_assert_result=%s'% resp_assert_result)
    print('resp_assert_result=%s'% resp_assert_result)
    if resp_assert_result != True:
        if database_teardown_sqls:
            for sql in database_teardown_sqls:
                try:
                    excute_sqls(sql, dbconfig)
                except Exception as e:
                    log.error('【异常】按响应内容校验不通过后清理数据异常')
                    raise AssertionError('数据库清理异常')
        log.error('【异常】按响应内容校验不通过')
        raise AssertionError('接口请求响应结果和预期不一致，act_response=%s,expected_response=%s'% (resp.text,expected_response))
    #3、判断数据库查询结果是否符合预期
    if db_assert_sqls:
        if db_assert_expected_rowcount:
            if len(db_assert_sqls) == len(db_assert_expected_rowcount):
                act_rowcounts = []
                for sql in db_assert_sqls:
                    act_rowcounts.append(query_rows_count(sql,dbconfig))
                if act_rowcounts:
                    for i in range(len(act_rowcounts)):
                        if act_rowcounts[i]!=db_assert_expected_rowcount[i]:
                            if database_teardown_sqls:
                                for sql in database_teardown_sqls:
                                    try:
                                        excute_sqls(sql, dbconfig)
                                    except Exception as e:
                                        log.error('【异常】按数据库校验不通过后清理数据异常')
                                        raise AssertionError('数据库清理异常')
                            log.error('【异常】按数据库校验不通过')
                            raise AssertionError('数据库校验不通过')
            else:
                if database_teardown_sqls:
                    for sql in database_teardown_sqls:
                        try:
                            excute_sqls(sql, dbconfig)
                        except Exception as e:
                            log.error('【异常】db_assert_sqls！=db_assert_expected_rowcount时清理数据异常')
                            raise AssertionError('数据库清理异常')
                log.error('【异常】db_assert_sqls！=db_assert_expected_rowcount')
                raise AssertionError('db_assert_sqls！=db_assert_expected_rowcount，请检查用例数据')
    #数据清理
    if database_teardown_sqls:
        for sql in database_teardown_sqls:
            try:
                excute_sqls(sql,dbconfig)
            except Exception as e:
                log.error('【异常】清理数据异常')
                raise AssertionError('数据库清理异常')