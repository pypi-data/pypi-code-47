from nada_dataprofilering.sql_script_generator.generic_functions import *


def min_len(schema_name, table_name, column_name):

    return chained_function_and_update(schema_name,
                                       table_name,
                                       column_name,
                                       ['min', 'length'],
                                       'integer',
                                       'min_len')


def max_len(schema_name, table_name, column_name):

    return chained_function_and_update(schema_name,
                                       table_name,
                                       column_name,
                                       ['max', 'length'],
                                       'integer',
                                       'max_len')


def mean_len(schema_name, table_name, column_name):

    return chained_function_and_update(schema_name,
                                       table_name,
                                       column_name,
                                       ['mean', 'length'],
                                       'number',
                                       'mean_len')


def median_len(schema_name, table_name, column_name):

    return chained_function_and_update(schema_name,
                                       table_name,
                                       column_name,
                                       ['median', 'length'],
                                       'integer',
                                       'mean_len')


def std_len(schema_name, table_name, column_name):

    return chained_function_and_update(schema_name,
                                       table_name,
                                       column_name,
                                       ['sqrt', 'variance', 'length'],
                                       'number',
                                       'std_value')

