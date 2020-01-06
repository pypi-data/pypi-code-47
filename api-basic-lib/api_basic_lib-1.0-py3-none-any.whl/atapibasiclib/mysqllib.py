'''
此模块包含数据库操作相关的函数，如查询，增删改
'''
import atApiBasicLibrary.log as logger
import pymysql

def queryonefrommysql(conn,sql):
    '''
    【功能】根据sql语句查询数据库并返回一条查询结果
    【参数】conn:mysql数据库连接对象
            sql:需要执行的sql查询语句
    【返回】返回查询结果，只有一条
    '''
    cursor = conn.cursor()
    try:
        logger.info("\n数据库执行SQL: " + sql, html=True, also_console=True)
        count = cursor.execute(sql)
        logger.info('count=%s' %count, html=True, also_console=True)
        # 取出所有行
        result = cursor.fetchall()
        fields_list = []
        for field in cursor.description:
            # field[0]是field名字，如果使用别名，就是别名
            fields_list.append(field[0])
        conn.commit()  # 提交事务
        if result is None or len(result) == 0:
            logger.info("数据库返回结果: None", html=True, also_console=True)
            return None
        result_list = []
        for i in range(len(result)):
            row_dict = {}
            row = result[i]
            for j in range(len(row)):
                row_dict[fields_list[j]] = row[j]
            result_list.append(row_dict)
        logger.info("数据库返回结果: " + str(result_list), html=True, also_console=True)
        return result_list
    except pymysql.MySQLError as e:
        conn.rollback()  # 若出错了，则回滚
        logger.error("数据库错误: " + e)
        raise AssertionError("数据库错误: " + e)

    finally:
        try:
            cursor.close()
        except pymysql.MySQLError as e:
            logger.error("关闭cursor出错: " + e)
        except pymysql.OperationalError as e:
            logger.error("关闭cursor出错: " + e)
        try:
            conn.close()
        except pymysql.MySQLError as e:
            logger.error("关闭数据库连接出错: " + e)
        except pymysql.OperationalError as e:
            logger.error("关闭数据库连接出错: " + e)



def queryfrommysql(conn,sql):
    '''
    【功能】根据sql语句查询数据库并返回查询结果
    【参数】conn:mysql数据库连接对象
            sql:需要执行的sql查询语句
    【返回】返回查询结果集，字典类型，如果为空，返回{}
    '''
    cursor = conn.cursor()
    try:
        logger.info("\n数据库执行SQL: " + sql, html=True, also_console=True)
        count = cursor.execute(sql)
        # 取出所有行
        result = cursor.fetchall()
        fields_list = []
        for field in cursor.description:
            # field[0]是field名字，如果使用别名，就是别名
            fields_list.append(field[0])
        conn.commit()  # 提交事务
        if result is None or len(result) == 0:
            logger.info("数据库返回结果: None", html=True, also_console=True)
            return None
        result_list = []
        for i in range(len(result)):
            row_dict = {}
            row = result[i]
            for j in range(len(row)):
                row_dict[fields_list[j]] = row[j]
            result_list.append(row_dict)
        logger.info("数据库返回结果: " + str(result_list), html=True, also_console=True)
        return result_list
    except pymysql.MySQLError as e:
        conn.rollback()  # 若出错了，则回滚
        logger.error("数据库错误: " + e)
        raise AssertionError("数据库错误: " + e)

    finally:
        try:
            cursor.close()
        except pymysql.MySQLError as e:
            logger.error("关闭cursor出错: " + e)
        except pymysql.OperationalError as e:
            logger.error("关闭cursor出错: " + e)
        try:
            conn.close()
        except pymysql.MySQLError as e:
            logger.error("关闭数据库连接出错: " + e)
        except pymysql.OperationalError as e:
            logger.error("关闭数据库连接出错: " + e)

def excutemysql(conn,sql):
    '''
    【功能】执行sql语句
    【参数】conn:mysql数据库连接对象
            sql:需要执行的sql语句
    【返回】返回影响的行数，整数类型
    '''
    cursor = conn.cursor()
    try:
        logger.info("\n数据库执行SQL: " + sql, html=True, also_console=True)
        count = cursor.execute(sql)
        logger.info("被影响的行数: " + str(count), html=True, also_console=True)
        conn.commit()  # 提交事务
        return count
    except pymysql.MySQLError as e:
        conn.rollback()  # 若出错了，则回滚
        logger.error("数据库错误: " + e)
        raise AssertionError("数据库错误: " + e)

    finally:
        try:
            cursor.close()
        except pymysql.MySQLError as e:
            logger.error("关闭cursor出错: " + e)
        except pymysql.OperationalError as e:
            logger.error("关闭cursor出错: " + e)
        try:
            conn.close()
        except pymysql.MySQLError as e:
            logger.error("关闭数据库连接出错: " + e)
        except pymysql.OperationalError as e:
            logger.error("关闭数据库连接出错: " + e)