import os
import json


class Storage(object):

    def __init__(self, storage_path):
        self.storage_path = storage_path

    def retrieve(self, key):
        if os.path.exists(os.path.join(self.storage_path, f'{key}.json')):
            with open(os.path.join(self.storage_path, f'{key}.json')) as json_file:
                data = json.load(json_file)
            return data
        else:
            return None

    def store(self, key, data):
        os.makedirs(self.storage_path, exist_ok=True)
        with open(os.path.join(self.storage_path, f'{key}.json'), 'w') as out_file:
            json.dump(data, out_file)

    def delete(self, key):
        os.remove(os.path.join(self.storage_path, f'{key}.json'))
