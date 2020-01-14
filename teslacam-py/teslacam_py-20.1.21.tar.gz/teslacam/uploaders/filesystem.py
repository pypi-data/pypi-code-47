from teslacam.models import Clip
from teslacam.contracts import Uploader

class FileSystemUploader(Uploader):
    def can_upload(self) -> bool:
        return True

    def upload(self, clip: Clip):
        pass