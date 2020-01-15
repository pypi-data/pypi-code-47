import skimage.io as imio
import os
import pandas as pd
import numpy as np
import re

base = 'completion_export/run00000/completion'
side_ = 'bottom'

print([fnm for fnm in
                   sorted(os.listdir(base), key=lambda fnm: int(re.match('\w+_(\d+)_\w+', fnm).group(1)))
                   if 'original' in fnm and side_ in fnm])

original_images = [imio.imread(os.path.join(base, fnm)) for fnm in
                   sorted(os.listdir(base), key=lambda fnm: int(re.match('\w+_(\d+)_\w+', fnm).group(1)))
                   if 'original' in fnm and side_ in fnm]

completion_images = [imio.imread(os.path.join(base, fnm)) for fnm in
                     sorted(os.listdir(base), key=lambda fnm: int(re.match('\w+_(\d+)_\w+', fnm).group(1)))
                     if 'completion' in fnm and side_ in fnm]

original_images = np.asarray(original_images)
original_images = np.concatenate([original_images[18:], original_images[:18]], axis=0)

completion_images = np.asarray(completion_images)
completion_images = np.concatenate([completion_images[18:], completion_images[:18]], axis=0)

completion_mses = pd.read_csv(os.path.join(base, '..', 'completion_mse.csv'))

completion_mses['left'] = completion_mses.index >= 50
completion_mses['image_index'] = range(100)

df = pd.DataFrame(
    data=dict(
        bottom=list(completion_mses['mse'][completion_mses['image_index'] >= 50]),
        left=list(completion_mses['mse'][(completion_mses['image_index'] < 50)])
    ),
)

df['average'] = (df['bottom'] + df['left']) / 2
df['image_index'] = range(len(original_images))

def pad_bottom_right(im):
    ret = np.zeros([x + 1 for x in im.shape])
    ret[:-1, :-1] = im
    return ret

def pad_top_left(im):
    ret = np.zeros([x + 1 for x in im.shape])
    ret[1:, 1:] = im
    return ret

def pad_bottom_white(im, size=5):
    ret = np.ones((im.shape[0] + size, im.shape[1])) * 255
    ret[:-size, :] = im
    return ret


def image_grid(orig, comp, rows, cols, side='left'):
    total = rows * cols
    if total != len(orig):
        indices = df.sort_values(by=side)['image_index'][:total]
    else:
        indices = list(range(len(orig)))

    orig = np.asarray(orig)[indices]
    comp = np.asarray(comp)[indices]

    row_images = []
    for ri in range(rows):
        orig_row = np.concatenate(
            [pad_bottom_right(im) for im in orig[ri * cols:(ri + 1) * cols]], axis=1)
        comp_row = np.concatenate(
            [pad_bottom_right(im) for im in comp[ri * cols:(ri + 1) * cols]], axis=1)
        full_row = pad_top_left(np.concatenate((orig_row, comp_row), axis=0))

        if ri < rows - 1:
            full_row = pad_bottom_white(full_row)
        row_images.append(full_row)

    return np.concatenate(row_images, axis=0)

imio.imsave('collage_{}.png'.format(side_), image_grid(original_images, completion_images, 5, 10, side_))
