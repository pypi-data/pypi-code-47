import shutil
import uuid
import requests
import os

def load_file(path):
    '''
    Returns path of input file. If given parameter 'path' is an url,
    first downloads the file
    '''

    if path.startswith(('https://', 'http://')):
        fileName = path.split('/')[-1]
        filePath = 'data/input/'
        os.makedirs(filePath, exist_ok=True)
        data = requests.get(path, stream=True)
        data.raw.decode_content = True
        with open(filePath+fileName, 'wb+') as f: shutil.copyfileobj(data.raw, f)
        return filePath+fileName
    else:
        path = path.replace('file://', '')
        return path

def expose_file(path):
    '''
    Saves file to make it accessible to API.
    '''
    fileExtension = path.split('.')[-1]
    filePath = 'data/output/'
    fileName = uuid.uuid4().hex + '.' + fileExtension
    new_path = filePath+fileName
    os.makedirs(os.path.dirname(filePath), exist_ok=True)
    shutil.move(path, new_path)
    return new_path

