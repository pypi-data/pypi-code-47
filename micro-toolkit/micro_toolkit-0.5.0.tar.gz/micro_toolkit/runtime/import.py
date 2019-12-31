from typing import Type, Text, Any


def class_from_module_path(module_path: Text) -> Type[Any]:
    # copied from rasa_nlu (https://github.com/RasaHQ/rasa) @ rasa_nlu/utils/__init__.py
    """Given the module name and path of a class, tries to retrieve the class.

    The loaded class can be used to instantiate new objects. """
    import importlib

    # load the module, will raise ImportError if module cannot be loaded
    if "." in module_path:
        module_name, _, class_name = module_path.rpartition('.')
        m = importlib.import_module(module_name)
        # get the class, will raise AttributeError if class cannot be found
        return getattr(m, class_name)
    else:
        return globals()[module_path]
