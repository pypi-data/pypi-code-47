import numpy as np
import matplotlib.pyplot as plt
from photonpy.smlmlib.gaussian import Gaussian
from photonpy.smlmlib.context import Context
import math
import os
import tifffile


def generate_storm_movie(gaussian, emitterList, numframes=100, imgsize=512, intensity=500, bg=2, sigma=1.5, p_on=0.1):
    frames = np.zeros((numframes, imgsize, imgsize), dtype=np.uint16)
    emitters = np.array([[e[0], e[1], sigma, sigma, intensity] for e in emitterList])

    on_counts = np.zeros(numframes, dtype=np.int32)

    for f in range(numframes):
        frame = bg * np.ones((imgsize, imgsize), dtype=np.float32)
        frame_emitters = emitters * 1
        on = np.random.binomial(1, p_on, len(emitters))
        frame_emitters[:, 4] *= on

        frames[f] = gaussian.Draw(frame, frame_emitters)
        on_counts[f] = np.sum(on)

    return frames, on_counts


psfSigma = 3
roisize = int(2 + (psfSigma + 1) * 2)
w = 256
N = 2000
numframes = 100
R = np.random.normal(0, 0.2, size=N) + w * 0.3
angle = np.random.uniform(0, 2 * math.pi, N)
emitters = np.vstack((R * np.cos(angle) + w / 2, R * np.sin(angle) + w / 2)).T


with Context(debugMode=False) as ctx:
    gaussian = Gaussian(ctx)
    mov, on_counts = generate_storm_movie(gaussian, emitters, numframes, imgsize=w, sigma=psfSigma, p_on=20 / N)
    mov = np.random.poisson(mov)

    fn = "test_localization_queue.mp4"
    print("Saving movie to {0}".format(fn))
    os.makedirs("../data", exist_ok=True)
    tifffile.imsave("../data/palm_ring_generated.tiff", np.array(mov, dtype=np.uint16))
    # su.save_movie(mov, fn, 20)


plt.figure()
plt.imshow(mov[0])
plt.title("Frame 0")

