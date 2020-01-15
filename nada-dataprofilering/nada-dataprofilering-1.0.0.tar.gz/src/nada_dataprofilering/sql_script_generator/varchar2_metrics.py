from nada_dataprofilering.sql_script_generator.util_sql_scripts import *
from math import *


def varchar2_min(schema, table, column):
    sql_string = f"select min(length({column})) from {schema}.{table}"
    return sql_string


def varchar2_median(schema, table, column):
    sql_string = f"select median(length({column})) from {schema}.{table}"
    return sql_string


def varchar2_max(schema, table, column):
    sql_string = f"select max(length({column})) from {schema}.{table}"
    return sql_string


def varchar2_mean(schema, table, column, number_rows, sample_pct, threshold=10000):
    sql_string = f"select avg(length({column})) from {schema}.{table} "
    if sample_bool(number_rows):
        sql_string += sample_statement(sample_pct, threshold)
    return sql_string


def varchar2_var(schema, table, column, number_rows, sample_pct, threshold=10000):
    sql_string = f"select variance(length({column})) from {schema}.{table} "
    if sample_bool(number_rows):
        sql_string += sample_statement(sample_pct, threshold)
    return sql_string


def varchar2_std(var_value):
    return sqrt(var_value)
