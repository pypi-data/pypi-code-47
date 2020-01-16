import os
from glob import glob

from _pytest.python import Metafunc
from typing import List, TextIO

from simple_test_generator.constants import test_data_directory, serialisation_type, filename_count_limit


class Scenario:
    def __init__(self, argnames, args, kwargs, expected):
        self.argnames = argnames
        self.args = args
        self.kwargs = kwargs
        self.expected = expected


def deserialise(f):
    if serialisation_type == 'yaml':
        fn = deserialise_yaml
    elif serialisation_type == 'json':
        fn = deserialise_json
    return fn(f)


def deserialise_yaml(f: TextIO):
    import yaml

    return yaml.load(f.read(), Loader=yaml.FullLoader)


def deserialise_json(f: TextIO):
    import jsonpickle as json

    return json.loads(f.read())


def load_data_file(module_name, function_name) -> List:
    from simple_test_generator import get_test_data_filename

    cases = []
    for i in range(filename_count_limit):
        filename = get_test_data_filename(f'{module_name}/{function_name}', f'{i+1:02}')
        try:
            with open(filename, 'r') as f:
                data = deserialise(f)
        except:
            continue
        for item in data['test_cases']:
            case = Scenario(data['argnames'], item['args'], item['kwargs'], item['expected'])
            cases.append(case)
    from importlib import import_module

    if module_name.endswith('.py'):
        module_name = module_name[: -len('.py')]
    split = module_name.split(os.sep)
    # module = import_module(split[1][: -len('.py')], split[0])
    # module = import_module(module_name.replace(os.sep, '.'), package)
    module = import_module('.'.join(split))
    fn = getattr(module, function_name)
    return [(fn, x.args, x.kwargs, x.expected) for x in cases]


def parametrize_stg_tests(metafunc: Metafunc):
    if metafunc.definition.name != 'test_simple_test_generator_test_cases':
        return
    sep = os.sep
    path_list = glob(f'{test_data_directory}{sep}**{sep}*.{serialisation_type}', recursive=True)
    all_test_data = []
    all_ids = []
    for data_file_path in path_list:
        split = data_file_path.split(sep)
        file_name = split[-1]
        module_name = sep.join(split[1:-2])
        index_length = 2  # e.g 00, 01, ...
        function_name = split[-2]
        test_data = load_data_file(module_name, function_name)
        ids = [module_name + '-' + function_name] * len(test_data)
        all_test_data.extend(test_data)
        all_ids.extend(ids)
    metafunc.parametrize(['fn', 'args', 'kwargs', 'expected'], all_test_data, ids=all_ids)
