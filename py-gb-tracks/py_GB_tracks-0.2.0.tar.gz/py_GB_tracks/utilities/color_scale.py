import bisect


class ColorScale:

    def __init__(self, min_value=None, max_value=None, n_bins=100, colors=((65, 134, 244), (244, 65, 65))):
        self.n_bins = n_bins
        self.min_value = min_value
        self.max_value = max_value
        self.colors = colors
        self.bins = []
        self.color_scale = []
        self.data_bins = None
        self.create_color_scale()
        if self.min_value is not None and self.max_value is not None and self.n_bins is not None:
            self.create_bins()

    def __str__(self):
        '''
        String representation for a color scale:
        (r-g-b, ..., r-g-b)
        '''
        return '({})'.format(', '.join('{}-{}-{}'.format(*color) for color in self.color_scale))

    def create_color_scale(self, colors=None, n_bins=None):
        '''
        Create a color scale for any number of RGB colors.
        '''
        self.set_if_value('colors', colors)
        self.set_if_value('n_bins', n_bins)
        self.check_n_bins()
        n_bins_subset = int(self.n_bins / (len(self.colors) - 1))
        for i in range(len(self.colors) - 1):
            start_color = self.colors[i]
            end_color = self.colors[i + 1]
            self.create_bicolor_scale(start_color=start_color, end_color=end_color, n_bins=n_bins_subset)

    def create_bicolor_scale(self, start_color=None, end_color=None, n_bins=None):
        '''
        Create a color scale from two RGB colors and a number of steps.
        '''
        self.check_valid_color(start_color)
        self.check_valid_color(end_color)
        self.check_n_bins()
        steps = tuple((e - s) / n_bins for s, e in zip(start_color, end_color))
        self.color_scale += [tuple(int(channel + i * step) for channel, step in zip(start_color, steps)) for i in range(n_bins + 1)]

    def create_bins(self, min_value=None, max_value=None, n_bins=None):
        '''
        Compute bins from a min value, a max value, and a number of bins.
        Values for min_value, max_values, and n_bins will be taken from function arguments if specified.
        '''
        self.set_if_value('n_bins', n_bins)
        self.check_n_bins()
        self.set_if_value('min_value', min_value)
        self.set_if_value('max_value', max_value)
        self.check_min_max_values()
        step = (self.max_value - self.min_value) / self.n_bins
        self.bins = tuple(float(self.min_value + i * step) for i in range(self.n_bins + 1))

    def assign_bins(self, data):
        '''
        Assign values from a list to bins computed from these values.
        '''
        self.data_bins = tuple(min(bisect.bisect_left(self.bins, d), self.n_bins) for d in data)

    def assign_colors(self, data, n_bins=None):
        '''
        Assign a color to each value from an iterable.
        Compute bins and assign them to a computed color scale.
        '''
        self.set_if_value('n_bins', n_bins)
        self.check_n_bins()
        min_value = min(data)
        max_value = max(data)
        self.create_bins(min_value=min_value, max_value=max_value)
        self.assign_bins(data)
        return {data[i]: self.color_scale[b] for i, b in enumerate(self.data_bins)}

    def assign_color(self, value):
        '''
        Assign color to a value when bins have been computed.
        '''
        if self.bins is not None and value is not None:
            return self.color_scale[min(min(bisect.bisect_left(self.bins, value), self.n_bins), len(self.color_scale) - 1)]
        else:
            return None

    def set_if_value(self, attribute, value):
        '''
        Set an attribute value if value is not None.
        '''
        if value is not None:
            setattr(self, attribute, value)

    def check_n_bins(self):
        '''
        Check that the number of bins is a positive integer and greater than the number of colors specified.
        '''
        if self.n_bins is None:
            raise ValueError('Missing value for number of bins in color scale')
            exit(1)
        if not isinstance(self.n_bins, int):
            raise ValueError('Incorrect value <{}> for number of bins in color scale (must be an integer)'.format(self.n_bins))
            exit(1)
        if self.n_bins <= 0:
            raise ValueError('Incorrect value <{}> for number of bins in color scale (must be greater than 0)'.format(self.n_bins))
            exit(1)
        if self.colors and self.n_bins < len(self.colors):
            raise ValueError('Incorrect value <{}> for number of bins in color scale (must be greater than the number of colors <{}>)'.format(self.n_bins, len(self.colors)))
            exit(1)

    def check_min_max_values(self):
        '''
        Check that min and max values for the scale are positive integers with min < max.
        '''
        if self.min_value is None:
            raise ValueError('Missing value for min value in color scale')
            exit(1)
        if self.max_value is None:
            raise ValueError('Missing value for max value in color scale')
            exit(1)
        if not isinstance(self.min_value, float):
            raise ValueError('Incorrect value <{}> for min value in color scale (must be an float)'.format(self.min_value))
            exit(1)
        if not isinstance(self.max_value, float):
            raise ValueError('Incorrect value <{}> for max value in color scale (must be an float)'.format(self.max_value))
            exit(1)
        if self.min_value > self.max_value:
            raise ValueError('Min value <{}> must be smaller than max value <{}> in color scale'.format(self.min_value, self.max_value))
            exit(1)

    def check_valid_color(self, value):
        '''
        Check that a color value has correct format: (x, y, z) where x, y, and z are int between 0 and 255.
        '''
        valid = True
        if value is None:
            valid = False
        elif not isinstance(value, tuple):
            valid = False
        elif len(value) != 3:
            valid = False
        else:
            for channel in value:
                if not isinstance(channel, int):
                    valid = False
                elif channel < 0 or channel > 255:
                    valid = False
        if not valid:
            raise ValueError('Incorrect color value <{}> for in color scale (must be an RGB tuple)'.format(value))
            exit(1)

    def check_colors(self):
        '''
        Check that the colors for color scale is a tuple of RGB tuples.
        '''
        if self.colors is None:
            raise ValueError('Missing value for colors in color scale')
            exit(1)
        if not isinstance(self.colors, tuple):
            raise ValueError('Incorrect value <{}> for colors in color scale.'.format(self.colors))
            exit(1)
        for color in self.colors:
            self.check_valid_color(color)
