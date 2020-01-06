import os
from hashlib import sha256
from datetime import datetime
def sanboxConfig():
    config = {
        'memory': '100M', # MB 
        'memory_swap': '100M', # MB
        'timeout': 3, # seconds
        'type': 'python3', 
        'dependency': 'todo',
        'cpu': 1,
        'pids_limit': 10,
        'host_path': os.getcwd(),
        'container_path': '/tmp',
        'image': 'library/python'
    }
    return config