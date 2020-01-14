import json

from Spitzer.host import get_interfaces
from Spitzer.print import print_error, print_warning

#handler for the three config files, every setting can the changed here
path = __file__[:-9]

config = open(path + 'config.json', 'r').read()
config = json.loads(config)

data = open(path + 'data.json', 'r').read()
data = json.loads(data)

def get_data(key):
    try: 
        return data[key]
    except KeyError:
        print_error('[!] key not found!')
        return None

def get_config(key):
    try:
        value = config[key][0]
        if value == 'True':
            return True
        elif value == 'False':
            return False
        else:
            return value

    except KeyError as e:
        print(e)
        print_error('[!] key not found!')
        return None

def set_config(key, value):
    config[key][0] = value

def print_config():
    printdict(config)

def printdict(diction):
    for key, value in diction.items():
            if isinstance(value, dict):
                print('\n' + key)
                print('=====================================')
                printdict(value)
            else:    
                spaces = 20*' '
                spaces = spaces[-len(str(value)):]
                print("%-20s %-20s %-30s" % (str(key), str(value[0]), str(value[1])))
    print()

def set_value(args):
    if len(args) < 2:
        print_error('Not enough values')
        return

    
    key = args[0]
    value = args[1]

    if len(args) > 2:
        args.pop(0)
        value = ' '.join(args)
    
    if key == 'interface':
        set_ip(value)

    if key in config:
        set_config(key, value)
    else:
        for val in config.items():
            if isinstance(val[1], dict) and key in val[1]:
                config[val[0]][key][0] = value
                return

        print_error('key not found')

def get_path():
    #full path with / at the end
    return path

def complete_key(key_part):
    result = []

    for key in config:
        if key.startswith(key_part):
            result.append(key)

    return result

def set_ip(interface):
    interfaces = get_interfaces()
    
    if interface is None:
        interface = get_config('interface')

    if interface not in interfaces:
        print_warning('Interface not found! make sure you use an exsisting interface')
        return

    set_value(['ip', interfaces[interface]])
    print_warning('Changed IP to ' + interfaces[interface])