from nada_dataprofilering.sql_script_generator.generic_functions import *


def date_min(schema_name, table_name, column_name, table, column):

    return basic_function_and_update(schema_name,
                                     table_name,
                                     column_name,
                                     'min',
                                     'date',
                                     table,
                                     column)


def date_max(schema_name, table_name, column_name, table, column):

    return basic_function_and_update(schema_name,
                                     table_name,
                                     column_name,
                                     'max',
                                     'date',
                                     table,
                                     column)


def date_median(schema_name, table_name, column_name, table, column):

    return basic_function_and_update(schema_name,
                                     table_name,
                                     column_name,
                                     'median',
                                     'date',
                                     table,
                                     column)

