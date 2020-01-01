from mayavi import mlab

FG_COLOR = (1, 1, 1)
BG_COLOR = (.1, .1, .1)


class PolyViewer3D:

    def __init__(
            self, lim=(10, 10, 10), alpha=1,
            title='Mayavi Visualizer', edges=False, light_mode=False):

        background_color = BG_COLOR
        foreground_color = FG_COLOR

        if light_mode:
            background_color = FG_COLOR
            foreground_color = BG_COLOR

        self.__fig = mlab.figure(
            figure=title,
            bgcolor=background_color,
            fgcolor=foreground_color,
            size=(800, 700),
        )

        self.__container = lim

        self.__alpha = alpha
        self.__edges = edges

        self.__best_fit = [0, 0, 0]

        self.__objects = []

        self.__polygons = []
        self.__triangles = []
        self.__points = []
        self.__point_color = foreground_color

        # TODO: make the scale self adjust
        self.__point_scale = 1

        self.__axes = None
        self.__orientation_axes = None

        self.__delay = 100
        self.anim = (mlab.animate(delay=self.__delay, ui=True, ))(self.anim)

    def plot_container(
            self, container=None, color=(.9, .9, .9),
            container_opacity=.1, dilate=.1):

        if container is None:
            container = self.__container

        from polyutils.rectangle import Rectangle
        c = Rectangle(size=container, triangular=True)

        if dilate is not None:
            c.old_dilate(rate=dilate)

        self.add_cell(
            cell=c,
            color=color,
            opacity=container_opacity,
            edges=False
        )
        return c

    def plot_container_auto(
            self, color=(.9, .9, .9),
            container_opacity=.1, dilate=.1):

        self.update_best_fit()

        self.__container = self.__best_fit

        c = self.plot_container(
            container=self.__container, color=color,
            container_opacity=container_opacity,
            dilate=dilate
        )
        return c

    def update_best_fit(self):

        from polyutils.placement_rules import get_obj_x, get_obj_y, get_obj_z

        if len(self.polygons) != 0:
            reference = self.polygons
        elif len(self.triangles) != 0:
            reference = self.triangles
        else:
            reference = self.points

        x = get_obj_x(reference)
        y = get_obj_y(reference)
        z = get_obj_z(reference)

        n_digits = 0
        x = round(x, ndigits=n_digits)
        y = round(y, ndigits=n_digits)
        z = round(z, ndigits=n_digits)

        self.__best_fit = [x, y, z]

    def add_axes(self, label='simple'):

        if label is 'complex_mode':
            x_label = 'x=' + str(self.__container[0])
            y_label = 'y=' + str(self.__container[1])
            z_label = 'z=' + str(self.__container[2])
        else:
            x_label = 'x'
            y_label = 'y'
            z_label = 'z'

        ranges = [
            0, self.__container[0],
            0, self.__container[1],
            0, self.__container[2]
        ]

        self.__axes = mlab.axes(
            xlabel=x_label,
            ylabel=y_label,
            zlabel=z_label,
            ranges=ranges,
            nb_labels=0,
            figure=self.__fig
        )

        self.__orientation_axes = mlab.orientation_axes(figure=self.__fig)

    def add_point(self, point, opacity=1):
        x, y, z = point[0], point[1], point[2]

        o = mlab.points3d(
            x, y, z,
            color=self.__point_color,
            opacity=opacity,
            scale_factor=self.__point_scale,
            figure=self.__fig,
        )

        self.__objects.append(o)

    def add_triangle(self, triangle, color=(.4, .9, .1), opacity=.8, edges=False):
        vertices = [*zip(*triangle.vertices)]
        x, y, z = vertices[0], vertices[1], vertices[2]

        triangles = [(0, 1, 2)]
        o = mlab.triangular_mesh(
            x, y, z, triangles, figure=self.__fig, color=color,
            opacity=opacity
        )

        self.__objects.append(o)

    def add_cell(self, cell, color=None, opacity=.8, edges=False):

        vertices = [*zip(*cell.vertices)]
        x, y, z = vertices[0], vertices[1], vertices[2]
        faces = cell.faces

        c = color

        if color is None:
            c = cell.color

        representation = 'surface'

        o = mlab.triangular_mesh(
            x, y, z, faces,
            color=c,
            opacity=opacity,
            representation=representation,
            resolution=80000,
            figure=self.__fig,
        )

        self.__objects.append(o)

        if edges is False:
            return

        if edges is True:
            # mlab.outline(figure=self.__fig, )
            representation = 'wireframe'

            o = mlab.triangular_mesh(
                x, y, z, faces,
                color=c,
                opacity=opacity,
                representation=representation,
                resolution=80000,
                figure=self.__fig,
            )

            self.__objects.append(o)

    def anim(self):
        for i in self.__polygons:
            self.add_cell(i, color=i.color, opacity=self.__alpha, edges=self.__edges)
            yield

        for i in self.__points:
            self.add_point(point=i, opacity=self.__alpha)
            yield

        for i in self.__triangles:
            self.add_triangle(point=i, opacity=self.__alpha)
            yield

    def plot_objects(self, animate=False, delay=500):

        self.__delay = delay

        if not animate:
            for i in self.__polygons:
                self.add_cell(cell=i, opacity=self.__alpha, edges=self.__edges)
            for i in self.__points:
                self.add_point(point=i, opacity=self.__alpha)
            for i in self.__triangles:
                self.add_triangle(triangle=i, opacity=self.__alpha)
            return

        self.anim()

        return

    @staticmethod
    def show():
        mlab.show()

    @property
    def polygons(self):
        return self.__polygons

    @polygons.setter
    def polygons(self, new_pols):
        self.__polygons = new_pols

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, new_points):
        self.__points = new_points

    @property
    def triangles(self):
        return self.__triangles

    @triangles.setter
    def triangles(self, new_triangles):
        self.__triangles = new_triangles

    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, new_container):
        self.__container = new_container

    @property
    def objects(self):
        return self.__objects

    @staticmethod
    def easy_plot(polygons=(), points=(), triangles=(), alpha=1,
                  animate=False, edges=False, container=None, light_mode=False):

        v = PolyViewer3D(lim=container, edges=edges, alpha=alpha, light_mode=light_mode)
        v.polygons = polygons
        v.triangles = triangles
        v.points = points

        if container is None:
            v.plot_container_auto(container_opacity=.1)

        else:
            v.container = container
            v.plot_container()

        v.add_axes(label='complex_mode')
        v.plot_objects(animate=animate, delay=5000)
        v.show()

        return v


def main():
    from polyutils import Polygon
    from polyutils import Rectangle
    from polyutils import Triangle
    from polyutils.placement_rules import bottom_front_left_2
    import numpy as np

    # Create some rectangles
    num_pols = 8
    ret = [Rectangle(size=np.random.randint(1, 8, 3),
                     color=np.random.rand(3),
                     id_pol=i,
                     triangular=True) for i in range(num_pols)
           ]

    # Add a person among the triangles
    person = Polygon.load_from_obj("instances/person.obj")
    tea_mug = Polygon.load_from_obj("instances/teamug.obj")
    dog = Polygon.load_from_obj("instances/dog.obj")
    dog.resize(.25)
    tea_mug.resize(1.5)
    ret.append(person)
    ret.append(tea_mug)
    ret.append(dog)

    # Place them in a fool way
    container = [20, 25, 25]
    ret = bottom_front_left_2(ret, container, rotation=True)

    # Create the visualizer
    visualizer = PolyViewer3D(alpha=1, edges=False)

    # Add the polygons list to the visualizer
    visualizer.polygons = ret

    # Add points to the scene
    points = [(10, 15, 8), (0, 0, 0), [-2, -4, -6], (6, 7, -1)]
    visualizer.points = points

    # Add triangles to the scene
    triangles = [Triangle([(0.0, 0.0, 0.0), (5, 12, 0.0), (0.0, 0.0, 9)]),
                 Triangle([(5, 0.0, 0.0), (0.0, 12, 0.0), (0.0, 12, 7)])]
    visualizer.triangles = triangles

    # Plot the given container
    # Set the container
    # visualizer.container = container
    # visualizer.plot_container()

    # If you want the best container,
    # you can use this instead of plot_container()
    visualizer.plot_container_auto(container_opacity=.1)

    # Optional: show axes
    visualizer.add_axes(label='complex_mode')

    # Add objects to the scene
    visualizer.plot_objects(animate=False, delay=10)

    # Finally show the scene
    visualizer.show()

    # Or more easy:
    # Just pass the polygons and the container (this is optional)
    # PolyViewer3D.easy_plot(ret, points, animate=True, edges=True, container=(50, 50, 50))

    # # Complex scratch
    # objects = visualizer.__dict__['_PolyViewer3D__objects']
    # polygon1 = objects[1].__dict__['mlab_source']
    # from pprint import pprint
    # pprint(polygon1.__dict__)
    # pprint(polygon1.__dict__['m_data'].__dict__)
    # pprint(polygon1.__dict__['dataset'].__dict__)


if __name__ == "__main__":
    main()
