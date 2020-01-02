#!/usr/bin/python
# -*- coding: utf-8 -*-

QUERY_TABLE_SETTINGS = """
    select
        trim(lower(n.nspname)) as schema,
        trim(lower(c.relname)) as table,
        trim(lower(unnest(c.reloptions))) as setting
    from pg_class c
    join pg_namespace n on
        n.oid = c.relnamespace AND
        n.nspname != ALL(%s)
    where c.reloptions is not null
    order by 1,2,3
"""

class TableSettings():
    def __init__(self, schema_name, table_name, setting):
        self.Schema = schema_name or ''
        self.Schema = self.Schema.strip().lower()
        assert len(self.Schema) > 0

        self.Table = table_name or ''
        self.Table = self.Table.strip().lower()
        assert len(self.Table) > 0

        self.FullTable = '%s.%s' % (self.Schema, self.Table)

        self.Setting = setting or ''
        self.Setting = self.Setting.strip().lower()
        assert len(self.Setting) > 0
        assert self.Setting.find('=') >= 0

        self.FieldName = self.Setting.split('=')[0].strip().upper()
        self.FieldValue = self.Setting.split('=')[1].strip().upper()

        self.FullName = '%s.%s.%s' % (self.Schema, self.Table, self.FieldName)

    def __str__(self):
        return "%s=%s" % (self.FieldName, self.FieldValue)

    def DDL_Table(self, style=""):
        return "  %s=%s" % (self.FieldName, self.FieldValue)

    def DDL_Drop(self, style=""):
        return """ALTER TABLE %s.%s RESET (%s);""" % (
            self.Schema, self.Table, self.FieldName)

    def DDL_Create(self, style=""):
        return """ALTER TABLE %s.%s SET (%s = %s);""" % (
            self.Schema, self.Table, self.FieldName, self.FieldValue)
