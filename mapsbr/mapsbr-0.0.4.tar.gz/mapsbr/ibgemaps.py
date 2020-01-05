import shapely
import functools
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
        assert geolevel, "You need to specify which geographic level this location is"
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
    "macrorregiao": 1,
    "macrorregioes": 1,
    "macroregion": 1,
    "macroregions": 1,
    "estado": 2,
    "estados": 2,
    "state": 2,
    "states": 2,
    "mesorregiao": 3,
    "mesorregioes": 3,
    "mesoregion": 3,
    "mesoregions": 3,
    "microrregiao": 4,
    "microrregioes": 4,
    "microregion": 4,
    "microregions": 4,
    "municipio": 5,
    "municipios": 5,
    "municipalitiy": 5,
    "municipalities": 5,
}


def parse_geojson(geojson):
    """
    Helper function to parse GeoJSON
    so as to get all geometries in all
    features.
    """
    features = utils.get_features(geojson)
    return [shapely.geometry.shape(feature["geometry"]) for feature in features]


def geocode(locations, geolevel=None):
    """
    Function to turn several locations
    code or name into its corresponding
    geometric shapely object.

    Parameters
    ----------
    locations : str, int, iterable
        Locations' names

    geolevel : str, default None
        Geographic level of location, needed
        if location is a string.

    Returns
    -------
    shapely objects
        shapely object or list of shapely objects
    """
    if utils.is_iter(locations):
        return [get_geometry(location, geolevel) for location in locations]
    else:
        return get_geometry(locations, geolevel)


@functools.lru_cache(maxsize=None)
def get_geometry(location, geolevel):
    """
    Get geometry of a single location code/name
    """
    if not utils.is_number(location) and location != "BR":
        assert geolevel, "You need to specify which geographic level this location is"
        location = ibgetools.ibge_encode(location, geolevel)
    if location == -1:
        return shapely.geometry.Polygon([])
    url = build_url(location)
    geojson = get_geojson(url)
    features = utils.get_features(geojson)
    return shapely.geometry.shape(features[0]["geometry"])
