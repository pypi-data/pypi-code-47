#!/usr/bin/python
# -*- coding: utf-8 -*-

from pg_metadata._Postgres          import Postgres
from pg_metadata.Namespace          import Namespace,       QUERY_NAMESPACE
from pg_metadata.Table              import Table,           QueryTable
from pg_metadata.TableColumn        import TableColumn,     QUERY_TABLE_COLUMN
from pg_metadata.TableConstraint    import TableConstraint, QUERY_TABLE_CONSTRAINT
from pg_metadata.TableIndex         import TableIndex,      QUERY_TABLE_INDEX
from pg_metadata.TableTrigger       import TableTrigger,    QUERY_TABLE_TRIGGER
from pg_metadata.View               import View,            QUERY_VIEW
from pg_metadata.Sequence           import Sequence,        QUERY_SEQUENCE
from pg_metadata.Function           import Function,        QUERY_FUNCTION
from pg_metadata.ForeignServer      import ForeignServer,   QUERY_FOREIGN_SERVER
from pg_metadata.ForeignTable       import ForeignTable,    QUERY_FOREIGN_TABLE

class Database():
    def __init__(self, connect, exclude_schemas=[]):
        self.PG = Postgres(connect)
        self.ExcludeSchemas = exclude_schemas

        self.Namespaces = {}

        self.Tables = {}
        self.TablesColumns = {}
        self.TablesConstraints = {}
        self.TablesIndexes = {}
        self.TablesTriggers = {}

        self.Views = {}

        self.Sequences = {}

        self.Functions = {}

        self.ForeignServers = {}
        self.ForeignTables = {}

    def __str__(self):
        return str(self.PG)

    def Parse(self):
        self.PG.Connect()

        for row in self.PG.Execute(QUERY_NAMESPACE, [self.ExcludeSchemas]):
            t = Namespace(row)
            self.Namespaces[t.Name] = t

        for row in self.PG.Execute(QUERY_VIEW, [self.ExcludeSchemas]):
            t = View(row)
            self.Views[t.FullName] = t

        for row in self.PG.Execute(QueryTable(self.PG.Version), [self.ExcludeSchemas]):
            t = Table(row)
            self.Tables[t.FullName] = t

        for row in self.PG.Execute(QUERY_TABLE_COLUMN, [self.ExcludeSchemas]):
            t = TableColumn(row)
            self.TablesColumns[t.FullName] = t
            self.Tables[t.FullTable].Columns.append(t)

        for row in self.PG.Execute(QUERY_TABLE_CONSTRAINT, [self.ExcludeSchemas]):
            t = TableConstraint(row)
            self.TablesConstraints[t.FullName] = t
            self.Tables[t.FullTable].Constraints.append(t)

        for row in self.PG.Execute(QUERY_TABLE_INDEX, [self.ExcludeSchemas]):
            t = TableIndex(row)
            self.TablesIndexes[t.FullName] = t

            if self.Tables.get(t.FullTable) is not None:
                self.Tables.get(t.FullTable).Indexes.append(t)

            if self.Views.get(t.FullTable) is not None:
                self.Views.get(t.FullTable).Indexes.append(t)

        for row in self.PG.Execute(QUERY_TABLE_TRIGGER, [self.ExcludeSchemas]):
            t = TableTrigger(row)
            self.TablesTriggers[t.FullName] = t
            self.Tables[t.FullTable].Triggers.append(t)

        for row in self.PG.Execute(QUERY_SEQUENCE, [self.ExcludeSchemas]):
            t = Sequence(row)
            self.Sequences[t.FullName] = t

        for row in self.PG.Execute(QUERY_FUNCTION, [self.ExcludeSchemas]):
            t = Function(row)
            self.Functions[t.FullName] = t

        for row in self.PG.Execute(QUERY_FOREIGN_SERVER, [self.ExcludeSchemas]):
            t = ForeignServer(row)
            self.ForeignServers[t.Name] = t

        for row in self.PG.Execute(QUERY_FOREIGN_TABLE, [self.ExcludeSchemas]):
            t = ForeignTable(row)
            self.ForeignTables[t.Name] = t

        self.PG.Disconnect()
