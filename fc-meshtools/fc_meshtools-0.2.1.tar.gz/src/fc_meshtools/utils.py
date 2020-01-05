import numpy as np
from fc_tools.graphics import Plane

def feval(fun,q):
  fun=np.vectorize(fun)
  if q.shape[0]==2:
    u=fun(q[0],q[1])
  if q.shape[0]==3:
    u=fun(q[0],q[1],q[2])
  return u

def barycenters(q,me):
  dim=q.shape[0]
  Ba=np.zeros((dim,me.shape[1]))
  for i in range(me.shape[0]):
    Ba+=q[:,me[i]]
  Ba/=me.shape[0]
  return Ba 

def cutMeshElements(q,me,cut_planes):
  ME=me
  if cut_planes != []:
    idxme=cutIndexMeshElements(q,me,cut_planes)
    ME=ME[:,idxme]
  return ME

def cutIndexMeshElements(q,me,cut_planes):
  # cut_planes is a list of fc_simesh.mayavi_tools.Plane objects
  idxme=np.arange(me.shape[1])
  for i in range(len(cut_planes)):
    assert( isinstance(cut_planes[i] , Plane) )
    idxme=np.setdiff1d(idxme,_cutIndexPlane(q,me,cut_planes[i]))
  return idxme

# private functions
      
def _cutIndexPlane(q,me,P):
  nq=q.shape[1]
  Z=np.dot( q.T-P.origin , P.normal) # using broadcasting
  idx=np.where(Z<0)[0]
  R=np.in1d(me[0],idx)
  for i in range(1,me.shape[0]):
    R[:]=R & np.in1d(me[i],idx) 
  return np.where(~R)[0]

def getDataPath(): 
  import os
  fullname=os.path.dirname(os.path.abspath(__file__))
  return fullname+os.sep+'data'

def getMesh(dim,d,**kwargs):
  import os
  assert( dim in [2,3] )
  assert( d in range(dim+1) )
  Type=kwargs.pop('type','simplex')
  assert( Type in ['simplex','orthotope'])
  small=kwargs.pop('small',False)
  surface=kwargs.pop('surface',False)
  verbose=kwargs.pop('verbose',False)
  order=kwargs.pop('order',1)
  assert( order in [1,2,3,4] )
  sstr='%dD'%dim
  if surface:
    assert( dim ==3 )
    sstr+='s'
  s=''
  if small:
    s='_small'
  filename='mesh%d%s%dorder%s%s.npz'%(d,Type[:4],order,sstr,s)  
  if verbose:
    print('Reading file '+filename)
  npzfile = np.load(getDataPath()+os.sep+filename)
  q=npzfile['arr_0']
  me=npzfile['arr_1']
  toGlobal=npzfile['arr_2']
  return q,me,toGlobal
