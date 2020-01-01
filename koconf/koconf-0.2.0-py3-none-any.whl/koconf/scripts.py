from pathlib import Path
from setuptools.command.install import install


class PostInstall(install):
    def run(self):
        install.run(self)

        with SetupManager() as setup:
            setup.set_need_setup()


class SetupManager():
    def __init__(self):
        self.__path = Path.home().joinpath('.need_setup')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def set_need_setup(self):
        self.__path.touch(exist_ok=True)

    def unset_need_setup(self):
        # TODO : If support python version is >= 3.8, use missing_ok
        if self.__path.exists():
            self.__path.unlink()

    def check_need_setup(self):
        return self.__path.exists()
