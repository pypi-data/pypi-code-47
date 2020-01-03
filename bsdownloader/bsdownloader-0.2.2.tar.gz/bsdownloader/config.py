import os
import pickle

app_folder = os.path.join(os.path.expanduser("~"), ".bs_downloader")
os.makedirs(app_folder, exist_ok=True)


def get_folder():
    return app_folder


class Config:
    def __init__(self):
        self.config_file = os.path.join(get_folder(), "config.bin")

        self.path = ""
        self.count = 200

        if os.path.isfile(self.config_file):
            with open(self.config_file, "rb") as f:
                data = pickle.load(f)
            self.path = data["path"]
            self.count = data["count"]

    def save(self):
        with open(self.config_file, "wb") as f:
            data = {"path": self.path, "count": self.count}
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
