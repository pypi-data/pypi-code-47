from nada_dataprofilering.sql_script_generator.generic_functions import *


def varchar2_min(schema_name, table_name, column_name, table, column):

    return chained_function_and_update(schema_name,
                                       table_name,
                                       column_name,
                                       ['min', 'length'],
                                       'integer',
                                       table,
                                       column)


def varchar2_max(schema_name, table_name, column_name, table, column):

    return chained_function_and_update(schema_name,
                                       table_name,
                                       column_name,
                                       ['max', 'length'],
                                       'integer',
                                       table,
                                       column)


def varchar2_mean(schema_name, table_name, column_name, table, column):

    return chained_function_and_update(schema_name,
                                       table_name,
                                       column_name,
                                       ['avg', 'length'],
                                       'number',
                                       table,
                                       column)


def varchar2_median(schema_name, table_name, column_name, table, column):

    return chained_function_and_update(schema_name,
                                       table_name,
                                       column_name,
                                       ['median', 'length'],
                                       'integer',
                                       table,
                                       column)


def varchar2_std(schema_name, table_name, column_name, table, column):

    return chained_function_and_update(schema_name,
                                       table_name,
                                       column_name,
                                       ['sqrt', 'variance', 'length'],
                                       'number',
                                       table,
                                       column)

