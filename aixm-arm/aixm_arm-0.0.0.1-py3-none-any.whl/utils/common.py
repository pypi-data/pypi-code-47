# @Time   : 2019-01-09
# @Author : zhangxinhao
import os
import sys
import logging
import logging.handlers
import json

class __path_object:
    pass

def __init_path():
    file_path = os.path.realpath(sys.argv[0])
    index = file_path.find('/src/')
    if index == -1:
        print('src 目录不存在!')
        sys.exit(0)
    project_path = file_path[:index]
    __path_object.project_path = project_path
    __path_object.data_path = os.path.join(project_path, 'data')
    __path_object.models_path = os.path.join(project_path, 'models')
    __path_object.conf_path = os.path.join(project_path, 'conf')
    __path_object.logs_path = os.path.join(project_path, 'logs')

    config_path = os.path.expanduser('~/.aixm/config.json')
    if os.path.isfile(config_path):
        with open(config_path) as f:
            path_dict = json.load(f)
            data_path = path_dict.get('data_path')
            if data_path is not None:
                __path_object.data_path = data_path
            models_path = path_dict.get('models_path')
            if models_path is not None:
                __path_object.models_path = models_path

    print('PROJECT_PATH=' + __path_object.project_path)
    print('DATA_PATH=' + __path_object.data_path)
    print('MODELS_PATH=' + __path_object.models_path)
    print('CONF_PATH=' + __path_object.conf_path)
    print('LOGS_PATH=' + __path_object.logs_path)
    print('*' * 36)


__init_path()

def reset_path():
    project_path = __path_object.project_path
    __path_object.data_path = os.path.join(project_path, 'data')
    __path_object.models_path = os.path.join(project_path, 'models')
    __path_object.conf_path = os.path.join(project_path, 'conf')
    __path_object.logs_path = os.path.join(project_path, 'logs')


def relative_project_path(*args):
    return os.path.realpath(os.path.join(__path_object.project_path, *args))


def relative_data_path(*args):
    return os.path.realpath(os.path.join(__path_object.data_path, *args))


def relative_conf_path(*args):
    return os.path.realpath(os.path.join(__path_object.conf_path, *args))


def relative_models_path(*args):
    return os.path.realpath(os.path.join(__path_object.models_path, *args))


def relative_logs_path(*args):
    return os.path.realpath(os.path.join(__path_object.logs_path, *args))


class Logger:

    formatter = logging.Formatter("%(asctime)s-%(filename)s[%(lineno)d]-%(levelname)s: %(message)s")

    def __init__(self, level, filename, is_debug, rotating_conf={'when':'W0','interval':1,'backupCount':53}):
        self.logger = logging.getLogger(filename)
        self.logger.setLevel(level)
        os.makedirs(relative_project_path('logs'), exist_ok=True)
        logfile = relative_project_path('logs', filename +".log")
        fh = logging.handlers.TimedRotatingFileHandler(logfile, when=rotating_conf['when'],
                                                interval=rotating_conf['interval'],
                                                backupCount=rotating_conf['backupCount'])
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        if is_debug:
           self.log_to_console()

    def log_to_console(self):
        ch = logging.StreamHandler()
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

    def __call__(self):
        return self.logger

_log_console = None # type: logging.Logger

def is_init_logger():
    return _log_console is not None

def init_logger(filename=None, level='DEBUG', is_log_console=True):
    global _log_console
    if filename is None:
        run_path = os.path.realpath(sys.argv[0])
        filename = run_path[run_path.rfind('/') + 1:-3]
        if 'start' in filename:
            filename = 'console_' + filename
        else:
            filename = 'console'
    _log_console = Logger(level, filename, is_log_console).logger

def log() -> logging.Logger:
    if _log_console is None:
        raise Exception('log error, not init')
    return _log_console

_config_dict = dict()


def local_config(config_name='config.json'):
    config = _config_dict.get(config_name)
    if config is None:
        with open(relative_conf_path(config_name)) as f:
            config = json.load(f)
            _config_dict[config_name] = config
    if config is None:
        raise Exception(config_name + ' is not exist!')
    return config


def set_local_config(config_name, config):
    _config_dict[config_name] = config


__all__ = ['reset_path',
           'relative_project_path',
           'relative_data_path',
           'relative_conf_path',
           'relative_models_path',
           'relative_logs_path',
           'is_init_logger',
           'init_logger',
           'log',
           'local_config',
           'set_local_config']
