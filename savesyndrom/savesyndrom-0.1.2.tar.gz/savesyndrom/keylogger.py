from datetime import datetime
from enum import Enum
import json
import sys
from threading import Thread
from time import sleep
from typing import Callable, Iterable, Optional, Union

import keyboard

from .activewindow import get_active_window


class KeyLoggerError(Exception):
    pass


class KeyLogger:
    def __init__(self, filename: str, buffer_size: int=1024, show: Callable=lambda: None):
        self._pressed = set()
        self._buffer = []
        self._all_processes = False
        self._all_combinations = False
        self._processes = set()
        self._combinations = {}
        self._file = open(filename, "at+")
        self._buffer_size = buffer_size
        self._show = show
        self._running = False

    def __del__(self):
        self.flush()
        self._file.close()

    def start(self):
        if self._all_combinations:
            keyboard.on_press(self._on_press)
            keyboard.on_release(self._on_release)
        else:
            for c in self._combinations:
                keyboard.add_hotkey("+".join(c), lambda: self.handle(*c))
        self._running = True
        self._add_buffer(action="start")

    def stop(self):
        if self._running:
            keyboard.unhook_all()
            self._add_buffer(action="stop")
            self.flush()
            self._running = False

    def _add_buffer(self, **kwargs):
        self._buffer.append({
            "time": int(datetime.now().timestamp()),
            **kwargs,
        })
        if len(self._buffer) > self._buffer_size:
            self.flush()

    def flush(self):
        for record in self._buffer:
            self._file.write(json.dumps(record) + "\n")
        self._file.flush()
        self._buffer.clear()

    def get_statistic(self) -> dict:
        result = {"pressed": {}, "time": 0}
        self._file.seek(0)
        time = 0
        last_time = 0
        for record in self._file:
            record = json.loads(record)
            if record["action"] == "start":
                last_time = record["time"]
            elif record["action"] == "stop":
                time += record["time"] - last_time
                last_time = record["time"]
            elif record["action"] == "pressed":
                row = (record["process"], frozenset(record["combination"]))
                if row in result["pressed"]:
                    result["pressed"][row] += 1
                else:
                    result["pressed"][row] = 1
        for record in self._buffer:
            if record["action"] == "start":
                last_time = record["time"]
            elif record["action"] == "stop":
                time += record["time"] - last_time
                last_time = record["time"]
            elif record["action"] == "pressed":
                row = (record["process"], frozenset(record["combination"]))
                if row in result["pressed"]:
                    result["pressed"][row] += 1
                else:
                    result["pressed"][row] = 1
        result["time"] = time
        return result

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

    def add_process(self, process: str):
        if self._all_processes:
            raise KeyLoggerError(f"Cannot add process '{process}' - all processes setted")
        self._processes.add(process)

    def remove_process(self, process: str):
        if self._all_processes:
            raise KeyLoggerError(f"Cannot remove process '{process}' - all processes setted")
        if process not in self._processes:
            raise KeyLoggerError(f"Cannot remove process '{process}' - doesn't exist")
        self._processes.remove(process)

    def clear_processes(self):
        self._processes.clear()

    def add_combination(self, combination: Iterable[str], show: bool=False):
        if self._all_combinations:
            raise KeyLoggerError(
                f"Cannot add combination '{'+'.join(sorted(combination))}'"
                " - all combinations setted",
            )
        self._combinations[frozenset(combination)] = show

    def remove_combination(self, combination: Iterable[str]):
        combination = frozenset(combination)
        if self._all_combinations:
            raise KeyLoggerError(
                f"Cannot remove combination '{'+'.join(sorted(combination))}'"
                " - all combinations setted",
            )
        if combination not in self._combinations:
            raise KeyLoggerError(
                f"Cannot remove combination '{'+'.join(sorted(combination))}'"
                " - doesn't exist",
            )
        del self._combinations[combination]

    def clear_combinations(self):
        self._combinations.clear()

    def _on_press(self, event: keyboard._keyboard_event.KeyboardEvent):
        self._pressed.add(event.name)

    def _on_release(self, event: keyboard._keyboard_event.KeyboardEvent):
        self.handle(*self._pressed)
        try:
            self._pressed.remove(event.name)
        except KeyError:
            pass

    def handle(self, *keys):
        keys = frozenset(keys)
        process = get_active_window()
        if process is None:
            return
        if not self._all_processes:
            for p in self._processes:
                if p in process:
                    process = p
                    break
            else:
                return
        if not self._all_combinations and keys not in self._combinations:
            return
        self._add_buffer(action="pressed", process=process, combination=list(keys))

        if not self._all_combinations and self._combinations[keys]:
            self._show(keys)
