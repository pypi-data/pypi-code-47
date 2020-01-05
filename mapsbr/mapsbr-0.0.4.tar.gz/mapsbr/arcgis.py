import pandas as pd
import geopandas as gpd
from .helpers import utils
from shapely.geometry import shape
from .helpers.request import get_geojson


def get_map(service, baseurl=None, service_type="MapServer", layer=0):
    """
    Get geometries associated with an ARCGIS host service.

    Parameters
    ----------
    service : str
        Service identifier, part of the url
        after "services/"

    baseurl : str, default None
        Base url or host. By default, it will
        be https://mapasinterativos.ibge.gov.br/arcgis/rest/services

    service_type : str, default "MapServer"
        Service type

    layer : int or str, default 0
        Service layer

    Returns
    -------
    GeoDataFrame
    """
    maps = pd.concat(
        get_all_features(service, baseurl, service_type, layer), axis="rows"
    )
    gdf = gpd.GeoDataFrame(maps)
    gdf.iloc[:, 1] = utils.from_iso88591_to_utf8(gdf.iloc[:, 1])
    return gdf


def get_all_features(service, baseurl=None, service_type="MapServer", layer=0):
    """
    Helper function to get all features from a
    service layer. This is a work around the API
    1000 row limit per response.
    """
    count = 0
    while True:
        url = build_url(service, baseurl, service_type, layer, count=count)
        geojson = get_geojson(url)
        if geojson["features"]:
            parsed_geojson = parse_geojson(geojson)
            yield pd.DataFrame(parsed_geojson)
            count += 1000
        else:
            break


def build_url(service, baseurl=None, service_type="MapServer", layer=0, count=0):
    """
    Helper function to build valid ARCGIS url.
    """
    if baseurl is None:
        baseurl = "https://mapasinterativos.ibge.gov.br/arcgis/rest/services"
    baseurl = baseurl.rstrip("/")
    where = f"where=objectId>={count}+and+objectId<{count+1000}"
    return f"{baseurl}/{service}/{service_type}/{layer}/query?{where}&f=geojson"


def parse_geojson(geojson):
    """
    Helper function to read GeoJSON to
    get all geometries and properties.
    """
    features = utils.get_features(geojson)
    property_dict = features[0].get("properties", "property")
    property_name = list(property_dict)[0]
    return [
        {
            "geometry": shape(feature["geometry"]),
            property_name: list(feature["properties"].values())[0],
        }
        for feature in geojson["features"]
        if feature["geometry"]["coordinates"] != []
    ]


def folders(folder=None, baseurl=None):
    """
    Search available folders in a ArcGIS server.

    Parameters
    ----------
    baseurl : str, default None
        Server url. By default, it will
        be https://mapasinterativos.ibge.gov.br/arcgis/rest/services

    folder : str, default None
        Path to search for folders.

    Returns
    -------
    DataFrame
        A DataFrame listing folders.
    """
    if baseurl is None:
        baseurl = "https://mapasinterativos.ibge.gov.br/arcgis/rest/services"
    folder = f"/{folder}" if folder else ""
    result = get_geojson(f"{baseurl}{folder}?f=json")
    return pd.DataFrame(result["folders"])


def services(folder=None, baseurl=None):
    """
    Search available services in a ArcGIS server folder.

    Parameters
    ----------
    baseurl : str, default None
        Server url. By default, it will
        be https://mapasinterativos.ibge.gov.br/arcgis/rest/services

    folder : str, default None
        Path to search for services.

    Returns
    -------
    DataFrame
        A DataFrame listing services.
    """
    if baseurl is None:
        baseurl = "https://mapasinterativos.ibge.gov.br/arcgis/rest/services"
    folder = f"/{folder}" if folder else ""
    result = get_geojson(f"{baseurl}{folder}?f=json")
    return pd.DataFrame(result["services"])


def layers(service_path, baseurl=None):
    """
    Search available layers in a ArcGIS service.

    Parameters
    ----------
    service_path : str
        Path to service.

    baseurl : str, default None
        Server url. By default, it will
        be https://mapasinterativos.ibge.gov.br/arcgis/rest/services

    Returns
    -------
    DataFrame
        A DataFrame listing service layers.
    """
    if baseurl is None:
        baseurl = "https://mapasinterativos.ibge.gov.br/arcgis/rest/services"
    result = get_geojson(f"{baseurl}/{service_path}/MapServer?f=json")
    return pd.DataFrame(result["layers"]).iloc[:, :2]

# vi: nowrap
