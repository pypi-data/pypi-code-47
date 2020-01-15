#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keepfresh.event import Event
from typing import List, TypeVar, Dict
import os
import time
import logging

logger = logging.getLogger(__name__)

PathString = TypeVar('PathString', bound=str)
ModifiedTimeString = TypeVar('ModifiedTimeString', bound=str)

class Observer:
    def __init__(self, base_dir: str, excluded_dirs: List[str]):
        self.base_dir = base_dir
        self.excluded_dirs = excluded_dirs
        self.path_map = self.create_path_map()
        logger.info(f"Watching {len(self.path_map)} files")

    def create_path_map(self) -> Dict[PathString, ModifiedTimeString]:
        """
        Create a path map, a map which maps a path to the modification time of that path
        """
        path_map = {}
        for dir_path, dirs, files in os.walk(self.base_dir, topdown=True):
            dirs[:] = [dir for dir in dirs if dir not in self.excluded_dirs]
            for file in files:
                file_path = os.path.join(dir_path, file)
                path_map[file_path] = os.stat(file_path).st_mtime
        return path_map

    def determine_events(self, existing_path_map: dict, new_path_map: dict) -> List[Event]:
        """
        Compare two path maps to determine the events
        """
        events = []

        # Determine new and modified files
        for path in new_path_map:
            if path not in existing_path_map:
                logger.info(f"{path} is new")
                events.append(Event(path=path, created=True))
            else:
                # If it already exists, check if the modified time is the same
                if new_path_map[path] != existing_path_map[path]:
                    logger.info(f"{path} has been modified")
                    events.append(Event(path=path, modified=True))

        # Determine deleted files
        for path in existing_path_map:
            if path not in new_path_map:
                logger.info(f"{path} has been deleted")
                events.append(Event(path=path, deleted=True))

        return events

    def observe_and_update(self) -> List[Event]:
        """
        Get the most recent path map, determine the events, update the stored path map
        and return the events
        """
        new_path_map = self.create_path_map()
        events = self.determine_events(
            new_path_map=new_path_map,
            existing_path_map=self.path_map
        )
        self.path_map = new_path_map
        return events

    def log(self, interval: int = 1):
        """
        Poll for events and log them
        """
        while True:
            new_path_map = self.create_path_map()
            self.determine_events(
                new_path_map=new_path_map,
                existing_path_map=self.path_map
            )
            self.path_map = new_path_map
            time.sleep(interval)

if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    observer = Observer(
        base_dir='../',
        excluded_dirs=['.git', '.env']
    )
    observer.log()
