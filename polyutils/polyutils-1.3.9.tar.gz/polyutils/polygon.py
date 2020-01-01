import numpy as np
from scipy.spatial import ConvexHull

DECIMALS = 6


def triangularize_list(array):
    """Create triples (triangularize) from given array."""
    new = []

    if len(array) is 3:
        return [array]

    for i in range(1, len(array) - 1):
        new.append([array[0], array[i], array[i + 1]])

    return new


def sum_arrays(vertices, offset):
    """Sum the value to the coordinates."""
    new_vertices = []
    for v in vertices:
        a = (v[0] + offset[0], v[1] + offset[1], v[2] + offset[2])
        new_vertices.append(a)

    return new_vertices


class Polygon:
    """
    This class represents the most primitive Polygon ever, with some
    attributes useful (or not) for this package.
    """

    def __init__(
            self, vertices, faces, color=tuple(np.random.rand(3)),
            volume=0, id_pol=0, triangular=False):

        """
        Create a Polygon object.

        :param vertices: list of vertex
        :param faces: list of lists of integers that forms a face
        :param color: a triple containing values between 0 and 1
        :param volume: a float that represents the volume
        :param id_pol: some identification
        :param triangular: True for triangularize the FACES.
        """
        self.__vertices = vertices
        self.__volume = volume
        self.__faces = faces
        self.__color = tuple(color)
        self.__id_pol = id_pol

        if triangular:
            self.triangularize_faces()

    def resize(self, scale=1.0):
        """
        Resize the polygon by given rate.

        :param scale: a scale rate that multiplies all the vertices.
        :return:
        """
        vertex_list = []
        for v in self.__vertices:
            a = [i * scale for i in v]
            vertex_list.append(a)

        # TODO this changes the volume too, fix-it later.

        self.__vertices = vertex_list

    def round_vertices(self, decimals=DECIMALS):
        """Round the vertices to given decimals."""

        vertex_list = []
        for v in self.__vertices:
            a = np.round(v, decimals=decimals)
            vertex_list.append(tuple(a))

        self.__vertices = vertex_list

    def rotate(self, alpha, beta, gamma):
        """
        Rotate the Polygon on space.

        :param alpha: rotation ANGLE on x axis
        :param beta: rotation ANGLE on y axis
        :param gamma: rotation ANGLE on z axis
        :return:
        """
        rotation_x = np.array(
            [
                [1, 0, 0],
                [0, np.cos(alpha), -np.sin(alpha)],
                [0, np.sin(alpha), np.cos(alpha)]
            ]
        )

        rotation_y = np.array(
            [
                [np.cos(beta), 0, np.sin(beta)],
                [0, 1, 0],
                [-np.sin(beta), 0, np.cos(beta)]
            ]
        )

        rotation_z = np.array(
            [
                [np.cos(gamma), -np.sin(gamma), 0],
                [np.sin(gamma), np.cos(gamma), 0],
                [0, 0, 1]
            ]
        )

        rotation_xy = np.matmul(rotation_x, rotation_y)
        rotation = np.matmul(rotation_xy, rotation_z)

        vertex = self.vertices

        new_v = []

        for i in vertex:
            v = np.matmul(rotation, i)
            new_v.append(tuple(v))

        self.__vertices = new_v

    @staticmethod
    def load_from_obj(file_path):

        """
        Read a Wavefront OBJ File and creates a Polygon from it.

        :param file_path: path/of/file.cell
        :return: an object of type Polygon
        """

        file = open(file_path, 'r')

        lines = file.readlines()
        id_pol = 0
        vertices = []
        faces = []
        color = (.5, .5, .5)

        for line in lines:

            attribute = line.split()

            if line == '\n':
                continue

            if attribute[0] == 'o':
                id_pol = attribute[1]

            elif attribute[0] == 'v':
                v = [float(i) for i in attribute[1:]]
                vertices.append(v)

            elif attribute[0] == 'f':
                face = []

                for value in attribute[1:]:
                    a = value.split('/')
                    a = a[0]
                    a = int(a) - 1
                    face.append(a)

                faces.append(face)

            elif attribute[0] == 'c':
                color = tuple(
                    [float(attribute[1]),
                     float(attribute[2]),
                     float(attribute[3])]
                )

        p = Polygon(
            vertices=vertices,
            faces=faces,
            color=color,
            id_pol=id_pol,
        )
        p.triangularize_faces()

        return p

    def write_obj(self, file_path, index=0, total=0):
        contents = self.get_obj()

        file = open(file_path, 'w')
        file.write(contents)
        file.close()

    def get_obj(self):
        """Return the Wavefront OBJ File notation to string format."""

        v = self.vertices
        file = ''

        name = 'o\tobject'

        vertex = ''
        for i in v:
            vertex += 'v\t' + str(i[0]) + '\t' + str(i[1]) + '\t' + str(i[2])
            vertex += '\n'

        faces = ''
        for i in self.faces:
            face = 'f\t'
            for j in i:
                face += str(j + 1) + '\t'
            faces += face + '\n'

        color = 'c\t'
        color += str(self.color[0]) + '\t'
        color += str(self.color[1]) + '\t'
        color += str(self.color[2])

        file += name + '\n'
        file += vertex
        file += faces
        file += color

        return file

    def change_position(self, offset):
        """
        Sum the given value to the vertices of a polygon,
        moving it on space.

        :param offset: a triple (x,y,z)
        :return:
        """
        new_vertices = sum_arrays(self.vertices, offset)

        self.vertices = new_vertices

    def move_to_origin(self):
        """Move the polygon to origin by its minimum vertices."""

        # Find the minimum point
        vertices = [*zip(*self.vertices)]
        minimum = [-min(vertices[0]), -min(vertices[1]), -min(vertices[2])]

        new_vertices = sum_arrays(self.vertices, minimum)

        self.vertices = new_vertices

    def triangularize_faces(self):
        """Triangularize all FACES of the polygon."""

        f = []
        for i in self.__faces:
            f.extend(triangularize_list(i))

        self.faces = f

    @property
    def vertices(self):
        """Return the list of vertices of the polygon."""
        return self.__vertices

    @vertices.setter
    def vertices(self, new_vertices):
        self.__vertices = new_vertices

    @property
    def faces(self):
        """Return the list of FACES of the polygon."""
        return self.__faces

    @faces.setter
    def faces(self, new_faces):
        self.__faces = new_faces

    @property
    def color(self):
        """Return the color of the polygon."""
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    @property
    def id_pol(self):
        """Return the id of the polygon."""
        return self.__id_pol

    @id_pol.setter
    def id_pol(self, new_id_pol):
        self.__id_pol = new_id_pol

    @property
    def volume(self):
        """Return the volume of the polygon."""
        return self.__volume

    @volume.setter
    def volume(self, new_volume):
        self.__volume = new_volume

    def show_info(self, complex_mode=False):
        """A PrettyPrint of the polygon and its attributes"""

        print('id_pol:\t', self.id_pol)

        if not complex_mode:
            print('vertices:\t', self.vertices)
        else:
            print('vertices:\t')
            for i in self.vertices:
                print('\t\t', i)

        if not complex_mode:
            print('FACES:\t', self.faces)
        else:
            print('FACES:\t')
            for i in self.faces:
                print('\t\t', i)

        print('color:\t', self.color)

    def dilate(self, rate=.1):
        """
        Dilate a polygon, i.e., expands it
        and keeps it on same position.

        """
        old_vertices = self.vertices
        new_vertices = []

        for vertex in old_vertices:

            new_vertex = list(vertex)
            k = []
            for i in new_vertex:
                i *= rate
                k.append(i)
            new_vertices.append(tuple(k))

        self.vertices = new_vertices
        p = (1 - rate) / 2
        self.change_position(offset=(p, p, p))

    def get_convex_hull(self):
        vertex = self.vertices
        return ConvexHull(vertex)

    def get_polygon_convex_hull(self):
        hull = self.get_convex_hull()

        faces = hull.simplices
        faces = [list(f) for f in faces]
        points = hull.points
        points = [list(p) for p in points]

        # TODO: the vertices are the same from original polygon because of faces
        # vertices_index = hull.vertices
        # for v in vertices_index:
        #     new_points.append(points[v])
        #
        # new_points = [list(p) for p in new_points]
        # new_points = [*zip(*new_points)]

        polygon_hull = Polygon(faces=faces, vertices=points)
        return polygon_hull


def main():
    bunny = Polygon.load_from_obj('instances/bunny.obj')
    bunny.resize(scale=10)
    bunny.color = (.9, .6, .85)

    bunny_hull = bunny.get_polygon_convex_hull()
    bunny_hull.color = (.2, .1, .3)

    from polyutils import PolyViewer3D
    PolyViewer3D.easy_plot([bunny, bunny_hull], alpha=.58)


if __name__ == "__main__":
    main()
