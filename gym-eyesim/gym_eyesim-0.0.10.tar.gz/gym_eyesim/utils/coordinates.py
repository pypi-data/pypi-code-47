import numpy as np

IMG_SIZE = (550, 550)
WORLD_SIZE = (3250, 3250)


def img_to_world(pos):
    if type(pos) is np.ndarray:
        pos = np.array([pos[1], IMG_SIZE[0] - pos[0]])
        return pos / np.array(IMG_SIZE) * np.array(WORLD_SIZE)
    else:
        return pos / IMG_SIZE[0] * WORLD_SIZE[0]
