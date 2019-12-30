#######################################
#
# File: 02antithetic_halton.py
# Author: Michel Bierlaire, EPFL
# Date: Sat Jul 25 12:21:10 2015
#
#######################################
#

from biogeme import *
from headers import *

integrand = 0.5 * (exp(bioDraws('U')) + exp(1.0-bioDraws('U')))
simulatedI = MonteCarlo(integrand)

trueI = exp(1.0) - 1.0 

sampleVariance = \
  MonteCarlo(integrand*integrand) - simulatedI * simulatedI
stderr = (sampleVariance / 10000.0)**0.5
error = simulatedI - trueI

simulate = {'01_Simulated Integral': simulatedI,
            '02_Analytical Integral': trueI,
            '03_Sample variance': sampleVariance,
            '04_Std Error': stderr,
            '05_Error': error}

rowIterator('obsIter') 

BIOGEME_OBJECT.SIMULATE = Enumerate(simulate,'obsIter')

BIOGEME_OBJECT.PARAMETERS['NbrOfDraws'] = "10000"
BIOGEME_OBJECT.PARAMETERS['RandomDistribution'] = "HALTON"
__rowId__ = Variable('__rowId__')
BIOGEME_OBJECT.EXCLUDE = __rowId__ >= 1
BIOGEME_OBJECT.DRAWS = { 'U': 'UNIFORM'}
