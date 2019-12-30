""" ====================
    fc_hypermesh package
    ====================
    
    The fc_hypermesh package contains a simple class object `OrthMesh` which 
    permits, in any dimension d>=1 to obtain a simplicial mesh or orthotope mesh 
    with all their m-faces, 0<=m<d,$ of a d-orthotope. If the `Matplotlib` package
    is installed, it is also possible with the `plotmesh` method of the class 
    object `OrthMesh` to represent a mesh or its m-faces for d<=3.
    
    ==================== =========================================================
    Objects
    ==============================================================================
    OrthMesh             Contain a main mesh of a d-orthotope and all its m-faces. 
                         See `OrthMesh` help.
    EltMesh              Elementary mesh (low level class).
                         See `EltMesh` help.
                         
    ==================== =========================================================
    Demo functions
    ==============================================================================
    See `demos` help
    
    ==================== =========================================================
    Benchmark functions
    ==============================================================================
    See `benchs` help
    
    Algorithms used in `fc_hypermesh` package are described in the report 
      'Vectorized algorithms for regular tessellations of d-orthotopes and 
       their faces' 
    by F. Cuvelier and available at http:\\...
    
    :author:     F. Cuvelier
    :email:      cuvelier@math.univ-paris13.fr
    :copyright:  (c) 2017
    :license:    GNU General Public License.
"""
__version__='0.1.1' # automaticaly written by setpackages.py script
__packages__={'fc-tools': '0.0.24', 'fc-bench': '0.2.0'} # automaticaly written by setpackages.py script
from fc_hypermesh.OrthMesh import OrthMesh
from fc_hypermesh.benchs import bench
from fc_hypermesh import demos

from fc_tools.others import isModuleFound
if isModuleFound('matplotlib'):
  from fc_hypermesh import Matplotlib
  
def gitinfo():
  return {'name': 'fc-hypermesh', 'tag': '0.1.1', 'commit': '97eb31268a3ddef0095d487bcb11190a309529f0', 'date': '2019-12-29', 'time': '14-51-49', 'status': '0'} # automatically updated
  if len(inf)>0: 
    return inf
  # Only for developpers
  import fc_tools,os
  D=os.path.realpath(os.path.join(__path__[0],os.path.pardir))
  if os.path.basename(D)=='src':
    D=os.path.realpath(os.path.join(D,os.path.pardir))
  return fc_tools.git.get_info(D)

