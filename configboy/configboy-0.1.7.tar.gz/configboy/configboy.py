import sys
from pathlib import Path
from configparser import RawConfigParser as _ConfigParser

class _PowerConfigParser(_ConfigParser):
    def optionxform(self, optionstr):
        return optionstr

    def geteval(self, section, option):
        result = self.get(section, option)
        try:
            return eval(result)
        except:
            return result

class Config:
    def __init__(self):
        self._dict = {}
        self._section = None
        self.read_ini()
    def read_ini(self,path='./config.ini'):
        p = Path(sys.argv[0])
        print("=" * 100)
        _ini_path = p.joinpath(p.parent, path)
        print('文件位置：', _ini_path)
        _conf = _PowerConfigParser()
        _conf.read(_ini_path, encoding="utf-8")
        # _sections = _conf.sections()
        # 调用读取配置模块中的类
        # _options = _conf.options("base")
        # for _option in _options:
        #     _values = _conf.geteval("base", _option)
        #     self._dict[_option] = _values
        #
        # configuration = _conf.geteval("config",'configuration')
        # self._section = configuration
        # _options = _conf.options(configuration)
        # for _option in _options:
        #     _values = _conf.geteval(configuration, _option)
        #     self._dict[_option]=_values
        _section = _conf.geteval("config", 'configuration')
        _list_session = _section.split(".")
        _names = []
        if '.' in _section:
            for _index in range(len(_list_session)):
                _n, *_ = _section.rsplit('.', _index)
                _names.insert(0, _n)
        else:
            _names.append(_section)
        print("加载配置顺序：", _names)
        # _conf = _PowerConfigParser()
        # _conf.read(_cfgpath, encoding="utf-8")
        _sections = _conf.sections()
        # sections
        print("所有项目配置：", _sections)
        for __name in _names:
            self._run(_conf,__name)
        for k, v in self._dict.items():
            if not k.startswith('_'):
                print("%-20s | %-14s | %s" % (k, type(v), v))
        print("=" * 100)
    def _run(self,_conf,name):
        # 调用读取配置模块中的类
        _options = _conf.options(name)
        for _option in _options:
            _values = _conf.geteval(name, _option)
            self._dict[_option]=_values

    def printall(self):
        print(self._dict)
        return self._dict

    def __getattr__(self, item):
        result = self._dict.get(item)
        if result is None:
            raise KeyError("arg <%s> not in section <%s>"%(item,self._section))
        return result

    def __call__(self, path):
        self._dict = {}
        self.read_ini(path)
config = Config()