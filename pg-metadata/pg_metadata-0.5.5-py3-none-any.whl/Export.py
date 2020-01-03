#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from pg_metadata._System import SEP, CheckPath

class Export():
    def __init__(self, name, type, parent, create, drop, is_sep_file):
        assert name is not None
        assert isinstance(name, str)
        assert len(name) > 0
        self.Name = name

        assert type is not None
        assert isinstance(type, str)
        assert len(type) > 0
        self.Type = type

        self.Parent = parent

        assert create is not None
        assert isinstance(create, str)
        assert len(create) > 0
        self.Create = create

        assert drop is not None
        assert isinstance(drop, str)
        assert len(drop) > 0
        self.Drop = drop

        self.IsSeparateFile = is_sep_file

    def WriteCreate(self, path):
        """
            Write CREATE script to file
            @param path: Path to folder
        """
        # Try to write as separate file
        self.WriteSeparateFile(path)

        file_name = "%s_1_insert.sql" % (self.Type)
        path = "/".join([path, file_name])

        with open(path, "a", encoding="utf8") as wf:
            wf.write(self.Create)
            wf.write(SEP)
            wf.write(SEP)

        print("CREATE", self.Name)

    def WriteDrop(self, path):
        """
            Write DROP script to file
            @param path: Path to folder
        """
        file_name = "%s_3_delete.sql" % (self.Type)
        path = "/".join([path, file_name])

        with open(path, "a", encoding="utf8") as wf:
            wf.write(self.Drop)
            wf.write(SEP)
            wf.write(SEP)

        print("DROP", self.Name)

    def WriteSeparateFile(self, path):
        """
            Write CREATE script as separate file
            @param path: Path to folder
        """
        if not self.IsSeparateFile:
            return

        path = "/".join([path, self.Type.lower()])
        CheckPath(path)

        file_name = self.Name.replace("%s_" % (self.Type.lower()), "")
        file_name = "/".join([path, "%s.sql" % (file_name)])

        with open(file_name, "w", encoding="utf8") as wf:
            wf.write(self.Create)
