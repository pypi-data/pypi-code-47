"""
Workload mutation module.
"""
from copy import deepcopy
from typing import Any, Callable, Dict, List, Set, Tuple, Union

from ...logger import get_logger
from ...workload import Workload

log = get_logger('Mutator')

# The op argument type. Ex: ('TENSOR', (1, 3, 224, 224))
ArgType = List[Union[str, Tuple[int, ...]]]

# The op attribute field type. Ex: (1, 3, 224, 224)
OpAttrFieldType = Union[int, str, Tuple[int, ...]]

# Map from a Relay op name to the mutator function.
MUTATOR_TABLE: Dict[str, Callable] = {}


def register_mutator(op_name: str) -> Callable:
    """Register a mutator function.

    Parameters
    ----------
    op_name: str
        A Relay op name.

    Returns
    -------
    reg: Callable
        A callable function for registration.
    """
    def _do_reg(func: Callable):
        if op_name in MUTATOR_TABLE:
            raise RuntimeError('The mutator of op %s has been registered' % op_name)
        MUTATOR_TABLE[op_name] = func
        return func

    return _do_reg


@register_mutator('conv2d')
def mutate_conv2d(rules: Dict[str, Any], base_workload: Workload) -> List[Workload]:
    """Mutate a conv2d workload. Currently we only support kernel size mutation.

    Parameters
    ----------
    rules: Dict[str, Any]
        The mutation rules.

    base_workload: Workload
        The workload to be mutated.

    Returns
    -------
    workloads: List[Workload]
        The mutated workload list (include the original one).
    """
    def mutate_kernel_size(workload: Workload, kernel_size: List[int]):
        """Mutate the kernel size of a given workload."""

        # Map data layout.
        data_shape: Dict[str, int] = {}
        for idx, dim in enumerate(workload['args'][-2]):
            data_shape[dim] = workload['args'][0][1][idx]

        arg_list = list(workload['args'])

        # Infer kernel layout and mutate kernel size.
        if data_shape['C'] == workload['args'][1][1][1]:  # OIHW
            arg_list[1] = tuple(['TENSOR', list(arg_list[1][1][:2]) + kernel_size, arg_list[1][2]])
        elif data_shape['C'] == arg_list[1][1][2]:  # HWIO
            arg_list[1] = tuple(['TENSOR', kernel_size + list(arg_list[1][1][2:]), arg_list[1][2]])
        else:
            raise RuntimeError('Cannot infer kernel layout in workload %s' % str(workload))

        workload['args'] = tuple(arg_list)

    mutators = {'kernel_size': mutate_kernel_size}

    workload_set: Set[Workload] = set([base_workload])
    for name, options in rules.items():
        if name not in mutators:
            raise RuntimeError('Mutate %s in conv2d is not supported' % name)

        new_workload_set = set()

        mutator = mutators[name]
        for option in options:
            for workload in workload_set:
                new_workload = deepcopy(workload)
                mutator(new_workload, option)
                new_workload_set.add(new_workload)
        workload_set = new_workload_set

    return list(workload_set)
