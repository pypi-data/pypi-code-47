import functools
import inspect
import sys
from time import perf_counter_ns
from typing import List, Dict

from loguru import logger
from recursive_decorator import recursive_decorator


def fn_description(f):
    return f'{f.__module__}.{f.__qualname__}'


class Invocation:
    def __init__(self, start, end, result, f, args, kwargs):
        self.start = start
        self.end = end
        self.result = result
        self.f = f
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        return f'Invocation(duration={self.duration}s, fn={fn_description(self.f)}'

    @property
    def duration(self):
        return self.end - self.start


def sort_fn(invocation):
    return invocation.end - invocation.start


def log_call(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        logger.debug(f'Entering {f}')
        result = f(*args, **kwargs)
        logger.debug(f'Exiting {f}')

        return result

    return wrapper


@log_call
def sort_invocations_by_individual_time(invocations):
    return sorted(invocations, key=sort_fn, reverse=True)


def duration(invocation):
    return invocation['end'] - invocation['start']


@log_call
def sort_invocations_by_function_time(group):
    name_speed_tuple_list = []
    for fn_name, invocations in group.items():
        total_per_function = sum(map(lambda x: duration(x), invocations))
        name_speed_tuple_list.append((fn_name, total_per_function, len(invocations)))
    return sorted(name_speed_tuple_list, key=lambda x: x[1], reverse=True)


@log_call
def group_by_function(invocations: List[Invocation]) -> Dict[object, List[Invocation]]:
    result = {}
    for invocation in invocations:
        f = invocation['f']
        if f not in result:
            result[f] = []
        result[f].append(invocation)
    return result


def is_site_package(module):
    return 'site-packages' in (module.__dict__.get('__file__') or {})


def exclude_paths(module):
    return module.__dict__.get('__file__')


def exclude_importers(module):
    loader = module.__dict__.get('__loader__')
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


def is_system_package(module):
    from importlib._bootstrap import BuiltinImporter

    loader = module.__dict__.get('__loader__')
    return (
        loader in [BuiltinImporter]
        or (
            hasattr(module, '__file__')
            and f"python{sys.version_info.major}.{sys.version_info.minor}/{(module.__package__ or '').replace('.', '/')}"
            in module.__file__
        )
        or module.__name__.startswith('typing.')
    )


def get_loaded_modules():
    import sys

    all_modules = []
    for name, module in sys.modules.items():
        all_modules.append((name, module))
    return all_modules


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


def time_fn():
    return perf_counter_ns()


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


@singleton
class Profiler:
    def __init__(self):
        logger.debug('creating instance of profiler')
        self.invocations = []

    def add_invocation(self, start, end, result, f):
        # i = Invocation(start, end, result, f, args, kwargs)
        i = {'start': start, 'end': end, 'result': result, 'f': f}
        self.invocations.append(i)

    def __enter__(self):
        bootstrap()
        logger.debug('Start recording invocations')

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.debug(f'stopped recording invocations, got {len(self.invocations)} of them.')

        invocation_group = group_by_function(self.invocations)
        by_time = sort_invocations_by_function_time(invocation_group)
        by_time = limit_results(by_time)
        print_results(by_time)


@recursive_decorator
def profile_recursive(f):
    return profile(f)


def profile(f):
    if f in [time_fn, profile]:
        return f

    # print('in profile', f)

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        # print('wrapped', f)
        start = time_fn()
        result = f(*args, **kwargs)
        end = time_fn()

        Profiler().add_invocation(start, end, result, f)
        return result

    return wrapper


def edit_functions(items, module):
    for fn_name, fn in items:
        if fn == edit_functions:
            continue
        # print('editing', fn_name, fn)
        new_item = mergeFunctionMetadata(fn, profile(fn))
        setattr(module, fn.__name__, new_item)


def bootstrap():
    for name, module in get_loaded_modules():
        # print('loading', name)
        try:
            items = inspect.getmembers(module, inspect.isfunction)
        except Exception as e:
            # I saw this could happen when in debug mode
            logger.warning(f'Failed getting members for module {module}, skipping')
            logger.error(e)
            continue
        # if 'main' not in name:
        exclude_site_package = True
        exclude_system_package = True
        if 'simple_python_profiler' in module.__name__:
            logger.trace('Excluding the profiler itself')
            continue
        if exclude_site_package and is_site_package(module):
            logger.trace(f'excluding site package {module}')
            continue
        if exclude_importers(module):
            logger.trace(f'excluding importer {module}')
            continue
        if exclude_system_package and is_system_package(module):
            logger.trace(f'excluding system module {module}')
            continue
        logger.debug(f'allowing module {module}')
        edit_functions(items, module)


def limit_results(groups):
    return groups[:100]


@log_call
def print_results(by_time):
    for item in by_time:
        logger.info(fn_description(item[0]) + f',invoked={item[2]} times, total={item[1] / 1_000_000}ms')
