#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Properties:

    def __init__(self, file_name):
        self.fileName = file_name
        self.properties = {}

        pro_file = None
        try:
            pro_file = open(self.fileName, 'r')
            for line in pro_file.readlines():
                line = line.strip().replace('/n', '')
                if line.find('=') > 0 and not line.startswith('#'):
                    strs = line.split('=')
                    self.properties[strs[0].strip()] = strs[1].strip()
        except Exception as e:
            print("read file is error - %s" % e)
        finally:
            if pro_file is not None:
                pro_file.close()

    def has_key(self, key = ''):
        return key in self.properties

    def get(self, key = '', default_value = ''):
        if key in self.properties:
            return self.properties[key]
        return default_value
