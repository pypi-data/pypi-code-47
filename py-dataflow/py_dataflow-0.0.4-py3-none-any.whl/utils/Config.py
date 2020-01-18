# -*- coding: utf-8 -*-

import re
import sys
import json
import yaml
from os.path import basename, dirname, isfile


class Config():
    dir = None
    type = None
    conf = {}
    script = None
    conf_file = None

    def __init__(self, conf_file=None):
        try:
            self.script = json.loads(sys.argv[0])["type"]

        except Exception as e:
            self.script = sys.argv[0]

        # self.dir = dirname(self.script)
        self.dir = dirname(__file__)
        self.type = basename(self.script)

        if conf_file:
            self.conf_file = conf_file
        else:
            self.conf_file = self.dir + \
                             "/../config/" + \
                             re.sub(r"py$", "yml", self.type, 1)

        try:
            project_conf_file = self.dir + "/../config/conf.yml"
            if isfile(project_conf_file):
                stream = open(project_conf_file, "r")
                self.conf = yaml.load(stream)
                stream.close()

            if isfile(self.conf_file):
                stream = open(self.conf_file, "r")
                self.conf.update(yaml.load(stream))
                stream.close()

            if len(self.conf) == 0:
                raise NoConfig(project_conf_file + " or " + self.conf_file)

        except Exception as e:
            print >> sys.stderr, str(e)


class NoConfig(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)