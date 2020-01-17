"""
csvfile.py

Read / Write USA city data in csv.

Usage:
    $ pipenv install
    $ pipenv run csvfile.py
"""
from dataclasses import dataclass
from serde import deserialize
from serde.csv import to_csv


@deserialize
@dataclass(unsafe_hash=True)
class City:
    city: str
    state: str
    population: int
    latitude: float
    longitude: float


def main():
    city = City('Davidsons Landing', 'AK', 0, 65.2419444, -165.2716667)
    print(to_csv(city))

    cities = [
        City('Davidsons Landing', 'AK', 0, 65.2419444, -165.2716667),
        City('Kenai', 'AK', 7610, 60.5544444, -151.2583333),
        City('Oakman', 'AL', 0, 33.7133333, -87.3886111),
        City('Richards Crossroads', 'AL', 0, 31.7369444, -85.2644444),
        City('Sandfort', 'AL', 0, 32.3380556, -85.2233333),
    ]
    print(to_csv(cities, header=True))


if __name__ == '__main__':
    main()
