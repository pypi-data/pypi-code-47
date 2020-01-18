from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import six
import os
import random
import re
import numpy as np
import math

from ..backend.common import *


__all__ = ['label_backend_adaptive','get_onehot']


_session=get_session()
_backend=_session.backend
_image_backend=_session.image_backend


def get_onehot(idx,len):
    if idx>=len:
        raise ValueError('')
    arr=np.zeros(len,dtype=np.float32)
    arr[idx]=1
    return arr




def label_backend_adaptive(label,label_mapping):
    if _backend == 'pytorch':
        label =np.array(label).astype(np.int64)
    else:
        label=get_onehot(label,len(label_mapping))
    return label

