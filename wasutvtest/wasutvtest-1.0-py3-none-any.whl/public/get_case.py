from WasuTvTest.public import read_yaml


class get_case:
    """
    获取用例的类
    :param  case_path
    :returns case_name,case_action

    """
    def __init__(self,path):
        self.path = path
        self.name = []
        self.action = []
        self.case = read_yaml(self.path).load_file()
    #
    # def get_yaml_file(self):
    #     yaml_file = open(self.path, 'r', encoding='utf-8').read()
    #     return yaml_file
    #
    # def load_case(self):
    #     case = yaml.full_load(self.get_yaml_file())
    #     return case

    def get_case_name(self):
        for key, value in self.case.items():
            self.name.append(value['name'])
        return self.name

    def get_case_action(self):
        for key, value in self.case.items():
            self.action.append(value['action'])
        return self.action
