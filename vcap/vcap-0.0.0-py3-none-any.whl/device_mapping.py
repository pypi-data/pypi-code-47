from typing import Callable, List
from threading import RLock

import tensorflow as tf
from tensorflow.python.client import device_lib

_devices = None
_devices_lock = RLock()


def get_all_devices() -> List[str]:
    """Returns a list of devices in the computer. Example:
    ['CPU:0', 'XLA_GPU:0', 'XLA_CPU:0', 'GPU:0', 'GPU:1', 'GPU:2', 'GPU:3']
    """
    global _devices, \
        _devices_lock, \
        _process_gpu_options

    # Initialize the device list if necessary
    with _devices_lock:
        if _devices is None:
            # We create a session because otherwise list_local_devices allocates
            # all of the available GPU memory to the computer
            _process_gpu_options = tf.GPUOptions(allow_growth=True)
            config = tf.ConfigProto(gpu_options=_process_gpu_options)

            with tf.Session(config=config):
                all_devices = device_lib.list_local_devices()
            _devices = [d.name.replace("/device:", "") for d in all_devices]

            # Remove duplicates, just in case...
            _devices = list(set(_devices))

    return _devices


class DeviceMapper:
    def __init__(self, filter: Callable[[List[str]], List[str]]):
        """The filter will take in a list of devices formatted as
        ["CPU:0", "CPU:1", "GPU:0", "GPU:1"], etc and output a filtered list of
        devices.
        """
        self.filter = filter

    @staticmethod
    def map_to_all_gpus(cpu_fallback=True) -> 'DeviceMapper':
        def filter(devices):
            gpus = [d for d in devices if d.split(':')[0] == "GPU"]
            if len(gpus) == 0 and cpu_fallback:
                return ['CPU:0']
            return gpus

        return DeviceMapper(filter=filter)

    @staticmethod
    def map_to_single_cpu() -> 'DeviceMapper':
        def filter(devices):
            return [next(d for d in devices if d.split(':')[0] == "CPU")]

        return DeviceMapper(filter=filter)
