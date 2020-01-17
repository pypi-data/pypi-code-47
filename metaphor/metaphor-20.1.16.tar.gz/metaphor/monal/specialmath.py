#-*- coding: ISO-8859-15 -*-
#===============================================================================
# $Id: specialmath.py 4789 2018-06-08 11:40:08Z jeanluc $
#  Module  _specialmath
#  Projet MonalPy
# 
#    Ce module pourra etre supprime avec python 3.x
# 
#  Implementation python de monal
#
#
# Copyright 2016 Jean-Luc PLOIX
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#===============================================================================

import sys, os  #, math
from math import  sqrt, isinf, isnan, fabs, fsum
from numpy.random import random
import numpy as np

try:
    from scipy.linalg import svd
except ImportError: pass

from .monalconst import LEV_EARLY, LEV_MONARI

assert sys.version_info > (2, 6) 

'''
Created on 30 déc. 2009

@author: Jean-Luc PLOIX
'''
DBL_MAX = 1.79769313486231e+308
DBL_MIN = 2.2250738585072013e-308

def sqr(X):
    return X*X
    
def isinfinite(value):
    return isinf(value)

def ispinfinite(value):
    return isinf(value) and (value > 0)

def isminfinite(value):
    return isinf(value) and (value < 0)

def isspecial(value):
    return isnan(value) or isinf(value)

class _Special(float):
    """_Special numbers: Inf, -Inf, NaN"""
    def __init__(self): super(_Special, self).__init__()
    def __int__(self): return self
    def __float__(self): return self
    def __repr__(self): return "%s()"% self.__class__.__name__
    def __eq__(self, val): return False
    def __ne__(self, val):  return not isinstance(val, self.__class__)
    def __radd__(self, val): return self.__add__(val)
    def __rmul__(self, val): return self.__mul__(val)
    def __bool__(self): return True
    def __hash__(self): return hash(self.__repr__())
        
class _baseInfinity(_Special):
    """Tous les infinis"""
    def otherimplementation(self): return None
    def __abs__(self): return INF
    def __mul__(self, val): 
        if isinstance(val, _NaN) or (val == 0): return NaN
        if val < 0: return self.otherimplementation()
        return self
    def __neg__(self): return self.otherimplementation()
    def __sub__(self, val): 
        if isinstance(val, (self.__class__, _NaN)): return NaN
        return self
    def __rsub__(self, val): 
        if isinstance(val, (self.__class__, _NaN)): return NaN
        return _NegInfinity()
    def __div__(self, val): 
        if isspecial(val): return NaN
        return self
    def __rdiv__(self, val): 
        if isspecial(val): return NaN
        return 0.0
    def __invert__(self):
        return 0.0

class _Infinity(_baseInfinity):
    """Classe représentant l'infini positif
"""
    def otherimplementation(self): return NEGINF
    def __str__(self): return 'INF'
    def sqrt(self, context=None): return self
    def __add__(self, val):
        if isinstance(val, (_NegInfinity, _NaN)): return NaN
        return self
    def __gt__(self, val):
        if isinstance(val, self.__class__): return False
        return True
    def __ge__(self, val):
        if isinstance(val, self.__class__): return False
        return True
    
class _NegInfinity(_baseInfinity):
    """Classe représentant l'infini negatif
"""
    def otherimplementation(self): return INF
    def __str__(self): return "-INF"
    def __add__(self, val): 
        if isinstance(val, (_Infinity, _NaN)): return NaN
        return self
    def __lt__(self, val):
        if isinstance(val, self.__class__): return False
        return True
    def __le__(self, val):
        if isinstance(val, self.__class__): return False
        return True
    
class _NaN(_Special):
    """Classe  représentant l'indetermination (le résultat de la division 0/0).
"""
    def __str__(self): return "NaN"
    def __rsub__(self, val): return self
    def __gt__(self, val): return False
    def __ge__(self, val): return False
    def __neg__(self): return self
    
INF = infinity = float('inf')
NEGINF = neginfinity = float('-inf')
NAN = nan = NaN = float('nan')

def dotex(*argv):
    # extension de la fonction numpy.dot a un nb qcq de matrices
    res = None
    for val in argv:
        if res is None:
            res = val
        else:
            res = np.dot(res, val)
    return res

def leverage(vec, mat):
    # compute zT M z
    return dotex(vec.T, mat, vec) 

def getCorrelMatrix(source, eye=1):
    # source est une matrice carrée symetrique
    """Creation de la matrice de correlation entre les paramètres à partir de la matrice de dispersion.
    La diagonale est mise à la valeur "eye"(1 par défaut).
    """ 
    N = source.shape[0]
    target = np.zeros((N,N))
    diag = np.diag(source)
    for i in range(N):
        target[i, i] = eye
        for j in range(i):
            target[i, j] = target[j, i] = source[i, j]/ sqrt(diag[i]*diag[j])
    return target

def getCorrelFromDispersion(dispersion):
    q, q2 = dispersion.shape
    assert q == q2
    correl =  np.zeros((q, q))
    diag = np.diag(dispersion)

    for i in range(q):
        for j in range(i):
            coeffa = diag[i]*diag[j]
            try:
                coeff = sqrt(coeffa)
            except ValueError:
                coeff = sqrt(-coeffa)
            correl[i, j] = correl[j, i] = dispersion[i, j]/ coeff
    return correl
    
# def getSVDChildrenOld(jacob):
#     """Calcul et exploitation de la decomposition SVD d'une matrice Jacobienne.
#     Retour :
#         matrice de dispersion 1/(ZtZ)
#         vecteur des leviers
#         matrice de correlation avec la diagonale à 0
#         determinant de la matrice de dispersion
#         vecteur des valeurs propres de la matrice de dispersion
#     """
#     N, q = jacob.shape
#     U, s, V = svd(jacob, full_matrices=False)
#     eigs = s**-2
#     dispersionMatrix = dot(dot(V.T, npdiag(eigs)), V)
#     leverages = zeros((N,))
#     correlMat = getCorrelFromDispersion(dispersionMatrix)
#     for i, Ui in enumerate(U):
#         Ui2 = Ui**2
#         Ui2.sort()
#         leverages[i] = sum(Ui2)
#     determinant = prod(s)
#     return dispersionMatrix, leverages, correlMat, determinant, eigs

def getLeveragesFromSVD(jacob):
    N, q = jacob.shape
    try:
        U, s, V = svd(jacob, False)
    except Exception:
        raise
    projectionMat = np.dot(U, U.T)
    return np.diag(projectionMat)

def getSVDChildren(jacob, style=0,  method=LEV_EARLY):
    """Calcul et exploitation de la decomposition SVD d'une matrice Jacobienne.
    Retour :
        matrice de demidispersion 
        vecteur des leviers
        matrice de correlation avec la diagonale à 0
        determinant de la matrice de dispersion
        vecteur des valeurs propres de la matrice de dispersion
    """
    N, q = jacob.shape
    try:
        U, s, V = svd(jacob, False)
    except Exception:
        raise
    eigs = np.zeros((q,))
    #s**-2
    determinant = 1
    rank = q  
    #VV = V.copy()
    for i in range(q):
        if fabs(s[i]) > 1E-10:
            V[i] /= s[i]
            determinant *= s[i]
            eigs[i] = s[i]**2
        else:
            V[i] *= 0.0
            rank -= 1
            eigs[i] = NaN
    halfdispersion = V.T
    if style == 1:
        return halfdispersion
    dispersionMatrix = V.T.dot(V)
    correlMat = np.zeros(dispersionMatrix.shape)
    diag = np.diag(dispersionMatrix)
    for i in range(q):
        correlMat[i, i] = 0
        for j in range(i):
            correlMat[i, j] = correlMat[j, i] = dispersionMatrix[i, j]/ sqrt(diag[i]*diag[j])
    if method == LEV_EARLY:
        levs = np.asarray([sum(ui**2) for ui in U])
    elif method == LEV_MONARI:
        mat = jacob.dot(halfdispersion)
        levs = np.asarray([vec.dot(vec.T) for vec in mat])
    else:
        dispersion = dispersionMatrix  #dot(halfdispersion, halfdispersion.T)
        levs = np.asarray([vec.T.dot(dispersion.dot(vec)) for vec in jacob])
    if method in [LEV_EARLY]:  #, LEV_MONARI
        #dispersion = dispersionMatrix
        #levUs = asarray([vec.T.dot(dispersion.dot(vec)) for vec in jacob])
        mat = jacob.dot(halfdispersion)
        levUs = np.asarray([vec.dot(vec.T) for vec in mat])
    else:
        levUs = levs
    return halfdispersion, levs, levUs, correlMat, determinant, eigs, rank

def s_leverage2(grad, VW): 
    """Calcul du levier par la méthode détournée proposée par Gaétan Monari.
    W et V viennent du SVD du jacobien.
    W est le vecteur des valeurs singulières, par ordre decroissant
    V est la troisième matrice fournie par svd.
    """
    P, Q = VW.shape
    if grad.shape[0] != P:
        raise ValueError("matrices are not aligned")
    lst = []
    for k in range(P):
        lstk = (grdi*vec[k] for grdi, vec in zip(grad, VW))
        val = fsum(lstk)
        lst.append(val*val)
    return fsum(lst)
        
def s_leverage(grad, VW): 
    """Calcul du levier par la méthode détournée proposée par Gaétan Monari.
    W et V viennent du SVD du jacobien.
    W est le vecteur des valeurs singulières, par ordre decroissant
    V est la troisième matrice fournie par svd.
    """
    if grad.shape[0] != VW.shape[0]:
        raise ValueError("matrices are not aligned")
    lst = []
    for vec in VW:
        val = fsum(veci*gradi for veci, gradi in zip(vec, grad))
        lst.append(sqr(val))
#<<<<<<< .mine
    return fsum(lst)
    #return fsum(sqr(dot(vec, grad)) for vec in VW)
# =======
#     return math.fsum(lst)
#     #return math.fsum(sqr(dot(vec, grad)) for vec in VW)
# >>>>>>> .r4366
    
def leverages(jac):
    N, Q = jac.shape # Nex, Nparam
    U, W, V = svd(jac, False)
    VW = np.asarray([vec/W[ind] for ind, vec in enumerate(V)])
    lst = [s_leverage(grad, VW) for grad in jac]
    return np.asarray(lst)
        
def leverages2(jac):
    N, Q = jac.shape # Nex, Nparam
    U, W, V = svd(jac, False)
    res = np.zeros((N,))
    for k in range(N):
        p = Q-1
        while p>= 0:
            w = W[p]
            res[k] += (jac[k].dot(V[p])/w)**2
            p -= 1
    return res
        
if __name__ == '__main__':
    from pylab import plot, scatter, show
    
    jacalea = 0
    
    import os, sys
    from importlib import import_module
    
    dir = "C:\Projets\GM\EnergieLibreSolv\BaseA138" 
    module = "basea138_iso05n"
    filename = "DsolvG_basea138_iso05n_8.gmx"
    dir = "C:\Projets\GM\DSolvG\BaseA138"
    module = "basea138_iso05n"
    filename = "DsolvG_basea138_iso05n_1.gmx"
    dir = "C:\Projets\GM\LogKd109\Base109"
    module = "base109_chi05n"
    filename = "LogKd_base109_chi05n_17.gmx"
    sys.path.append(dir)
    os.chdir(dir)
    mod = import_module(module)
    
    if jacalea:
        jac = random((138,81))*2-1
    else:
        with np.load(filename, allow_pickle=True) as source:
            pp = source["params"]
        jac = mod.getjacobian(pp)
    
    lev4 = leverages(jac)
    print("lev4", lev4)
    print("sum lev4", sum(lev4))
    
    halfdispersion, projectionMat, correlMat, determinant, eigs, rank = getSVDChildren(jac)
    dispersionMatrix2 = halfdispersion.dot(halfdispersion.T)
    
    #print dispersionMatrix
    #print
    #print dispersionMatrix2
    
    U, s, Vh = svd(jac, False)
# <<<<<<< .mine
    #mat = U.dot(npdiag(s)).dot(Vh)
# =======
#     #mat = U.dot(diag(s)).dot(Vh)
# >>>>>>> .r4366
    #for a, b in zip(jac.flat, mat.flat):
    #    print a, b
    #Q, R = linalg.qr(jac, mode="economic")
    
# <<<<<<< .mine
#     #W2 = npdiag(s**-2)
# =======
#     #W2 = diag(s**-2)
# >>>>>>> .r4366
#     #M = Vh.T.dot(W2).dot(Vh)
    
    for i in range(s.shape[0]):
        Vh[i] /= s[i]
    lev3 = np.asarray([s_leverage(grd, Vh) for grd in jac])
    
    lev0 = np.diag(U.dot(U.T))
    print("Lev_U")
    print(lev0)
    print("sum Lev_U", sum(lev0))
    
    lev1 = np.asarray([s_leverage2(grd, halfdispersion.T) for grd in jac])
    print("Lev_G")
    print(lev1)
    print("sum Lev_G", sum(lev1))
    
    #===========================================================================
# <<<<<<< .mine
#     # lev2 = npdiag(Q.dot(Q.T))
# =======
#     # lev2 = diag(Q.dot(Q.T))
# >>>>>>> .r4366
    # if jacalea:
    #    print "Lev_Q"
    #    print lev2
    #    print "sum Lev_Q", sum(lev2)
    #===========================================================================
    
    #V = Vh.T
    #===========================================================================
    # Q = Vh.shape[0]
    # for i in xrange(Q):
    #   Vh[i] /= s[i]
    # V = Vh.T
    #===========================================================================
    #V = halfdispersion
    #s = scatter(lev3, lev1)
    #show()
    s1 = plot((0,1), (0,1))
    s1 = scatter(lev0, lev1)
    show()
    
    #print R.dot(R.T)
    #===========================================================================
# <<<<<<< .mine
#     # jac2 = random.random((138,81))*2-1
# =======
#     # jac2 = random((138,81))*2-1
# >>>>>>> .r4366
    # print jac2
    # print
    # print
# <<<<<<< .mine
#     # savez("jac2.npy")
# =======
#     # np .savez("jac2.npy")
# >>>>>>> .r4366
    # 
    # U, s, Vh = svd(jac2, False)
    # Q, R = linalg.qr(jac2, mode="economic")
    # 
# <<<<<<< .mine
#     # W2 = npdiag(s**-2)
# =======
#     # W2 = diag(s**-2)
# >>>>>>> .r4366
    # M = Vh.T.dot(W2).dot(Vh)
    # 
# <<<<<<< .mine
#     # lev0 = npdiag(U.dot(U.T))
# =======
#     # lev0 = diag(U.dot(U.T))
# >>>>>>> .r4366
    # print "lev_U"
    # print lev0
    # print "sum lev0", sum(lev0)
    # 
# <<<<<<< .mine
#     # lev2 = npdiag(Q.dot(Q.T))
# =======
#     # lev2 = diag(Q.dot(Q.T))
# >>>>>>> .r4366
    # print "lev_Q"
    # print lev2
    # print "sum lev2", sum(lev2)
    # 
    # #V = Vh.T
    # Q = Vh.shape[0]
    # for i in xrange(Q):
    #    Vh[i] /= s[i]
    # V = Vh.T
    # lev1 = asarray([s_leverage(grd, V, None) for grd in jac2])
    # print "lev_G"
    # print lev1
    # print "sum lev1", sum(lev1)
    #===========================================================================
# <<<<<<< .mine
#     #lev2 = npdiag(jac.dot(M).dot(jac.T))
# =======
#     #lev2 = diag(jac.dot(M).dot(jac.T))
# >>>>>>> .r4366
    #print lev2.shape
    
    #print "lev2"
    #print sum(lev2)
    #print lev2
    print("done")
    