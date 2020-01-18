from os.path import isfile as os_path_isfile
from psychopy.core import Clock
from time import sleep


def wait_downloading(directory_saved_as, max_seconds_wait=60):

    wait = True
    in_time = True
    downloaded = False
    timer = Clock()
    while wait and in_time:
        if os_path_isfile(directory_saved_as):
            wait = False
            downloaded = True
            # print('exist')
        else:
            # print('does not exist')
            in_time = timer.getTime() < max_seconds_wait
            sleep(1)
            
    return downloaded
