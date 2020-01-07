class PathBuilder:
    def __init__(self,template:str):
        self.template = template

    def build(self,name):
        return self.template.format(name=name)
