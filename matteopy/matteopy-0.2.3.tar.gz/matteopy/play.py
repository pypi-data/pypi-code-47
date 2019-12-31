from matteopy.utils.package_data import get_path_of_data_dir
from glob import glob
import os
import numpy as np
from pydub import AudioSegment
from pydub.playback import play


files = glob(os.path.join(get_path_of_data_dir(),'matteo*' ))



def playsound():

    # get a random sound
    
    f = np.random.choice(files)

    sound = AudioSegment.from_file(f)

    play(sound)
