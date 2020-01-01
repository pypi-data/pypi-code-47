class QueryBuilder():
    def echo_table_existence(self, table):
        return '''
            SELECT name FROM sqlite_master
                WHERE type = 'table'
                AND name = '{}'
            '''.format(table)

    def create_table(self, table, scheme):
        return 'CREATE TABLE {} ({})'.format(
            table,
            ', '.join(['{} {}'.format(key, value) for key, value in scheme.items()])
        )

    def replace(self, table, row):
        return 'REPLACE INTO {} ({}) VALUES ({})'.format(
            table,
            ', '.join(row.keys()),
            ', '.join(['"{}"'.format(value) for value in row.values()])
        )

    def select(self, table, scheme, key, value):
        operator = None
        if 'TEXT' in scheme[key]:
            operator = 'LIKE'
        elif 'TIMESTAMP' in scheme[key]:
            operator = '>'

        return 'SELECT {} FROM {} WHERE {} {} "{}"'.format(
            ', '.join(scheme.keys()),
            table,
            key,
            operator,
            value
        )
