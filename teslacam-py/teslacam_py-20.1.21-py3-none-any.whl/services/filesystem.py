from os import path
from pathlib import Path
from typing import List, Mapping

try:
    from sh import mount, umount
except:
    def mount(path: str):
        pass

    def umount(path: str):
        pass

from teslacam.config import Configuration
from teslacam.consts import TESLACAM_DIR, RECENT_DIR, SAVED_DIR, SENTRY_DIR
from teslacam.enums import ClipType
from teslacam.models import Clip

CLIP_TYPE_DIR_MAPPING: Mapping[ClipType, str] = {
    ClipType.RECENT: RECENT_DIR,
    ClipType.SAVED: SAVED_DIR,
    ClipType.SENTRY: SENTRY_DIR
}

class FileSystem:
    def __init__(self, cfg: Configuration):
        self.__cfg = cfg

    def read_clips(self, type: ClipType) -> List[Clip]:
        clips_dir = path.join(self.__cfg.tesla_cam_directory,
            TESLACAM_DIR, CLIP_TYPE_DIR_MAPPING[type])

        clips_path = Path(clips_dir)

        if not clips_path.exists():
            return []

        clips = FileSystem.__get_items(clips_path, type)

        return clips

    def mount_directory(self):
            mount(self.__cfg.tesla_cam_directory)

    def unmount_directory(self):
            umount(self.__cfg.tesla_cam_directory)

    @staticmethod
    def __get_items(clips_path: Path, type: ClipType, items: List[Clip]=None, event: str=None) -> List[Clip]:
        items = [] if items == None else items

        for item in clips_path.iterdir():
            if item.is_file() and path.splitext(item.name)[1] == ".mp4":
                items.append(Clip(item, type, event))
            
            if item.is_dir():
                FileSystem.__get_items(item, type, items, item.name)

        return items