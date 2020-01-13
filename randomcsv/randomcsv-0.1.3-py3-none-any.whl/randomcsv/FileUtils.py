import os
from pathlib import Path


def write(file_name, content):
    Path(os.path.dirname(file_name)).mkdir(parents=True, exist_ok=True)
    with open(file_name, 'w') as file:
        file.write(content)


def read_line_looping(file_name, count):
    i = 0
    lines = []
    file = open(file_name, 'r')
    line = file.readline()
    if line == '':
        raise EmptyFileError(f'Error: Dictionary {file_name} seems to be empty')
    while i < count:
        lines.append(line.strip())
        i += 1
        line = file.readline()
        if line == '':
            file.close()
            file = open(file_name, 'r')
            line = file.readline()
    file.close()
    return lines


class EmptyFileError(Exception):
    pass
