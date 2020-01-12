from collections import OrderedDict
from random import choice
from sys import argv
from os import path
import xml.dom.minidom
import xmltodict
import re

lower_ascii = 'abcdefghijklmnopqrstuvwxyz'
upper_ascii = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b_choice = [True, False]
numbers = '123456789'

is_number = re.compile('^\d$')


def randomize(value):
    if is_number.match(value) is not None:
        return choice(numbers)
    elif value == ' ':
        if choice(b_choice):
            return ' '
        else:
            return choice(lower_ascii+upper_ascii)
    elif value.islower():
        return choice(lower_ascii)
    elif value.isupper():
        return choice(upper_ascii)
    else:
        return value


def anonymize_value(value):
    if isinstance(value, str):
        return ''.join([
            randomize(c) for c in value
        ])
    return value


def transform_dico(dico, transform: callable=lambda v: v):
    return {
        key:
            transform_dico(value, transform)
            if isinstance(value, OrderedDict) or isinstance(value, dict)
            else (
                [
                    transform_dico(item, transform)
                    if isinstance(item, OrderedDict) or isinstance(item, dict)
                    else transform(value)
                    for item in value
                ]
                if isinstance(value, list)
                else transform(value)
            )
        for (key, value) in dico.items()
    }


def anonymize_dict(dico):
    return transform_dico(
        dico,
        anonymize_value
    )


def anonymize_xml_string(xml_string):
    return anonymize_dict(
        xmltodict.parse(
            xml_string
        )
    )


def anonymize_xml_file(file):
    with open(file, 'rb') as xml_file:
        return xml.dom.minidom.parseString(
             xmltodict.unparse(
                anonymize_xml_string(
                    xml_file.read()
                )
             )
        ).toprettyxml()


def main(file_path):
    if not path.exists(file_path):
        raise Exception('{0} does not exists'.format(file_path))
    print(anonymize_xml_file(file_path))


if __name__ == '__main__':
    main(argv[1])