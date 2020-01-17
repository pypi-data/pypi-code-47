import case_setup
import uedge.uedgeplots as up
from uedge.hdf5 import *
hdf5_restore('d3d.hdf5')
from uedge import bbb
bbb.exmain()
#up.plotmesh(block=True)
from uedge.double import uedouble
uedouble()
bbb.exmain()
#up.plotmesh(block=True)
#up.plotmeshval(bbb.tis/bbb.ev)
up.rendermeshval('junk.tris',bbb.tis,ixmax=10,iymax = 5)
