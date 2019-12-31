import numpy as np


def memoize(function):
    cache = {}

    def decorated_function(arg, *args, **kwargs):
        if arg not in cache:
            cache[arg] = function(arg, *args, **kwargs)
        return cache[arg]
    return decorated_function


@np.vectorize
def vectorized_get(dictionary, key):
    return dictionary.get(key, -1)


@np.vectorize
def is_number(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def get_features(geojson):
    try:
        features = geojson["features"]
    except KeyError:
        raise KeyError(f"{geojson} is an invalid GeoJSON. Not a feature collection")
    return features


@np.vectorize
def from_iso_8859_1_to_utf_8(string):
    try:
        return bytes(string, "iso-8859-1").decode("utf-8")
    except UnicodeDecodeError:
        return string
