import functools
import inspect
import os
import sys
from typing import List, Dict

from loguru import logger

from simple_test_generator.common import get_test_data_filename
from simple_test_generator.constants import serialisation_type, test_data_directory, filename_count_limit

invocation_limit_per_function = int(os.environ.get('PYTESTGEN_TEST_CASE_COUNT_PER_FUNCTION', '5'))
manual_start_record = 'PYTESTGEN_MANUAL_START_RECORD' in os.environ
# TODO: use a default test directory where to place test_pytestgen_cases, could check if test, testing or tests exists and use that.


def fn_description(f):
    return f'{f.__module__}.{f.__qualname__}'


def log_call(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        logger.debug(f'Entering {f}')
        return_value = f(*args, **kwargs)
        logger.debug(f'Exiting {f}')

        return return_value

    return wrapper


def log_error(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger.error(f'Error in {f} with {args[:2]}: {e}, skipping test cases for function.')

    return wrapper


@log_call
def group_by_function(invocations: List) -> Dict[object, List]:
    result = {}
    for invocation in invocations:
        f = invocation['f']
        if f not in result:
            result[f] = []
        if len(result[f]) < invocation_limit_per_function:
            result[f].append(invocation)
    return result


def is_site_package(module):
    return 'site-packages' in (get_dict(module).get('__file__') or {})


def exclude_paths(module):
    return get_dict(module).get('__file__')


def exclude_importers(module):
    loader = get_dict(module).get('__loader__')
    loader_type = type(loader)
    if hasattr(loader_type, '__name__'):
        name = loader_type.__name__
    elif hasattr(loader, 'name'):
        name = loader.name
    if loader:
        qualified_name = loader_type.__module__ + '.' + name
    else:
        qualified_name = ''
    return qualified_name.endswith('._SixMetaPathImporter')


def get_name(module):
    return module.__name__ if hasattr(module, '__name__') else ''


def is_system_package(module):
    from importlib._bootstrap import BuiltinImporter, FrozenImporter

    dict__ = get_dict(module)
    loader = dict__.get('__loader__')
    name__ = get_name(module)
    return (
        loader in [BuiltinImporter, FrozenImporter]
        or (
            hasattr(module, '__file__')
            and (module.__file__ is not None)
            and f"python{sys.version_info.major}.{sys.version_info.minor}/{(module.__package__ or '').replace('.', '/')}"
            in module.__file__
        )
        or name__.startswith('typing.')
    )


def get_dict(module):
    if hasattr(module, '__dict__'):
        return module.__dict__
    return {}
    # return get_dict(get_module(module)) or {}


def get_module(name):
    return sys.modules.get(name)


def get_loaded_modules():
    import sys

    all_modules = []
    for name, module in sys.modules.items():
        all_modules.append((name, module))
    return all_modules


def singleton(cls):
    obj = cls()
    # Always return the same object
    cls.__new__ = staticmethod(lambda cls: obj)
    # Disable __init__
    try:
        del cls.__init__
    except AttributeError:
        pass
    return cls


def save_example_script():
    with open('../test_pytestgen_cases.py', 'w') as f:
        f.write(
            f"""
def pytest_generate_tests(metafunc):
    ""\"This should probably be placed in conftest.py\"""
    from simple_test_generator import parametrize_stg_tests

    parametrize_stg_tests(metafunc)


def test_simple_test_generator_test_cases(fn, args, kwargs, expected):
    ""\"See {test_data_directory}{os.sep} directory for test cases\"""
    assert fn(*args, **kwargs) == expected
"""
        )


def save_test_data(invocation_group):
    for fn, invocations in invocation_group.items():
        fn_name = fn.__name__
        module = inspect.getmodule(fn)
        module_name = module.__file__
        if os.sep in module_name:
            module_name = module_name[len(os.getcwd()) + 1 :]
        parameters = inspect.signature(fn).parameters
        argnames = list(parameters.keys())
        test_cases = [{'args': x['args'], 'kwargs': x['kwargs'], 'expected': x['return_value']} for x in invocations]

        write_data_file(module_name, fn_name, test_cases, argnames)


def print_invocation_group_summary(group):
    for fn, invocations in group.items():
        logger.info(f'{fn.__module__}.{fn} got {len(invocations)} invocations')


@singleton
class Recorder:
    def __init__(self):
        logger.debug('creating instance of recorder')
        self.invocations = []
        if not manual_start_record:
            self.bootstrap()

    def add_invocation(self, return_value, f, args, kwargs):
        i = {'return_value': return_value, 'f': f, 'args': args, 'kwargs': kwargs}
        self.invocations.append(i)

    def __enter__(self):
        if manual_start_record:
            self.bootstrap()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exit()

    def edit_functions(self, items, module):
        for fn_name, fn in items:
            if fn == self.edit_functions:
                continue
            fn_module = get_module(fn.__module__)
            if not self.is_module_allowed(fn_module):
                logger.trace(f'skipping {fn_module}.{fn}')
                continue
            # logger.debug(get_dict(fn.__module__))
            logger.debug(f'editing {fn_name} {module} ({fn.__module__}).{fn}')
            new_item = self.mergeFunctionMetadata(fn, self.record_test_data(fn))
            setattr(module, fn.__name__, new_item)

    def mergeFunctionMetadata(self, f, g):
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

    def record_test_data(self, f):
        this = self
        if f in [self.record_test_data]:
            return f

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            # print('wrapped', f)
            return_value = f(*args, **kwargs)

            this.add_invocation(return_value, f, args, kwargs)
            return return_value

        return wrapper

    def bootstrap(self):
        for name, module in get_loaded_modules():
            # TODO: time, importlib, etc should not be allowed, /local/lib/python3.8/, tests/conftest.py, eclude all under tests/?, in __. ?, mock.*, tests.*
            #  module __main__ from setup.py ?
            # pytest_*,  : what if testing the pytest project itself?
            logger.debug(f'loading {name}')
            try:
                items = inspect.getmembers(module, inspect.isfunction)
            except Exception as e:
                # I saw this could happen when in debug mode
                logger.warning(f'Failed getting members for module {module}, skipping')
                logger.error(e)
                continue
            if not self.is_module_allowed(module):
                continue
            logger.debug(f'allowing module {module}')
            self.edit_functions(items, module)

        logger.debug('Start recording invocations')

    def is_module_allowed(self, module):
        exclude_site_package = True
        exclude_system_package = True
        module_name = get_name(module)
        if 'simple_test_generator' in module_name:
            logger.trace('Excluding the recorder itself')
            return
        if 'pytest' in module_name:
            logger.trace('Excluding pytest and its plugins')
            return
        if 'pydev' in module_name or 'py.builtin' in module_name:
            logger.trace('Excluding debugger modules')
            return
        if exclude_site_package and is_site_package(module):
            logger.trace(f'excluding site package {module}')
            return
        if exclude_importers(module):
            logger.trace(f'excluding importer {module}')
            return
        if exclude_system_package and is_system_package(module):
            logger.trace(f'excluding system module {module}')
            return
        return True

    def exit(self):
        logger.debug(f'Stopped recording invocations, got {len(self.invocations)} of them.')
        invocation_group = group_by_function(self.invocations)
        print_invocation_group_summary(invocation_group)
        save_example_script()
        save_test_data(invocation_group)


@log_error
def write_data_file(module_name, function_name, test_cases, argnames):
    if not test_cases:
        return
    subdir = f'{module_name}/{function_name}'
    create_directory(subdir)

    success = False
    for i in range(filename_count_limit):
        filename = get_test_data_filename(subdir, f'{i+1:02}')
        if os.path.exists(filename):
            logger.trace(f'{filename} already exists, skipping.')
            continue
        contents = serialise(argnames, test_cases)
        with open(filename, 'w') as f:
            f.write(contents)
            success = True
            break
    if not success:
        logger.error(
            f'Could not save test data for function {module_name}.{function_name}, e.g at {filename}. Merge existing test case files or delete them and try again.'
        )


def serialise(argnames, test_cases):
    if serialisation_type == 'yaml':
        fn = serialise_yaml
    elif serialisation_type == 'json':
        fn = serialise_json
    return fn(argnames, test_cases)


def serialise_json(argnames, test_cases):
    import jsonpickle as json

    return json.dumps({'test_cases': test_cases, 'argnames': argnames})


def serialise_yaml(argnames, test_cases):
    import yaml

    return yaml.dump({'test_cases': test_cases, 'argnames': argnames}, Dumper=yaml.SafeDumper)


def create_directory(sub_dir):
    from os import makedirs

    try:
        makedirs(f'{test_data_directory}{os.sep}{sub_dir}')
    except:
        pass


@log_call
def print_results(by_time):
    for item in by_time:
        logger.info(fn_description(item[0]) + f',invoked={item[2]} times, total={item[1] / 1_000_000}ms')
