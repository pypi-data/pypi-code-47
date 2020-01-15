__version__ = "0.0.7"

# custom submodules
from .core import *
from .experimental import *

# useful common external packages
import os
import re
import sys
import json
import random
import sklearn
import pendulum
import numpy as np
import pandas as pd
import chartify as ch
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from tqdm import tqdm

# nice-to have styling, utils
from IPython.display import clear_output, display
plt.style.use("ggplot")
pd.set_option("display.max_colwidth", 300)