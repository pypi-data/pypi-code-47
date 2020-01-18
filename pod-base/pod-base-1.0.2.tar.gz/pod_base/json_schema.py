try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

import json


class JsonSchemaRules(object):
    __slots__ = "__json_schema"

    def __init__(self, file_path):
        self.__load_json_schema(file_path)

    def __load_json_schema(self, file_path):
        if file_path.__len__() == 0:
            self.__json_schema = {}
            return

        try:
            with open(file_path) as schema:
                self.__json_schema = json.load(schema)
        except FileNotFoundError:
            raise FileNotFoundError("file {0} not found".format(file_path))

    def get_rules(self, schema_name):
        if schema_name in self.__json_schema:
            return self.__json_schema[schema_name]

        return {}
