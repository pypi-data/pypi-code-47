import numpy as np
import os
import yaml
import imageio


def read_dataset(file):
    yamlfile = yaml.load(open(file, 'r'), Loader=yaml.FullLoader)
    root = yamlfile.get("root", "")
    inputs = yamlfile.get("inputs", [])
    inputs = [os.path.join(root, input) for input in inputs]
    labels = yamlfile.get("labels", np.repeat(None, len(inputs)))
    classes = yamlfile.get("classes", [])
    return root, inputs, labels, classes


def read_image(args, **kwargs):
    return imageio.imread(args, **kwargs)


def one_hot(labels, C):
    one_hot = np.zeros(C)
    one_hot[np.array(labels)] = 1
    return one_hot


def save_dict(*args, **kwargs):
    np.save(*args, **kwargs)
    return


def get_from_dict(dict, keys):
    return [dict.get(key, None) for key in keys]


def read_dict(file, keys=None):
    d = np.load(file, allow_pickle=True).item()
    if keys is None:
        return d
    else:
        return get_from_dict(d, keys)


def hello():
    print('Thib')
