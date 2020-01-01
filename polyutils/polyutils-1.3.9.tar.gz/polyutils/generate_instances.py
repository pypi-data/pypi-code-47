from polyutils.rectangle import Rectangle
import numpy as np

ret = [
    Rectangle(
        [1, 2, 4], color=np.random.rand(1, 3), id_pol=i
    ) for i in range(6)
]

for k, i in enumerate(ret):
    i.rotate_rectangle(k)

objs = [i.get_obj(k, 5) for k, i in enumerate(ret)]

path = 'instances1/'
for k, obj in enumerate(objs):
    file = open(path + "coelho{}.obj".format(k), "w")
    file.write(obj)
    file.close()
