from .. import unicode
from ..completer.style import CompleterStyle


class LoaderStyle:
    """
    style used by loader ui class
    """

    def __init__(self, width=5, cursor_width=3, fill=unicode.FULL_BLOCK, empty=' ', prefix='[', postfix=']'):
        self.width = width
        self.cursor_width = cursor_width
        self.fill = fill
        self.empty = empty

        self.prefix = prefix
        self.postfix = postfix

        self._indefinite = []
        self.indefinite_index = 0

        self.generate(width, cursor_width, fill, empty, prefix, postfix)

    @staticmethod
    def default():
        return LoaderStyle()

    @staticmethod
    def ascii():
        return LoaderStyle(fill='=')

    def generate(self, width=5, cursor_width=3, fill=unicode.FULL_BLOCK, empty=' ', prefix='[', postfix=']'):

        if type(width) != int:
            raise TypeError('bar width must be of type int')

        if width <= 0:
            raise ValueError('bar width must be greater that 1')

        if type(cursor_width) != int:
            raise TypeError('cursor width must be of type int')

        if cursor_width <= 0:
            raise ValueError('cursor width must be greater that 0')

        if width < cursor_width:
            raise ValueError('cursor width must be greater than bar width')

        self.width = width
        self.cursor_width = cursor_width
        self.fill = fill
        self.empty = empty

        self.prefix = prefix
        self.postfix = postfix

        self._indefinite = []

        # all the generation math
        snake = list((self.fill * cursor_width) + (self.empty * (width * 2)))
        fallout_start = self.cursor_width - 1
        fallout_end = self.width + self.cursor_width - 1

        i = 0
        while True:
            segment = snake[fallout_start:fallout_end]
            self._indefinite.append(f"{prefix}{''.join(segment)}{postfix}")

            if all(bit == self.empty for bit in segment):
                break

            # crawl forward
            bit = snake.pop(-1)
            snake.insert(0, bit)

            i += 1

        reverse = reversed(self._indefinite[:-1])
        empty_state = self._indefinite[-1]

        self._indefinite += reverse
        self._indefinite.append(empty_state)

        self.indefinite_index = len(self._indefinite) - 1

        # for state in self.indefinite:
        #     print(state)

        # print('[', end='')
        # for i in range(self.width):
        #     print(i % 10, end='')
        # print(']')

        # print({'start': fallout_start, 'end': fallout_end, 'width': fallout_end - fallout_start})

    def indefinite(self, increment=True):
        if increment:
            self.indefinite_index = (self.indefinite_index + 1) % len(self._indefinite)
        return self._indefinite[self.indefinite_index]

    def definite(self, value: float) -> str:
        """
        :param value: float between 0 (inclusive) and 1 (inclusive)
        :return: string denoting the amount loaded
        """
        value = max(0, value)
        value = min(1, value)
        filled = int(value * self.width)
        return f'{self.prefix}{self.fill * filled}{self.empty * (self.width - filled)}{self.postfix}'

    def to_completer(self):
        return CompleterStyle(prefix=self.prefix, postfix=self.postfix)
