from utils import helpers
import json


def select(spark, table, filtros={}, limit=20):
    query_base = 'select * from ' + table
    where = ""
    tot = 0
    if filtros:
        for filtro in filtros:
            if tot > 0:
                where += " AND "
            else:
                where += " where "
            where += filtro + "='" + str(filtros[filtro]) + "'"
            tot += 1
    sql_statement = query_base + where #+ " limit " + str(limit)
    df = spark.sql(sql_statement)
    _dict = helpers.dfToJson(df=df)
    return _dict


def insert(spark, table, values=[]):
    cols = getColumns(spark, table)
    cont_line = 0
    cont_col = 0
    _value = values[0]
    sql = "INSERT OVERWRITE TABLE "+table+" PARTITION(" + \
            getPartition(spark=spark, table=table, cols=cols, _value=_value)+") VALUES "
    for line in values:
        sql += "("
        cont_line += 1
        cont_col = 0
        for col in cols:
            try:
                cont_col += 1
                separetor = "" if cont_col == len(cols) else ","
                sql += "'" + col.format(**line) + "'" + separetor
            except:
                sql += str("null") + separetor
        sql += ")" if cont_line == len(values) else "),"
    spark.sql(sql)
    return sql


def getPartition(spark, table, cols, _value):
    partdf = spark.sql("desc " + table)
    partjs = helpers.dfToJson(partdf)
    partjs.reverse()
    parts = ""
    for row in partjs:
        if row.get("col_name") == "# col_name":
            parts = parts[0:-1]
            break
        partition = str(row.get("col_name"))
        val_part = _value.get(str(partition))
        print("partition => "+ partition)
        print("_value =>"+ str(_value))
        print("val_part =>"+ val_part)
        parts += partition + "=\"" + val_part + "\","
        cols.remove("{"+ partition +"}")
    return parts


def getColumns(spark, table):
    sql = "SHOW COLUMNS FROM " + table
    df = spark.sql(sql)
    _dict = helpers.dfToJson(df=df)
    cols = ""
    cont = 0
    for line in _dict:
        cont += 1
        separetor = "" if cont == len(_dict) else ","
        for field, value in line.iteritems():
            cols += '{%s}'%(value) + separetor
    _cols = cols.split(",")
    return _cols


def insertBF(spark, table, values=[]):
    dt_foto = helpers.now("%Y-%m-%d")
    events = len(values)
    bf_size = 16
    cycles, extra = int(events / bf_size), bool(events % bf_size)
    last = 0
    for count in range(cycles+extra):
        q = "INSERT OVERWRITE TABLE "+ table + " PARTITION(dt_foto=\"" + dt_foto + "\") VALUES ("
        start = last
        last += bf_size
        for data in safe_values(values[start:last]):
            q += "\""
            q += "','".join(data)
            q += "\","
        q = q[0:-1] + ")"
        return q


def safe_values(values):
    for line in values:
        values = []
        for field, value in line.iteritems():
            if type(value) in [str, unicode]:
                values.append(value.decode('utf-8').encode('utf-8').replace("'", ''))
            else:
                values.append(str(value).decode('utf-8').encode('utf-8').replace("'", ''))
        yield(values)