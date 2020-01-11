"""
Define frequently used services-shortcuts to work with 17track API
"""
from typing import Dict, List

import requests

from .entity import PackageEntity
from .models import Track17Country, Track17Carrier
from .settings import (
    TRACK17_CARRIERS_URL,
    TRACK17_COUNTRIES_URL
)
from .track17 import Track17Adapter
from .validators import validate_response_code

__all__ = (
    'populate_countries',
    'populate_carriers',
    'register_track',
    'get_track_info',
    'get_track_info_as_packages'
)


def populate_countries():
    """
    Fetch countries
    """
    response = requests.get(TRACK17_COUNTRIES_URL)
    data = response.json()
    Track17Country.objects.all().delete()
    Track17Country.objects.create(
        key='0000',
        title='Unknown'
    )
    Track17Country.objects.bulk_create([
        Track17Country(
            key=str(item['key']).lstrip('0'),
            title=item['_name']
        ) for item in data
    ])


def populate_carriers():
    """
    Fetch carriers
    """
    if not Track17Country.objects.exists():
        populate_countries()
    response = requests.get(TRACK17_CARRIERS_URL)
    data = response.json()
    Track17Carrier.objects.all().delete()
    Track17Carrier.objects.bulk_create([
        Track17Carrier(
            key=str(item['key']).lstrip('0'),
            title=item['_name'],
            can_track=True if item['_canTrack'] == 1 else 0,
            url=item["_url"],
            country=Track17Country.objects.filter(key=item['_country']).first()
        ) for item in data
    ])


def register_track(*tracking_numbers: str) -> Dict[str, List]:
    """
    Register given tracking numbers

    Raises:
        DateProcessingError

    Return:
        {
            "accepted": [
                {
                    "number": "RR123456789CN",
                    "carrier": 3011
                }
            ],
            "rejected": [
                {
                    "number": "1234",
                    "error": {
                        "code": -18010012,
                        "message": "The format of '1234' is invalid."
                    }
                }
            ]
        }
    """
    track17 = Track17Adapter()
    response = track17.register(*tracking_numbers)
    response_data = response.data
    validate_response_code(response_data['code'])
    return response_data['data']


def get_track_info(*tracking_numbers: str) -> Dict[str, List]:
    """
    Fetch actual info about given tracking numbers

    Raises:
        DateProcessingError

    Return:
        {
            "accepted": [
                {
                    "number": "RM101474005CN",
                    "track": {
                        "w1": 3011,
                        "w2": 18031,
                        "b": 301,
                        "c": 1803,
                        "z1": [
                            {
                                "a": "2015-05-13 14:47",
                                "b": null,
                                "c": "",
                                "d": "",
                                "z": "电子信息已收到"
                            }
                        ],
                        "z2": [
                            {
                                "a": "2015-05-31 00:00",
                                "b": null,
                                "c": "",
                                "d": "",
                                "z": "Distribué ANDORRE LA VIEILLE (09)."
                            }
                        ],
                        "ygt1": 370,
                        "ygt2": 0,
                        "is1": 1,
                        "is2": 0,
                        "ln1": "zh-CHS",
                        "ln2": null,
                        "hs": 627236210,
                        "z0": {
                            "a": "2015-05-29 09:00",
                            "b": null,
                            "c": "BLAGOVESCH 1",
                            "d": "",
                            "z": "移交海关"
                        },
                        "ylt1": "2015-06-01 20:44:52",
                        "ylt2": "2079-01-01 00:00:00",
                        "e": 10,
                        "f": -1
                    }
                }
            ]
        }
    """
    track17 = Track17Adapter()
    response = track17.get_track_info(*tracking_numbers)
    response_data = response.data
    validate_response_code(response_data['code'])
    return response_data['data']


def get_track_info_as_packages(data: List) -> List[PackageEntity]:
    """
    Return `accepted` tracking numbers as a list of `PackageEntity` instances

    Return:
        List of PackageEntity
    """
    packages: List = []
    for package in data:
        number = package.get('number')
        package_info: dict = package.get("track", {})
        kwargs: dict = {
            'tracking_number': number,
            'first_carrier': package_info.get('w1'),
            'second_carrier': package_info.get('w2'),
            "origin_country": package_info.get("b"),
            "destination_country": package_info.get("c"),
            "last_event_time": package_info.get("z0", {}).get("a"),
            "last_event_location": package_info.get("z0", {}).get("c"),
            "last_event_description": package_info.get("z0", {}).get("z"),
            "tracking_info_language": package_info.get("ln1", "Unknown"),
            "status": package_info.get("e", 0),
        }
        kwargs = {key: value for key, value in kwargs.items() if value}
        packages.append(PackageEntity(**kwargs))
    return packages
