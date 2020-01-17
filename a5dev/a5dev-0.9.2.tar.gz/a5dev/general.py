from sys import getsizeof
import json
import wget
import os
import zipfile

def open_json(path):
    '''
    Read Json file as dict.
    '''
    with open(path) as file:
        json_dict = json.load(file)
    return json_dict


def byte_to_mb(size):
    return size/(1024**2)


def dir_size(path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return byte_to_mb(total_size)


def file_size(path):
    file_stats = os.stat(file_name)
    return byte_to_mb(file_stats.file_size)


def var_size(var):
    return byte_to_mb(getsizeof(var))


def download_necessary_files():
    if '.a5dev_data' not in os.listdir():
        path = wget.download('https://transfer.sh/UBJEj/.a5dev_data.zip')
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall('')
        os.remove(path)