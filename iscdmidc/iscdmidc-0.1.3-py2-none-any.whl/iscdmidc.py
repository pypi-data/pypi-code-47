from __future__ import print_function
import os, sys

#__version__ = "0.1.2"

TYPE = {
    0:  'bios',
    1:  'system',
    2:  'base board',
    3:  'chassis',
    4:  'processor',
    7:  'cache',
    8:  'port connector',
    9:  'system slot',
    10: 'on board device',
    11: 'OEM strings',
    15: 'system event log',
    16: 'physical memory array',
    17: 'memory device',
    19: 'memory array mapped address',
    24: 'hardware security',
    25: 'system power controls',
    27: 'cooling device',
    32: 'system boot',
    41: 'onboard device',
    }


def parse_dmi(content):
    """
    Parse the whole dmidecode output.
    Returns a list of tuples of (type int, value dict).
    """
    info = []
    lines = iter(content.strip().splitlines())
    while True:
        try:
            line = next(lines)
        except StopIteration:
            break

        if line.startswith('Handle 0x'):
            typ = int(line.split(',', 2)[1].strip()[len('DMI type'):])
            if typ in TYPE:
                info.append((TYPE[typ], _parse_handle_section(lines)))
    return info


def _parse_handle_section(lines):
    """
    Parse a section of dmidecode output

    * 1st line contains address, type and size
    * 2nd line is title
    * line started with one tab is one option and its value
    * line started with two tabs is a member of list
    """
    data = {
        '_title': next(lines).rstrip(),
        }

    for line in lines:
        line = line.rstrip()
        if line.startswith('\t\t'):
            data[k].append(line.lstrip())
        elif line.startswith('\t'):
            k, v = [i.strip() for i in line.lstrip().split(':', 1)]
            if v:
                data[k] = v
            else:
                data[k] = []
        else:
            break

    return data


def system_uuid():
    if os.isatty(sys.stdin.fileno()):
        content = _get_output()
    else:
        content = sys.stdin.read()
    
    info = parse_dmi(content)
    return _system_uuid(info)


def _system_uuid(info):
    def _get(i):
        return [v for j, v in info if j == i]
    
    system = _get('system')[0]
    
    return system['UUID'].encode('utf-8')

def _get_output():
    import subprocess
    try:
        output = subprocess.check_output(
        'PATH=$PATH:/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin '
        'sudo dmidecode', shell=True)
    except Exception as e:
        print(e, file=sys.stderr)
        if str(e).find("command not found") == -1:
            print("please install dmidecode", file=sys.stderr)
            print("e.g. sudo apt install dmidecode",file=sys.stderr)

        sys.exit(1)
    return output.decode()


if __name__ == '__main__':
    system_uuid()
