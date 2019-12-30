""" ============================
    Cartesian Grid Tessellations
    ============================
    
    Provides tessellation of a cartesian grid CG(N)=[0,N1]x...x[0,Nd] with 
    p-order unit hypercubes or with p-order simplices.
    
    Explanation can be found in the report 'Vectorized algorithms for regular and 
    conforming tessellations of d-orthotopes and their faces with high-order 
    orthotopes or simplicial elements' by F. Cuvelier and available at 
    http:\\...

    ==================== =========================================================
    Utility functions
    ==============================================================================
    perms                Generate all permutations of V.
                         See `Perms`function in the report.
    combs                Generate all combinations of V taken k at a time.
                         See `Combs` function in the report.
    betafunc             Compute the 'beta' integer array.
                         See `CGbeta` function in the report.
    
    ==================== =========================================================
    
    ==================== =========================================================
    Tessallation functions
    ==============================================================================
    points               Compute the points of the Cartesian grid CG(N)
                         See `CartesianGridPoints` function in the report.
    TessHyp              Cartesian grid CG(N) tessallation with unit hypercube
                         see `CartesianGridTessHyp` function in the report 
    KuhnTriangulation    Kuhn's triangulation of the unit d-hypercube [0,1]^d with
                         d! simplices. 
                         See `KuhnTriangulation` function in the report.
    TessSim              Cartesian grid CG(N) tessallation with simplices.
                         see `CGTessTri` function in the report
    TessFaces            Computes all m-faces tessellations of the cartesian grid 
                         CG(N) with unit m-hypercubes.
                         see `CGTriFaces` function in the report
    TriFaces             Computes all m-faces tessellations of the cartesian grid 
                         CG(N) with unit m-simplices.
                         see `CGTessFaces` function in the report
    ==================== =========================================================
  
"""

import numpy as np
import itertools
from math import factorial


def perms(V):
  """ P=perms(V)
  Generate all permutations of V, one row per permutation. The lexicographical 
  order is choosen. The result is a numpy array with size N!-by-N, where N 
  is the length of V. 
  
  Parameters
  ----------
  V : list or array of N scalars
  
  Returns
  -------
  P : (N!,N) shaped ndarray
  
  As an example, 'perms ([1, 2, 3])' returns the numpy array
  
  >>> P=perms([1, 2, 3])
  >>> P
  array([[1, 2, 3],
         [1, 3, 2],
         [2, 1, 3],
         [2, 3, 1],
         [3, 1, 2],
         [3, 2, 1]])    
          
  See `Perms` function in the report.
  """
  return np.array([x for x in itertools.permutations(V,len(V))])

def combs(V,k):
  """
  C=combs(V,k)
  
  Generate all combinations of V taken k at a time, one row per combination. 
  The lexicographical order is choosen. The result is a numpy array with 
  size N!/(k!(n-k)!)-by-k, where N is the length of V and 1<=k<=N.
  
  Parameters
  ----------
  V : list or array of N scalars
  k : integer (0<=k<=N)
  
  Returns
  -------
  C : (N!/(k!(N-k)!),k) shaped ndarray
  
  As an example:
  
  >>> C=combs([1,2,3,4],2)
  >>> C  
  array([[1, 2],
         [1, 3],
         [1, 4],
         [2, 3],
         [2, 4],
         [3, 4]])
    
  See `Combs` function in the report.
  """
  assert (len(V)>=k) and (k>=1)
  return np.array([x for x  in itertools.combinations(V,k)],dtype=np.int64)

def betafunc(N):
  """ beta=betafunc(N)
  
      Compute the 'beta' integer array of size `len(N)` such that
        beta[0]=1 
      and for all l in {1,...,len(N)-1} 
        beta[l] = beta[l-1]*(N[l-1]+1)  
      
      See `CGbeta` function in the report.
  """
  N=np.array(N,dtype=int)
  d=len(N)
  beta=np.ones((d,),dtype=int)
  for l in np.arange(1,d):
    beta[l]=beta[l-1]*(N[l-1]+1)
  return beta

def points(N):
  """ q=points(N)
  
      Compute a d-by-nq array which contains all the points of the cartesian grid CG(N)
      with ``d=len(N)`` and ``nq = (N[0]+1)*...*(N[d]+1)``
      
      Parameters
      ----------
      N : list or array of d integers. The cartesian grid CG(N) is then defined on
             [0,N[0]]x...x[O,N[d-1]]
      
      Returns
      -------
      q : vertices array of the triangulation of CG(N), (d,nq)-shaped ndarray of 
          floats where ``nq=prod(N+1)`` and ``d=len(N)``
      
      As an example:
  
      >>> q=points([10,7,9,13])
      >>> q
      array([[  0.,   1.,   2., ...,   8.,   9.,  10.],
            [  0.,   0.,   0., ...,   7.,   7.,   7.],
            [  0.,   0.,   0., ...,   9.,   9.,   9.],
            [  0.,   0.,   0., ...,  13.,  13.,  13.]])      
            
      See `CartesianGridPoints` function in the report.
  """
  N=np.array(N,dtype=int)
  d=len(N)
  beta=betafunc(N)
  q=np.zeros((d,np.prod(N+1))) # Must be float when using with MappingBox function
  for r in range(d):
    A=np.tile(np.arange(N[r]+1),(beta[r],1)).flatten(order='F')
    q[r,:]=np.tile(A,(1,np.prod(N[r+1:]+1)))
  return q

def TessHyp(N,p=1):
  """ q,me=TessHyp(N,p=1)
  
      Computes the vertices array ``q`` and the connectivity array ``me`` obtained 
      from a tesselation of the cartesian grid CG(N) with unit ``p``-order hypercube.
      
      Parameterslabel
      ----------
      N : list or array of d integers. The cartesian grid CG(N) is then defined on
             [0,N[0]]x...x[O,N[d-1]]
      p : order, positive integer.
      
      Returns
      -------
      q : vertices array of the triangulation of CG(N), (d,nq)-shaped ndarray of 
          integers where ``nq=prod(p*N+1)`` and ``d=len(N)``
      me: connectivity array of the triangulation of CG(N), ((p+1)^d,nme) shaped ndarray 
          of integers  where ``nme=prod(N)``. 
      
      As an example:
  
      >>> q,me=TessHyp([10,7,9,13])
      >>> q
      array([[  0.,   1.,   2., ...,   8.,   9.,  10.],
            [  0.,   0.,   0., ...,   7.,   7.,   7.],
            [  0.,   0.,   0., ...,   9.,   9.,   9.],
            [  0.,   0.,   0., ...,  13.,  13.,  13.]])
      >>> me
      array([[    0,     1,     2, ..., 11337, 11338, 11339],
            [    1,     2,     3, ..., 11338, 11339, 11340],
            [   11,    12,    13, ..., 11348, 11349, 11350],
            ..., 
            [  969,   970,   971, ..., 12306, 12307, 12308],
            [  979,   980,   981, ..., 12316, 12317, 12318],
            [  980,   981,   982, ..., 12317, 12318, 12319]])      
      
      See `CGTessHyp` function in the report.
  """
  N=np.array(N,dtype=int)
  d=len(N)
  q=points(p*N)/p
  Hinv=p*points(N-1).astype(int)
  pqhat=points(p*np.ones(d)).astype(int)
  beta=betafunc(p*N)
  iBase=beta.dot(Hinv) # array index start to 0 
  nl=(p+1)**d
  me=np.tile(iBase,(nl,1)) +np.tile(beta.dot(pqhat).reshape((nl,1)),(1,len(iBase)))
  return q,me

def NodesSimRef(d,k):
  q=points(k*np.ones((d,)))/k
  return q[:,np.sum(q,axis=0)<=1]

def RefElement(d,order,**kwargs):
  EltType=kwargs.get('type','simplex')
  assert(EltType in ['simplex','orthotope'])
  q=points(order*np.ones((d,)))/order
  if EltType=='simplex':
    q=q[:,np.sum(q,axis=0)<=1]
  me=np.arange(q.shape[1]).reshape((q.shape[1],1))
  return q,me
  
def VerticesIdxHypRef(d,k):
  N=np.ones((d,))
  beta=betafunc(k*N)
  q=k*points(N)
  Idx=beta.dot(q).astype(int)
  #Idxc=setdiff1d(np.arange((k+1)**d),Idx)
  return Idx#,Idxc

def VerticesIdxSimRef(d,k):
  Kref=NodesSimRef(d,k)
  Idx=np.zeros((d+1,),dtype=int)
  Idx[0]=np.where(Kref.sum(axis=0)==0)[0][0]
  for i in range(d):
    Idx[i+1]=np.where(Kref[i]==1)[0][0]
  #Idxc=np.setdiff1d(np.arange(Kref.shape[1]),Idx)
  return Idx#,Idxc

def KuhnTriangulation(d):
  """ q,me=KuhnTriangulation(d)
  
      Kuhn's triangulation of the unit d-hypercube [0,1]^d with d! simplices.
      (positive orientation) 

      Parameters
      ----------
      d : space dimension
      
      Returns
      -------
      q : vertices array of the unit d-hypercube [0,1]^d. 
          (d,2^d)-shaped ndarray of integers.
      me: connectivity array of the unit d-hypercube [0,1]^d. 
          (d+1,d!) shaped ndarray of integers.
  
      As firt example:
      
      >>> q,me=KuhnTriangulation(2)
      >>> q 
      array([[ 0.,  1.,  0.,  1.],
             [ 0.,  0.,  1.,  1.]])
      >>> me
      array([[0, 3],
             [1, 2],
             [3, 0]])
                   
      As second example:
      
      >>> q,me=KuhnTriangulation(3)
      >>> q 
      array([[ 0.,  1.,  0.,  1.,  0.,  1.,  0.,  1.],
             [ 0.,  0.,  1.,  1.,  0.,  0.,  1.,  1.],
             [ 0.,  0.,  0.,  0.,  1.,  1.,  1.,  1.]])
      >>> me
      array([[0, 7, 7, 0, 0, 7],
             [1, 1, 2, 4, 2, 4],
             [3, 5, 3, 5, 6, 6],
             [7, 0, 0, 7, 7, 0]])            
                       
      See `KuhnTriangulation` function in the report.
  """
  q=points(np.ones(d))
  qref=np.vstack([np.zeros((1,d)),np.tril(np.ones((d,d)))]).T
  P=perms(np.arange(d))
  nme=factorial(d);nq=2**d
  me=np.zeros((d+1,nme),dtype=int)
  A=np.matrix(2**np.arange(d))
  for k in range(nme):
    me[:,k]=A*qref[P[k]]
    ql=q[:,me[:,k]]
    if np.linalg.det(np.r_[ql,np.ones((1,d+1))])<0:
      tmp=me[0,k];me[0,k]=me[d,k];me[d,k]=tmp
  return q,me

def KuhnTriangulationOrder(d,p):
  q,me=KuhnTriangulation(d)
  if p==1:
    return q,me
  QSimRef=p*NodesSimRef(d,p)
  N=QSimRef.shape[1]
  beta=betafunc(p*np.ones((d,),dtype=int))
  qk=points(p*np.ones((d,),dtype=int))/p
  nme=me.shape[1] # i.e. d!
  mek=np.zeros((N,nme),dtype=int)
  for l in range(nme):
    Q=q[:,me[:,l]]
    AK=Q[:,1:]-Q[:,0]
    QK=np.matmul(AK,QSimRef)+p*Q[:,0].reshape((d,1))
    mek[:,l]=np.matmul(beta,QK)
  return qk,mek

def TessSim(N,p=1):  
  """ q,me=TessSim(N,p=1)
  
      Compute the vertices array ``q`` and the connectivity array ``me`` obtained 
      from a tesselation of the cartesian grid CG(N) with p-order simplices by using 
      the Kuhn Triangulation.
      
      Parameters
      ----------
      N : list or array of d integers. The cartesian grid CG(N) is then defined on
             [0,N[0]]x...x[O,N[d-1]]
      p : order, positive integer
      
      Returns
      -------
      q : nodes array of the triangulation of CG(N), (d,nq)-shaped ndarray of 
          integers where ``nq=prod(p*N+1)`` and ``d=len(N)``
      me: connectivity array of the triangulation of CG(N), (C,nme) shaped ndarray 
          of integers  where ``nme=factorial(d)*prod(N). 
      
      As an example: 
      
      >>> q,me=Triangulation([20,100,30])
      >>> q
      array([[   0.,    1.,    2., ...,   18.,   19.,   20.],
             [   0.,    0.,    0., ...,  100.,  100.,  100.],
             [   0.,    0.,    0., ...,   30.,   30.,   30.]])
      >>> me
      array([[    0,  2143,  2143, ..., 63607, 63607, 65750],
             [    1,     1,    21, ..., 65728, 63628, 65728],
             [   22,  2122,    22, ..., 65729, 65749, 65749],
             [ 2143,     0,     0, ..., 65750, 65750, 63607]])
      
      See function `CGTessSim` in the report.
  """
  N=np.array(N)
  d=len(N)
  q=points(p*N)/p
  beta=betafunc(p*N)
  ibase=p*beta.dot(points(N-1))
  Nh=ibase.shape[0]
  qK,meK=KuhnTriangulationOrder(d,p)
  fd=factorial(d)
  me=np.zeros((meK.shape[0],fd*Nh),dtype=int)
  Idx=fd*np.arange(Nh)
  for j in range(meK.shape[0]):
    for l in range(fd):
      me[j,Idx+l]=ibase+p*beta.dot(qK[:,meK[j,l]])
  return q,me
    
def genTessFaces(N,m,**kwargs):
  """ Computes all m-faces tessellations of the cartesian grid CG(N) 
      with m-simplices or m-orthotopes.
      
      See `CGTessSimFaces` or `CGTessHypFaces` functions in the report.
  """
  from .EltMesh import EltMesh
  EltType=kwargs.get('type','simplex')
  p=kwargs.get('order',1)
  assert(EltType in ['simplex','orthotope'])
  if EltType=='simplex':
    TessFun=lambda N: TessSim(N,p)
  else:
    TessFun=lambda N: TessHyp(N,p)
  N=np.array(N)
  d=len(N)
  level=d-m
  beta=betafunc(p*N)
  sTh=[]
  if m==0:
    Q=np.diag(N).dot(points(np.ones(d)))
    ind=p*beta.dot(Q)
    for k in range(Q.shape[1]):
      sTh.append(EltMesh(d,m,np.array([Q[:,k]]).T,np.array([[0]]),toGlobal=ind[k]))
    return sTh
  S=points(np.ones(level))
  L=combs(np.arange(d),d-m)
  nc=L.shape[0]
  R=np.flipud(combs(np.arange(d),m))
  for l in range(nc):
    qw,mew=TessFun(N[R[l,:]])
    nq=qw.shape[1]
    for r in range(2**level):
      q=np.zeros((d,nq))
      q[R[l],:]=qw
      tmp=np.matrix(N[L[l,:]].T*S[:,r]).T
      q[L[l],:]=tmp*np.ones(nq)
      sTh.append(EltMesh(d,m,q,mew,toGlobal=(p*beta).dot(q),order=p))
  return sTh
    
def TriFaces(N,m):    # TriFaces -> TessSimFaces
  """ sTh=TriFaces(N,m)
  
      Compute all m-faces tessellations of the cartesian grid CG(N) 
      with m-simplices.
      
      Parameters
      ----------
      N : list or array of d integers. The cartesian grid CG(N) is then defined on
             [0,N[0]]x...x[O,N[d-1]]
      m : integer (0<=m<=len(N)).
      
      Returns
      -------
      sTh :  list of EltMesh. Its length is the number of m-faces of CG(N):
          len(sTh)== 2**(d-m)*factorial(d)/(factorial(m)*factorial(d-m))
          
      :example:
      
      >>> sTh=TriFaces([20,100,30],2)
      >>> len(sTh)
      6
      >>> sTh[3]
      EltMesh object 
          type (str): simplicial
          type : 0
            d : 3
            m : 2
            q : (3,651)
            me : (3,1200)      
      
      See `CGTriFaces` function in the report.
  """
  return genTessFaces(N,m,type='simplex')

def TessFaces(N,m):     # TessFaces -> TessHypFaces
  """ sTh=TessFaces(N,m)
  
      Compute all m-faces tessellations of the cartesian grid CG(N) 
      with unit m-hypercubes.
      
            Parameters
      ----------
      N : list or array of d integers. The cartesian grid CG(N) is then defined on
             [0,N[0]]x...x[O,N[d-1]]
      m : integer (0<=m<=len(N)).
      
      Returns
      -------
      sTh :  list of EltMesh. Its length is the number of m-faces of CG(N):
          len(sTh)== 2**(d-m)*factorial(d)/(factorial(m)*factorial(d-m))
          
      :example:
      
      >>> sTh=TessFaces([20,100,30],2)
      >>> len(sTh)
      6
      >>> sTh[3]
      EltMesh object 
          type (str): orthotope
          type : 1
            d : 3
            m : 2
            q : (3,651)
            me : (4,600)
      
      See `CGTessFaces` function in the report.
  """
  return genTessFaces(N,m,type='orthotope')
