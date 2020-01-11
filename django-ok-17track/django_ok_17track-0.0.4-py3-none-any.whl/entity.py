"""
Define entity for a tracking number info, retrieved from 17track API
"""

from dataclasses import dataclass, field
from typing import Union

from .constants import PACKAGE_STATUS_MAP
from .exceptions import InvalidCarrierCode
from .models import Track17Country, Track17Carrier

__all__ = (
    'get_carrier',
    'get_default_country',
    'PackageEntity',
)


def get_carrier(code: str):
    """
    Return a carrier by a given code
    """
    try:
        return Track17Carrier.objects.get(key=str(code))
    except Track17Carrier.DoesNotExist:
        raise InvalidCarrierCode(
            message='An invalid carrier code or a desired carrier does not exist.'
        )


def get_default_country():
    """
    Return a default country
    """
    country, _ = (
        Track17Country.objects.get_or_create(key='0', title='Unknown')
    )
    return country


@dataclass
class PackageEntity:
    """
    Package object to store all important data about tracking number
    """
    tracking_number: str
    first_carrier: str = ""
    second_carrier: str = ""
    last_event_time: str = ""
    last_event_location: str = ""
    last_event_description: str = ""
    tracking_info_language: str = "Unknown"
    status: Union[str, int] = 0
    origin_country: str = field(default_factory=get_default_country)
    destination_country: str = field(default_factory=get_default_country)

    def __post_init__(self):
        if self.first_carrier:
            self.first_carrier = get_carrier(self.first_carrier)

        if self.second_carrier:
            self.second_carrier = get_carrier(self.second_carrier)

        if self.origin_country:
            self.origin_country = (
                Track17Country.objects.filter(key=self.origin_country).first() or ""
            )

        if self.destination_country:
            self.destination_country = (
                Track17Country.objects.filter(key=self.destination_country).first() or ""
            )

        self.status = PACKAGE_STATUS_MAP[self.status]
