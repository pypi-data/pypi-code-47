from pathlib import Path
from typing import Union


def _create_tmp_subdir(tmpdir: Path, sub_dir_name: str) -> Path:
    """
    Creates a new subdirectory at the given path (appends a dir to the current allocated temporary directory)
    :param tmpdir: Parent directory
    :param sub_dir_name: Name of the new directory
    :return: the new directory path
    """
    newpath = tmpdir / Path(sub_dir_name)
    newpath.mkdir(exist_ok=True)
    return newpath


# Python 3.8 : :param: all_levels_to: typing.Literral['DEBUG', 'INFO', 'WARNING', 'ERROR','CRITICAL']
def get_log_config(tmpdir: Path, all_levels_to: str = None):
    logdir = _create_tmp_subdir(tmpdir, 'logs')
    logconfig = {
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
            'default': {
                'format': '%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s'
            }
        },

        'handlers': {
            'stream_handler': {
                'class': 'logging.StreamHandler',
                'formatter': 'default'
            },
            'file_handler': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'default',
                'filename': str(logdir / Path('swy.log')),
                'maxBytes': 1000000
            },
        },

        'loggers': {
            'app': {
                'handlers': ['stream_handler', 'file_handler'],
                'level': all_levels_to if all_levels_to else 'WARNING'
            },
            'adb': {
                'handlers': ['stream_handler', 'file_handler'],
                'level': all_levels_to if all_levels_to else 'WARNING'
            },
            'manager': {
                'handlers': ['stream_handler', 'file_handler'],
                'level': all_levels_to if all_levels_to else 'WARNING'
            }
        }
    }
    return logconfig
