#!/usr/bin/python
# -*- coding: utf-8 -*-

from pg_metadata._System import SEP
from pg_metadata.ACL     import ACL
from pg_metadata.Owner   import Owner
from pg_metadata.Comment import Comment

QUERY_SEQUENCE = """
    SELECT
        c.oid,
        trim(lower(n.nspname)) AS schema,
        trim(lower(c.relname)) AS name,
        trim(lower(r.rolname)) AS owner,
        trim(coalesce(obj_description(c.oid), '')) AS comment,
        c.relacl::varchar[],
        s.increment,
        s.minimum_value,
        s.maximum_value,
        s.cycle_option = 'YES' AS is_cycle,
        1 AS start,
        1 AS cache
    FROM pg_class c
    JOIN pg_namespace n ON
        n.oid = c.relnamespace AND
        n.nspname != ALL(%s)
    JOIN pg_roles r ON
        r.oid = c.relowner
    JOIN information_schema.sequences s ON
        s.sequence_schema = n.nspname and
        s.sequence_name = c.relname
    WHERE c.relkind = 'S'
    ORDER BY 2,3
"""

class Sequence():
    def __init__(self, row={}, ddl_style=""):
        assert row is not None
        assert isinstance(row, dict)
        assert len(row.keys()) > 0

        self.Type = "SEQUENCE"

        self.Oid = row.get('oid')
        assert self.Oid is not None and self.Oid > 0

        self.Schema = row.get('schema') or ''
        self.Schema = self.Schema.strip()
        assert len(self.Schema) > 0

        self.Name = row.get('name') or ''
        self.Name = self.Name.strip()
        assert len(self.Name) > 0

        self.FullName = "%s.%s" % (self.Schema, self.Name)

        self.Increment = row.get("increment")
        self.MinValue  = row.get("minimum_value")
        self.MaxValue  = row.get("maximum_value")
        self.IsCycle   = row.get("is_cycle")
        self.Cache     = row.get("cache")

        self.Folder = "sequence"

        self.DDLStyle = ddl_style

        self.Owner = Owner(
            "TABLE",
            self.FullName,
            row.get("owner"),
            self.DDLStyle
        )

        self.Comment = Comment(
            self.Type,
            self.FullName,
            row.get("comment"),
            self.DDLStyle
        )

        self.ACL = ACL(
            self.Type,
            self.FullName,
            self.Owner.Owner,
            row.get("relacl"),
            self.DDLStyle
        )

    def __str__(self):
        return self.FullName

    def QueryAdd(self):
        r = ""
        r += "CREATE SEQUENCE %s" % (self.FullName)
        r += SEP
        r += "  INCREMENT %s" % (self.Increment)
        r += SEP
        r += "  MINVALUE %s" % (self.MinValue)
        r += SEP
        r += "  MAXVALUE %s" % (self.MaxValue)
        r += SEP
        r += "  START %s" % (1)
        r += SEP
        r += "  CACHE %s" % (self.Cache)
        r += SEP
        if self.IsCycle:
            r += "  CYCLE"
        return r.strip() + ";"

    def QueryRemove(self):
        return 'DROP SEQUENCE %s;' % (self.FullName)

    def DDL_Full(self):
        result = ""
        if self.DDLStyle == "pgadmin3":
            result += "-- Sequence: %s" % (self.FullName)
            result += SEP
            result += SEP
            result += "-- %s" % (self.QueryRemove())
            result += SEP
            result += SEP
            result += self.QueryAdd()
            result += SEP
            result += self.Owner.DDL_Create()
            result += SEP
            result += self.ACL.DDL_Create()
            result += SEP

            if self.Comment.IsExists:
                result += self.Comment.DDL_Create()
                result += SEP

        else:
            result += "-- Sequence: %s" % (self.FullName)
            result += SEP
            result += SEP
            result += "-- %s" % (self.QueryRemove())
            result += SEP
            result += SEP
            result += self.QueryAdd()
            result += SEP
            result += SEP
            result += self.Owner.DDL_Create()
            result += SEP
            result += self.ACL.DDL_Create()
            result += SEP
            result += SEP

            if self.Comment.IsExists:
                result += self.Comment.DDL_Create()
                result += SEP

        return result.strip() + SEP
