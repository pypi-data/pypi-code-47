def get_max_x(p):
    vertices = [*zip(*p.vertices)]
    return max(vertices[0])


def get_max_y(p):
    vertices = [*zip(*p.vertices)]
    return max(vertices[1])


def get_max_z(p):
    vertices = [*zip(*p.vertices)]
    return max(vertices[2])


def get_obj_x(pols):
    if len(pols) == 0:
        return None

    a = []
    for pol in pols:
        a.append(get_max_x(pol))

    obj = max(a)
    return obj


def get_obj_y(pols):
    if len(pols) == 0:
        return None
    a = []
    for pol in pols:
        a.append(get_max_y(pol))

    obj = max(a)
    return obj


def get_obj_z(pols):
    if len(pols) == 0:
        return None
    a = []
    for pol in pols:
        a.append(get_max_z(pol))

    obj = max(a)
    return obj


def bottom_front_left_shelf(polygons, container):
    raise NotImplementedError


def bottom_front_left(polygons, container):
    """
    The placement of the polygons according to Bottom Front Left rule.
    :param polygons: list of polygons
    :param container: container to place the pieces.
    Note that only tha base is needed.
    :return: list of polygons
    """
    width, length = container[0], container[1]

    x_max, y_max, z_max = 0, 0, 0
    y_list, z_list = [], []

    for i in range(1, len(polygons)):
        current, previous = polygons[i], polygons[i - 1]
        x_max = get_max_x(previous)
        y_list.append(get_max_y(previous))
        z_list.append(get_max_z(previous))

        if get_max_x(current) + x_max > width:
            x_max = 0
            y_max = max(y_list)
            y_list = []
        if get_max_y(current) + y_max > length:
            x_max = 0
            y_max = 0
            z_max = max(z_list)
            y_list = []
            z_list = []

        current.change_position([x_max, y_max, z_max])

    return polygons


def bottom_front_left_2(polygons, container, rotation=False):
    """
    A better version of Bottom Front Left with some pre sorting option.
    It tests the best sort mode.
    :param polygons: list of polygons
    :param container: container to place the pieces.
    :param rotation: choose if bottom_front_left will admit rotations
    Note that only the base is needed.
    :return: list of polygons
    """

    from copy import deepcopy
    solutions = []
    for i in range(8):
        sol = polygons_sort(
            polygons, container,
            sort_mode=i, rotation=rotation
        )

        solutions.append(deepcopy(sol))

    best = min(solutions, key=get_obj_z)
    return best


def polygons_sort(polygons, container, sort_mode=0, rotation=False):
    # Rotate does an arbitrary rotation
    if rotation:
        import numpy as np
        for pol in polygons:
            x, y, z = get_max_x(pol), get_max_y(pol), get_max_z(pol)

            if z > x or z > y:
                pol.rotate(0, np.pi / 2, 0)
            if x > y:
                pol.rotate(np.pi / 2, 0, 0)

            pol.move_to_origin()

    if sort_mode == 0:
        polygons.sort(key=get_max_x, reverse=True)

    elif sort_mode == 1:
        polygons.sort(key=get_max_x, reverse=False)

    elif sort_mode == 2:
        polygons.sort(key=get_max_y, reverse=True)

    elif sort_mode == 3:
        polygons.sort(key=get_max_y, reverse=False)

    elif sort_mode == 4:
        polygons.sort(key=get_max_z, reverse=True)

    elif sort_mode == 5:
        polygons.sort(key=get_max_z, reverse=False)

    elif sort_mode == 6:
        polygons.sort(key=lambda p: p.volume, reverse=True)

    elif sort_mode == 7:
        polygons.sort(key=lambda p: p.volume, reverse=False)

    new_polygons = bottom_front_left(polygons, container)

    return new_polygons


def select_candidate(points, pol):
    # possibles = []
    # for point in points:
    #     pol.change_vertex(point)
    #     x = get_max_z(pol)
    #     possibles.append(x)
    # best = min(possibles)
    # print(best)

    best = min(points, key=lambda x: x[2])
    print(best)
    return best


def find_candidate(polygons):
    new_points = [(1, 3, 2), (4, 4, 2)]
    return new_points


def extreme_point_based(polygons, container):
    from copy import deepcopy
    width, length = container[0], container[1]

    polygons = polygons[:1]

    points = [
        (0, 0, 0),
        (1, 1, 1),
        (2, 2, 2)
    ]

    new_polygons = []

    for pol in polygons:
        candidate = select_candidate(points, deepcopy(pol))
        pol.change_position(candidate)
        points.remove(candidate)

        new_polygons.append(pol)

        new_candidates = find_candidate(new_polygons)
        points.extend(new_candidates)

    return new_polygons


def main():
    from polyutils import Rectangle
    from polyutils import PolyViewer3D
    import numpy as np

    container = [20, 20, 20]
    rectangles = []
    for i in range(50):
        b = Rectangle(
            size=np.random.randint(1, 8, size=3),
            id_pol=i, color=np.random.random(3),
            triangular=True
        )
        rectangles.append(b)

    rectangles = extreme_point_based(rectangles, container)

    print(get_obj_z(rectangles))

    v = PolyViewer3D(light_mode=True)
    v.polygons = rectangles
    v.points = [(-1, -1, -1)]

    v.container = container
    v.plot_container_auto()
    v.add_axes()

    v.plot_objects(animate=False)
    v.show()


if __name__ == "__main__":
    main()
