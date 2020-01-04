import configparser

from config_file.parsers.base_parser import BaseParser, ParsingError


class IniParser(BaseParser):

    def __init__(self):
        pass

    @staticmethod
    def __value_is_blank(line):
        if line.rfind(":") != -1:
            key, value = line.split(":")
        elif line.rfind("=") != -1:
            key, value = line.split("=")
        else:
            raise ParsingError("INI Parser expects keys and values to be separated by = or :")

        return value == "" or value.isspace()