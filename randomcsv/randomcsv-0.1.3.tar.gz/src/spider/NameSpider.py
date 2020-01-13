import json
import os

import requests
from pkg_resources import resource_filename

names_dictionary_file = os.path.join(resource_filename('randomcsv.resources.dictionaries', ''), 'firstNames.txt')
api_url = 'https://uinames.com/api/'


def getNamesBatch(count=500):
    response = requests.get(f'{api_url}?amount={count}')
    data = json.loads(response.text)
    return data


def print_first_names(name_dicts):
    with open(names_dictionary_file, 'w') as file:
        for name in name_dicts:
            if name['name'].strip():
                file.write(name['name'] + '\n')


if __name__ == '__main__':
    names = getNamesBatch()
    print_first_names(names)
