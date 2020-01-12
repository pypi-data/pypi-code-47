import logging
import platform
import threading
import subprocess
import zipfile
from pathlib import Path
from shutil import rmtree
from typing import List, Tuple, Union, Iterable
from importlib import import_module

import requests

from swy.core.exceptions.swyexceptions import *
import swy.data.phones

logger = logging.getLogger('adb')


class AdbInterface:
    """
    Main ADB entry point for phone communication
    This class is a singleton to ensure only one point communicates with the phone,
    and solve implementation details.
    """
    _instance = None  # Thread safe Singleton implementation
    _lock = threading.Lock()

    def __new__(cls, tmpdir: Path):
        """
        Singleton implementation, to easily solve problems like multiple adb binaries download,
        and async sharing
        """
        if AdbInterface._instance is None:
            with AdbInterface._lock:
                if AdbInterface._instance is None:
                    AdbInterface._instance = super().__new__(cls)
        return AdbInterface._instance

    def __init__(self, tmpdir: Path):
        logger.debug('Initialising AdbInterface in temp dir : {}'.format(tmpdir))
        self.tmpdir: Path = tmpdir
        self.screenshotsdir = None  # done in post_init
        self.phonelib = None        # done in post_init
        self.adb = None             # done in post_init

    def post_init(self):
        self.adb: Path = self._make_adb_available()  # Download adb binaries, and get adb.exe path
        self._start_adb_server()  # Start ADB local server
        self.screenshotsdir = self._create_tmp_subdir('screnshots')
        self.phonelib = self._autoselect_phone_lib()  # TODO: select phone from list_devices

    def _create_tmp_subdir(self, sub_dir_name: str, exists_ok=True) -> Path:
        """
        Creates a new subdirectory at the given path (appends a dir to the current allocated temporary directory)
        :param sub_dir_name: Name of the new directory
        :param exists_ok: argument given to the mkdir function, to ignore error on already existing dir
        :return: the new directory path
        """
        logger.debug('Creating new directory {} inside {}'.format(sub_dir_name, self.tmpdir))
        newpath = self.tmpdir / Path(sub_dir_name)
        newpath.mkdir(exists_ok)  # Overriding defaut behavior on exists_ok
        return newpath

    def _start_adb_server(self):
        logger.debug('Starting ADB server')
        self._exec(('start-server',))

    def _adb_execute(self, command: Iterable, capture_output=True, shell=False) -> Union[str, None]:
        """
        Executes a command with the adb binary, and get output or not.
        :param command: an iterable containing the command, eg ('devices','-l'). Do not pass bare string.
        :param capture_output: Bool to return output produced or not (utf-8 encoding)
        :param shell: Passed to the subprocess.run() call
        :return: None if not capture_output, else a string for the output produced
        """
        logger.debug('Executing command with adb : ({})'.format(' '.join(command)))
        # TODO: Async or not ?
        rep = subprocess.run((self.adb.resolve(), *command),
                             stdout=subprocess.PIPE if capture_output else None,
                             stderr=subprocess.STDOUT if capture_output else None,
                             encoding='utf-8',
                             shell=shell
                             )
        if capture_output:
            return str(rep.stdout)

    def _exec_stdout(self, command: Iterable, shell=False) -> str:
        """
        Executes a command with ADB, with ouput capture
        :param command: an iterable containing the command, eg ('devices','-l'). Do not pass bare string.
        :param shell: Passed to the subprocess.run() call
        :return: The output produced by the command
        """
        return self._adb_execute(command, capture_output=True, shell=shell)

    def _exec(self, command: Iterable, shell=False) -> None:
        """
        Executes a command with ADB, with no ouput capture
        :param command: an iterable containing the command, eg ('devices','-l'). Do not pass bare string.
        :param shell: Passed to the subprocess.run() call
        :return: None
        """
        self._adb_execute(command, capture_output=False, shell=shell)

    def list_device_info(self) -> dict:
        """
        TODO: WARNING: The parser is not resilient at all
        :return: a dict containing 'serialno', 'state', 'product', 'model', 'device', 'transport_id', all as strings
        """
        logger.debug('Listing devices')
        resp = self._exec_stdout(('devices', '-l'))
        # parsing response: get 1 line for each phone
        phones = [line for line in resp.split('\n') if line and line[0] not in ('', '*', 'L')]
        # raise errors if no phone or multiple phone is connected
        if not phones:
            logger.error('No phone found')
            raise PhoneNotFoundException(
                'No connected phone found, please make sure you enabled USB debugging on the phone, and '
                'have a working cable. You may have to authorize the computer on first cable '
                'connection.'
            )
        if len(phones) > 1:
            logger.error('Multiple phones found')
            raise MultiplePhonesException(
                'Multiple phones have been found, this version does currently allow '
                'only one phone at a time.'
            )

        try:
            resp_splitted = phones[0].split()
            # We have one phone connected, parse infos and fill dict
            phone_infos = {
                'serialno': resp_splitted[0],            # serial number
                'state': resp_splitted[1],                           # Union['device','offline','no device']
                'product': resp_splitted[2].split(':')[1],                         # dont know what this is
                'model': resp_splitted[3].split(':')[1],                           # Public model code
                'device': resp_splitted[4].split(':')[1],                          # dont know what this is
                'transport_id': resp_splitted[-1].split(':')[1]                     # in case of multiple phones ?
            }
        except (ValueError, TypeError, IndexError) as e:
            logger.error('Unable to parse list devices response', exc_info=True)
            logger.error('Got : {}'.format(resp))
            raise AdbException('Exception during list devices parsing') from e

        return phone_infos

    def get_battery_status(self) -> float:
        ...

    def get_screen_size(self) -> Tuple[int, int]:
        ...

    def is_model_connected(self, model: str):
        logger.debug('Asking if model {} is connected'.format(model))
        return self.list_device_info().get('model').lower() == model.lower()

    def screenshot(self):
        logger.debug('Taking screenshot')
        self._exec(('exec-out', 'screencap -p', '>', self.screenshotsdir / Path('img.png')), shell=True)

    def tap(self, x, y):
        logger.debug('Tapping screen at {} {}'.format(x, y))
        self._exec(('shell', 'input', 'tap', str(x), str(y)))

    def _autoselect_phone_lib(self):
        logger.debug('Autoselecting phone library')
        model = self.list_device_info().get('model')
        if not model:
            logger.error('Unable to get phone model')
            raise PhoneNotFoundException('Unable to get the phone model')

        model = model.upper().replace('_', '-')
        for phone in swy.data.phones.phones:
            if phone.get('reference') == model:
                # get this phone lib
                logger.debug('Importing module for phone {}'.format(model))
                return import_module('swy.data.phones.'+phone.get('module_name'))

        logger.warning('Unable to find phone via direct lookup, trying compatibility mode')
        # If we have not found it the direct way, we now try the compatibility table
        for phone in swy.data.phones.phones:
            if model in phone.get('compatibility'):
                logger.warning('No direct match for the phone reference, loading '
                               'module from compatibility table. Strange behaviour'
                               ' may happen')
                logger.debug('Importing module for phone {}'.format(model))
                return import_module('swy.data.phones.' + phone.get('module_name'))

        logger.error('Unable to find a library for the connected phone {}'.format(model))
        raise PhoneLibNotFoundException('No pre configured library has been found for your phone.'
                                        ' Your phone may not be supported for the moment.'
                                        ' You can collect the data yourself and send it to the repository,'
                                        ' with a pull request or anything. (swy/data/phones/<yourphonemodel>'
                                        )

    def quit(self):
        self._delete_adb()

    def _make_adb_available(self) -> Path:
        """
        This functions makes the adb binaries available to the application.
        Current implementations does not check if binaries have already been downloaded,
        and stores them in a os dependant new temporary folder.
        :return: Path to adb binary
        """

        # Static google urls for adb binaries
        adb_dl_url = {
            'linux': 'https://dl.google.com/android/repository/platform-tools-latest-linux.zip',
            'windows': 'https://dl.google.com/android/repository/platform-tools-latest-windows.zip'
        }

        # Get current platform link
        try:
            url = adb_dl_url[platform.system().lower()]
        except KeyError:
            logger.error('Did not found an adb download for OS...', exc_info=True)
            raise OSError('Unsupported Operating System, found {}'.format(platform.system().lower()))

        logger.debug('Downloading adb from url : {}'.format(url))

        # Download binaries into directory
        req = requests.get(url)
        if req.status_code != 200:
            logger.error('Unable to download ADB binaries, got HTTP {} from {}'.format(req.status_code, url))
            raise ConnectionError('Problem downloading (HTTP {}) from {}'.format(req.status_code, url))

        # Write content to disk
        try:
            with open(str(self.tmpdir / 'archive.zip'), 'wb') as f:
                f.write(req.content)
        except IOError:
            logger.error('Unable to write adb binaries downloaded data to disk', exc_info=True)
            raise

        # Get archive name (vary with versions)
        zip_archive = tuple(self.tmpdir.glob('archive.zip'))
        if not zip_archive:
            logger.error('Unable to find the downloaded zip file in {}'.format(self.tmpdir))
            raise FileNotFoundError('Unable to locate the downloaded zip file under {}'.format(self.tmpdir))
        else:
            zip_archive = zip_archive[0]

        # unzip everything
        try:
            with zipfile.ZipFile(zip_archive) as archive:
                archive.extractall(self.tmpdir / 'adb')
        except zipfile.BadZipFile as e:
            logger.error('Unable to unzip zip archive to temporary directory, zip may be corrupted.', exc_info=True)
        except Exception:
            logger.error('Error during archive unziping', exc_info=True)
            raise

        # test adb presence
        real_adb = [el for el in (self.tmpdir / Path('adb/platform-tools')).glob('adb*') if el.stem == 'adb']
        if not real_adb:
            logger.error('Unable to find previously downloaded and unzipped adb binaries')
            raise FileNotFoundError('Unable to locate ADB executable in {}'.format(self.tmpdir))
        else:
            logger.debug('Successfully got adb binaries downloaded and found.')
            return real_adb[0]

    def _delete_adb(self):

        # We intentionnaly dont delete the whole folder, in case we need the logs
        # Deleting adb binaries should be enough, as these are the big files.
        # The rest can be cleaned by the OS.
        logger.debug('Clearing files from temporary folder')
        paths_to_delete = (
            self.tmpdir / 'archive.zip',
            self.tmpdir / 'adb'
        )

        for path in paths_to_delete:
            try:
                if path.is_file:
                    path.unlink()  # file
                else:
                    rmtree(path, ignore_errors=True)  # directory
            except OSError as e:
                logger.error('Unable to delete {}, passing... {}'.format(path, e))
                # Intentionnal pass
