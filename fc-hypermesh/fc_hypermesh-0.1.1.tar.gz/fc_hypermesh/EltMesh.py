""" =======
    EltMesh
    =======
    
    Only contains the `EltMesh` class used by `OrthMesh` class.
"""

from fc_tools.others import isModuleFound

class EltMesh:
  """ class EltMesh
  
      This class is used to store an elementary mesh given by its vertices array `q` and 
      its connectivity array `me`
      
      see description in `Class object OrthMesh` in the report.
  """
  def __init__(self,d,m,q,me,**kwargs):
    import numpy as np
    from scipy.special import comb
    color=kwargs.get('color', [0,0,1] )
    label=kwargs.get('label', 0 )
    type=kwargs.get('type', None)
    toGlobal=kwargs.get('toGlobal', None)
    p=kwargs.get('order', 1 )
    assert  m <= d 
    assert q.shape[0]==d 
    self.d=d
    self.m=m
    self.q=q
    self.me=me
    self.order=p
    if type is None:
      if (me.shape[0]==comb(m+p,p)): # m-simplicial
        self.type=0
      elif (me.shape[0]==(p+1)**m): # m-orthotope
        self.type=1;
      else:
        raise NameError('Trouble with "me" dimension!')
    else:
      assert type in [0,1]
      assert ( (type==0) and (me.shape[0]==comb(m+p,p)) ) or ( (type==1) and (me.shape[0]==(p+1)**m) ) 
      self.type=type
      
    self.nq=q.shape[1]
    self.nme=me.shape[1]
    if toGlobal is None:
      self.toGlobal=None
    else:
      self.toGlobal=np.array(toGlobal,dtype=int)
    from fc_hypermesh import CartesianGrid as CG  
    if self.type==0:
      self.ivertex=CG.VerticesIdxSimRef(m,p)
    else:
      self.ivertex=CG.VerticesIdxHypRef(m,p)
    self.color=color
    self.label=label
    
  def __repr__(self):
    strret = ' %s object \n'%self.__class__.__name__ 
    #strret += '    type (str): %s\n'%self.strtype()
    strret += '    type : %d (%s)\n'%(self.type,self.strtype())
    strret += '   order : %d\n'%self.order
    strret += '   label : %d\n'%self.label
    strret += '       d : %d\n'%self.d 
    strret += '       m : %d\n'%self.m
    strret += '       q : (%d,%d)\n'%self.q.shape
    strret += '      me : (%d,%d)\n'%self.me.shape
   # strret += 'toGlobal : (%d,)\n'%self.toGlobal.shape
    return strret  

  def strtype(self):
    if self.type==0:
      return 'simplex'
    if self.type==1:  
      return 'orthotope'
    return 'unknow'
  
  def barycenters(self):
    import numpy as np
    Ba=np.zeros((self.d,self.nme))
    for i in range(len(self.ivertex)):
      Ba+=self.q[:,self.me[self.ivertex[i]]]
    Ba/=len(self.ivertex)
    return Ba
  
  def sizeof(self):
    import sys
    return (sys.getsizeof(self.q),sys.getsizeof(self.me)+sys.getsizeof(self.toGlobal)+sys.getsizeof(self.ivertex))
  
  #def get_memory(self):  % in bytes (only arrays)
    #return 4*(np.prod(self.me.shape)+len(self.toGlobal)+len(self.ivertex))+8*np.prod(self.q.shape)
  
  if isModuleFound('matplotlib'):
    from .Matplotlib import plotmesh,plotnodes,plotnodesNumber,ploteltsNumber
    
