class jsonPos:
    def __init__(self):
        self.Pos = []

    def add(self, type, key):
        if type not in [list, dict]:
            raise Exception()
        self.Pos.append((type, key))

    def __repr__(self):
        rstr = ''
        for p in self.Pos:
            if p[0] == list:
                rstr += '['
                rstr += str(p[1])
            else:
                rstr += '{'
                rstr += str(p[1])
        return rstr
