import sys
import os

sys.path.insert(0, os.path.abspath("."))
from appteka.pyqt import testing
from appteka.pyqtgraph.waveform import MultiWaveform


class TestMultiWaveform(testing.TestDialog):
    """Test case for MultiWaveform widget."""
    def __init__(self):
        super().__init__()
        self.resize(600, 600)

    def test_top_axis(self):
        # Given multiwaveform
        w = MultiWaveform(self)
        self.set_widget(w)

        # When add plot
        w.add_plot('a', title='plot A')

        # Then there is top axis
        self.add_assertion("There is top axis")

    def test_scaling(self):
        # Scenario: scaling with keys CONTROL and SHIFT
        w = MultiWaveform(self)
        self.set_widget(w)

        w.add_plot('a', title='plot A')
        w.add_plot('b', title='plot B')

        w.update_data('a',
                      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [1, 2, 0, 3, 1, 2, 3, 4, 1, 3])

        w.update_data('b',
                      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [2, 1, 1, 1, 4, 6, 2, 3, 4, 3])

        self.add_assertion("both axis scaling with mouse wheel")
        self.add_assertion("x-scaling with CONTROL pressed")
        self.add_assertion("y-scaling with SHIFT pressed")


testing.run(TestMultiWaveform)
