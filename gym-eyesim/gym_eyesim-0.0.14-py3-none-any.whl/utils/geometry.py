import math
import numpy as np


def dist_between_points(p1, p2):
    return np.linalg.norm(p2 - p1)


def dist_to_line(p1, p2, p3):
    return abs(np.cross(p2 - p1, p3 - p1)) / np.linalg.norm(p2 - p1)


def side_of_line(p1, p2, p3):
    """Check on which side of a line a point is.

    Args:
        p1 (array): First point of the line.
        p2 (array): Second point of the line.
        p3 (array): Point to check.

    Returns:
        A value larger than 0 if p3 is left of p1 and p2.
    """

    return np.cross(p2 - p1, p3 - p1)


def angle_between_vectors(v1, v2):
    v1 /= np.linalg.norm(v1)
    v2 /= np.linalg.norm(v2)
    return np.arccos(np.clip(np.dot(v1, v2), -1.0, 1.0))
