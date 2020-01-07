import os

import pickle
import h5py


def create_knee_dict(base_path):
    subject_base_str = 'rep_%02d'  # e.g.'rep_03', from 2-7
    knees = ['LEFT', 'RIGHT']

    knee_dict = {}
    # initialize map from subject-knee --> series
    for sub in range(2, 8):
        for knee in knees:
            curr_sub = subject_base_str % sub
            k = '%s-%s' % (curr_sub, knee)
            series = []
            sub_knee_dir = os.path.join(base_path, curr_sub, knee)
            files = os.listdir(sub_knee_dir)
            for f in files:
                if os.path.isdir(os.path.join(sub_knee_dir, f)):
                    series.append(f)
            series.sort()

            knee_dict[k] = (curr_sub, knee, series)

    return knee_dict


def mkdirs(dir_path: str):
    """Recursively create directories if directory does not exist.

    Args:
        dir_path (str): Directory to create. If exists, no intermediate directories will be created.

    Returns:
        str: ``dir_path``.

    Examples:
        >>> mkdirs('/example/directory')
        '/example/directory'
    """
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

    return dir_path


def load_h5(file_path: str):
    """Load data in H5DF format.

    Args:
        file_path (str): Path to H5 file.

    Returns:
        dict: Data dictionary.

    Raises:
        FileNotFoundError: If ``file_path`` doesn't exist.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError("{} does not exist".format(file_path))

    data = dict()
    with h5py.File(file_path, "r") as f:
        for key in f.keys():
            data[key] = f.get(key).value

    return data


def save_pik(data, file_path: str):
    """Save data using ``pickle``.

    Args:
        data: Data to save.
        file_path (str): File path.
    """
    with open(file_path, "wb") as f:
        pickle.dump(data, f)


def load_pik(file_path: str):
    """Load data using ``pickle``.

    Args:
        file_path (str): File path.

    Returns:
        Data saved using :obj:`save_pik`
    """
    with open(file_path, "rb") as f:
        return pickle.load(f)


def save_ims(file_path):
    im_path = '%s.im' % file_path
    with h5py.File(im_path, 'r') as f:
        im = f['data'][:]

    seg_path = '%s.seg' % file_path
    with h5py.File(seg_path, 'r') as f:
        seg = f['data'][:].astype('float32')
        seg = seg[..., 0, 0]
    file_path = mkdirs(file_path)
    # save ims
    cv2.imwrite(os.path.join(file_path, 'im.png'), scale_img(im))

    # save segs
    cv2.imwrite(os.path.join(file_path, 'seg.png'), scale_img(seg))