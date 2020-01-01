from itertools import combinations as combine
from itertools import product

from polyutils.triangle_triangle_intersection import triangles_intersection

from polyutils.geometric_tools import *


def overlap_list(polygons, mode='triangular'):
    """
    Return those polygons whose are overlapping.
    :param polygons: list of polygons
    :return: True and the pairs of overlapping polygons, or False.
    """
    pairs = list(combine(polygons, 2))
    bad_polygons = []

    if mode == 'convex':
        function = convex_overlap
    elif mode == 'triangular':
        function = triangular_overlap
    else:
        raise ModuleNotFoundError

    for pol in pairs:
        if function(pol[0], pol[1]) is True:
            bad_polygons.append(pol[0])
            bad_polygons.append(pol[1])

    if len(bad_polygons) == 0:
        return False, None
    return True, bad_polygons


def convex_overlap(pol1, pol2):
    """
    A geometry based function that verifies if two polygons overlaps or not.
    :param pol1: Polygon 1
    :param pol2: Polygon 2
    :return: True if the polygons overlap, False if does not.
    """
    planes1, v1 = get_planes_and_vertex_of_pol(pol1)
    planes2, v2 = get_planes_and_vertex_of_pol(pol2)

    for pl in planes1:
        if plane_separating_set(pl, v1, v2) is True:
            return False

    for pl in planes2:
        if plane_separating_set(pl, v1, v2) is True:
            return False

    return True


def triangular_overlap(pol1, pol2):
    triangles1 = get_triangles(pol1)
    triangles2 = get_triangles(pol2)

    pairs = list(product(triangles1, triangles2))

    points = []
    for p in pairs:
        r, null = triangles_intersection(p[0], p[1])
        points.append(r)
        # if r:
        #     print('T1,T2 = {}, {}'.format(p[0], p[1], r))

    if True in points:
        return True
    return False


def main():
    from polyutils import Rectangle

    a = Rectangle([1, 1, 1], 1, triangular=True)
    b = Rectangle([1, 1, 1], 1, triangular=True)
    b.change_position([.7, .7, .7])

    polygons = [a, b]

    x, bad = overlap_list(polygons, mode='triangular')
    print('Overlap? ', x)

    from polyutils import PolyViewer3D
    v = PolyViewer3D(edges=True)
    v.polygons.extend([a, b])
    v.plot_container_auto()
    v.plot_objects(animate=False)
    v.show()


if __name__ == "__main__":
    main()
