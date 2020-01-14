from os import path

from teslacam import config
from teslacam.log import log
from teslacam.services.filesystem import FileSystem
from teslacam.services.notification import NotificationService
from teslacam.services.upload import UploadService

def get_version():
    with open(path.join(path.dirname(__file__), "VERSION"), encoding="utf-8") as file:
        return file.read()

def main():
    cfg = config.load_config()
    
    fs = FileSystem(cfg)
    notification = NotificationService(cfg)

    upload = UploadService(cfg, fs, notification)

    # Start upload service
    upload.start()

    log(f"Started TeslaCam v{get_version()}")

if __name__ == "__main__":
    main()