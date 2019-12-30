from math import factorial
#from sage.combinat.combination import binomial
from scipy.special import binom as binomial

def NumberOfFaces(d,m):
  return 2**(d-m)*binomial(d,m)

def int2str(Num):
  sNum=str(Num)
  nl=len(sNum)
  nlf=nl+int(len(sNum)/3)
  S=[' ']*nlf
  k=nlf-1
  j=0
  for i in range(nl-1,-1,-1):
    S[k]=sNum[i]
    k=k-1
    j=j+1
    if (j%3==0) :
      j=0
      k=k-1
  start=0
  if S[i]==' ':
    start=1
  sNum=''
  for i in range(start,len(S)):
    sNum+=S[i]
  #sNum=sNum.replace(' ','\, ')
  #return '$'+sNum+'$'
  return sNum

def setN(N,d):
  import numpy as np
  if d==0:
    return np.array([1],dtype=int)
  if isinstance(N, list):
    assert len(N)==d
    N=np.ndarray(N,dtype=int)
  if isinstance(N,int):
    N=N*np.ones((d,),dtype=int)
  assert( isinstance(N,np.ndarray) )
  assert( (N.shape==(d,)) )
  return N

def nq(N,d,order=1):
  import numpy as np
  #N=setN(N,d)
  return np.prod(order*N+1)

def nme_orth(N,d):
  import numpy as np
  if d==0:
    return 1
  N=setN(N,d)
  return int(np.prod(N))
  
def nme_simp(N,d):
  import numpy as np
  if d==0:
    return 1
  N=setN(N,d)
  return factorial(d)*int(np.prod(N))

def faces_nq_nme(N,m,order=1,type='simplex'):
  from fc_hypermesh.CartesianGrid import combs
  import numpy as np
  assert( type in ['simplex','orthotope'])
  d=len(N)
  N=np.array(N,dtype=int)
  level=d-m
  nl=2**level
  if m==0:
    Lnq=np.ones((nl,),dtype=int)
    Lnme=np.ones((nl,),dtype=int)
    return (Lnq,Lnme)
  
  if type=='simplex':
    C=factorial(m)
  else:
    C=1
  
  if m==d:
    Lnq=np.array(nq(N,d,order=order),dtype=int)
    Lnme=np.array(C*np.prod(N),dtype=int)
    return (Lnq,Lnme)
  
  L=combs(np.arange(d),d-m)
  nc=L.shape[0]
  R=np.flipud(combs(np.arange(d),m))
  nl=2**level
  nf=nl*nc # nb of m-faces
  Lnq=np.zeros((nf,),dtype=int)
  Lnme=np.zeros((nf,),dtype=int)
  
  k=0
  for l in range(nc):
    NN=N[R[l,:]]
    for i in range(nl):
      Lnq[k]=nq(NN,len(NN),order=order)
      Lnme[k]=C*np.prod(NN)
      k+=1  
  return (Lnq,Lnme)

def OrthMesh_nbs(N,**kwargs):
  """
     Returns numbers of float and int
  """
  type=kwargs.get('type','simplex')
  assert( type in ['simplex','orthotope'])
  order=kwargs.get('order',1)
  from scipy.special import comb
  import numpy as np
  d=len(N)
  Lm=kwargs.get('Lm',np.arange(d+1))
  Lm=np.unique(np.array(Lm,dtype=int))
  assert(Lm.max()<=d and Lm.min()>=0)
  
  nb_float=0;nb_int=0
  if type=='simplex':
    fun=lambda m: comb(m+order,order)
  else:
    fun=lambda m: (order+1)**m  
  
  for m in Lm:
    Lnq,Lnme=faces_nq_nme(N,m,order=order,type=type)
    Lnq=Lnq.sum()
    nb_float+=d*Lnq
    S=Lnme.sum()
    if m<d:
      nb_int+=S*fun(m)+Lnq # me and toGlobal array
    else:
      nb_int+=S*fun(m)
  return (int(nb_float),int(nb_int))

def sizeof_OrthMesh(N,**kwargs):
  split=kwargs.pop('split',False)
  nb_float,nb_int=OrthMesh_nbs(N,**kwargs)
  bytes_float=kwargs.get('bytes_float',8)
  bytes_int=kwargs.get('bytes_int',8)
  if split:
    return (bytes_float*nb_float,bytes_int*nb_int)
  else:
    return bytes_float*nb_float+bytes_int*nb_int
  
def qsize(N,d,order=1):
  return int(nq(N,d,order)*d*8) # size in octets, double : 8 octets
  
def mesize_orth(N,d,order=1):
  return int(nme_orth(N,d)*((order+1)**d)*4) # size in octets, int : 4 octets
  
def mesize_simp(N,d,order=1):
  return int(nme_simp(N,d)*(binomial(d+order,order))*4) # size in octets, int : 4 octets

def memOrthMesh_simp(N,d,order=1):
  N=setN(N,d)
  mem_size=0
  for m in range(d):
    nbFaces=NumberOfFaces(d,m)
    memByFace=mesize_simp(N,m,order)+qsize(N,m,order)
    mem_size+= nbFaces*memByFace
  return int(mem_size)

def memOrthMesh_orth(N,d,order=1):
  N=setN(N,d)
  mem_size=0
  for m in range(d):
    nbFaces=NumberOfFaces(d,m)
    memByFace=mesize_orth(N,m,order)+qsize(N,m,order)
    mem_size+= nbFaces*memByFace
  return int(mem_size)

def memOrthMesh(N,d,order=1,type='simplex'):
  assert( type in ['simplex','orthotope'] )
  if type=='simplex':
    return memOrthMesh_simp(N,d,order=order)
  return memOrthMesh_orth(N,d,order=order)

def checkmem(N,d,order=1,type='simplex',verbose=False):
  import math,fc_tools
  RAM=fc_tools.Sys.getRAM()/10**3 # in Go
  RAMneeded=memOrthMesh(N,d,order=order,type=type)/10**9
  if verbose:
    print('RAM, available=%.2f Go, needed=%.2f Go'%(RAM,RAMneeded))
  return (RAM> 1.5*RAMneeded)

def ino(obj):
  return int2str(obj)+' o'

def inKo(obj):
  obj=int(obj/10**3)
  return int2str(obj)+' ko'

def inMo(obj):
  obj=int(obj/10**6)
  return int2str(obj)+' Mo'

def inGo(obj):
  obj=int(obj/10**9)
  return int2str(obj)+' Go'

def inTo(obj):
  obj=int(obj/10**12)
  return int2str(obj)+' To'

def autoO(obj):
  if (obj < 10**3):
    return ino(obj)
  elif (obj < 10**6):
    return inKo(obj)
  elif (obj < 10**9):
    return inMo(obj)
  elif (obj < 10**12):
    return inGo(obj)
  else:
    return inTo(obj)
  
def inB(obj):
  return int2str(obj)+' B'

def inKB(obj):
  obj=int(obj/10**3)
  return int2str(obj)+' KB'

def inMB(obj):
  obj=int(obj/10**6)
  return int2str(obj)+' MB'

def inGB(obj):
  obj=int(obj/10**9)
  return int2str(obj)+' GB'

def inTB(obj):
  obj=int(obj/10**12)
  return int2str(obj)+' TB'

def autoB(obj):
  if (obj < 10**3):
    return inB(obj)
  elif (obj < 10**6):
    return inKB(obj)
  elif (obj < 10**9):
    return inMB(obj)
  elif (obj < 10**12):
    return inGB(obj)
  else:
    return inTB(obj)
  
def double2str(x,prec=3):
  ff='%%.%df'%prec
  return ff%x
