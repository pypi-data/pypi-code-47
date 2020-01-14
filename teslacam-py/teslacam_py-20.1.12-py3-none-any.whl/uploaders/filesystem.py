from teslacam.models import Clip
from teslacam.contracts import Uploader

class FilesystemUploader(Uploader):
    def can_upload(self) -> bool:
        return False

    def upload(self, clip: Clip):
        pass