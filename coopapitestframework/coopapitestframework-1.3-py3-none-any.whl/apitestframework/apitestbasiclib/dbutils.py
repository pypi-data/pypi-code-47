# coding:utf-8

import pymysql

def query_rows_count(sqlstatment,configdict):
    '''
    【功能】执行查询语句，返回查询结果的条数
    【参数】rul:数据库地址
            username:数据库连接名
            pwd:数据库连接密码
            dbname:数据库名称
    【返回】查询的结果行数
    '''
    conn = pymysql.connect(**configdict)
    cursor = conn.cursor()
    try:
        cursor.execute(sqlstatment)
        # rows = len(cursor.fetchall())
        rows = cursor.rowcount
    except:
        print("Error: unable to fetch data")
    conn.close()
    return rows

def query_result_all(sqlstatment,configdict):
    '''
    【功能】执行查询语句，返回查询结果
    【参数】rul:数据库地址
            username:数据库连接名
            pwd:数据库连接密码
            dbname:数据库名称
            sqlstatment:要执行的sql语句
    【返回】查询的结果,列表类型，元素为字典
    '''
    conn = pymysql.connect(**configdict)
    cursor = conn.cursor()
    cursor.execute(sqlstatment)
    count = cursor.rowcount
    print('count=%s' % count)
    des = cursor.description
    filed_list = []
    for field in des:
        filed_list.append(field[0])
    print('filed_list=%s'% filed_list)
    result_list = []
    try:
        results = cursor.fetchall()
        for i in range(count):
            print('i=%s'% i)
            result_dict = {}
            for j in range(len(filed_list)):
                result_dict[filed_list[j]] = results[i][j]
            result_list.append(result_dict)
    except:
        print("Error: unable to fetch data")
    conn.close()
    return result_list

def query_result_one(sqlstatment,configdict):
    '''
    【功能】执行查询语句，返回查询结果
    【参数】rul:数据库地址
            username:数据库连接名
            pwd:数据库连接密码
            dbname:数据库名称
            sqlstatment:要执行的sql语句
    【返回】查询的结果,字典类型
    '''
    conn = pymysql.connect(**configdict)
    cursor = conn.cursor()
    cursor.execute(sqlstatment)
    count = cursor.rowcount
    print('count=%s' % count)
    des = cursor.description
    filed_list = []
    for field in des:
        filed_list.append(field[0])
    print('filed_list=%s'% filed_list)
    result_dict = {}
    try:
        result = cursor.fetchone()
        for j in range(len(filed_list)):
            result_dict[filed_list[j]] = result[j]
    except:
        print("Error: unable to fetch data")
    conn.close()
    return result_dict

def excute_sqls(sqlstatment,configdict):
    '''
    【功能】执行sql语句，增删改操作时调用此函数
    【参数】rul:数据库地址
            username:数据库连接名
            pwd:数据库连接密码
            dbname:数据库名称
    【返回】影响的结果行数
    '''
    conn = pymysql.connect(**configdict)
    cursor = conn.cursor()
    try:
        cursor.execute(sqlstatment)
        # rows = len(cursor.fetchall())
        conn.commit()
    except:
        print("Error: unable to fetch data")
        conn.rollback()
    conn.close()
    # return rowcount


########################################################################################
if __name__=='__main__':
    sqlstatment1 = "SELECT id,prod_no from retail_product where prod_no like 'AP%'"
    configdict = {
                    'host':'phoenix-t.xforceplus.com',
                    'port':23318,
                    'user':'root',
                    'password':'xplat',
                    'db':'xforce_retail',
                    'charset':'utf8mb4'
                }
    # rows = query_rows_count(sqlstatment1,configdict)
    # print('rows=%d'% rows)
    sqlstatment2 = "SELECT id,prod_no  from retail_product where prod_no like 'AP%'"
    results = query_result_one(sqlstatment2,configdict)
    print(results)
