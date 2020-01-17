

class Calibration(object):
    def __init__(self, array):
        self.array = np.asarray(array)
        self.arrayT = self.array.T
        if self.array.shape[1] != 7:
            raise CalibrationError(
                "Invalid input data. See the docs for instructions"
            )

    @property
    def frequencies(self):
        return self.arrayT[0]

    @property
    def magnitude(self):

    @property
    def phase(self):
        




("Frequency", "f"),
    ...             ("Median Mag", "f"),
    ...             ("Phase (Rad)", "f"),
    ...             ("-1 Sigma Mag", "f"),
    ...             ("-1 Sigma Phase", "f"),
    ...             ("+1 Sigma Mag", "f"),
    ...             ("+1 Sigma Phase", "f")
