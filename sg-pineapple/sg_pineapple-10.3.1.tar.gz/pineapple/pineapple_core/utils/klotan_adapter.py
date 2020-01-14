from klotan import criterias
from typing import Any, Dict, List, Optional


optional_class = Optional[str]


def type_list_to_klotan_list(type_list: List[Any]) -> List[Any]:
    """Transforms recursively a list of types to a list of klotan criterias

    Parameters
    ==========
    type_list: List[Any]
        List of types to transform into klotan criterias

    Returns
    =======
    List[Any]:
        Copy of the list sent in parameter with types transformed into klotan criterias
    """
    new_list = []
    for value in type_list:
        # Checking if the class starts with typing,
        # as the class name of Optional changes between versions of python
        if isinstance(value, type) or str(value.__class__) == str(optional_class.__class__):
            new_list.append(criterias.is_type(value))
        elif isinstance(value, dict):
            new_list.append(type_dict_to_klotan_dict(value))
        elif isinstance(value, (list, tuple)):
            new_list.append(type_list_to_klotan_list(value))
        elif callable(value):
            pass
        else:
            raise RuntimeError(
                f"Non-klotan item in list {value}, expected (type, list, dict, tuple, callable)"
            )
    return new_list


def type_dict_to_klotan_dict(type_dict: Dict[Any, Any]) -> Dict[Any, Any]:
    new_dict = {}
    for key, value in type_dict.items():
        # Checking if the class starts with typing,
        # as the class name of Optional changes between versions of python
        if isinstance(value, type) or str(value.__class__) == str(optional_class.__class__):
            new_dict[key] = criterias.is_type(value)
        elif isinstance(value, (list, tuple)):
            new_dict[key] = type_list_to_klotan_list(value)
        elif isinstance(value, dict):
            new_dict[key] = type_dict_to_klotan_dict(value)
        elif callable(value):
            pass
        else:
            raise RuntimeError(
                f"Non-klotan item in dict {value}, expected (type, list, dict, tuple, callable)"
            )
    return new_dict
