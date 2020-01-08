from nada_dataprofilering.sql_script_generator.generic_functions import *


def min_number(schema_name, table_name, column_name):

    return basic_function_and_update(schema_name,
                                     table_name,
                                     column_name,
                                     'min',
                                     'number',
                                     'min_value')


def max_number(schema_name, table_name, column_name):

    return basic_function_and_update(schema_name,
                                     table_name,
                                     column_name,
                                     'max',
                                     'number',
                                     'max_value')


def mean_number(schema_name, table_name, column_name):
    return basic_function_and_update(schema_name,
                                     table_name,
                                     column_name,
                                     'mean',
                                     'number',
                                     'mean_value')


def median_number(schema_name, table_name, column_name):

    return basic_function_and_update(schema_name,
                                     table_name,
                                     column_name,
                                     'median',
                                     'number',
                                     'max_value')


def std_number(schema_name, table_name, column_name):

    return chained_function_and_update(schema_name,
                                       table_name,
                                       column_name,
                                       ['sqrt', 'variance'],
                                       'number',
                                       'std_value')


def num_zero(schema_name, table_name, column_name):

    return count_value_function_and_update(schema_name,
                                           table_name,
                                           column_name,
                                           '0',
                                           'number_zero')


def quantile(schema_name, table_name, column_name, p, nada_column):
    declare_string = declare_variables([{'name': 'quantile_value', 'data_type': 'number'},
                                       {'name': 'num_rows', 'data_type':'integer'},
                                       {'name': 'nearest_rank', 'data_type': 'integer'},
                                       {'name': 'current_row', 'data_type': 'integer'}])

    calculating_string = standard_select(column_name, 'count') + into(schema_name, table_name, 'num_rows')

    calculating_string += f"nearest_rank :=ceil({p}*num_rows); \n" + \
                          "current_row := 1; \n" + \
                          f"for i in (select {column_name}) from {schema_name}.{table_name} order by {column_name} asc)\n" +\
                          "loop \n" + \
                          "if current_row = nearest_rank then \n" +\
                          "quantile_value = i.{column_name}; \nexit; \nend if;\n" + \
                          "current_row = current_row +1;￿ \n" +\
                          "end loop;"

    update_string = update_nada_profilering(schema_name, table_name, column_name, nada_column, 'quantile_value')

    sql_string = declare_string + begin_and_end(calculating_string+update_string)

    return sql_string


def value_range(schema_name, table_name, column_name):
    declare_string = declare_variables([{'name': 'range_value', 'data_type': 'number'}])

    select_into_string = f"select max({column_name}) - min({column_name})" + into(schema_name, table_name, 'range_value')

    update_string = update_nada_profilering(schema_name, table_name, column_name, 'range', 'range_value')

    sql_string = declare_string + begin_and_end(select_into_string + update_string)

    return sql_string


def iqr(schema_name, table_name, column_name):
    p1 = 0.25
    p3 = 0.75
    declare_string = declare_variables([{'name': 'q1_value', 'data_type': 'number'},
                                        {'name': 'q3_value', 'data_type': 'number'},
                                        {'name': 'iqr', 'data_type': 'number'},
                                        {'name': 'num_rows', 'data_type': 'integer'},
                                        {'name': 'q1_nearest_rank', 'data_type': 'integer'},
                                        {'name': 'q3_nearest_rank', 'data_type': 'integer'},
                                        {'name': 'current_row', 'data_type': 'integer'}])

    calculating_string = standard_select(column_name, 'count') + into(schema_name, table_name, 'num_rows')
    calculating_string += f"q1_nearest_rank :=ceil({p1}*num_rows); \n" + \
                          f"q3_nearest_rank :=ceil({p3}*num_rows); \n" + \
                          "current_row := 1; \n" + \
                          f"for i in (select {column_name}) from {schema_name}.{table_name} order by {column_name} asc)\n" + \
                          "loop \n" + \
                          "if current_row = q1_nearest_rank then \n" + \
                          "q1_value = i.{column_name}; \n" +\
                          "end if \n" +\
                          "if current_row = q3_nearest_rank then \n" + \
                          "q3_value = i.{column_name}; \n" +\
                          "end if \n" +\
                          "current_row = current_row +1;￿ \n" + \
                          "end loop;\n" +\
                          "iqr := q3_value - q1_value;\n"

    update_string = update_nada_profilering(schema_name, table_name, column_name, 'iqr_value', 'iqr')

    sql_string = declare_string + begin_and_end(calculating_string + update_string)

    return sql_string


def coef_variation(schema_name, table_name, column_name):

    declare_string = declare_variables([{'name': 'cov', 'data_type': 'number'}])
    select_string = f"select sqrt(variance({column_name}))/avg({column_name}) " + into(schema_name, table_name, 'cov')
    update_string = update_nada_profilering(schema_name, table_name, column_name, 'cov_value', 'cov')
    sql_string = declare_string + begin_and_end(select_string + update_string)

    return sql_string


def value_sum(schema_name, table_name, column_name):

    return basic_function_and_update(schema_name,
                                     table_name,
                                     column_name,
                                     'sum',
                                     'number',
                                     'sum_value')


def value_variance(schema_name, table_name, column_name):

    return basic_function_and_update(schema_name,
                                     table_name,
                                     column_name,
                                     'variance',
                                     'number',
                                     'variance')


def mad_value(schema_name, table_name, column_name):
    declare_string = declare_variables([{'name': 'mad', 'data_type': 'number'},
                                        {'name': 'mu', 'data_type': 'number'}])

    mean_string = standard_select(column_name, 'avg') + into(schema_name, table_name, 'mu')
    mad_string = f"select median(abs({column_name}-mu)) " + into(schema_name, table_name, 'mad')

    update_string = update_nada_profilering(schema_name, table_name, column_name, 'mad_value', 'mad')

    sql_string = declare_string + begin_and_end(mean_string + mad_string + update_string)

    return sql_string


def kurtosis_value(schema_name, table_name, column_name):
    declare_string = declare_variables([{'name': 'num_rows', 'data_type': 'integer'},
                                        {'name': 'mu', 'data_type': 'number'},
                                        {'name': 'second_moment', 'data_type': 'number'},
                                        {'name': 'fourth_moment', 'data_type': 'number'},
                                        {'name': 'kurt', 'data_type': 'number'}])

    num_rows_string = standard_select(column_name, 'count') + into(schema_name, table_name, 'num_rows')
    mu_string = standard_select(column_name, 'avg') + into(schema_name, table_name, 'mu')
    second_moment_string = f"select sum(power({column_name}-mu, 2))/num_rows " + into(schema_name, table_name, 'second_moment')
    fourth_moment_string = f"select sum(power({column_name}-mu,4))/num_rows" + into(schema_name, table_name, 'fourth_moment')
    kurt_string = "kurt := (fourth_moment / power(second_moment,2)) -3;\n"

    update_string = update_nada_profilering(schema_name, table_name, column_name, 'kurt_value', 'kurt')

    sql_string = declare_string + begin_and_end(num_rows_string + mu_string + second_moment_string +
                                                fourth_moment_string + kurt_string + update_string)

    return sql_string


def skewness_value(schema_name, table_name, column_name):
    declare_string = declare_variables([{'name': 'num_rows', 'data_type': 'integer'},
                                        {'name': 'mu', 'data_type': 'number'},
                                        {'name': 'sigma', 'data_type': 'number'},
                                        {'name': 'third_moment', 'data_type': 'number'},
                                        {'name': 'skewness', 'data_type': 'number'}])

    num_rows_string = standard_select(column_name, 'count') + into(schema_name, table_name, 'num_rows')
    mu_string = standard_select(column_name, 'avg') + into(schema_name, table_name, 'mu')
    third_moment_string = f"select sum(power({column_name}-mu, 3))/num_rows " + into(schema_name, table_name, 'third_moment')
    sigma_string = chained_funcs_select(column_name, ['sqrt', 'variance']) + into(schema_name, table_name, 'sigma')
    skewness_string = "skewness:= third_moment/power(sigma,3); \n"

    update_string = update_nada_profilering(schema_name, table_name, column_name, 'skewness_value', 'skewness')

    sql_string = declare_string + begin_and_end(num_rows_string + mu_string + third_moment_string +
                                                sigma_string + skewness_string + update_string)

    return sql_string

