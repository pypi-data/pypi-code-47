from polyutils import Polygon
import pyvoro


def get_vertices(vertex_dict):
    v = []
    for i in vertex_dict['vertices']:
        v.append(tuple(i))

    return v


def get_faces(face):
    f = []
    for i in face:
        f.append(i['vertices'])
    return f


class PolyGenerator:

    def __init__(self, seeds, container, scale=1):
        self.__seeds = seeds
        self.__container = container
        self.__scale = scale
        self.__polygon_array = None

    def get_polygons(self) -> list:
        polygons_array = []

        cells = self.get_cells()

        for key, cell in enumerate(cells):
            ve = get_vertices(cell)
            fa = get_faces(cell['faces'])
            seed = cell['original']
            volume = cell['volume']

            polygon = Polygon(vertices=ve,
                              faces=fa,
                              color=seed / self.__scale,
                              volume=volume,
                              id_pol=key,
                              )

            polygons_array.append(polygon)

        self.__polygon_array = polygons_array
        return self.__polygon_array

    def get_cells(self) -> dict:
        cells = pyvoro.compute_voronoi(
            points=self.__seeds,
            limits=self.__container,
            dispersion=3,

            # radii=[], # Some obscure parameters to explore later
            # periodic=[False, False, False],
        )

        return cells


def generate(num_seeds, scale=1):
    import numpy as np
    scale = scale
    container_generate = [[0, scale]] * 3

    seeds = np.random.rand(num_seeds, 3) * scale

    polygons = PolyGenerator(seeds=seeds,
                             container=container_generate,
                             scale=scale
                             )

    ret = polygons.get_polygons()

    for r in ret:
        r.triangularize_faces()

    return ret


def main():
    # # To generate
    # polygons_list = generate(50, scale=10)
    # from polyutils import get_max_z
    # polygons_list.sort(key=lambda p: get_max_z(p)) # Just to make a pretty plot
    #
    # # To save in file
    # import pickle
    # filename = 'voronoi.data'
    # file_write_list = open(filename, 'wb')
    # pickle.dump(polygons_list, file_write_list)

    # To load from file
    import pickle
    filename = 'voronoi.data'
    file_read_list = open(filename, 'rb')
    polygons_list = pickle.load(file_read_list)

    from polyutils import PolyViewer3D
    PolyViewer3D.easy_plot(polygons_list, animate=True)


if __name__ == '__main__':
    main()
