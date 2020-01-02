#!/usr/bin/python
# -*- coding: utf-8 -*-

from pg_metadata._System import SEP

class Comment():
    def __init__(self, instance_type, instance_name, comment, ddl_style=""):
        self.InstanceType = instance_type or ""
        self.InstanceType = self.InstanceType.strip().upper()
        assert len(self.InstanceType) > 0

        self.ObjectType = ("%s_COMMENT" % (self.InstanceType)).strip().upper()

        self.InstanceName = instance_name or ""
        self.InstanceName = self.InstanceName.strip()
        assert len(self.InstanceName) > 0

        self.Comment = comment or ""
        self.Comment = self.Comment.strip()

        self.IsExists = len(self.Comment) > 0

        self.DDLStyle = ddl_style

    def __str__(self):
        return "%s -> %s -> %s" % (self.InstanceType, self.InstanceName, self.Comment)

    def DDL_Create(self):
        r = ""
        if len(self.Comment) > 0:
            if self.DDLStyle == "pgadmin3":
                r += "COMMENT ON %s %s" % (self.InstanceType, self.InstanceName)
                r += SEP
                r += "  IS '%s';" % (self.Comment)
            else:
                r += "COMMENT ON %s %s IS '%s';" % (self.InstanceType, self.InstanceName, self.Comment)
        return r

    def DDL_Drop(self):
        r = ""
        if self.DDLStyle == "pgadmin3":
            r += "COMMENT ON %s '%s'" % (self.InstanceType, self.InstanceName)
            r += SEP
            r += "  IS '';"
        else:
            r += "COMMENT ON %s %s IS '';" % (self.InstanceType, self.InstanceName)
        return r
