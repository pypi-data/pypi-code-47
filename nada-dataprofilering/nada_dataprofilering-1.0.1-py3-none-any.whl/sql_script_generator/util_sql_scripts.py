def sample_statement(sample_pct, seed=0):
    return f"sample({sample_pct}) seed({seed})"


def sample_bool(number_rows, threshold=10000):
    if number_rows > threshold:
        return True
    else:
        return False


def metadata():
    sql_string = """select
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
     where a.owner = 'DT_P' and b.owner = 'DT_P' and c.owner = 'DT_P' and d.schema_name = 'DT_P'"""

    return sql_string


