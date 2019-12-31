import shapely
import functools
import numpy as np
import geopandas as gpd
from .helpers import utils, ibgetools
from .helpers.request import get_geojson


def get_map(location, including=None, geolevel=None):
    """
    Get and turn a GeoJSON of a IBGE
    location into a GeoSeries.

    Parameters
    ----------
    location : int or str
        Location identifier (code or string)
        as in IBGE.

    including : str, default None
        Map level of detail, e.g. "states"
        "municipalities", etc.
        By default, include no details.

    geolevel : str
        If location is a name, the geographic level
        of that location. This is needed so the name
        can be converted to IBGE's code.

    Returns
    -------
    GeoSeries
        A GeoSeries with shapely objects only.
    """
    if isinstance(location, str) and location != "BR":
        location = ibgetools.ibge_encode(location, geolevel)
    if location == -1:
        return gpd.GeoSeries(shapely.geometry.Polygon([]))
    url = build_url(location, including)
    geojson = get_geojson(url)
    parsed_geojson = parse_geojson(geojson)
    return gpd.GeoSeries(parsed_geojson)


def build_url(code, including=None):
    """
    Helper function to build valid URL
    for IBGE API.
    """
    baseurl = "http://servicodados.ibge.gov.br/api/v2/malhas/"
    resolution = resolutions.get(including, 0)
    url = f"{baseurl}{code}?resolucao={resolution}&formato=application/vnd.geo+json"
    return url


resolutions = {
    "macrorregioes": 1,
    "macroregions": 1,
    "estados": 2,
    "states": 2,
    "mesorregioes": 3,
    "mesoregions": 3,
    "microrregioes": 4,
    "microregions": 4,
    "municipios": 5,
    "municipalities": 5,
}


def parse_geojson(geojson):
    features = utils.get_features(geojson)
    return [shapely.geometry.shape(feature["geometry"]) for feature in features]


@np.vectorize
@functools.lru_cache(maxsize=16)
def geocode(location, geolevel=None):
    """
    Vectorized function to turn location
    code or name into its corresponding
    geometric shapely object.

    Parameters
    ----------
    locations : iterable
        Locations' names

    geolevel : str, default None
        Geographic level of location, needed
        if location is a string.

    Returns
    -------
    ndarray
        Numpy array with shapely geometric
        objects.
    """
    if not utils.is_number(location) and location != "BR":
        location = ibgetools.ibge_encode(location, geolevel)
    url = build_url(location)
    geojson = get_geojson(url)
    features = utils.get_features(geojson)
    return shapely.geometry.shape(features[0]["geometry"])
