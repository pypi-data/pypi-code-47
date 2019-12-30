class Dimensions():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class LdrawDimensions(Dimensions):
    def __init__(self, x, y, z, flag_convert_from_stark=False):
        if not flag_convert_from_stark:
            super().__init__(x, y, z)
        else:
            x, y, z = self.convertFromStarkDimensions(x,y,z)
            super().__init__(x, y, z)

    def convertToStarkDimensions(self, x, y, z):
        return x / 20, y / -8, z / 20
    def convertFromStarkDimensions(self, x, y, z):
        return x * 20, y * -8, z * 20

class StarkDimensions(Dimensions):
    def __init__(self, x, y, z, flag_convert_from_ldraw=False):
        if not flag_convert_from_ldraw:
            super().__init__(x, y, z)
        else:
            x, y, z = self.convertFromLdrDimensions(x,y,z)
            super().__init__(x, y, z)

    def convertToLdrDimensions(self, x, y, z):
        return int(x * 20), int(y * -8), int(z * 20)
    def convertFromLdrDimensions(self, x, y, z):
        return int(x / 20), int(y / -8), int(z / 20)