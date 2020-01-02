#!/usr/bin/python
# -*- coding: utf-8 -*-

from pg_metadata._System import SEP
from pg_metadata.ACL     import ACL
from pg_metadata.Owner   import Owner
from pg_metadata.Comment import Comment

QUERY_FOREIGN_SERVER = """
    select
        s.oid,
        s.srvname as server_name,
        w.fdwname as fdw_name,
        o.rolname as owner_name,
        s.srvoptions as options,
        s.srvacl::varchar[],
        obj_description(s.oid) AS comment
    from pg_foreign_server s
    join pg_roles o on
        o.oid = s.srvowner
    join pg_foreign_data_wrapper w on
        w.oid = s.srvfdw
"""

class ForeignServer():
    def __init__(self, row={}, ddl_style=""):
        assert row is not None
        assert isinstance(row, dict)
        assert len(row.keys()) > 0

        self.Type = "SERVER"

        self.Schema = "_foreign"
        self.Folder = "server"

        self.Name = row.get('server_name')
        assert self.Name is not None
        self.Name = self.Name.strip().lower()
        assert len(self.Name) > 0

        self.FDW = row.get('fdw_name')
        assert self.FDW is not None
        self.FDW = self.FDW.strip().lower()
        assert len(self.FDW) > 0

        self.Owner = row.get('owner_name')
        assert self.Owner is not None
        self.Owner = self.Owner.strip()
        assert len(self.Owner) > 0

        self.Comment = row.get("comment")

        self.Options = row.get("options")

        self.DDLStyle = ddl_style

        self.Owner = Owner(
            self.Type,
            self.Name,
            row.get("owner_name"),
            self.DDLStyle
        )

        self.Comment = Comment(
            self.Type,
            self.Name,
            row.get("comment"),
            self.DDLStyle
        )

        self.ACL = ACL(
            "FOREIGN SERVER",
            self.Name,
            self.Owner.Owner,
            row.get("relacl"),
            self.DDLStyle
        )

    def __str__(self):
        return self.Name

    def QueryRemove(self):
        return 'DROP SERVER IF EXISTS %s;' % (self.Name)

    def QueryDDL(self):
        r = ""
        r += "-- Server: %s" % (self.Name)
        r += SEP
        r += SEP
        r += "-- %s" % (self.QueryRemove())
        r += SEP
        r += SEP
        r += "CREATE SERVER %s" % (self.Name)
        r += SEP
        r += "FOREIGN DATA WRAPPER %s" % (self.FDW)
        r += SEP
        r += "OPTIONS("
        r += SEP
        r += self.QueryOptions()
        r += SEP
        r += ");"
        r += SEP
        r += SEP
        r += self.Owner.DDL_Create()
        r += SEP
        r += self.ACL.DDL_Create()
        r += SEP

        if self.Comment.IsExists:
            r += self.Comment.DDL_Create()
            r += SEP

        return r.strip() + SEP

    def QueryOptions(self):
        result = []

        for o in sorted(self.Options):
            o = o.split("=")
            if len(o) != 2:
                continue
            result.append("    %s = '%s'" % (o[0], o[1]))

        separator = ",%s" % (SEP)
        return separator.join(result)
