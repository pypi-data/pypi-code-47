#!/usr/bin/python
# -*- coding: utf-8 -*-

from pg_metadata._System import SEP

class Owner():
    def __init__(self, instance_type, instance_name, owner_name, ddl_style=""):
        self.InstanceType = instance_type or ""
        self.InstanceType = self.InstanceType.strip().upper()
        assert len(self.InstanceType) > 0

        self.ObjectType = ("%s_OWNER" % (self.InstanceType)).strip().upper()

        self.InstanceName = instance_name or ""
        self.InstanceName = self.InstanceName.strip()
        assert len(self.InstanceName) > 0

        self.Owner = owner_name or ""
        self.Owner = self.Owner.strip()
        assert len(self.Owner) > 0

        self.DDLStyle = ddl_style

    def __str__(self):
        return "%s -> %s -> %s" % (self.InstanceType, self.InstanceName, self.Owner)

    def DDL_Create(self):
        r = ""
        if self.DDLStyle == "pgadmin3":
            r += "ALTER %s %s" % (self.InstanceType, self.InstanceName)
            r += SEP
            r += "  OWNER TO %s;" % (self.Owner)
        else:
            r += "ALTER %s %s OWNER TO %s;" % (self.InstanceType, self.InstanceName, self.Owner)
        return r
