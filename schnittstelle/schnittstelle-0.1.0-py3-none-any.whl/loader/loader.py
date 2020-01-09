from .drawing import BrushThread
from ..item import UItem


class Loader(UItem):
    def __init__(self, **kwargs):
        """
        keyword arguments are fed to :class:`BrushThread`

        :keyword value: progress
        :keyword total: total progress value
        :keyword message: label text
        :keyword frequency: number of refreshes per second
        :keyword style: progress style
        """
        super().__init__('')

        self.brush = BrushThread(**kwargs)
        self.brush.daemon = True

    @property
    def message(self) -> str:
        return self._message

    @message.setter
    def message(self, val):
        self._message = val

        self.brush.message = val

    def init(self):
        """
        starts the drawing brush thread and displays the progress bar
        """
        # start drawing
        self.brush.start()

        return self

    def complete(self):
        """
        stops drawing progress bar and shows check to signify execution was successfull
        """
        super().complete()

        # stop drawing
        self.brush.stopped = True

        # sanity check
        while self.brush.is_alive():
            pass

    def fail(self, error=Exception()):
        """
        stops drawing progress bar and shows cross to signify failure to execute successfully
        """
        super().fail()

        # stop drawing
        self.brush.exception = error
        self.brush.stopped = True

        # sanity check
        while self.brush.is_alive():
            pass