from WasuTvTest.public import read_yaml


class appium_config:
    def __init__(self, path):
        self.path = path
        self.config = {}

    def get_file(self):
        file = read_yaml(self.path).load_file()
        return file

    def get_config(self):
        file = self.get_file()
        for key, value in file.items():
            self.config.update({key:value})
        return self.config
