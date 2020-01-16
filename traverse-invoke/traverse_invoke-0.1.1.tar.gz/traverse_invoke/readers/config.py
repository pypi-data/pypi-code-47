from configparser import ConfigParser

def _dict_chain(root, path):
    curr = root
    print(curr,path)
    for key in path:
        x = curr.get(key,{})
        curr[key] = x
        curr = x
    return curr

def get_config(filename):
    config = ConfigParser()
    config.read_file(open(filename))
    root = config.defaults()
    root = dict(root)
    #my_config_parser_dict = {s:dict(config.items(s)) for s in config.sections()}
    #print(my_config_parser_dict)
    for section in config.sections():
        path = section.split('.')
        last = _dict_chain(root, path)
        last.update(config[section])
    return root

