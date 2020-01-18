import os

import psutil
import torch
from utify import approximate_size


def get_device(use_gpu=True, gpu_idx=None, return_str=False):
    """Return `torch.device('cuda:idx')` if `use_gpu` and cuda is available else `torch.device('cpu')`

    Args:
        use_gpu (bool): if True, try to detect if GPU is available
        gpu_idx (gpu_idx): if provided, must be a non-negative integer less than the number of GPUs
        return_str (bool): if True, return a string of the device, otherwise return a `torch.device`

    Returns:
        :py:class:`str` or :py:class:`torch.device`
    """
    use_cuda = torch.cuda.is_available() and use_gpu
    if gpu_idx:
        assert isinstance(gpu_idx, int), "gpu_idx must be an integer"
        assert gpu_idx < get_gpu_count(), "gpu_idx can't exceed the number of GPUs"
    gpu = f'cuda:{gpu_idx}' if gpu_idx else 'cuda'
    device_str = gpu if use_cuda else 'cpu'
    return device_str if return_str else torch.device(device_str)


def get_memory_info():
    """Return the memory usage information
    """
    return psutil.virtual_memory()


def get_total_memory(return_bytes=True, echo=True, human_readable=True):
    """Return the total memory of current machine

    Returns:

    """
    total_memory = psutil.virtual_memory().total
    if echo:
        if human_readable:
            print('total memory:', approximate_size(total_memory))
        else:
            print('total memory (bytes):', total_memory)
    if return_bytes:
        return total_memory


def get_free_memory(return_bytes=True, echo=True, human_readable=True):
    """Return the free memory of current machine

    Returns:

    """
    free_memory = psutil.virtual_memory().free
    if echo:
        if human_readable:
            print('free memory:', approximate_size(free_memory))
        else:
            print('free memory (bytes):', free_memory)
    if return_bytes:
        return free_memory


def get_available_memory(return_bytes=True, echo=True, human_readable=True):
    """Return the available memory of current machine

    Returns:

    """
    available_memory = psutil.virtual_memory().available
    if echo:
        if human_readable:
            print('available memory:', approximate_size(available_memory))
        else:
            print('available memory (bytes):', available_memory)
    if return_bytes:
        return available_memory


def get_cpu_count():
    """Return the number of available cpus
    """
    if hasattr(os, 'sched_getaffinity'):
        return len(os.sched_getaffinity(0))
    else:
        return os.cpu_count()


def get_gpu_count():
    """Return the number of available cpus
    """
    return torch.cuda.device_count()


def get_gpu_info(return_info=False):
    """Show and optionally return the inforamtion of available GPUs
    """
    gpu_count = get_gpu_count()
    if gpu_count == 0:
        print('No available GPUs.')
        return None
    else:
        gpu_info = {}
        for gpu_idx in range(gpu_count):
            gpu_properties = torch.cuda.get_device_properties(gpu_idx)
            gpu_info[gpu_idx] = {
                'name':                  gpu_properties.name,
                'major':                 gpu_properties.major,
                'minor':                 gpu_properties.minor,
                'total_mem':             approximate_size(gpu_properties.total_memory),
                'multi_processor_count': gpu_properties.multi_processor_count
            }
            str_info = "GPU {}: {name} {major}.{minor} [{total_mem} total memory, {multi_processor_count} processors]"
            print(str_info.format(gpu_idx, **gpu_info[gpu_idx]))

        if return_info:
            return gpu_info
