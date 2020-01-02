#!/usr/bin/python
# -*- coding: utf-8 -*-

from pg_metadata._System import SEP
from pg_metadata.ACL     import ACL
from pg_metadata.Owner   import Owner
from pg_metadata.Comment import Comment

QUERY_NAMESPACE = """
    SELECT
        n.oid,
        trim(lower(n.nspname)) AS name,
        trim(lower(r.rolname)) AS owner,
        trim(coalesce(obj_description(n.oid), '')) AS comment,
        n.nspacl::varchar[] as acl
    FROM pg_namespace n
    JOIN pg_roles r ON
        r.oid = n.nspowner
    WHERE n.nspname != ALL(%s)
    ORDER BY 2,3
"""

class Namespace():
    def __init__(self, row={}, ddl_style=""):
        assert row is not None
        assert isinstance(row, dict)
        assert len(row.keys()) > 0

        self.Oid = row.get("oid")
        assert self.Oid is not None and self.Oid > 0

        self.Name = row.get("name") or ""
        self.Name = self.Name.strip()
        assert len(self.Name) > 0

        self.Type = "SCHEMA"
        self.DDLStyle = ddl_style

        self.Owner = Owner(self.Type, self.Name, row.get("owner"), self.DDLStyle)
        self.Comment = Comment(self.Type, self.Name, row.get("comment"), self.DDLStyle)

        self.Path = [self.Name]
        self.File = self.Name

        self.ACL = ACL(self.Type, self.Name, self.Owner.Owner, row.get("relacl"), self.DDLStyle)

    def __str__(self):
        return self.Name

    def DDL_Create(self):
        r = ""
        r += "CREATE SCHEMA %s;" % (self.Name)
        return r

    def DDL_Drop(self):
        return "DROP SCHEMA IF EXISTS %s;" % (self.Name)

    def DDL_Full(self):
        r = ""
        if self.DDLStyle == "pgadmin3":
            r += "-- Schema: %s" % (self.Name)
            r += SEP
            r += SEP
            r += "-- %s" % (self.DDL_Drop())
            r += SEP
            r += SEP
            r += self.DDL_Create()
            r += SEP
            r += SEP
            r += self.Owner.DDL_Create()
            r += SEP
            r += self.ACL.DDL_Create()
            r += SEP
            r += self.Comment.DDL_Create()
            r += SEP
        else:
            r += "-- Schema: %s" % (self.Name)
            r += SEP
            r += SEP
            r += "-- %s" % (self.DDL_Drop())
            r += SEP
            r += SEP
            r += self.DDL_Create()
            r += SEP
            r += SEP
            r += self.Owner.DDL_Create()
            r += SEP
            r += SEP
            r += self.ACL.DDL_Create()
            r += SEP
            r += SEP

            if self.Comment.IsExists:
                r += self.Comment.DDL_Create()
                r += SEP

        return r.strip() + SEP
