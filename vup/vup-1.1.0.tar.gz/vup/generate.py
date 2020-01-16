import json
import re

from . import setting
from . import update


def __version_string(pref: setting.Setting, lock: setting.Lock):
    s = ''
    for t in ('major', 'minor', 'build', 'revision'):
        if getattr(pref, t).type != setting.Type.Null:
            s += str(getattr(lock, t).current) + '.'

    return s.rstrip('.')


def do_update(pref, lock):
    update.do_update(pref, lock, **{k: False for k in ('major', 'minor', 'build', 'revision')})


def __generate_c_cxx(fp, pref, lock, is_cxx, cxx_version, support_inline_variable):
    print('#ifndef VUP_AUTO_GENERATE_HEADER', file=fp)
    print('#define VUP_AUTO_GENERATE_HEADER', file=fp)

    print('', file=fp)
    if is_cxx:
        if cxx_version >= 17:
            print('#include <string_view>', file=fp)
        print('#include <string>', file=fp)
        print('', file=fp)
        print('namespace vup {', file=fp)
        if support_inline_variable:
            print(
                '    inline constexpr std::string_view Version = "{}";'.format(__version_string(pref, lock)),
                file=fp)
        print(
            '    inline std::string GetVersion() {' + 'return "{}";'.format(__version_string(pref, lock)) + '}',
            file=fp)
        print('} // namespace vup', file=fp)
    else:
        print(
            '    inline std::string VupGetVersion() {' + 'return "{}";'.format(__version_string(pref, lock)) + '}',
            file=fp)

    print('', file=fp)
    print('#endif // VUP_AUTO_GENERATE_HEADER', file=fp)


def __generate_python(fp, pref: setting.Setting, lock: setting.Lock):
    to_string_format = "'"
    to_string_data = []

    for t in ('major', 'minor', 'build', 'revision'):
        if getattr(pref, t).type != setting.Type.Null:
            to_string_format += '{}.'
            to_string_data.append(t)
    to_string_data = ', '.join(to_string_data)
    to_string = to_string_format.rstrip('.') + "'.format(" + to_string_data + ')'

    print('class VupVersion:', file=fp)
    print('    def __init__(self, major, minor, build, revision):', file=fp)
    print('        self.__major = {}'.format(lock.major.current), file=fp)
    print('        self.__minor = {}'.format(lock.minor.current), file=fp)
    print('        self.__build = {}'.format(lock.build.current), file=fp)
    print('        self.__revision = {}'.format(lock.revision.current), file=fp)
    print('', file=fp)
    print('    @property', file=fp)
    print('    def major(self):', file=fp)
    print('        return self.__major', file=fp)
    print('', file=fp)
    print('    @property', file=fp)
    print('    def minor(self):', file=fp)
    print('        return self.__minor', file=fp)
    print('', file=fp)
    print('    @property', file=fp)
    print('    def build(self):', file=fp)
    print('        return self.__build', file=fp)
    print('', file=fp)
    print('    @property', file=fp)
    print('    def revision(self):', file=fp)
    print('        return self.__revision', file=fp)
    print('', file=fp)
    print('    def __str__(self):', file=fp)
    print('        return {}'.format(to_string))
    print('', file=fp)
    print('', file=fp)
    print('version = VupVersion({major}, {minor}, {build}, {revision})'.format(**{
        k: getattr(lock, k).current for k in ['major', 'minor', 'build', 'revision']}))


def generate(args):
    with open('vup.json') as fp:
        pref = setting.Setting.create(json.load(fp))
    with open('vup-lock.json') as fp:
        lock = setting.Lock.create(json.load(fp))

    if args.pre_update:
        do_update(pref, lock)

    file = args.output
    is_cxx = args.language == 'c++'
    file += '.hpp' if is_cxx else '.h'

    vs = re.sub(r'[^\d]+(\d+)', r'\1', args.standard)
    cxx_version = int(vs)
    support_inline_variable = cxx_version >= 17

    with open(file, 'w') as fp:
        if args.language == 'python':
            __generate_python(fp, pref, lock)
        else:
            __generate_c_cxx(fp, pref, lock, is_cxx, cxx_version, support_inline_variable)

    if args.post_update:
        do_update(pref, lock)
