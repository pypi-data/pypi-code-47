from __future__ import print_function
import time
from . import OrthMesh
    
def setOrthotope(In,verbose,**kwargs):
  from fc_bench.bench import bData
  import numpy as np
  d=In[0]
  N=In[1]
  order=kwargs.get('order',1)
  etype=kwargs.get('type','simplex')
  m_min=kwargs.get('m_min',0)
  box=kwargs.get('box',np.tile([-1,1],(d,1)))
  Print=kwargs.get('Print',lambda s: print(s))
  mapping=kwargs.get('mapping',None)
  if isinstance(box,list):
    box=np.array(box)

  if verbose:
    Print('# fc_hypermesh.OrthMesh constructor with')
    Print('#   d      =%d'%d)
    Print('#   type   =%s'%etype)
    Print('#   order  =%d'%order)
    Print('#   box    =%s'%str(box.tolist()))
    if mapping is None:
      Print('#   mapping=None')
    else:
      from fc_tools.others import func2str
      Print('#   mapping='+func2str(mapping))
  bDs=[bData('{:>7}'.format('N'), N, '{:>7d}',7,'i8')]
  bDs.append(bData('{:>10}'.format('nq'), lambda Oh: Oh.Mesh.nq, '{:>10d}',strlen=10,numpy='i8'))
  bDs.append(bData('{:>10}'.format('nme'), lambda Oh: Oh.Mesh.nme, '{:>10d}',strlen=10,numpy='i8'))
  return ((d,N,etype,order,box,mapping,m_min),bDs,[])  
    
def bench(d,LN,**kwargs):
  import fc_bench
  import numpy as np
  Lfun=[lambda d,N,etype,order,box,mapping,m_min: OrthMesh(d,N,type=etype,order=order,box=box,mapping=mapping,m_min=m_min)]
  def setfun(In,verbose,**options):
    options.update(kwargs)
    return setOrthotope(In,verbose,**options)
  #setfun=lambda In,verbose,**options: setOrthotope(In,verbose,**options,**kwargs)
  In=np.vstack((d*np.ones((len(LN),),dtype=int),LN)).T
  return fc_bench.bench(Lfun,setfun,In,names=['OrthMesh'])
  
def benchold(d,LN,**kwargs):
  #d=3
  #ctype='simplicial'
  #Box=[[-1,1],[-1,1],[-1,1]]
  #LN=range(20,170,20)
  import numpy as np
  ctype=kwargs.get('type', 'simplex' )
  assert(ctype in ['simplex','orthotope'])
  box=kwargs.get('box',np.ones((d,1))*np.array([0,1]))
  order=kwargs.get('order', 1 )
  Oh=OrthMesh(d,2,type=ctype,box=box,order=order) # To force compilation
  print('#\n# BENCH in dimension %d with %s mesh (order %d)'%(d,ctype,order))
  print('#\n#d: %d'%d)
  print('#type: %s'%ctype)
  print('#order: %d'%order)
  print('#box: %s'%str(box).replace('\n',','))
  print('#desc:  N            nq           nme    time(s)')
  for N in LN:
    tstart=time.time()
    Oh=OrthMesh(d,N,type=ctype,box=box,order=order)
    t=time.time()-tstart
    print('     %4d  %12d  %12d     %2.3f'%(N,Oh.Mesh.nq,Oh.Mesh.nme,t))
    
def allbenchs_paper():
  import numpy as np
  boxfun=lambda dim: np.tile([-1,1],(dim,1)) 
  
  for etype in ['orthotope','simplex']:
    bench(2,np.arange(1000,5001,1000),type=etype,box=boxfun(2),order=1)
    bench(3,np.arange(40,181,20),type=etype,box=boxfun(3),order=1)
    bench(4,np.hstack((10,range(20,41,5))),type=etype,box=boxfun(4),order=1)
    bench(5,np.arange(2,13,2),type=etype,box=boxfun(5),order=1)
    
    bench(2,np.arange(1000,5001,1000),type=etype,box=boxfun(2),order=2)
    bench(3,np.arange(40,181,20),type=etype,box=boxfun(3),order=2)
    bench(4,np.hstack((10,range(20,41,5))),type=etype,box=boxfun(4),order=2)
    bench(5,np.arange(2,13,2),type=etype,box=boxfun(5),order=2)
    
    bench(2,np.hstack((500,range(1000,4001,1000))),type=etype,box=boxfun(2),order=3)
    bench(3,np.arange(40,141,20),type=etype,box=boxfun(3),order=3)
    bench(4,np.hstack((5,10,range(20,31,5))),type=etype,box=boxfun(4),order=3)
    bench(5,np.array([3,5,7,9,10]),type=etype,box=boxfun(5),order=3)
  
def allbenchs_small():
  import numpy as np
  boxfun=lambda dim: np.tile([-1,1],(dim,1)) 
  
  for etype in ['orthotope','simplex']:
    bench(2,np.array([300,350,400,450,500]),type=etype,box=boxfun(2),order=1)
    bench(3,np.arange(20,61,10),type=etype,box=boxfun(3),order=1)
    bench(4,np.arange(3,12,2),type=etype,box=boxfun(4),order=1)
    bench(5,np.arange(3,9,1),type=etype,box=boxfun(5),order=1)
    
    bench(2,np.arange(100,251,25),type=etype,box=boxfun(2),order=2)
    bench(3,np.arange(20,61,10),type=etype,box=boxfun(3),order=2)
    bench(4,np.arange(3,12,2),type=etype,box=boxfun(4),order=2)
    bench(5,np.arange(2,7,1),type=etype,box=boxfun(5),order=2)
    
    bench(2,np.arange(30,81,10),type=etype,box=boxfun(2),order=3)
    bench(3,np.arange(10,51,10),type=etype,box=boxfun(3),order=3)
    bench(4,np.arange(3,13,3),type=etype,box=boxfun(4),order=3)
    bench(5,np.arange(1,6,1),type=etype,box=boxfun(5),order=3)  

