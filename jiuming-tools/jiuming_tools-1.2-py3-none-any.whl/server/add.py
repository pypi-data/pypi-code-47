import yaml

y_file = open('./test.yaml', 'w+')


def add():
    s = {'name': '111111'}
    yaml.safe_dump(s, y_file)
