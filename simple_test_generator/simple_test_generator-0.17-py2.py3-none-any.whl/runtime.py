import functools
import os
from glob import glob

import inspect
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


def mergeFunctionMetadata(f, g):
    # this function was copied from Twisted core, https://github.com/racker/python-twisted-core
    # licence notice in file ../LICENCE-Twisted-core
    """
    Overwrite C{g}'s name and docstring with values from C{f}.  Update
    C{g}'s instance dictionary with C{f}'s.
    To use this function safely you must use the return value. In Python 2.3,
    L{mergeFunctionMetadata} will create a new function. In later versions of
    Python, C{g} will be mutated and returned.
    @return: A function that has C{g}'s behavior and metadata merged from
        C{f}.
    """
    try:
        g.__name__ = f.__name__
    except TypeError:
        try:
            import types

            merged = types.FunctionType(
                g.func_code, g.func_globals, f.__name__, inspect.getargspec(g)[-1], g.func_closure
            )
        except TypeError:
            pass
    else:
        merged = g
    try:
        merged.__doc__ = f.__doc__
    except (TypeError, AttributeError):
        pass
    try:
        merged.__dict__.update(g.__dict__)
        merged.__dict__.update(f.__dict__)
    except (TypeError, AttributeError):
        pass
    merged.__module__ = f.__module__
    return merged


def transform_function(f):
    from types import GeneratorType

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return_value = f(*args, **kwargs)
        if isinstance(return_value, GeneratorType):
            return list(return_value)
        return return_value

    return wrapper


def load_data_file(module_directory, function_name) -> List:
    from simple_test_generator import get_test_data_filename

    cases = []
    for i in range(filename_count_limit):
        filename = get_test_data_filename(f'{module_directory}/{function_name}', f'{i + 1:02}')
        try:
            with open(filename, 'r') as f:
                data = deserialise(f)
        except:
            continue
        for item in data['test_cases']:
            case = Scenario(data['argnames'], item['args'], item['kwargs'], item['expected'])
            cases.append(case)
    from importlib import import_module

    if module_directory.endswith('.py'):
        module_directory = module_directory[: -len('.py')]
    split = module_directory.split(os.sep)
    # module = import_module(split[1][: -len('.py')], split[0])
    # module = import_module(module_name.replace(os.sep, '.'), package)
    module = import_module('.'.join(split))
    # TODO: find a better way to load modules, e.g by saving import paths when recording
    fn = getattr(module, function_name)

    new_item = mergeFunctionMetadata(fn, transform_function(fn))
    setattr(module, fn.__name__, new_item)
    return [(new_item, x.args, x.kwargs, x.expected) for x in cases]


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
        module_directory = sep.join(split[2:-2])
        index_length = 2  # e.g 00, 01, ...
        function_name = split[-2]
        test_data = load_data_file(module_directory, function_name)
        ids = [f'{module_directory}-{function_name}'] * len(test_data)
        all_test_data.extend(test_data)
        all_ids.extend(ids)
    metafunc.parametrize(['fn', 'args', 'kwargs', 'expected'], all_test_data, ids=all_ids)
