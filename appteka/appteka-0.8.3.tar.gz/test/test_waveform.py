import sys
import os

from PyQt5 import QtWidgets

sys.path.insert(0, os.path.abspath("."))
from appteka.pyqt import testing
from appteka.pyqtgraph.waveform import Waveform, MultiWaveform


class TestWaveform(testing.TestDialog):
    """Test suite for Waveform widget."""
    def __init__(self):
        super().__init__()
        self.resize(600, 600)

    def test_just_visible(self):
        w = Waveform()
        self.set_widget(w)
        text = "- Widget is visible"
        self.set_text(text)

    def test_xlabel(self):
        w = Waveform(self, "Time [sec]")
        self.set_widget(w)
        text = "- x label is 'Time [sec]'"
        self.set_text(text)

    def test_time_axis_false(self):
        w = Waveform(self, time_axis=False)
        self.set_widget(w)
        w.update_data([0, 1, 2, 3], [1, 2, 1, 2])
        text = "x values are usual numbers from 0 to 3"
        self.set_text(text)

    def test_time_axis_true(self):
        w = Waveform(self, time_axis=True)
        self.set_widget(w)
        w.update_data([0, 1, 2, 3], [1, 2, 1, 2])
        text = "x values are time values"
        self.set_text(text)

    def test_scaling(self):
        # Scenario: scaling with keys CONTROL and SHIFT
        w = Waveform(self)
        self.set_widget(w)
        w.update_data([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [1, 2, 0, 3, 1, 2, 3, 4, 1, 3])

        text = "- both axis scaling with mouse wheel\n"
        text += "- x-scaling with CONTROL pressed\n"
        text += "- y-scaling with SHIFT pressed"

        self.set_text(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    TestWaveform().run()
    sys.exit(app.exec())
