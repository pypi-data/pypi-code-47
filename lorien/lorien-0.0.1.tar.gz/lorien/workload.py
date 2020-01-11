"""
Workload Definition Module.
"""
from typing import Any, Dict, List

import yaml

from tvm import autotvm
from tvm.autotvm.task.task import Task

from .logger import get_logger

log = get_logger('Workload')

# Initialize AutoTVM task extract env to register TOPI tasks.
autotvm.task.topi_integration.TaskExtractEnv()


class Workload():
    """The workload for an op.
    A workload can be used to created an AutoTVM task for tuning.
    """
    def __init__(self):
        # The template_key should be deprecated in the future.
        self._data: Dict[str, Any] = {
            'lib': 'unknown',
            'task_name': 'unknown',
            'target': 'unknown',
            'platform': '',
            'args': [],
            'template_key': ''
        }

    @classmethod
    def from_yaml(cls, yaml_str: str) -> 'Workload':
        """Create a workload from a string in YAML format.

        Parameters
        ----------
        yaml_str: str
            The YAML string of the workload.

        Returns
        -------
        workload: Workload
            The initialized workload.
        """

        yaml_data = yaml.load(yaml_str, Loader=yaml.Loader)

        workload = Workload()
        for field in workload._data:
            if field not in yaml_data:
                raise RuntimeError('Failed to create a workload because "%s" is missing in %s' %
                                   (field, yaml_str))
        workload._data = yaml_data
        return workload

    @classmethod
    def from_task(cls, task: Task) -> 'Workload':
        """Create a workload from an AutoTVM task.

        Parameters
        ----------
        task: Task
            The AutoTVM task for the workload.

        Returns
        -------
        workload: Workload
            The initialized workload.
        """

        workload = cls()

        # Initialize target, platform and task name
        if task.target is None:
            raise RuntimeError(
                'Failed to generate workload from AutoTVM task %s: No target specified' %
                str(task))
        workload._data['task_name'] = task.name
        workload._data['target'] = task.target.target_name
        workload._data['platform'] = ' '.join(task.target.options)
        workload._data['args'] = task.args
        workload._data['template_key'] = task.config_space.template_key

        # FIXME(comaniac): Support other libraries.
        workload._data['lib'] = 'topi'

        return workload

    def to_yaml(self) -> str:
        """Serialize the workload to a YAML string

        Returns
        -------
        ret: str
            The string in YAML format.
        """
        return yaml.safe_dump(self._data, default_flow_style=True, width=float('inf'))[:-1]

    def to_task(self) -> Task:
        """Create an AutoTVM task from this workload.
        Note that task may not be created if this workload violates the rules defined in
        the schedule. For example, a schedule may only work for the conv2d with 4n channel
        numbers. In this case, the task cannot be created if this workload has 18 channels.

        Returns
        -------
        task: Task
            Return the created task, or raise RuntimeError if failed.
        """

        task_args: List[Any] = [
            tuple([arg[0], tuple(arg[1]), arg[2]])
            if isinstance(arg, list) and arg[0] == 'TENSOR' else arg for arg in self._data['args']
        ]

        # Make TVM target string
        tvm_target = '{0} {1}'.format(self._data['target'], self._data['platform'])

        # Try to create task.
        try:
            if self._data['template_key']:
                template_key = self._data['template_key']
            else:
                template_key = 'direct'
            task = autotvm.task.create(self._data['task_name'],
                                       tuple(task_args),
                                       tvm_target,
                                       template_key=template_key)
        except Exception as err:  # pylint: disable=broad-except
            # We cannot expect the exceptions from schedules in libraries like TOPI so
            # we have to catch broad exceptions.
            raise RuntimeError('Failed to create task for workload {0}: {1}'.format(
                self.to_yaml(), str(err)))

        return task

    def __getitem__(self, key: str) -> Any:
        if key not in self._data:
            raise RuntimeError('Key %s is unavailable' % key)
        return self._data[key]

    def __setitem__(self, key: str, val: Any) -> Any:
        if key not in self._data:
            raise RuntimeError('Key %s is unavailable' % key)
        self._data[key] = val

        # Invalid the primary key
        self.primary_key = None

    def __contains__(self, key: str) -> bool:
        return key in self._data

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Workload) and self.__hash__() == other.__hash__()

    def __str__(self) -> str:
        return self.to_yaml()
