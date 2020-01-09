import threading
import time

from .style import LoaderStyle
from ..completer import Completer
from ..line import delete_line


class BrushThread(threading.Thread):
    _exception: Exception

    def __init__(
            self,
            value=-1,
            total=1,
            message='',
            frequency=20,
            style=LoaderStyle.default(),
            *args, **kwargs
    ):
        """
        :param value: current progress value
        :param total: total progress value
        :param message: progress bar message
        :param frequency: number of refreshes per second
        :param style: progress style
        """
        # threading specific
        super(BrushThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

        # drawing specific
        self._message = message
        self._frequency = frequency
        self._style = style

        # values
        self._total = total
        self._value = value

        # error
        self._exception = None

        # misc
        self._timer = 1 / frequency

    @property
    def stopped(self) -> bool:
        return self._stop_event.is_set()

    @stopped.setter
    def stopped(self, val: bool):
        if val:
            self._stop_event.set()

    # misc
    @property
    def style(self):
        return self._style

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

        delete_line()
        self._next(increment=False)

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, value):
        self._frequency = value
        self._timer = 1 / self.frequency

    # values
    @property
    def total(self) -> float:
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    # error
    @property
    def exception(self) -> Exception:
        return self._exception

    @exception.setter
    def exception(self, exception):
        self._exception = exception

    def run(self):
        """
        Starts the thread
        """
        while True:

            # draws the progress bar according to value
            self._next()

            # if thread stopped, draw a completer depending on exception status
            if self.stopped:
                delete_line()
                c = Completer(f'{self.message}', self.style.to_completer()).init()
                if self.exception is None:
                    c.complete()
                else:
                    c.fail(s=' '.join((str(i) for i in self.exception.args)))
                return

            # pause thread execution for 1 / self.frequency to sync to drawing frequency
            time.sleep(self._timer)

    def _next(self, increment=True):
        if self.value < 0:
            print(f'\r{self.style.indefinite(increment)} {self.message}', end='')
        else:
            print(f'\r{self.style.definite(self.value / self.total)} {self.message}', end='')

    def print(self, s):
        """
        Proper way to print something when progress bar is being displayed
        avoids concatenation of progress bar and :param s:

        :param s: string to print
        :type s: able to be cast to str
        """
        delete_line()
        print(f'\r{s}')
