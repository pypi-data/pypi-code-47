import numpy as np

DECIMALS = 6
DECIMALS_LIM = 10 ** -5


def get_triangles(pol):
    vertex = [*zip(*pol.vertices)]

    triangles = []
    for f in pol.faces:
        a = vertex[f[0] - 1]
        b = vertex[f[1] - 1]
        c = vertex[f[2] - 1]
        t = (a, b, c)
        triangles.append(t)

    return triangles


def get_planes_and_vertex_of_pol(pol):
    """
    It is obvious
    :param pol: an object like Polygon
    :return: returns the list of planes and the list of vertices of a polygon
    """
    vertex_pol = pol.vertices
    planes = []

    for f in pol.faces:
        faces_planes = []
        for v in f[0:3]:  # Only the three first vertices are necessary
            faces_planes.append(vertex_pol[v])

        # Create all the planes of a polygon
        plane = plane_equation(
            faces_planes[0], faces_planes[1], faces_planes[2]
        )
        planes.append(plane)

    return planes, vertex_pol


def plane_separating_set(plane, points1, points2):
    """
    Give a plane and two sets of points, this function
    checks if the plane separates the two sets
    :param plane: array defining the plane equation
    :param points1: a set of 3D points
    :param points2: a set of 3D points
    :return: True if given plane separates the tho sets, False if does not.
    """

    side_a = all_points_same_side(plane, points1)
    side_b = all_points_same_side(plane, points2)

    # print('Sides: ',side_a, side_b)

    if side_a is False or side_b is False:
        return False
    if side_a == -1 * side_b:
        return True
    return False


def intersection_line_plane(points, plane):
    p0, p1 = points[0], points[1]

    line = (p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2])

    # p0 * plane equation
    a = plane[0] * p0[0] + plane[1] * p0[1] + plane[2] * p0[2]

    # line * plane equation
    b = plane[0] * line[0] + plane[1] * line[1] + plane[2] * line[2]

    c = a + plane[3]
    t = -c / b

    point = (p0[0] + line[0] * t, p0[1] + line[1] * t, p0[2] + line[2] * t)

    return point


def is_convex(pol):
    plane, points = get_planes_and_vertex_of_pol(pol)

    for pl in plane:
        if not all_points_same_side(pl, points):
            return False

    return True


def all_points_same_side(plane, points, admit_zero=True):
    """
    if all points are on the same side of a plane,
    it returns the side (1 or -1), else
    returns False
    :param plane: array defining the plane equation
    :param points: a set of 3D points
    :param admit_zero: if point intersection is not allowed
    :return: 1, -1 or False
    """

    results = []
    for p in points:
        s = point_plane_side(plane, p)
        results.append(s)

    results = set(results)

    if admit_zero:
        results.discard(0)

    if len(results) == 1:
        return list(results)[0]
    return False


def point_plane_side(plane, point, decimals_lim=DECIMALS_LIM):
    """
    Return the side of a plane where the point is located
    :param plane: plane: array defining the plane equation
    :param point: a 3D point
    :return: -1 or 1 if is located in any side, or 0 if it is on plane
    """

    # NumPy is so slow!!!
    # v = np.dot(point, plane[0:3]) + plane[3]
    # v = np.round(v, decimals=DECIMALS)

    v = point[0] * plane[0] \
        + point[1] * plane[1] \
        + point[2] * plane[2] \
        + plane[3]

    if abs(v) < decimals_lim:
        v = 0

    v = np.sign(v)

    return v


def matmul(v1, v2):
    m = [v1[1] * v2[2] - v1[2] * v2[1],
         v1[2] * v2[0] - v1[0] * v2[2],
         v1[0] * v2[1] - v1[1] * v2[0]]

    return m


def plane_equation(v0, v1, v2):
    v1_v0 = [v1[0] - v0[0], v1[1] - v0[1], v1[2] - v0[2]]
    v2_v0 = [v2[0] - v0[0], v2[1] - v0[1], v2[2] - v0[2]]

    n = matmul(v1_v0, v2_v0)

    d = -(n[0] * v0[0] + n[1] * v0[1] + n[2] * v0[2])

    n.append(d)

    return n


def signed_distance_array(t, p):
    d = []
    for v in t:
        k = v[0] * p[0] + v[1] * p[1] + v[2] * p[2] + p[3]
        d.append(k)

    return d


def sign(n):
    if n >= 0:
        return 1
    elif n < 0:
        return -1

    return None


def signed_array(array):
    result = []
    for a in array:
        result.append(sign(a))

    return result


def same_sign(array):
    result = signed_array(array)
    result = set(result)

    if len(result) == 1:
        return True

    return False


def get_intersection_points(triangle, plane):
    # Get intersection points between a triangle and a plane
    # If there are any intersection, we need to find the
    # two points that intersect a plane
    # Note that only two lines intersects this plane.
    # The third one results in a division by zero.

    pairs = [
        (triangle[0], triangle[1]),
        (triangle[0], triangle[2]),
        (triangle[1], triangle[2])
    ]

    points = []
    for pair in pairs:
        try:
            p = intersection_line_plane(pair, plane)
            points.append(p)
        except:
            pass

    # These points represents the line that is the intersection
    # between the two planes described by the triangles
    return points


def triangle_area(p1, p2, p3):
    # Too hard to think about at 4am
    # Source: https://math.stackexchange.com/a/2169905

    x1, y1, z1 = p1[0], p1[1], p1[2]
    x2, y2, z2 = p2[0], p2[1], p2[2]
    x3, y3, z3 = p3[0], p3[1], p3[2]

    a = (x2 * y1) - (x3 * y1) - (x1 * y2) + (x3 * y2) + (x1 * y3) - (x2 * y3)
    b = (x2 * z1) - (x3 * z1) - (x1 * z2) + (x3 * z2) + (x1 * z3) - (x2 * z3)
    c = (y2 * z1) - (y3 * z1) - (y1 * z2) + (y3 * z2) + (y1 * z3) - (y2 * z3)

    # d = (a + b + c) ** .5
    d = ((a ** 2) + (b ** 2) + (c ** 2)) ** .5

    area = d / 2

    return area


def is_point_inside_triangle(point, triangle):
    total_area = triangle_area(triangle[0], triangle[1], triangle[2])

    a, b, c = triangle[0], triangle[1], triangle[2]

    t1 = triangle_area(a, b, point)
    t2 = triangle_area(a, c, point)
    t3 = triangle_area(b, c, point)

    decomposed_area = t1 + t2 + t3

    if abs(total_area - decomposed_area) < 0.00005:
        # The point belongs to the triangle
        return True

    return False


def triangle_plot(polygons=(), points=(), title=''):
    color = [
        (.1, .4, .9),
        (.1, .9, .4),
        (.4, .1, .9),
        (.4, .9, .1),
        (.9, .1, .4),
        (.9, .4, .1),
    ]
    triangles = [(0, 1, 2)]
    scale = .25
    opacity = 1

    from mayavi import mlab
    f = mlab.figure(size=[1000, 700], bgcolor=(.1, .1, .1), figure=title)
    f.scene.disable_render = False

    # Plot points and labels
    for p in points:
        if p is not None:
            mlab.points3d(p[0], p[1], p[2], scale_factor=scale, figure=f)
            mlab.text3d(p[0], p[1], p[2], text=str(p), scale=scale * 1.2)

    # Plot triangles
    for k, p in enumerate(polygons):
        if p is not None:
            # Plotters separate the x's, y's and z's in three different arrays
            p = [*zip(*p)]
            mlab.triangular_mesh(
                p[0], p[1], p[2], triangles, figure=f, color=color[k % 6],
                opacity=opacity
            )

    mlab.orientation_axes(figure=f)

    mlab.show()
