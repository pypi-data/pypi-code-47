from typing import Mapping, Type

from teslacam.contracts import Notifier, Uploader
from teslacam.notifiers.pushover import PushoverNotifier
from teslacam.uploaders.blobstorage import BlobStorageUploader
from teslacam.uploaders.filesystem import FilesystemUploader

UPLOADERS: Mapping[str, Type[Uploader]] = {
    "blobStorage": BlobStorageUploader,
    "filesystem": FilesystemUploader
}

NOTIFIERS: Mapping[str, Type[Notifier]] = {
    "pushover": PushoverNotifier
}

TESLACAM_DIR = "TeslaCam"
RECENT_DIR = "RecentClips"
SAVED_DIR = "SavedClips"
SENTRY_DIR = "SentryClips"

MIN_FILE_SIZE_BYTES = 1048576 # 1 MB