from nada_dataprofilering.sql_script_generator.util_sql_scripts import *
from math import *


def num_min(schema, table, column):
    sql_string = f"select min({column}) from {schema}.{table}"
    return sql_string


def num_max(schema, table, column):
    sql_string = f"select max({column}) from {schema}.{table}"
    return sql_string


def num_median(schema, table, column):
    sql_string = f"select median({column}) from {schema}.{table}"
    return sql_string


def num_percentile(schema, table, column, p):
    sql_string = f"select percentile_disc({p}) within group(order by {column}) from {schema}.{table}"
    return sql_string


def num_range(min_value, max_value):
    return max_value - min_value


def num_iqr(q1, q3):
    return q3 - q1


def num_mean(schema, table, column, number_rows, sample_pct, threshold=10000):
    sql_string = f"select avg({column}) from {schema}.{table} "
    if sample_bool(number_rows):
        sql_string += sample_statement(sample_pct, threshold)

    return sql_string


def num_var(schema, table, column, number_rows, sample_pct, threshold=10000):
    sql_string = f"select variance({column}) from {schema}.{table} "
    if sample_bool(number_rows):
        sql_string += sample_statement(sample_pct, threshold)

    return sql_string


def num_std(var_value):
    return sqrt(var_value)


def num_cov(std_value, mean_value):
    if mean_value != 0:
        return std_value/mean_value
    else:
        return None


def num_sum(schema, table, column):
    sql_string = f"select sum({column}) from {schema}.{table}"
    return sql_string


def num_mad(schema, table, column, mean_value, number_rows, sample_pct, threshold=10000):
    sql_string = f"select median(abs({column} - {mean_value})) from {schema}.{table} "
    if sample_bool(number_rows, threshold):
        sql_string += sample_statement(sample_pct)

    return sql_string


def num_sum_n_power(schema, table, column, number_rows, sample_pct, mean_value, n, threshold=10000):
    sql_string = f"select power(sum({column}- {mean_value}),{n}) from {schema}.{table} "
    if sample_bool(number_rows):
        sql_string += sample_statement(sample_pct, threshold)

    return sql_string


def num_skewness(number_rows, sample_size, std_value, sum_2_power):
    if sample_bool(number_rows):
        return (sum_2_power/sample_size)/(std_value**3)
    else:
        return (sum_2_power/sample_size)/(std_value**3)


def num_kurt(number_rows, sample_size, sum_2_power, sum_4_power):
    if sample_bool(number_rows):
        return ((sum_4_power/sample_size)/(sum_2_power/sample_size)) - 3
    else:
        return ((sum_4_power / number_rows) / (sum_2_power / number_rows)) - 3


def num_zero(schema, table, column):
    sql_script = f"select sum(case when {column} = 0 then 1 end) from {schema}.{table}"
    return sql_script



