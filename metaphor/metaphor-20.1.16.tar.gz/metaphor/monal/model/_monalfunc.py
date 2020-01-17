# -*- coding: ISO-8859-15 -*-
#===============================================================================
# $Id: _monalfunc.py 4713 2018-01-27 10:40:41Z jeanluc $
#
#  Module  monalfunc.py
#  Projet MonalPy
#
#  Exposition des fonctions utilisées par le moteur neuronal pour les activations 
#    et les calculs de coûts.
#
#  Author: Jean-Luc PLOIX  -  NETRAL
#  Decembre 2009
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

"""Module monalfunc pour Monal Python

   fonctions mathématiques,
   dictionnaires de fonctions
""" 

from numpy import arctan, sqrt, pi, tanh, sin, cos, exp, log, cosh, any
from math import erf, asinh
from ..monalconst import NONE, SQUAREDELTA, SQUARELOGDELTA, LEASTSQUAREDELTA, \
    WEIGHTEDSQUAREDELTA, UNCLASSIFIED, WEIGHTEDCLASSIFICATION, RELATIVESQUAREDELTA, \
    GAUSSSQUAREDELTA, CROSSEDENTROPY, EXPSQUAREDELTA, \
    IDENTITY, UNIT, TANH, STEP, GAUSS, SINE, EXP, QUADRATIC, ATAN, MOMENT0, MOMENT1, \
    REVERSE, LOG, CUBIC, SIGMOID, COMPLEMENT, ROOT, ARCSH, SQR, COS, ERF


# fonctions utiles
sqr = lambda X: X*X
cubic = lambda X: X*X*X
gaussNorm = lambda X: exp(-0.5*X*X)/sqrt(2*pi)
#gaussNorm = lambda X: exp(-0.5*X*X)/sqrt(2*pi)

def erorFunction(X):
    """fonction integrale de la gaussienne normalisee"""
    if X == 0:
        return 0.5
    if X < 0:
        return 1 - erorFunction(-X)
    T = 1/(1 + 0.2316419*X)
    R = ((((1.330274429*T - 1.821255978)*T + 1.781477937)*T - 0.356563782)*T + 
         0.31938153)*T
    return 1 - R*gaussNorm(X)

#===========================================================================
# Functors de cout
#===========================================================================
class basecost(object):
    
    def __init__(self):
        self.clear()
    def clear(self): pass
    def __str__(self): return
    def __repr__(self): return
    def __call__(self, A, B, C=1): return None
    def derive(self, A, B, C=1): return None
    
class nullcost(basecost):
    def __str__(self): return "null"
    def __repr__(self): return "null"
    def __call__(self, A, B, C=1): return 0
    def derive(self, A, B, C=1): return 0

class quadcost(basecost):
    def __str__(self): return "deltasquare"
    def __repr__(self): return "delta square"
    def __call__(self, A, B, C=1): return sqr(A-B)/2
    def derive(self, A, B, C=1): return A-B

class logquadcost(basecost):
    def __str__(self): return "logdeltasquare"
    def __repr__(self): return "logarithm delta square"
    def __call__(self, A, B, C=1): return sqr(log(float(A)/B))/2
    def derive(self, A, B, C=1): return log(float(A) / B)/A

class minquadcost(basecost):
    def __str__(self): return "leastdeltasquare"
    def __repr__(self): return "least delta square"
    def __call__(self, A, B, C=1): return sqrt(1 + sqr(abs((A - B) / C))) - 1
    def derive(self, A, B, C=1): return (A - B) / C/C / sqrt(1 + sqr((A - B)/C))

class weightquadcost(basecost):
    def __str__(self): return "weighteddeltasquare"
    def __repr__(self): return "weighted delta square"
    def __call__(self, A, B, C=1): return sqr(A - B) / 2 / (1 + sqr(B / C))
    def derive(self, A, B, C=1): return (A - B) / (1 + sqr(B / C))

class mispositioncost(basecost):
    def __str__(self): return "misclassified"
    def __repr__(self): return "misclassified"
    def __call__(self, A, B, C=1): return int((A - C) * (B - C) < 0)

class relquadcost(basecost):
    def __str__(self): return "reldeltasquare"
    def __repr__(self): return "relative delta square"
    def __call__(self, A, B, C=1): return sqr(A / B - 1) / 2
    def derive(self, A, B, C=1): return (A / B - 1) / B

class gaussquadcost(basecost):
    def __str__(self): return "gaussdeltasquare"
    def __repr__(self): return "gaussian delta square"
    def __call__(self, A, B, C=1): return sqr(A - B) / 2 * exp(-sqr(B / C))
    def derive(self, A, B, C=1): return (A - B) * exp(-sqr(B / C))

def crossentropycost(basecost):
    def __str__(self): return "crossentropy"
    def __repr__(self): return "cross entropy"
    def __call__(A, B, C=1): return B*(1-A) + A*(1-B)
#        if B == 1: return 1 - A
#        return A - B
    def derive(A, B, C=1): return 1 - 2*B
#        if B == 1: return -1
#        return 1

class expquadcost(basecost):
    def __str__(self): return "expdeltasquare"
    def __repr__(self): return "exponent delta square"
    def __call__(self, A, B, C=1): return 10 * (exp(sqr(A - B) / 2) - 1)
    def derive(self, A, B, C=1): return 10 * (exp(sqr(A - B) / 2) - 1)
    
class lateralcost(basecost):
    def __str__(self): return "weightclassification"
    def __repr__(self): return "weighted classification"
    def __call__(self, A, B, C=1):
        X = A - C
        V = sqrt(1 + sqr(X))
        if B < C: return sqr((V + X) / 2)
        else: return sqr((V - X) / 2)
    def derive(self, A, B, C=1):
        X = A - C;
        V = sqrt(1 + sqr(X))
        if B < C: return sqr((X + V)) / V / 2
        else: return -sqr((X - V)) / V / 2
        
#===========================================================================
# Fin des functors de cout
#===========================================================================
# Les fonctions de coût. 
classCostIndex = {
    NONE: nullcost,                      # 0
    SQUAREDELTA: quadcost,               # 1
    SQUARELOGDELTA: logquadcost,         # 2
    LEASTSQUAREDELTA: minquadcost,       # 3
    WEIGHTEDSQUAREDELTA: weightquadcost, # 4
    UNCLASSIFIED: mispositioncost,       # 5
    WEIGHTEDCLASSIFICATION: lateralcost, # 6
    RELATIVESQUAREDELTA: relquadcost,    # 7
    GAUSSSQUAREDELTA: gaussquadcost,     # 8
    CROSSEDENTROPY: crossentropycost,    # 9
    EXPSQUAREDELTA: expquadcost          # 10
    }

costderivelist = {}

# la clé est le nom du functor, un functor peut apparaitre plusieurs fois.
classCostDict = {
    "": nullcost,
    "Null": nullcost,
    "deltasquare": quadcost,
    "Delta carré": quadcost,
    "logdeltasquare": logquadcost,
    "Delta log carré": logquadcost,
    "lesslogdelta": minquadcost,
    "Delta carré minoré": minquadcost,
    "weighteddeltasquare": weightquadcost,
    "weightlogdelta": weightquadcost,
    "Delta carré pondéré": weightquadcost,
    "mispositionned": mispositioncost,
    "misclassified": mispositioncost,
    "Classement incorrect": mispositioncost,
    "weightposition": lateralcost,
    "weightclassification": lateralcost,
    "Classement pondéré": lateralcost,
    "reldeltasquare": relquadcost,
    "relativedeltaquad": relquadcost,
    "Delta carré relatif": relquadcost,
    "gaussdeltasquare": gaussquadcost,
    "Delta carré gauss": gaussquadcost,
    "crossentropy": crossentropycost,
    "Entropie croisée": crossentropycost,
    "expdeltasquare": expquadcost,
    "exponentdeltasquare": expquadcost,
    "Exponentielle delta carré": expquadcost
    } 

def getCostClass(index):
    try: return classCostDict[index.lower()]
    except: return classCostIndex[index]


#===========================================================================
# Functors d'activation
#===========================================================================
class baseactiv(object):
    index = -1
    def __init__(self):
        self.clear()
    
    def clear(self):
        self._X = None
        self._XD = None
        self._XD2 = None
        self._Y = None
        self._YD = None
        self._YD2 = None
    
    def template(self): return ""
    
    def formula(self, expr):
        try: return self.template()% expr
        except: pass
        try: return self.template()% (expr, expr)
        except: pass
        try: return self.template()% (expr, expr, expr)
        except: pass
        try: return self.template()% (expr, expr, expr, expr)
        except: pass
        return self.self.template()
    
    def __call__(self, value, withDerive=False):
        if withDerive:
            ff = self.func(value)
            if hasattr(self, 'funcDY'):
                fd = self.funcDY(value, ff)
            else:
                fd = self.funcD(value)
            return ff, fd
        try:
            self._X = value[:]
            self._Y = self.func(value)[:]
        except:
            self._X = value
            self._Y = self.func(value)
        return self._Y

#     def funcAndDerive(self, value):
#         ff = self.func(value)
#         if hasattr(self, 'funcDY'):
#             fd = self.funcDY(value, ff)
#         else:
#             fd = self.funcD(value)
#         return ff, fd
    
    def derive(self, value):
        if hasattr(self, 'funcDY') and equal(self._XD, value):
            self._YD = self.funcDY(self._X, self._Y)
        else:
            self._YD = self.funcD(value)
        return self._YD

    def derive2(self, value):
        self._XD2 = value
        if hasattr(self, 'funcD2D') and (self._XD == value):
            self._YD2 = self.funcD2D(self._XD, self._YD)
        elif hasattr(self, 'funcD2Y') and (self._X == value):
            self._YD2 = self.funcD2Y(self._X, self._Y)
        else:
            self._YD2 = self.funcD2(value)           
        return self._YD2

#@singleton
class identityactiv(baseactiv):
    index = 0
    def __str__(self): return "ident"
    def __repr__(self): return "identity"
    def template(self): return "%s"
    def __call__(self, X): return X
    def derive(self, X): return 1.
    def derive2(self, X): return 0.

class oneactiv(baseactiv):
    index = 1
    def __str__(self): return "1"
    def __repr__(self): return "fixed one"
    def template(self): return "1"
    def __call__(self, X): return 1.
    def derive(self, X): return 0.
    def derive2(self, X): return 0.

class stepactiv(baseactiv):
    index = 2
    def __str__(self): return "heaviside"
    def __repr__(self): return "heaviside step"
    def template(self): return "heaviside(%s)"
    def __call__(self, X): 
        if X < 0: return 0.
        return 1.

class tanhactiv(baseactiv):
    index = 3
    def __str__(self): return "tanh"
    def __repr__(self): return "hyperbolic tangent"
    def template(self): return "tanh(%s)"
    def func(self, X): return tanh(X)
    def funcD(self, X): return 1 / sqr(cosh(X))
    def funcDY(self, X, Y): return 1 - Y*Y
    def funcDY2(self, Y): return 1 - Y*Y 
    def funcD2(self, X): return -2*tanh(X)/sqr(cosh(X))
    def funcD2Y(self, X, Y): return -2*Y*(1-Y*Y)

class gaussactiv(baseactiv):
    index = 4
    def __str__(self): return "gauss"
    def __repr__(self): return "gaussian"
    def template(self): return "exp(-%s*%s)"
    def func(self, X): return exp(-X*X)
    def funcD(self, X): return -2*X*exp(-X*X)
    def funcDY(self, X, Y): return -2*X*Y
    def funcD2(self, X): return 2*(2*X*X-1)*exp(-X*X)
    def funcD2Y(self, X, Y): return 2*(2*X*X-1)*Y
        
class sineactiv(baseactiv):
    index = 5
    def __str__(self): return "sin"
    def __repr__(self): return "sine"
    def template(self): return "sin(%s)"
    def func(self, X): return sin(X)
    def funcD(self, X): return cos(X)
    def funcD2(self, X): return -sin(X)
    def funcD2Y(self, X, Y): return -Y
        
class expactiv(baseactiv):
    index = 6
    def __str__(self): return "exp"
    def __repr__(self): return "exponential"
    def template(self): return "exp(%s)"
    def func(self, X): return exp(X)
    def funcD(self, X): return exp(X)
    def funcDY(self, X, Y): return Y
    def funcD2(self, X): return exp(X)
    def funcD2Y(self, X, Y): return Y
    def funcD2D(self, X, YD): return YD
        
class quadraticactiv(baseactiv):
    index = 7
    def __str__(self): return "quadratic"
    def __repr__(self): return "half square"
    def template(self): return "%s*%s/2"
    def func(self, X): return X*X/2
    def derive(self, X): return X
    def derive2(self, X): return 1
        
class atanactiv(baseactiv):
    index = 8
    def __str__(self): return "atan"
    def __repr__(self): return "argument tangent"
    def template(self): return "atan(%s)"
    def func(self, X): return arctan(X)
    def funcD(self, X): return 1/(1 + X*X)
    def funcD2(self, X): return -2*X/sqr(1 + X*X)

class moment0activ(baseactiv):
    index = 9
    def __str__(self): return "m0"
    def __repr__(self): return "order 0 moment"
    def template(self): return "(1 - %s*%s)/(1 + %s*%s)"   
    def func(self, X):
        Z = sqr(X)
        return (1 - Z)/(1 + Z)
    def funcD(self, X): return -4*X/sqr(1 + sqr(X))
    def funcD2(self, X): return -4*(1 - 3*sqr(X))/cubic(1 + sqr(X))

class moment1activ(baseactiv):
    index = 10
    def __str__(self): return "m1"
    def __repr__(self): return "order 1 moment"
    def template(self): return "%s/(1 + %s*%s)"
    def func(self, X): return X/(1 + X*X)
    def funcD(self, X): return (1-sqr(X))/sqr(1 + sqr(X))
    def funcD2(self, X): return 2*X*(-3 + X*X)/cubic(1 + X*X)

class reverseactiv(baseactiv):
    index = 11
    def __str__(self): return "reverse"
    def __repr__(self): return "reverse"
    def template(self): return "1/%s"
    def func(self, X): return 1/X
    def funcD(self, X): return -1/(X*X)
    def funcDY(self, X, Y): return -Y*Y
    def funcD2(self, X): return 2/(X*X*X)
    def funcD2Y(self, X, Y): return 2*cubic(Y)

class lognactiv(baseactiv):
    index = 12
    def __str__(self): return "log"
    def __repr__(self): return "neperian logarithm"
    def template(self): return "log(%s)"
    def func(self, X): return log(X)
    def funcD(self, X): return 1/X
    def funcD2(self, X): return -1/(X*X)

class cubicactiv(baseactiv):
    index = 13
    def __str__(self): return "cubic"
    def __repr__(self): return "cubic"
    def template(self): return "%s*%s*%s"
    def func(self, X): return X*X*X
    def funcD(self, X): return 3*X*X
    def funcD2(self, X): return 6*X

class sigmoidactiv(baseactiv):
    index = 14
    def __str__(self): return "sig"
    def __repr__(self): return "sigmoid"
    def template(self): return "0.5*(1 + tanh(%s))"
    def func(self, X): return 0.5*(1 + tanh(X))
    def funcD(self, X): return 1 / (2*sqr(cosh(X)))
    def funcDY(self, X, Y): return 2*Y*(1-Y)
    def funcD2(self, X): return -tanh(X)/sqr(cosh(X))

class complement1activ(baseactiv):
    index = 15
    def __str__(self): return "complement"
    def __repr__(self): return "complement to 1"
    def template(self): return "1 - %s"
    def __call__(self, X): return 1-X
    def derive(self, X): return -1
    def derive2(self, X): return 0

class rootactiv(baseactiv):
    index = 16
    def __str__(self): return "sqrt"
    def __repr__(self): return "square root"
    def template(self): return "sqrt(%s)"
    def func(self, X): return sqrt(X)
    def funcD(self, X): return 1/(2*sqrt(X))
    def funcDY(self, X, Y): return 1/(2*Y)
    def funcD2(self, X): return -0.25/cubic(sqrt(X))
    def funcD2Y(self, X, Y): return -0.25/cubic(Y)

class arcsinhactiv(baseactiv):
    index = 17
    def __str__(self): return "asinh"
    def __repr__(self): return "hyperbolic sine argument"
    def template(self): return "asinh(%s)"
    def func(self, X): return asinh(X) 
    def funcD(self, X): return 1/sqrt(1 + sqr(X))
    def funcD2(self, X): return -X/sqrt(cubic(1 + sqr(X)))

class sqractiv(baseactiv):
    index = 18
    def __str__(self): return "sqr"
    def __repr__(self): return "square"
    def template(self): return "%s*%s"
    def func(self, X): return X*X
    def funcD(self, X): return 2*X
    def derive2(self, X): return 2
    
class cosactiv(baseactiv):
    index = 19
    def __str__(self): return "cos"
    def __repr__(self): return "cosine"
    def template(self): return "cos(%s)"
    def func(self, X): return cos(X)
    def funcD(self, X): return -sin(X)
    def funcD2(self, X): return -cos(X)
    def funcD2Y(self, X, Y): return -Y

class erfactiv(baseactiv):
    index = 20
    def __str__(self): return "erf"
    def __repr__(self): return "error activ"
    def formula(self): return "erf(%s)"
    def func(self, X): return 0.5 + 0.5*erf(X)  #erorFunction(X)
    def funcD(self, X): return gaussNorm(X)
    def funcD2(self, X): return -X*gaussNorm(X) 
    def funcD2D(self, X, YD): return -X*YD

#===========================================================================
# Fin des functors d'activation
#===========================================================================
classActivIndex = {
    IDENTITY: identityactiv,        # 0
    UNIT: oneactiv,                 # 1
    TANH: tanhactiv,                # 2
    STEP: stepactiv,                # 3
    GAUSS: gaussactiv,              # 4
    SINE: sineactiv,                # 5
    EXP: expactiv,                  # 6
    QUADRATIC: quadraticactiv,      # 7
    ATAN: atanactiv,                # 8
    MOMENT0: moment0activ,          # 9
    MOMENT1: moment1activ,          # 10
    REVERSE: reverseactiv,          # 11
    LOG: lognactiv,                 # 12
    CUBIC: cubicactiv,              # 13
 #   QUASIABS: ,                     # 14
    SIGMOID: sigmoidactiv,          # 15
    COMPLEMENT: complement1activ,  # 16
    ROOT: rootactiv,                # 17
    ARCSH: arcsinhactiv,            # 18
    SQR: sqractiv,                  # 19
    COS: cosactiv,                  # 20
    ERF: erfactiv                    # 21
}

classActivDict = {
    "": identityactiv,
    "ident": identityactiv,
    "identity": identityactiv,
    "unit": oneactiv,
    "tanh": tanhactiv,
    "gauss": gaussactiv,
    "sin": sineactiv,
    "sine": sineactiv,
    "exp": expactiv,
    "exponent": expactiv,
    "halfsquare": quadraticactiv,
    "quadratic": quadraticactiv,
    "atan": atanactiv,
    "arctan": atanactiv,
    "m0": moment0activ,
    "m1": moment1activ,
    "inv": reverseactiv,
    "inverse": reverseactiv,
    "reverse": reverseactiv,
    "ln": lognactiv,
    "cube6": cubicactiv,
    "sig": sigmoidactiv,
    "sigmoid": sigmoidactiv,
    "comp1": complement1activ,
    "sqrt": rootactiv,
    "arcsh": arcsinhactiv,
    "arcsinh": arcsinhactiv,
    "asinh": arcsinhactiv,
    "erf": erfactiv,
    "errorfct": erfactiv,
    "sqr": sqractiv,
    "cos": cosactiv,
    "cosine": cosactiv}

def getActivClass(index):
    try: return classActivDict[index.lower()]
    except: return classActivIndex[index]
    
def getIndexFromActivClass(aclass):
    if isinstance(aclass, str):
        aclass = classActivDict[aclass]
    for item in list(classActivIndex.items()):
        if item[1] == aclass:
            return item[0]
    return None

def deriveDF(func, X, delta):
    return (func(X+delta/2)-func(X-delta/2))/delta

def derive2DF(func, X, delta):
    return (func(X+delta) + func(X-delta) - 2*func(X))/(delta*delta)

if __name__ == "__main__":
    import unittest
    class TestFunctions(unittest.TestCase):
        
        def __init__(self, *args, **kwargs):
            super(TestFunctions, self).__init__(*args, **kwargs)
            
        def testErf(self):
            F = erfactiv()
            X = 10.0
            self.assertAlmostEqual(erorFunction(X), F(X), 8)
            X = 0.1
            self.assertAlmostEqual(erorFunction(X), F(X), 3)
    
            
    unittest.main()
    
def equal(X, Y):
    try:
        temp = X - Y
        return not any(temp)
    except:
        return X == Y
        