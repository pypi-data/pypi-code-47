"PowerSupply homie-spec node"
import os
import time
from pathlib import Path
from typing import NamedTuple, Iterator, Type, List, Mapping, Optional
from functools import lru_cache

from homie_spec import Node
from homie_spec.properties import PercentageProperty, BooleanProperty, Property, Datatype


class PowerSupply(NamedTuple):
    "PowerSupply representation"
    name: str

    @staticmethod
    def base_directory() -> Path:
        "Path to the power supply base directory"
        default_path = "/sys/class/power_supply"
        return Path(os.getenv("POWER_SUPPLY_DIRECTORY") or default_path)

    @property
    def path(self) -> Path:
        "Path to the power supply directory"
        return self.base_directory() / self.name

    @property
    def uvent_path(self) -> Path:
        "Path to the power supply directory"
        return self.path / "uevent"

    @lru_cache()
    def read_power_supply_uevent(self, ttl_h: Optional[int] = None) -> Mapping[str, str]:
        """
        Reads the power supply uvent file for data.

        Its data is retrieved by parsing `KEY=VALUE` on each line.
        Only lines with the prefix `POWER_SUPPLY_` are included.

        The prefix is dropped and the rest converted to lowercase
        in the return dictionary.

        This function optionally accepts the parameter `ttl_h`
        which is combination with its `lru_cache`, gives us the chance
        to avoid calling it multiple times.
        """
        del ttl_h
        with open(self.uvent_path, "r") as file:
            contents = file.readlines()

        return {
            key.replace("POWER_SUPPLY_", "").lower(): value.strip()
            for key, value in [x.split("=", maxsplit=1) for x in contents]
            if key.startswith("POWER_SUPPLY_")
        }

    @lru_cache()
    def keys(self) -> List[str]:
        "List of keys the power supply supports"
        return list(self.read_power_supply_uevent().keys())

    def value(self, key: str) -> str:
        """
        Retrieve the value of a key from the power supply.
        Uses ttl_h to use previous results if they were
        available within the last minute.
        """

        seconds = 60
        ttl_hash = int(time.time() / seconds)

        return self.read_power_supply_uevent(ttl_h=ttl_hash)[key.lower()]

    @lru_cache()
    def properties(self) -> Mapping[str, Property]:
        "Returns a list of properties"
        props = {}
        for key in self.keys():
            name = key.capitalize()
            if key == "capacity":
                props[key] = PercentageProperty(
                    name=name, get=lambda: self.value("capacity")
                )
            elif key == "online":

                def int_to_bool_to_str(key: str = key) -> str:
                    return str(bool(int(self.value(key)))).lower()

                props[key] = BooleanProperty(name=name, get=int_to_bool_to_str)
            elif key == "status":

                def get(key: str = key) -> str:
                    return self.value(key)

                props[key] = Property(
                    name=name,
                    datatype=Datatype.ENUM,
                    get=get,
                    formatOf="Unknown,Full,Discharging,Charging",
                )
            elif key == "cycle_count":

                def get(key: str = key) -> str:
                    return self.value(key)

                props[key] = Property(
                    name=name, datatype=Datatype.INTEGER, get=get, unit="#"
                )
            elif key.startswith("voltage_"):

                def micro_to_unit(key: str = key) -> str:
                    return str(int(self.value(key)) / 10 ** 6)

                props[key] = Property(
                    name=name, datatype=Datatype.FLOAT, get=micro_to_unit, unit="V"
                )
            elif key == "power_now":

                def micro_to_unit(key: str = key) -> str:
                    return str(int(self.value(key)) / 10 ** 6)

                props[key] = Property(
                    name=name, datatype=Datatype.FLOAT, get=micro_to_unit, unit="W"
                )
            elif key.startswith("energy_"):

                def micro_to_unit(key: str = key) -> str:
                    return str(int(self.value(key)) / 10 ** 6)

                props[key] = Property(
                    name=name, datatype=Datatype.FLOAT, get=micro_to_unit, unit="W/h"
                )
            elif key == "capacity_level":

                def get(key: str = key) -> str:
                    return self.value(key)

                props[key] = Property(
                    name=name, datatype=Datatype.ENUM, get=get, formatOf="Normal"
                )
            else:

                def get(key: str = key) -> str:
                    return self.value(key)

                props[key] = Property(name=name, datatype=Datatype.STRING, get=get)

        return props

    def node(self, whitelist_properties: Optional[List[str]] = None) -> Node:
        "Create a node for the PowerSupply represented by this instance"
        node = Node(
            name=self.name,
            typeOf="power-supply",
            properties={
                prop_name: prop
                for prop_name, prop in self.properties().items()
                if whitelist_properties is None or prop_name in whitelist_properties
            },
        )
        return node

    @classmethod
    def find_all(cls: Type["PowerSupply"]) -> Iterator["PowerSupply"]:
        """
        This is the most common method a PowerSupply object is instanciated.

        It returns an iterator with any PowerSupply it finds.

        It looks for files within `cls.base_directory`
        """
        power_supplies = cls.base_directory().glob("*")
        for power_supply in power_supplies:
            yield PowerSupply(name=power_supply.name)
