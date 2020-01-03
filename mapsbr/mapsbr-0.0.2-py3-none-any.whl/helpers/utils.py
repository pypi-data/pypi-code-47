import numpy as np


@np.vectorize
def vectorized_get(dictionary, key):
    """
    Helper vectorized function to get keys
    from a dictionary.
    """
    return dictionary.get(key, -1)


@np.vectorize
def is_number(x):
    """
    Helper vectorized function to test
    if a value is or represents a number,
    i.e., an integer.
    """
    try:
        int(x)
        return True
    except ValueError:
        return False


def get_features(geojson):
    """
    Helper function to extract features
    from dictionary. If it doesn't find
    it, raise a value error with a more
    informative error message.
    """
    try:
        features = geojson["features"]
    except KeyError:
        raise KeyError(f"{geojson} is an invalid GeoJSON. Not a feature collection")
    return features


@np.vectorize
def from_iso88591_to_utf8(string):
    """
    Convert weird characters to UTF-8.
    For example, "mÃ©dio" should be "médio".
    """
    try:
        return bytes(string, "iso-8859-1").decode("utf-8")
    except UnicodeDecodeError:
        return string
