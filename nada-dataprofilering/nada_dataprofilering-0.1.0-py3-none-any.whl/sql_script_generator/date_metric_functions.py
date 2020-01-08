from nada_dataprofilering.sql_script_generator.generic_functions import *


def min_date(schema_name, table_name, column_name):

    return basic_function_and_update(schema_name,
                                     table_name,
                                     column_name,
                                     'min',
                                     'date',
                                     'min_date')


def max_date(schema_name, table_name, column_name):

    return basic_function_and_update(schema_name,
                                     table_name,
                                     column_name,
                                     'max',
                                     'date',
                                     'max_date')


def median_date(schema_name, table_name, column_name):

    return basic_function_and_update(schema_name,
                                     table_name,
                                     column_name,
                                     'median',
                                     'date',
                                     'median_date')

