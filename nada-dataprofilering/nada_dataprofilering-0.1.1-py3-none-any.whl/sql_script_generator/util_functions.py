def declare_variables(variables):
    """
    Function that generates a sql declare statement

    :param variables: list of dictionaries. Each dict has two keys 'name' and 'data_type'.
    :return: A sql script that declares variables as a string.
    """
    sql_string = "declare \n"
    for var in variables:
        sql_string += f"{var['name']} {var['data_type']}; \n"

    return sql_string


def begin_and_end(content):
    """
    Function that generates a begin end block
    :param content: A string with sql statements that will be in the begin end block
    :return: A begin end block with content in the block as a string.
    """
    sql_string = "begin \n" + content + "\nend;"
    return sql_string


def into(schema_name, table_name, variable):
    sql_string = f"into {variable} from {schema_name}.{table_name}; \n"
    return sql_string


def standard_select(column_name, sql_func):
    sql_string = f"select {sql_func}({column_name}) "
    return sql_string


def chained_funcs_select(column_name, sql_funcs):
    sql_string = f"select "
    for i in range(len(sql_funcs)):
        sql_string += sql_funcs[i] + "("
    sql_string += f"{column_name}" + len(sql_funcs) * ")" + " "

    return sql_string


def count_value_select(column_name, value):
    if value.upper() == 'NULL':
        sql_script = f"select sum(case when {column_name} is NULL then 1 else 0 end) "
    else:
        sql_script = f"select sum(case when {column_name} = {value} then 1 else 0 end) "

    return sql_script


def update_table(schema_name, table_name, column_name, table, column, value):
    sql_string = f"update {table} set {column} ={value} \n" +\
                 f"where schema_name ='{schema_name}' and table_name ='{table_name}' and column_name ='{column_name}';"

    return sql_string

# Return sql scrips that makes table


def create_nada_table(table_name):
    sql_string = f"""create
    table
    {table_name} as
    (SELECT
     a.owner as schema_name,
     a.table_name,
     a.column_name,
     a.data_type,
     b.comments as column_description,
     c.comments as table_description,
     d.team_name

     from all_tab_cols a
     inner join all_col_comments b
     on  a.table_name = b.table_name and a.column_name = b.column_name
     inner join all_tab_comments c
     on a.table_name = c.table_name
     inner join OSDDM_REPORT_REPOS.dmo_dstr_tables_to_team d on a.table_name = d.table_name
     where a.owner = 'DT_P' and b.owner = 'DT_P' and c.owner = 'DT_P' and d.schema_name = 'DT_P')"""

    return sql_string


def new_column_table(table, columns):
    sql_string = f"alter table {table} \nadd (\n"

    for i in range(len(columns)):
        if i != len(columns) - 1:
            sql_string += f"{columns[i]['name']} {columns[i]['data_type']},\n"
        else:
            sql_string += f"{columns[i]['name']} {columns[i]['data_type']}"

    sql_string += ")"

    return sql_string


def update_column(table, column, schema_name, table_name, column_name, value):
    sql_string = f"update {table} set {column} = {value} \n"
    sql_string += f"where schema_name = '{schema_name}' and table_name = '{table_name}' and column_name = '{column_name}';"

    return sql_string


def column_dict(name, data_type):
    return {'name': name, 'data_type': data_type}
