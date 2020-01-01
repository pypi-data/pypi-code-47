# from scipy.spatial import Delaunay
#
# polygon = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
#
# tri = Delaunay(polygon)
#
# print(len(tri.simplices))
# print(tri.simplices)

from polyutils.rectangle import Rectangle

r = Rectangle(size=(1,2,3))

xxx = r.vertices

for x in xxx:
    print(x)
