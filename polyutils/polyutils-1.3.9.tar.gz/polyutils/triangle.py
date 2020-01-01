import numpy as np

from polyutils.polygon import Polygon
from polyutils.geometric_tools import triangle_area

# Faces is the same for all rectangles ;)
TRIANGLES = [0, 1, 2]


class Triangle(Polygon):

    def __init__(
            self, points, id_pol=0,
            color=np.random.rand(3), ):
        """
        Class constructor
        Create a rectangle with given size

        :param size: triple representing the size (length, width, height)
        :param color: triple that represents a color (RGB),
        random if not specified
        """

        vertices = [points[0], points[1], points[2]]

        area = triangle_area(points[0], points[1], points[2])

        super().__init__(
            vertices=vertices,
            faces=TRIANGLES,
            volume=area,
            id_pol=id_pol,
            color=color,
            triangular=False,
        )

    def dilate(self, rate=.1):
        pass


def main():
    t1 = Triangle([(2, 2, 5), (0, 10, -5), (8, 8, 5)])
    t2 = Triangle([(0, 0, 0), (0, 10, 0), (10, 10, 0)])

    print(t1.vertices)
    print(t2.faces)

    vertices_to_plot = []
    vertices_to_plot.extend(t1.vertices)
    vertices_to_plot.extend(t2.vertices)
    print(vertices_to_plot)



    from polyutils import PolyViewer3D
    PolyViewer3D.easy_plot(triangles=[t1, t2], points=vertices_to_plot)


if __name__ == "__main__":
    main()
