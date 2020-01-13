import json
from typing import Iterable, Optional


class SettingsError(Exception):
    pass


class Settings:
    ENGLISH = "en"
    RUSSIAN = "ru"
    LANGUAGES = {
        ENGLISH: "English",
        RUSSIAN: "Русский",
    }

    def __init__(self):
        self._all_processes = False
        self._all_combinations = False

        self._processes = set()
        self._combinations = {}
        self._language = self.ENGLISH

        self._text_fontsize = 40
        self._text_font = "Times"
        self._text_color = (0, 0, 0, 255)
        self._text_position = (0, 0)
        self._text_size = (200, 100)
        self._text_time = 3000

        self._window_position = (0, 0)
        self._window_size = (800, 600)

    @classmethod
    def load(cls, filename: str):
        settings = cls()
        try:
            with open(filename, "rt") as settingsfile:
                data = json.load(settingsfile)
        except FileNotFoundError:
            return settings
        combinations = {
            frozenset(key.split("+")): value for key, value in data["combinations"].items()
        }
        settings._all_processes = data["all_processes"]
        settings._all_combinations = data["all_combinations"]
        settings._processes = set(data["processes"])
        settings._combinations = combinations
        settings._language = data["language"]
        settings._text_fontsize = data["text_fontsize"]
        settings._text_font = data["text_font"]
        settings._text_color = tuple(data["text_color"])
        settings._text_position = tuple(data["text_position"])
        settings._text_size = tuple(data["text_size"])
        settings._text_time = data["text_time"]
        settings._window_position = tuple(data["window_position"])
        settings._window_size = tuple(data["window_size"])
        return settings

    def save(self, filename: str):
        combinations = {
            "+".join(tuple(key)): value for key, value in self._combinations.items()
        }
        with open(filename, "wt") as settingsfile:
            json.dump({
                "all_processes": self._all_processes,
                "all_combinations": self._all_combinations,
                "processes": list(self._processes),
                "combinations": combinations,
                "language": self._language,
                "text_fontsize": self._text_fontsize,
                "text_font": self._text_font,
                "text_color": list(self._text_color),
                "text_position": list(self._text_position),
                "text_size": list(self._text_size),
                "text_time": self._text_time,
                "window_position": list(self._window_position),
                "window_size": list(self._window_size),
            }, settingsfile)

    @property
    def all_processes(self):
        return self._all_processes

    @all_processes.setter
    def all_processes(self, value: bool):
        self._all_processes = value

    @property
    def all_combinations(self):
        return self._all_combinations

    @all_combinations.setter
    def all_combinations(self, value: bool):
        self._all_combinations = value

    def get_processes(self):
        return self._processes.copy()

    def add_process(self, process: str):
        if self._all_processes:
            raise SettingsError(f"Cannot add process '{process}' - all processes setted")
        self._processes.add(process)

    def remove_process(self, process: str):
        if self._all_processes:
            raise SettingsError(f"Cannot remove process '{process}' - all processes setted")
        if process not in self._processes:
            raise SettingsError(f"Cannot remove process '{process}' - doesn't exist")
        self._processes.remove(process)

    def clear_processes(self):
        self._processes.clear()

    def get_combinations(self):
        return self._combinations.copy()

    def add_combination(self, combination: Iterable[str], show: bool=False):
        if self._all_combinations:
            raise SettingsError(
                f"Cannot add combination '{'+'.join(sorted(combination))}'"
                " - all combinations setted",
            )
        self._combinations[frozenset(combination)] = show

    def remove_combination(self, combination: Iterable[str]):
        combination = frozenset(combination)
        if self._all_combinations:
            raise SettingsError(
                f"Cannot remove combination '{'+'.join(sorted(combination))}'"
                " - all combinations setted",
            )
        if combination not in self._combinations:
            raise SettingsError(
                f"Cannot remove combination '{'+'.join(sorted(combination))}'"
                " - doesn't exist",
            )
        del self._combinations[combination]

    def clear_combinations(self):
        self._combinations.clear()

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, language: str):
        if language not in self.LANGUAGES:
            raise SettingsError(f"Incorrect language: {language}")
        self._language = language

    @property
    def text_fontsize(self):
        return self._text_fontsize

    @text_fontsize.setter
    def text_fontsize(self, value: int):
        self._text_fontsize = value

    @property
    def text_font(self):
        return self._text_font

    @text_font.setter
    def text_font(self, value: str):
        self._text_font = value

    def get_text_color(self):
        return self._text_color

    def set_text_color(self, red: int, green: int, blue: int, alpha: int):
        self._text_color = (red, green, blue, alpha)

    def get_text_position(self):
        return self._text_position

    def set_text_position(self, x: int, y: int):
        self._text_position = (x, y)

    def get_text_size(self):
        return self._text_size

    def set_text_size(self, width: int, height: int):
        self._text_size = (width, height)

    @property
    def text_time(self):
        return self._text_time

    @text_time.setter
    def text_time(self, value: int):
        self._text_time = value

    def get_window_position(self):
        return self._window_position

    def set_window_position(self, x: int, y: int):
        self._window_position = (x, y)

    def get_window_size(self):
        return self._window_size

    def set_window_size(self, width: int, height: int):
        self._window_size = (width, height)
