import functools
import inspect
import os
import sys
from fnmatch import fnmatch
from os.path import abspath
from typing import List, Dict

from loguru import logger

from simple_test_generator.common import get_test_data_filename
from simple_test_generator.constants import (
    serialisation_type,
    test_data_directory,
    filename_count_limit,
    test_filename,
    test_directory,
)

invocation_limit_per_function = int(os.environ.get('PYTESTGEN_TEST_CASE_COUNT_PER_FUNCTION', '5'))
manual_start_record = 'PYTESTGEN_MANUAL_START_RECORD' in os.environ
allow_all_modules = 'PYTESTGEN_ALLOW_ALL_MODULES' in os.environ
add_modules = os.environ.get('PYTESTGEN_ADD_MODULES', '').split(',')
# TODO: option to disable recorder with env var would be useful to avoid code change between generate run, and normal run
# TODO: how to load files saved at paths like test-data/2019.1/config/plugins/python/helpers/pycharm/_jb_runner_tools.py/_parse_parametrized/01.json ?
# TODO: how to handle test files under t_generator?
# TODO: try pickling with dill to try to serialise more types, e.g functions
# TODO: how to use this with tox projects? because tox writes files in temporary virtual envs
# TODO: can we support object's methods as well?
# TODO: test with kwargs and optional parameters
# TODO: add real-world examples of running real projects with it (like pytest, httpie, jsonpickle, pytest, ansible, pipenv itself!)
# TODO: allow toggling debug logs
# TODO: show how to use with web frameworks like Django
# TODO: why not simply deepcopy function instead of merge metadata?


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
        if len(result[f]) >= invocation_limit_per_function:
            continue
        if is_function(invocation['return_value']):
            continue
        result[f].append(invocation)
    return result


def is_function(param):
    return inspect.isroutine(param)
    # import types
    #
    # return isinstance(
    #     param, (types.FunctionType, types.BuiltinFunctionType, types.MethodType, types.BuiltinMethodType)
    # )


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
    from importlib import import_module

    # import_module('__main__')
    # mod = __import__('__main__', globals(), locals(), ['Hey'], 0)
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
    with open(f'{test_directory}/{test_filename}', 'w') as f:
        f.write(
            f"""
def pytest_generate_tests(metafunc):
    ""\"This should probably be placed in conftest.py\"""
    from simple_test_generator import parametrize_stg_tests

    parametrize_stg_tests(metafunc)


def test_simple_test_generator_test_cases(fn, args, kwargs, expected):
    ""\"See {test_data_directory} directory for test cases\"""
    actual = fn(*args, **kwargs)
    assert actual == expected
"""
        )


def get_class_that_defined_method(meth):
    if inspect.ismethod(meth):
        for cls in inspect.getmro(meth.__self__.__class__):
            if cls.__dict__.get(meth.__name__) is meth:
                return cls
        meth = meth.__func__  # fallback to __qualname__ parsing
    if inspect.isfunction(meth):
        cls = getattr(inspect.getmodule(meth), meth.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0])
        if isinstance(cls, type):
            return cls
    return getattr(meth, '__objclass__', None)


def save_test_data(invocation_group):
    for fn, invocations in invocation_group.items():
        fn_name = fn.__name__
        module = inspect.getmodule(fn)
        clazz = get_class_that_defined_method(fn)
        logger.debug(f'{module}---{fn}---{clazz}')
        module_name = module.__file__
        if os.sep in module_name:
            module_name = module_name[len(os.getcwd()) + 1 :]
        parameters = inspect.signature(fn).parameters
        argnames = list(parameters.keys())

        # 'return_type': type(x['return_value']),
        test_cases = [{'args': x['args'], 'kwargs': x['kwargs'], 'expected': x['return_value']} for x in invocations]

        write_data_file(module_name, clazz, fn_name, test_cases, argnames)


def print_invocation_group_summary(group):
    for fn, invocations in group.items():
        # if fn.__name__ == '__init__':
        #   logger.debug(fn.__new__)
        logger.info(f'{fn.__module__}.{fn.__name__} got {len(invocations)} invocations')


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
                logger.trace(f'skipping {fn_module}.{fn.__name__}')
                continue
            # logger.debug(get_dict(fn.__module__))
            logger.trace(f'editing {fn_name} {module} ({fn.__module__}).{fn.__name__}')
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
        logger.trace(f)
        if f in [self.record_test_data]:
            return f

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            logger.trace(f'wrapped {f}')
            return_value = f(*args, **kwargs)

            this.add_invocation(return_value, f, args, kwargs)
            return return_value

        return wrapper

    def bootstrap(self):
        self.edit_module_level_functions()
        self.edit_module_level_classes()

        logger.debug('Start recording invocations')

    def edit_module_level_classes(self):
        for name, module in get_loaded_modules():
            logger.trace(f'loading {name}')
            if not self.is_module_allowed(module):
                continue
            try:
                classes = inspect.getmembers(module, inspect.isclass)
            except Exception as e:
                logger.warning(f'Failed getting members for module {module}, skipping')
                logger.error(e)
                continue
            # TODO: patch parent class methods
            # TODO: what if a module imported a class from another module?

            for class_name, clazz in classes:
                # clazz = class_tuple[1]
                if clazz == self.__class__:
                    continue
                fn_name: str
                for fn_name, fn in clazz.__dict__.items():
                    if not is_function(fn):
                        continue
                    if fn_name.startswith('__'):  # and fn_name != '__init__':
                        continue
                    if inspect.isbuiltin(fn):
                        continue
                    logger.trace(f'editing {class_name}.{fn_name}')
                    if hasattr(fn, '__func__'):
                        # logger.debug(dir(fn.__func__))
                        fn = fn.__func__
                    try:
                        new_item = self.mergeFunctionMetadata(fn, self.record_test_data(fn))
                    except Exception as e:
                        logger.error(e)
                        continue
                    # TODO: if not being able to recreate method properly, can check how boto3 does it
                    try:
                        setattr(clazz, fn_name, new_item)
                    except Exception as e:
                        logger.error(e)
                        continue

                # break
            # break
        # hey = Hey()
        # hey.go()
        # hey.go_class()
        # Hey.go_static()
        # sys.exit()

    def edit_module_level_functions(self):
        for name, module in get_loaded_modules():
            # TODO: time, importlib, etc should not be allowed, /local/lib/python3.8/, tests/conftest.py, eclude all under tests/?, in __. ?, mock.*, tests.*
            #  module __main__ from setup.py ?
            # pytest_*,  : what if testing the pytest project itself?
            logger.trace(f'loading {name}')
            if not self.is_module_allowed(module):
                continue
            try:
                items = inspect.getmembers(module, inspect.isfunction)
            except Exception as e:
                # I saw this could happen when in debug mode
                logger.warning(f'Failed getting members for module {module}, skipping')
                logger.error(e)
                continue
            logger.trace(f'allowing module {module}')
            self.edit_functions(items, module)

    def is_module_explicitly_allowed(self, module_name):
        for item in add_modules:
            if fnmatch(module_name, item):
                return True

    def is_module_allowed(self, module):
        if allow_all_modules:
            return True
        module_name = get_name(module)
        if self.is_module_explicitly_allowed(module_name):
            logger.debug(f'Module explicitly allowed: {module}')
            return True
        exclude_site_package = True
        exclude_system_package = True
        if 'simple_test_generator' in module_name:
            logger.trace('Excluding the recorder itself')
            return
        if module_name.startswith('py.'):
            logger.trace('Skipping modules starting with py.')
            return
        # if 'pytest' in module_name:
        #     logger.trace('Excluding pytest and its plugins')
        #     return
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
def write_data_file(module_name, clazz, function_name, test_cases, argnames):
    if not test_cases:
        return
    subdir = f'{module_name}/{function_name}'
    create_directory(subdir)

    success = False
    for i in range(filename_count_limit):
        filename = get_test_data_filename(subdir, f'{i+1:02}')
        filepath = abspath(filename)
        if os.path.exists(filepath):
            logger.trace(f'{filename} already exists, skipping.')
            continue
        contents = serialise(argnames, clazz, test_cases)
        logger.debug(f'Writing data file at {filepath}')
        with open(filepath, 'w') as f:
            f.write(contents)
            success = True
            break
    if not success:
        logger.error(
            f'Could not save test data for function {module_name}.{function_name}, e.g at {filename}. Merge existing test case files or delete them and try again.'
        )


def serialise(argnames, clazz, test_cases):
    return serialise_json(argnames, clazz, test_cases)


def serialise_json(argnames, clazz, test_cases):
    import jsonpickle as json

    return json.dumps({'test_cases': test_cases, 'argnames': argnames, 'class': clazz})


def create_directory(sub_dir):
    from os import makedirs

    try:
        makedirs(os.path.join(test_data_directory, sub_dir))
    except Exception as e:
        logger.error(e)


@log_call
def print_results(by_time):
    for item in by_time:
        logger.info(fn_description(item[0]) + f',invoked={item[2]} times, total={item[1] / 1_000_000}ms')
