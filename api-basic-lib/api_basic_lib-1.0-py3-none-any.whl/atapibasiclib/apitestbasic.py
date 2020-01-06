'''
此模块包含api测试的相关基础方法
'''
import json
import time

import pymysql

from atapibasiclib import apirequest, jsoncompare
import atApiBasicLibrary.log as logger

from atapibasiclib.mysqllib import excutemysql, queryfrommysql, queryonefrommysql

config = {'host':'phoenix-t.xforceplus.com','port':23315,'user':'root','password':'xplat','db':'bdt-config','charset':'utf8mb4'}
def getmysqlconnwithconfig():
    '''
    【功能】根据数据库配置获取mysql数据库连接对象
    【参数】无，使用本模块全局变量config
    【结果】返回connection
    '''
    try:
        logger.info("数据库连接" + str(config))
        if config.get("charset") is None:
            config['charset']='utf8'
        connection = pymysql.connect(**config)
        return connection
    except pymysql.OperationalError as e:
        logger.error('连接数据库失败，原因：%s' % e)
        raise AssertionError(e)
    except pymysql.MySQLError as e:
        logger.error('连接数据库失败，原因：%s' % e)
        raise AssertionError('连接数据库失败，原因：%s' % e)


def apitest(case_data):
    '''
    【功能】接口测试执行脚本
    【参数】case_data:测试用例数据
    【结果】预期结果和实际结果校验，如果相同，用例通过，否则用例执行失败
    '''
    #初始化数据
    if case_data.get('database_setup') is not None:
        sqlsetups = str(case_data.get('database_setup')).split(';')
        print('setupsqls=%s' % sqlsetups)
        for i in range(len(sqlsetups)):
            if sqlsetups[i] !='':
                excutemysql(getmysqlconnwithconfig(),sqlsetups[i])
    #获取接口token,并添加到header中
    url = case_data.get('loginUrl') + case_data.get('loginPath')
    header = eval(case_data.get('header'))
    token = apirequest.getxforcesaastoken(url=url, reqbody=eval(case_data.get('loginBody')), headers=header)
    header['xforce-saas-token'] = token

    #如果database_query不为空，则将查询的值追加到请求body中
    if case_data.get('database_query') is not None:
        if case_data.get('return_value') is None:
            logger.info('database_query和return_value的数量不一致，请修改用例数据......')
            assert 1==0
            return
        else:
            querysqls = str(case_data.get('database_query')).split(';')
            returnvalues = str(case_data.get('return_value')).split(';')
            if len(querysqls) != len(returnvalues):
                logger.info('database_query和return_value的数量不一致，请修改用例数据......',html=True,also_console=True)
                assert 1 == 0
                return
            else:
                for m in range(len(querysqls)):
                    if querysqls[m] != '':
                        queryresult = queryonefrommysql(getmysqlconnwithconfig(), querysqls[m])
                        case_data[returnvalues[m]] = list(queryresult[0].values())[0]
                        print('case_data=%s' % json.dumps(case_data))
                        logger.info('case_data==%s'+json.dumps(case_data), html=True,also_console=True)

    method = str(case_data.get('method')).upper()
    url = case_data.get('hostUrl') + case_data.get('path')
    #如果case_data的data列不为空，则执行sql语句并替代urlParameter中的变量，两列均不为空的情况下执行
    if case_data.get('data') is not None:
        if case_data.get('urlParameter') is not None:
            datasqls = str(case_data.get('data')).split(';')
            dataresultdict = {}
            for n in range(len(datasqls)):
                if datasqls[n]!='':
                    dataresultdict[list((queryonefrommysql(getmysqlconnwithconfig(),datasqls[n])[0]).keys())[0]] = list((queryonefrommysql(getmysqlconnwithconfig(),datasqls[n])[0]).values())[0]
            urlParameter = str(case_data.get('urlParameter'))
            for key in dataresultdict:
                urlParameter = urlParameter.replace('${'+key+'}',str(dataresultdict[key]))
            logger.info('urlParameter=%s' % urlParameter, html=True, also_console=True)
    # 判断接口请求类型，GET  POST  INPUT DELETE 并发送请求
    resp = None
    if method == 'POST':
        resp = apirequest.httppostresponsebody(url=url, reqbody=eval(case_data.get('request_body')), headers=header)
    elif method == 'GET':
        url = url + urlParameter
        resp = apirequest.httpgetresponsebody(url=url,headers=header)
    elif method == 'PUT':
        url = url + urlParameter
        resp = apirequest.httpputresponsebody(url=url, json=eval(case_data.get('request_body')), headers=header)
    elif method == 'DELETE':
        url = url + urlParameter
        resp = apirequest.httpdeleteresponsebody(url=url,headers=header)
    print('resp=%s' % resp)
    #判断接口响应是否为空，如果为空则用例失败
    if resp is None:
        logger.info('接口请求失败，无响应',html=True,also_console=True)
        #如果database_teardown不为空，则需清理数据
        if case_data.get('database_teardown') is not None:
            teardownsqls = str(case_data.get('database_teardown')).split(';')
            for j in range(len(teardownsqls)):
                if teardownsqls[j] != '':
                    excutemysql(getmysqlconnwithconfig(),teardownsqls[j])
        raise AssertionError('接口无响应，用例执行失败......')

    #结果验证
    result1 = True
    result2 = True
    #1、请求响应结果验证
    logger.info('开始进行响应结果验证......',html=True,also_console=True)
    expected_resp = eval(case_data.get('expected_response'))
    result1 = jsoncompare.json_comp(resp, expected_resp)
    print('result1=%s' % result1)
    #如果响应结果校失败，则用例执行失败，否则进行数据库校验
    if result1 == False:
        raise AssertionError('实际结果和期望结果不一致......')
    else:
        #2、数据库验证
        logger.info('开始进行数据库验证......', html=True, also_console=True)
        if case_data.get('database_verification') is not None:
            verificationsqls = str(case_data.get('database_verification')).split(';')
            if case_data.get('expected_rowcount') is None:
                raise AssertionError('用例参数expected_rowcount不能为空，请补充数据......')
            else:
                expectedrowcount = str(case_data.get('expected_rowcount')).split(';')
                logger.info('expectedrowcount=%s' % expectedrowcount,html=True,also_console=True)
                if len(verificationsqls)!=len(expectedrowcount):
                    raise AssertionError('expected_rowcount数量和database_verification数量不一致，请检查用例数据.......')
                else:
                    for k in range(len(verificationsqls)):
                        if verificationsqls[k]!='':
                            if queryfrommysql(getmysqlconnwithconfig(),verificationsqls[k]) is not None:
                                count = len(queryfrommysql(getmysqlconnwithconfig(),verificationsqls[k]))
                            else:
                                count = 0
                            logger.info('count=%d' % count,html=True,also_console=True)
                            if count == int(expectedrowcount[k]):
                                result2 = True
                            else:
                                time.sleep(10)
                                if case_data.get('database_delete') is not None:
                                    print('数据库校验失败，开始清理数据.......')
                                    deletesqls = str(case_data.get('database_delete')).split(';')
                                    for m in range(len(deletesqls)):
                                        if deletesqls[m]!='':
                                            excutemysql(getmysqlconnwithconfig(),deletesqls[m])
                                print('数据库校验失败，开始重新请求.......')
                                resp = apirequest.getpostresponsebody(url=url, reqbody=eval(case_data.get('request_body')), headers=header)
                                print('resp=%s'% resp)
                                result2 = False

    #清理数据
    if case_data.get('database_teardown') is not None:
        teardownsqls = str(case_data.get('database_teardown')).split(';')
        for j in range(len(teardownsqls)):
            if teardownsqls[j] != '':
                excutemysql(getmysqlconnwithconfig(), teardownsqls[j])

    assert result1 & result2 == True



# #=====================================================================================
# if __name__=='__main__':
#     sqls = 'SELECT * FROM t_retail_channel WHERE channel_key="test";'
#     print(len(sqls.split(';')))
#     for i in range(len(sqls.split(';'))):
#         print('----%s' % sqls.split(';')[i])
#         if sqls.split(';')[i] != '':
#             print('===%s'% sqls.split(';')[i])