from rascal.calibrator import Calibrator
from rascal.util import load_calibration_lines

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import json

from scipy.signal import find_peaks

with open("./keck_deimos_830g_l_PYPIT.json") as json_file:  
    data = json.load(json_file)
    spectrum = np.array(data["spec"])


peaks, _ = find_peaks(spectrum, height=1000)

fig = plt.figure()
ax = fig.add_subplots(0)
ax.plot(spectrum)
ax.hlines(peaks, 0, 1000)
plt.show()

c = Calibrator(peaks, elements = ["Ne", "Ar", "Kr"],
                      min_wavelength=5500,
                      max_wavelength=6500,
                      )

best_p = c.fit(3)
print(best_p)
c.plot_fit(spectrum, best_p)

