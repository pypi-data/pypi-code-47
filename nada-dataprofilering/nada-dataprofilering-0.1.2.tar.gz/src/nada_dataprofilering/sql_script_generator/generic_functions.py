from nada_dataprofilering.sql_script_generator.util_functions import *


def basic_function_and_update(schema_name, table_name, column_name, sql_func, data_type, table, column):
    declare_string = declare_variables([{'name': 'answer', 'data_type': data_type}])

    select_into_string = standard_select(column_name, sql_func) + into(schema_name, table_name, 'answer')

    update_string = update_table(schema_name, table_name, column_name, table, column, 'answer')

    sql_string = declare_string + begin_and_end(select_into_string + update_string)

    return sql_string


def chained_function_and_update(schema_name, table_name, column_name, sql_funcs, data_type, table, column):
    declare_string = declare_variables([{'name': 'answer', 'data_type': data_type}])

    select_into_string = chained_funcs_select(column_name, sql_funcs) + into(schema_name, table_name, 'answer')

    update_string = update_table(schema_name, table_name, column_name, table, column, 'answer')

    sql_string = declare_string + begin_and_end(select_into_string + update_string)

    return sql_string


def count_value_function_and_update(schema_name, table_name, column_name, value, table, column):
    declare_string = declare_variables([{'name': 'answer', 'data_type': 'integer'}])

    select_into_string = count_value_select(column_name, value) + into(schema_name, table_name, 'answer')

    update_string = update_table(schema_name, table_name, column_name, table,  column, 'answer')

    sql_string = declare_string + begin_and_end(select_into_string + update_string)

    return sql_string
