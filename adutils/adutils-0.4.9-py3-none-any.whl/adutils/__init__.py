"""adutils - helper functions for AppDaemon apps

  @benleb / https://github.com/benleb/adutils
"""

from datetime import datetime, timedelta, timezone
from pprint import pformat
from typing import Any, Dict, Iterable, Optional, Union


def hl(text: Union[int, float, str]) -> str:
    return f"\033[1m{text}\033[0m"


def hl_entity(entity: str) -> str:
    domain, entity = entity.split(".")
    return f"{domain}.{hl(entity)}"


class ADutils:
    def __init__(
        self,
        name: str,
        config: Dict[str, Any],
        icon: Optional[str] = None,
        ad: Any = None,
        show_config: bool = False,
    ) -> None:
        self._name = name
        self.icon = icon
        self.config = config
        self.ad = ad

        if show_config:
            self.show_info()

    @property
    def appdaemon_v3(self) -> bool:
        return bool(int(self.ad.get_ad_version()[0]) < 4)

    @property
    def name(self) -> str:
        return self._name

    def log(
        self, msg: str, icon: Optional[str] = None, *args: Any, **kwargs: Any
    ) -> None:

        kwargs.setdefault("ascii_encode", False)

        if self.appdaemon_v3:
            icon = None
            kwargs.pop("ascii_encode", None)

        message = f"{f'{icon} ' if icon else ' '}{msg}"

        self.ad.log(message, *args, **kwargs)

    def show_info(self) -> None:
        # check if a room is given
        room = ""
        if "room" in self.config:
            room = f" - {hl(self.config['room'].capitalize())}"

        self.log("")
        self.log(f"{hl(self.name)}{room}", icon=self.icon)
        self.log("")

        listeners = self.config.pop("listeners", None)

        for key, value in self.config.items():

            # hide "internal keys" when displaying config
            if key in ["module", "class"] or key.startswith("_"):
                continue

            if isinstance(value, list):
                self.print_collection(key, value, 2)
            elif isinstance(value, dict):
                self.print_collection(key, value, 2)
            else:
                self._print_cfg_setting(key, value, 2)

        if listeners:
            self.log(f"  event listeners:")
            for listener in sorted(listeners):
                self.log(f"    - {hl(listener)}")

        self.log("")

    def print_collection(
        self, key: str, collection: Iterable[Any], indentation: int = 2
    ) -> None:

        self.log(f"{indentation * ' '}{key}:")
        indentation = indentation + 2

        for item in collection:
            indent = indentation * " "

            if isinstance(item, dict):
                if "name" in item:
                    self.print_collection(item.pop("name", ""), item, indentation)
                else:
                    self.log(f"{indent}{hl(pformat(item, compact=True))}")

            elif isinstance(collection, dict):
                self._print_cfg_setting(item, collection[item], indentation)

            else:
                self.log(f"{indent}- {hl(item)}")

    @staticmethod
    def hl(text: Union[int, float, str]) -> str:
        return hl(text)

    @staticmethod
    def hl_entity(entity: str) -> str:
        return hl_entity(entity)

    async def get_timezone(self) -> timezone:
        return timezone(
            timedelta(minutes=self.ad.get_tz_offset()), name=self.ad.get_timezone()
        )

    async def last_update(self, entity: str) -> Any:
        lu_date, lu_time = await self.to_localtime(entity, "last_updated")
        last_updated = str(lu_time.strftime("%H:%M:%S"))
        if lu_date != await self.ad.date():
            last_updated = f"{last_updated} ({lu_date.strftime('%Y-%m-%d')})"
        return last_updated

    async def to_localtime(self, entity: str, attribute: str) -> Any:
        attributes = await self.ad.get_state(entity_id=entity, attribute="all")
        time_utc = datetime.fromisoformat(attributes[attribute])
        time_local = time_utc.astimezone(await self.get_timezone())
        return (time_local.date(), time_local.time())

    def _print_cfg_setting(
        self, key: str, value: Union[int, str], indentation: int
    ) -> None:
        unit = prefix = ""
        indent = indentation * " "

        # legacy way
        if key == "delay" and isinstance(value, int):
            unit = "min"
            min_value = f"{int(value / 60)}:{int(value % 60):02d}"
            self.log(
                f"{indent}{key}: {prefix}{hl(min_value)}{unit} ≈ " f"{hl(value)}sec"
            )

        else:
            if "_units" in self.config and key in self.config["_units"]:
                unit = self.config["_units"][key]
            if "_prefixes" in self.config and key in self.config["_prefixes"]:
                prefix = self.config["_prefixes"][key]

            self.log(f"{indent}{key}: {prefix}{hl(value)}{unit}")
