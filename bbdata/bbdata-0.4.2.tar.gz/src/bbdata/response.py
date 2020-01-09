import pandas as pd
from operator import itemgetter
import json


class Response:
    """
    A class, that handles the responses done by the route. This is the base
    class that returns a generic json
    """

    def __init__(self, return_value=None, *args, **kwargs):
        self.raw_out = return_value
        self.df = None

    def to_json(self, filename=None, path='./', safe=False):
        if safe:
            if filename is None or path is None:
                raise ValueError("If you want to save to .json please provide "
                                 "a filename")
            else:
                with open(path + filename + '.json', 'w') as out_json:
                    json.dump(self.to_json(), out_json)
        return self.raw_out

    def to_dataframe(self):
        raise NotImplementedError

    def to_csv(self, filename, path='./'):
        raise NotImplementedError

    def to_pickle(self, filename: str, path: str = './'):
        raise NotImplementedError

    def __repr__(self):
        return self.to_json()

    def __str__(self):
        return str(self.raw_out)

    def __iter__(self):
        return ResponseIterator(self.raw_out)

    def __getitem__(self, item):
        return self.raw_out[item]


class ValueResponse(Response):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_csv(self, filename: str, path: str = './'):
        if self.df is None:
            self.df = self.to_dataframe()
        file = path + filename + '.csv'
        self.df.to_csv(file)

    def to_pickle(self, filename: str, path: str = './'):
        if self.df is None:
            self.df = self.to_dataframe()
        file = path + filename + '.pickle'
        self.df.to_pickle(file)

    def to_dataframe(self):
        # for ind in range(len(self.raw_out)):
        # col_name = self.raw_out[ind]['objectId']
        rows = self.get_timestamp_set()
        columns = self.get_columns()
        self.df = pd.DataFrame(index=rows, columns=columns)
        for obj in self.raw_out:
            self.add_object_data(obj)
        return self.df

    def add_object_data(self, obj):
        obj_name = obj['objectId']
        values = sorted(obj['values'], key=itemgetter('timestamp'))
        for value in values:
            self.df.at[value['timestamp'], obj_name] = value['value']

    def get_columns(self):
        return [obj['objectId'] for obj in self.raw_out]

    def get_timestamp_set(self):
        # [x for b in a for x in b]
        timestamps = sorted(
            list(set([d['timestamp'] for obj in self.raw_out
                      for d in obj['values'] if 'timestamp' in d])))
        return timestamps


class ResponseIterator:
    """
    Iterator for the Response-object
    """

    def __init__(self, raw_out):
        self._raw_out = raw_out

        self._index = 0

    def __next__(self):
        if self._index < len(self._raw_out):
            result = self._raw_out[self._index]
            self._index += 1
            return result

        raise StopIteration
