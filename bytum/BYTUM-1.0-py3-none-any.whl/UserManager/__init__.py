log = 0
class User():
    def __init__(self, name, password):
        self.name = name
        self.password = password
    def save_(self):
        with open((self.name)+'.txt',mode='a',encoding='utf-8') as f:
            f.write(self.name)
            f.write('    ')
            f.write(self.password)

