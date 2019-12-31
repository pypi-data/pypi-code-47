import json
import requests
import functools


s = requests.Session()


@functools.lru_cache(maxsize=16)
def get_geojson(url, **kwargs):
    response = s.get(url, timeout=60, **kwargs)
    response.raise_for_status
    try:
        return response.json()
    except json.JSONDecodeError:
        raise ValueError(f"A request to {url} didn't produce any GeoJSON.")
