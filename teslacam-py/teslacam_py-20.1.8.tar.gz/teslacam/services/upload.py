from teslacam.services.notification import NotificationService
from threading import Timer
from typing import List, Optional

from teslacam.config import Configuration
from teslacam.consts import MIN_FILE_SIZE_BYTES, UPLOADERS
from teslacam.enums import ClipType
from teslacam.funcs import group_by
from teslacam.log import log
from teslacam.models import Clip
from teslacam.services.filesystem import FileSystem

class UploadService:
    def __init__(self, cfg: Configuration, fs: FileSystem, notification: NotificationService):
        self.__cfg = cfg
        self.__fs = fs
        self.__notification = notification

        self.__uploader = UPLOADERS[cfg.uploader](cfg)
        self.__timer: Optional[Timer] = None

    def start(self):
        """
        Starts a timer that will periodically upload TeslaCam clips.
        """
        if self.__timer is not None:
            return

        self.__timer = Timer(self.__cfg.upload_interval, self.__process_clips)
        self.__timer.start()

    def __process_clips(self):
        if (self.__cfg.mount_directory):
            self.__fs.mount_directory()

        for type in self.__cfg.clip_types:
            self.__process_of_type(type)

        if (self.__cfg.mount_directory):
            self.__fs.unmount_directory()
        
        log("Processing complete")

        self.__timer = None
        self.start()

    def __process_of_type(self, type: ClipType):
        log(f"Processing {str(type)} clips...")

        clips = self.__fs.read_clips(type)
        log(f"Found {len(clips)} clips")

        uploaded = 0

        for clip in self.__get_clips_to_upload(clips):
            if self.__uploader.can_upload():
                log(f"Uploading clip '{clip.name}'")
                self.__uploader.upload(clip)
                uploaded += 1
            else:
                clips.remove(clip) # Don't delete it

        for clip in clips:
            log(f"Deleting clip '{clip.name}'")
            clip.delete()

        self.__notification.notify(f"Uploaded {uploaded} clips")

    def __get_clips_to_upload(self, clips: List[Clip]) -> List[Clip]:
        to_upload: List[Clip] = []

        for event_clips in group_by(clips, lambda c: c.event).values():
            clips_by_date = group_by(event_clips, lambda c: c.date)
            dates = sorted(clips_by_date.keys())[-self.__cfg.last_event_clips_count:]

            clips_to_upload = [clip
                for date in dates
                for clip in clips_by_date[date]
                if clip.size >= MIN_FILE_SIZE_BYTES]

            to_upload.extend(clips_to_upload)

        return to_upload