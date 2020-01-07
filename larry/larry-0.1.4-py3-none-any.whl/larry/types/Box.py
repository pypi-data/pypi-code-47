import collections


class Box(collections.UserDict):
    def __init__(self, *data):
        collections.UserDict.__init__(self)
        for dat in data:
            self.update(dat)

    @classmethod
    def from_position(cls, position, calc_coordinates=False, **kwargs):
        obj = cls(position, kwargs)
        if calc_coordinates:
            obj._calc_coordinates()
        return obj

    @classmethod
    def from_coords(cls, coordinates, calc_position=False, **kwargs):
        obj = cls({'coordinates': coordinates}, kwargs)
        if calc_position:
            obj._calc_position()
        return obj

    def _calc_coordinates(self):
        self['coordinates'] = [self['left'], self['top'], self['left'] + self['width'] - 1,
                               self['top'] + self['height'] - 1]

    def _calc_position(self):
        self['left'] = self['coordinates'][0]
        self['top'] = self['coordinates'][1]
        self['width'] = self['coordinates'][2] - self['coordinates'][0] + 1
        self['height'] = self['coordinates'][3] - self['coordinates'][1] + 1

    def __missing__(self, key):
        if key == 'coordinates':
            self._calc_coordinates()
            return self['coordinates']
        else:
            raise KeyError(key)