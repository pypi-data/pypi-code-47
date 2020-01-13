__version__ = '1.0.0'

from glob import glob
from os import path, remove, getcwd
from platform import system
from time import sleep
from zipfile import ZipFile

from requests import get


class CheckDriver:
    @staticmethod
    def download(url):
        local_filename = url.split('/')[-1]
        r = get(url, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        return local_filename

    @staticmethod
    def unzip(zipfile):
        with ZipFile(zipfile, 'r') as zip_ref:
            zip_ref.extractall(getcwd())

        remove(path.join(getcwd(), zipfile))

    def check(self):
        systems = {'Darwin': 'mac64', 'Linux': 'linux64', 'Windows': 'win32'}
        os = systems[system()]
        url = 'https://chromedriver.storage.googleapis.com'

        if not glob('chromedriver*'):
            lr = get(f'{url}/LATEST_RELEASE')
            self.download(f'{url}/{lr.text}/chromedriver_{os}.zip')
            while not glob('*.zip'):
                sleep(1)
            self.unzip(f'chromedriver_{os}.zip')
