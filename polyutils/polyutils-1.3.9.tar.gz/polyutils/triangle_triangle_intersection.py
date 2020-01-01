from polyutils.geometric_tools import *


def triangles_intersection(triangle_1, triangle_2):
    """
    
    """
    plane_triangle_1 = plane_equation(triangle_1[0], triangle_1[1], triangle_1[2])
    plane_triangle_2 = plane_equation(triangle_2[0], triangle_2[1], triangle_2[2])

    # This test checks if one triangle plane separates the points of the other one.
    # If any is True, then they sure don't overlap
    # If both are False, we need to check more carefully
    # This case also verifies if the triangles are parallel when both are True
    ssd_t1_p2 = same_sign(
        signed_distance_array(triangle_1, plane_triangle_2)
    )
    ssd_t2_p1 = same_sign(
        signed_distance_array(triangle_2, plane_triangle_1)
    )

    # print('ssd:  ', ssd_t1_p2, ssd_t2_p1)

    if ssd_t1_p2 or ssd_t2_p1 is True:
        # Every plane separates the points
        return False, []

    # This case is sufficient all of the other commutative cases
    # If there is only one intersection point, then we have a semi intersection case
    points = get_intersection_points(triangle_2, plane_triangle_1)

    intersect_points = []
    for p in points:
        if is_point_inside_triangle(p, triangle_1):
            intersect_points.append(p)

    # This case verifies if the one above fails, for non-commutative cases
    if len(intersect_points) == 0:

        # Sadly this gives a recursion error, I'll fix one day...
        # x, intersect_points = triangles_intersection(triangle_2, triangle_1, get_points=get_points)

        points = get_intersection_points(triangle_1, plane_triangle_2)
        intersect_points = []
        for p in points:
            if is_point_inside_triangle(p, triangle_2):
                intersect_points.append(p)

    # This verifies edge intersection that is allowed
    # TODO check if intersection points is some vertex
    if len(intersect_points) == 2:
        if (intersect_points[0] in triangle_1
                or intersect_points[1] in triangle_1
                or intersect_points[0] in triangle_2
                or intersect_points[1] in triangle_2):
            return False, []

    # A missing obvious case
    if len(intersect_points) == 0:
        return False, []

    # Remove duplicated points
    intersect_points = list(set(intersect_points))

    # If there is nothing more to do:
    return True, intersect_points


def triangular_intersection_tests_from_file(file_path='triangles_tests.txt'):
    tests_file = open(file_path, 'r')
    lines = tests_file.readlines()
    tests = []
    for line in lines:
        value = line.split()
        value = [float(v) for v in value]
        value = [value[n:n + 3] for n in range(0, len(value), 3)]
        pair = [value[n:n + 3] for n in range(0, len(value), 3)]
        tests.append(pair)

    for cases in tests:
        T1 = cases[0]
        T2 = cases[1]
        answer, points = triangles_intersection(T1, T2)
        print(cases, answer)


def main():
    # Main tests
    # No intersect test (equal triangles) - commutative
    # T1 = [(0, 0, 0), (0, 10, 0), (10, 10, 0)]
    # T2 = [(0, 0, 0), (0, 10, 0), (10, 10, 0)]

    # No intersect test (parallel) - commutative
    # T1 = [(0, 0, 0), (0, 10, 0), (10, 10, 0)]
    # T2 = [(0,0, 5), (0, 10, 5), (10,10, 5)]

    # No intersect test (not parallel) - commutative
    # T1 = [(0, 0, 0), (0, 10, 0), (10, 10, 0)]
    # T2 = [(0, 0, 5), (0, 10, 1), (10, 10, 5)]

    # No intersect test (point intersection) - commutative
    # T1 = [(0, 0, 5), (0, 10, 0), (10, 10, 0)]
    # T2 = [(0, 0, 5), (0, 10, 5), (10, 10, 5)]

    # No intersect test (line intersection) - commutative
    # T1 = [(0, 0, 5), (0, 10, 5), (10, 10, 0)]
    # T2 = [(0, 0, 5), (0, 10, 5), (10, 10, 5)]

    # Intersect test (semi intersection) - commutative
    # T1 = [(0, 0, 0), (0, 10, 0), (10, 10, 0)]
    # T2 = [(2, 2, 5), (0, 10, -5), (11, 11, 5)]

    # Intersect test - sadly, not commutative
    # T1 = [(0, 0, 0), (0, 10, 0), (10, 10, 0)]
    # T2 = [(2, 2, 5), (0, 10, -5), (8, 8, 5)]

    # Intersect test (two on edges) - commutative
    # T1 = ((0.0, 0.0, 0.0), (5, 12, 0.0), (0.0, 0.0, 20))
    # T2 = ((5, 0.0, 0.0), (0.0, 12, 0.0), (0.0, 12, 20))

    # Intersect test - one point on edge TODO: fix it
    T1 = ((5, 0.0, 0.0), (0.0, 12, 0.0), (0.0, 12, 20))
    T2 = ((5, 12, 0.0), (0.0, 12, 20), (0.0, 0.0, 20))
    # But this one works
    # T1 = ((0.0, 0.0, 0.0), (5, 0.0, 0.0), (5, 12, 20))
    # T2 = ((0.0, 0.0, 0.0), (5, 12, 0.0), (0.0, 0.0, 20))

    # T1 blue, T2 green
    polygons = [T1, T2]

    points_to_plot = []
    for p in polygons:
        for i in p:
            points_to_plot.append(i)

    answer, points = triangles_intersection(T1, T2)
    print(answer, points)

    points_to_plot.extend(points)
    triangle_plot(polygons=polygons, points=points_to_plot)


def triangular_intersection_autotest(quantity=1):
    # x = list(np.random.uniform(size=18) * 10)
    for i in range(quantity):
        x = list(np.random.randint(low=0, high=5, size=18))
        x = [round(i, 5) for i in x]
        x = [x[n:n + 3] for n in range(0, len(x), 3)]
        points_to_plot = x
        x = [x[0:3], x[3:6]]
        answer, points = triangles_intersection(x[0], x[1])
        if answer:
            print(i, x)
            points_to_plot.extend(points)
            triangle_plot(x, points_to_plot, '{} {}'.format(i, answer))


if __name__ == "__main__":
    triangular_intersection_autotest(50)
