from inspect import ismodule, isfunction, signature, Parameter
from importlib import import_module
from sys import modules
from os.path import exists, join
from os import getcwd


def __get_cur_module():
    return modules[globals()['__name__']]


def __get_module(module_name, package_path):
    if isinstance(module_name, str) and isinstance(package_path, str):
        return import_module(name=module_name, package=package_path)

    elif not isinstance(module_name, str):
        raise ValueError('Need to specify the module name!')

    elif not isinstance(package_path, str):
        raise ValueError('Need to specify the path to the module!')


def __get_function(module, func_name):
    if isinstance(func_name, str):
        return getattr(module, func_name)
    else:
        raise ValueError('Need to specify the function name!')


def __subset_dictionary(dict_, subset_keys):
    return {key: value for key, value in dict_.items() if key in subset_keys}


def get_required_parameters(func):
    """
    Return a set of parameters in <func>'s header that don't have default values

    :param func: Function Object
    :return: Set of String in <func> that don't have default values

    >>> get_required_parameters(gexec).difference({'parameters', 'func'})
    set()
    """

    return set([key for key, default_value in signature(func).parameters.items() if default_value.default is Parameter.empty])


def get_optional_parameters(func):
    """
    Return a set of parameters in <func>'s header that have default values

    :param func: Function Object
    :return: Set of String in <func> that have default values

    >>> get_optional_parameters(gexec).difference({'module', 'package_path'})
    set()
    """

    return set([key for key, default_value in signature(func).parameters.items() if default_value.default is not Parameter.empty])


def __get_valid_input(func, parameters):
    parameter_keys = set(parameters.keys())

    required_parameters = get_required_parameters(func)

    if bool(required_parameters - parameter_keys):
        raise ValueError('Missing parameters:\n{0}'.format(', '.join(required_parameters - parameter_keys)))

    all_func_keys = set(signature(func).parameters.keys())

    valid_parameter_keys = parameter_keys.intersection(all_func_keys)

    valid_parameters = __subset_dictionary(parameters, valid_parameter_keys)

    return valid_parameters


def __get_module_obj(module, package_path):
    if not isinstance(module, str):
        raise ValueError('module must be either a Module Object or a String!')

    elif not isinstance(package_path, str):
        raise ValueError('package_path must be set!')

    elif not exists(package_path):
        raise ValueError('Invalid path: "{0}"'.format(package_path))

    elif not exists(join(package_path, module + '.py')):
        raise ValueError('Module "{0}" does not exist at "{1}"!'.format(module, package_path))

    else:
        module = __get_module(module_name=module, package_path=package_path)

    return module


def __get_function_obj(func, module=None, package_path=None):
    if isinstance(func, str):
        if not ismodule(module):
            # <module> is not a Module Object

            if isinstance(package_path, str):
                module = __get_module_obj(module=module, package_path=package_path)
                func = __get_function(module=module, func_name=func)

            elif hasattr(__get_cur_module(), func):
                func = __get_function(module=__get_cur_module(), func_name=func)

            else:
                raise ValueError('If the function is not in the current module, package_path must specify the directory!')

    else:
        raise ValueError('func must be either a Function Object or a String!')

    return func


def gexec(func, parameters, module=None, package_path=None):
    """
    Executes the function <func> using the intersection of parameters between the
        function header and keys in <parameters>

    Note:
        If the func is a String and is not in the current module;
            it will try to import the module <module> in <package_path> to execute <func>

    :param func: Function Object | String
    :param parameters: Dictionary
    :param module: Module Object | String
    :param package_path: String
    :return: None | Object

    >>> gexec(func=__subset_dictionary, parameters={'dict_': {'a': 1, 'b': 2}, 'subset_keys': {'a'}})
    {'a': 1}

    >>> gexec(func='__subset_dictionary', parameters={'dict_': {'a': 1, 'b': 2}, 'subset_keys': {'a'}})
    {'a': 1}

    >>> gexec(func='__subset_dictionary', parameters={'dict_': {'a': 1, 'b': 2}, 'subset_keys': {'a'}}, \
            module='gexecute', package_path=getcwd())
    {'a': 1}

    >>> gexec(func='__subset_dictionary', \
            parameters={'dict_': {'a': 1, 'b': 2}, 'subset_keys': {'a'}, 'junk': 'shouldn\\'t show up'}, \
            module='gexecute', package_path=getcwd())
    {'a': 1}
    """

    if not isfunction(func):
        # <func> is not a Function Object
        func = __get_function_obj(func=func, module=module, package_path=package_path)

    valid_parameters = __get_valid_input(func=func, parameters=parameters)

    return func(**valid_parameters)
