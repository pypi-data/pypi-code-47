import grabgpu.gpuinfo
import time

def get_idle(device_ids=[]):
    for device_id in device_ids:
        gpu_status = gpuinfo.get(device_id=device_id)
        if gpu_status['memory_used'] < 100:
            return device_id

    return None

def wait_until_available(device_ids=[]):
    while True:
        idle_device = get_idle(device_ids)
        if idle_device is not None:
            print(idle_device)
            return idle_device

        time.sleep(3)
