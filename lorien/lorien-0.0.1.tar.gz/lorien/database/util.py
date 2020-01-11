"""
The utilities of database manipulations.
"""
from typing import Any, Dict, List, Tuple, Union

from tvm.autotvm.task import Task
from tvm.autotvm.task.space import ConfigEntity

from ..logger import get_logger

log = get_logger('DB-Util')


def gen_primary_key(task: Task) -> str:
    """Generate the unique key of a given AutoTVM task as the database primary key.
    FIXME: Support the op library other than TOPI.

    Parameters
    ----------
    task: Task
        The AutoTVM task.

    Returns
    ------
    key: str
        Generate and return the string key.
    """
    # Task name
    primary_key = task.name

    # Arguments
    for arg in task.args:
        serialized_arg = str(arg).replace('(', '_').replace(')', '_') \
                                 .replace('[', '_').replace(']', '_') \
                                 .replace(' ', '').replace('\'', '').replace(',', '_')
        primary_key += '#{}'.format(serialized_arg)

    return primary_key


def parse_target(target: str) -> Tuple[str, str]:
    """Parse TVM target and figure out our target (e.g., llvm, cuda) and platform.
    The platform is defined as the flag specified in TVM targets.
    For example, the platform of the TVM target "llvm -mcpu=core-avx2" is "-mcpu=core-avx2".

    Parameters
    ----------
    target: str
        The TVM target string.

    Returns
    -------
    target_n_platform: Tuple[str, str]
        The target and platform of the task. Note that platform will be " " if no flag
        is specified in the TVM target, because DynamoDB does not allow empty strings.
    """
    tokens = target.split(' ')
    if len(tokens) == 1:  # No platform.
        return (target, ' ')
    if len(tokens) == 2:
        return (tokens[0], tokens[1])
    raise RuntimeError('Unrecognized TVM target: %s' % target)


def convert_to_db_list(orig_list: Union[Tuple[Any, ...], List[Any]]) -> Dict[str, Any]:
    """Convert a list to the DynamoDB list type.
    Note: There is no tuple type in DynamoDB so we will also convert tuples to "L" type,
    which is also a list.

    Parameters
    ----------
    orig_list: List[Any]
        The native list.

    Returns
    -------
    new_list: Dict[str, Any]
        The DynamoDB list: {'L': [<list elements>]}.
    """
    new_list: List[Any] = []
    for elt in orig_list:
        if isinstance(elt, str):
            new_list.append({'S': elt})
        elif isinstance(elt, (int, float)):
            new_list.append({'N': str(elt)})
        elif isinstance(elt, (list, tuple)):
            new_list.append(convert_to_db_list(elt))
        elif isinstance(elt, dict):
            new_list.append(convert_to_db_dict(elt))
        elif elt is None:
            new_list.append({'S': 'None'})
        else:
            raise RuntimeError('Cannot convert %s (%s)' % (str(elt), type(elt)))

    return {'L': new_list}


def convert_to_db_dict(orig_dict: Dict[str, Any]) -> Dict[str, Any]:
    """Convert a dict to the DynamoDB dict form.

    Parameters
    ----------
    orig_dict: Dict[str, Any]
        The native dict.

    Returns
    -------
    new_dict: Dict[str, Any]
        The DynamoDB dict: {'M': {<dict elements>}}.
    """
    new_dict: Dict[str, Any] = {}
    for key, val in orig_dict.items():
        if isinstance(val, str):
            new_dict[key] = {'S': val}
        elif isinstance(val, (int, float)):
            new_dict[key] = {'N': str(val)}
        elif isinstance(val, (list, tuple)):
            new_dict[key] = convert_to_db_list(val)
        elif isinstance(val, dict):
            new_dict[key] = convert_to_db_dict(val)
        elif val is None:
            new_dict[key] = {'S': 'None'}
        else:
            raise RuntimeError('Cnanot convert %s (%s)' % (str(val), type(val)))

    return {'M': new_dict}


def convert_to_list(db_list: Dict[str, Any]) -> List[Any]:
    """Convert a DynamoDB list to a native list.

    Parameters
    ----------
    db_list: Dict[str, Any]
        A DynamoDB list: {'L': [<list elements>]}.

    Returns
    -------
    new_list: List[Any]
        A native list.
    """
    if 'L' not in db_list:
        raise RuntimeError('Not a DynamoDB list: %s' % (str(db_list)))

    new_list: List[Any] = []
    for elt in db_list['L']:
        assert len(elt) == 1
        dtype = list(elt.keys())[0]

        if dtype == 'S':
            new_list.append(str(elt[dtype]) if elt[dtype] != 'None' else None)
        elif dtype == 'N':
            new_list.append(float(elt[dtype]))
        elif dtype == 'L':
            new_list.append(convert_to_list(elt))
        elif dtype == 'M':
            new_list.append(convert_to_dict(elt))
        else:
            raise RuntimeError('Cannot convert %s (%s)' % (str(elt), dtype))

    return new_list


def convert_to_dict(db_dict: Dict[str, Any]) -> Dict[str, Any]:
    """Convert a DynamoDB dict to a native dict.

    Parameters
    ----------
    db_dict: Dict[str, Any]
        A DynamoDB dict: {'M': {<dict elements>}}.

    Returns
    -------
    new_dict: Dict[str, Any]
        A native dict.
    """
    if 'M' not in db_dict:
        raise RuntimeError('Not a DynamoDB dict: %s' % str(db_dict))

    new_dict: Dict[str, Any] = {}
    for key, elt in db_dict['M'].items():
        dtype = list(elt.keys())[0]

        if dtype == 'S':
            new_dict[key] = str(elt[dtype]) if elt[dtype] != 'None' else None
        elif dtype == 'N':
            new_dict[key] = float(elt[dtype])
        elif dtype == 'L':
            new_dict[key] = convert_to_list(elt)
        elif dtype == 'M':
            new_dict[key] = convert_to_dict(elt)
        else:
            raise RuntimeError('Cannot convert %s (%s)' % (str(elt), dtype))

    return new_dict


def serialize_sche_config(sche_config: ConfigEntity) -> str:
    """Serialize a schedule config to a string.

    Parameters
    ----------
    sche_config: ConfigEntity
        The AutoTVM config entity.

    Returns
    -------
    ret: str
        The serialized schedule config string.
    """

    ret = ''
    for name, val in sche_config._entity_map.items():
        if isinstance(val, list):
            ret += '_{0}_{1}'.format(name, ','.join([str(e) for e in val]))
        else:
            ret += '_{0}_{1}'.format(name, val)
    return ret
