import crccheck.crc


class Checksum:
    def __init__(self, data=None):
        self._crc = crccheck.crc.Crc32c()
        if data is not None:
            self.update(data)

    def update(self, data):
        self._crc.process(data)

    def final(self):
        return self._crc.final()
