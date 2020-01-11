import os
def main():
    if os.path.exists("./config.ini"):
        raise Exception("Existing file config.ini")
    if os.path.exists("./config.py"):
        raise Exception("Existing file config.py")
    with open("./config.ini","a") as f:
        f.write("""
[configman]
username=configman

[configman.dev]
username=devname
api=qwe

[configman.dev.api]
username=devname
api=qwe
        """)
    with open("./config.py","w") as f:
        f.write("""# coding:utf-8
from configparser import RawConfigParser as _ConfigParser
import os as _os
import sys as _sys
from copy import copy as _copy
# 用os模块来读取
_curpath = _os.path.dirname(_os.path.realpath(__file__))
_cfgpath = _os.path.join(_curpath, "config.ini")  # 读取到本机的配置文件
print("="*100)
print('文件位置：', _cfgpath)


# 添加getjson功能
class _PowerConfigParser(_ConfigParser):
    def optionxform(self, optionstr):
        return optionstr

    def geteval(self, section, option):
        result = self.get(section, option)
        try:
            return eval(result)
        except:
            return result
try:
    _section = _sys.argv[1]
    _list_session = _section.split('.')
    print("当前项目配置：", _section)
except:
    print("未传入项目名称")
    print("强行结束应用")
    _sys.exit(1)
else:
    _names = []
    if '.' in _section:
        for _index in range(len(_list_session)):
            _n,*_ = _section.rsplit('.', _index)
            _names.insert(0,_n)
    print("加载配置顺序：",_names)
    _conf = _PowerConfigParser()
    _conf.read(_cfgpath, encoding="utf-8")
    _sections = _conf.sections()
    # sections
    print("所有项目配置：" ,   _sections)
    def _run(name):
        # 调用读取配置模块中的类
        _options = _conf.options(name)
        for _option in _options:
            _values = _conf.geteval(name, _option)
            globals()[_option] = _values
    for __name in _names:
        _run(__name)
    d = _copy(globals())
    for k,v in d.items():
        if not k.startswith('_'):
            print("%-20s | %-14s | %s" % (k, type(v), v))

print("="*100)""")

if __name__ == '__main__':
    main()