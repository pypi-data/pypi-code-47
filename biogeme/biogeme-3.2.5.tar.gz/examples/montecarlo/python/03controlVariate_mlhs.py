#######################################
#
# File: 03controlVariate_mlhs.py
# Author: Michel Bierlaire, EPFL
# Date: Sat Jul 25 12:24:25 2015
#
#######################################
#

from biogeme import *
from headers import *

integrand = exp(bioDraws('U'))
simulatedI = MonteCarloControlVariate(integrand,bioDraws('U'),0.5)

trueI = exp(1.0) - 1.0 

error = simulatedI - trueI

simulate = {'01_Simulated Integral': simulatedI,
            '02_Analytical Integral': trueI,
            '05_Error': error}


rowIterator('obsIter') 

BIOGEME_OBJECT.SIMULATE = Enumerate(simulate,'obsIter')

BIOGEME_OBJECT.PARAMETERS['NbrOfDraws'] = "20000"
BIOGEME_OBJECT.PARAMETERS['RandomDistribution'] = "MLHS"
__rowId__ = Variable('__rowId__')
BIOGEME_OBJECT.EXCLUDE = __rowId__ >= 1
BIOGEME_OBJECT.DRAWS = { 'U': 'UNIFORM'}
