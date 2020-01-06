import pandas as pd
import pkg_resources

def _load_from_resource(resource_path):
    return pd.read_csv(pkg_resources.resource_filename(__name__,resource_path))

def _return_file(string):
    resource_path = '/'.join(('data',string + '.zip'))
    return _load_from_resource(resource_path)

def load_movies():
    return _return_file('movies')

