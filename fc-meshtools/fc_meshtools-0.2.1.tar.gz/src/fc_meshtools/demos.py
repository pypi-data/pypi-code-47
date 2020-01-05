import numpy as np
import os

from fc_meshtools import simplicial,orthotope,feval,getMesh

def demo(dim,**kwargs):
  assert( dim in [2,3] )
  surface=kwargs.get('surface',False)
  Type=kwargs.get('type','simplex')
  verbose=kwargs.get('verbose',False)
  small=kwargs.get('small',True)
  assert( Type in ['simplex','orthotope'])
  dmax=dim
  if surface:
    assert( dim ==3 )
    dmax=2
  if dim==3:
    u=lambda x,y,z:  3*np.exp(-((x-1)**2+y**2)/10)*np.cos(x-1)*np.sin(y-z);
  else:
    u=lambda x,y:  3*np.exp(-((x-1)**2+y**2)/10)*np.cos(x-1)*np.sin(y);
    
  Q,ME,toG=getMesh(dim,dmax,**kwargs)
  U=feval(u,Q)
  if verbose:
    print('  -> d=%d, q: %s array, me: %s array'%(dmax,str(Q.shape),str(ME.shape))) 
  res=0
  for d in reversed(range(dmax)):
    q,me,toGlobal=getMesh(dim,d,**kwargs)
    if verbose:
      print('  -> d=%d, q: %s array, me: %s array'%(d,str(q.shape),str(me.shape)))
    E=np.max(np.abs(Q[:,toGlobal]-q)) 
    res=res+(E >1e-15)
    if verbose:
      if E >1e-15:
        print('  Test 1: failed with E=%g'%(E))
      else:
        print('  Test 1: OK')
    Ul=feval(u,q)
    E=np.max(np.abs(U[toGlobal]-Ul))
    res=res+(E >1e-15)
    if verbose:
      if E >1e-15:
        print('  Test 2: failed with E=%g'%(E))
      else:
        print('  Test 2: OK')
  return res==0

def rundemo(strdemo):
  print('[fc_meshtools] Running %s'%strdemo)
  isOK=eval(strdemo)
  if isOK:
    print('  -> OK')
  else:
    print('  -> Failed')
  return isOK
  
def alldemos(verbose=False):
  res=0
  for order in [1,2,3,4]:
    for Type in ['simplex','orthotope']:
      for small in [False,True]:
        strdem="demo(2,verbose=%s,small=%s,surface=False,type='%s',order=%d)"%(verbose,small,Type,order)
        isOK=rundemo(strdem)
        res+= (not isOK)
        strdem="demo(3,verbose=%s,small=%s,surface=True,type='%s',order=%d)"%(verbose,small,Type,order)
        isOK=rundemo(strdem)
        res+= (not isOK)
        strdem="demo(3,verbose=%s,small=%s,surface=False,type='%s',order=%d)"%(verbose,small,Type,order)
        isOK=rundemo(strdem)
        res+= (not isOK)  
  if res==0:
    print("=========")
    print("ALL IS OK")
    print("=========")
  else:
    print("===========================")
    print("AT LEAST ONE TEST FAILED!!!")
    print("===========================")
