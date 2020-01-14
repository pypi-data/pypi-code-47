import inspect
import json


def make_value_serializable(value):
    try:
        json.dumps(value)
        return value
    except TypeError:
        if hasattr(value, "__repr__") and not inspect.isclass(value):
            return value.__repr__()
        elif hasattr(value, "__static_repr__") and inspect.isclass(value):
            return value.__static_repr__()
        else:
            return str(value)
