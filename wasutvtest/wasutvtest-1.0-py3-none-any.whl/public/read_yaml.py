import yaml


class read_yaml:
    """
    :param yaml_path
    :return dict(file)

    """
    def __init__(self, path):
        self.path = path

    def get_yaml_file(self):
        yaml_file = open(self.path, 'r', encoding='utf-8').read()
        return yaml_file

    def load_file(self):
        file = yaml.full_load(self.get_yaml_file())
        return file
