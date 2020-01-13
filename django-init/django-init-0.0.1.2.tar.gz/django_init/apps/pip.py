
class PIPManager:

    def get_requirements(self, app):
        pass

    def install(self):
        pass

    def uninstall(self):
        pass


from pip._internal import main

def install(package):
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
# Example
if __name__ == '__main__':
    install('twine')