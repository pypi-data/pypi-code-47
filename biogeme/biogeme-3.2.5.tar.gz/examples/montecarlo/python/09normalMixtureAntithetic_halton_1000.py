#######################################
#
# File: 09normalMixtureAntithetic_halton_1000.py
# Author: Michel Bierlaire, EPFL
# Date: Sat Jul 25 19:14:42 2015
#
#######################################

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *

#Parameters 
ASC_CAR = 0.137
ASC_TRAIN = -0.402
ASC_SM = 0
B_TIME = -2.26
B_TIME_S = 1.66
B_COST = -1.29

# Define a random parameter, normally distirbuted, designed to be used
# for Monte-Carlo simulation

B_TIME_RND = B_TIME + B_TIME_S * bioDraws('B_TIME_RND')
B_TIME_RND_MINUS = B_TIME - B_TIME_S * bioDraws('B_TIME_RND')

# Utility functions

#If the person has a GA (season ticket) her incremental cost is actually 0 
#rather than the cost value gathered from the
# network data. 
SM_COST =  SM_CO   * (  GA   ==  0  ) 
TRAIN_COST =  TRAIN_CO   * (  GA   ==  0  )

# For numerical reasons, it is good practice to scale the data to
# that the values of the parameters are around 1.0. 
# A previous estimation with the unscaled data has generated
# parameters around -0.01 for both cost and time. Therefore, time and
# cost are multipled my 0.01.

TRAIN_TT_SCALED = DefineVariable('TRAIN_TT_SCALED', TRAIN_TT / 100.0)
TRAIN_COST_SCALED = DefineVariable('TRAIN_COST_SCALED', TRAIN_COST / 100)
SM_TT_SCALED = DefineVariable('SM_TT_SCALED', SM_TT / 100.0)
SM_COST_SCALED = DefineVariable('SM_COST_SCALED', SM_COST / 100)
CAR_TT_SCALED = DefineVariable('CAR_TT_SCALED', CAR_TT / 100)
CAR_CO_SCALED = DefineVariable('CAR_CO_SCALED', CAR_CO / 100)

V1 = ASC_TRAIN + B_TIME_RND * TRAIN_TT_SCALED + B_COST * TRAIN_COST_SCALED
V2 = ASC_SM + B_TIME_RND * SM_TT_SCALED + B_COST * SM_COST_SCALED
V3 = ASC_CAR + B_TIME_RND * CAR_TT_SCALED + B_COST * CAR_CO_SCALED

V1_MINUS = ASC_TRAIN + B_TIME_RND_MINUS * TRAIN_TT_SCALED + B_COST * TRAIN_COST_SCALED
V2_MINUS = ASC_SM + B_TIME_RND_MINUS * SM_TT_SCALED + B_COST * SM_COST_SCALED
V3_MINUS = ASC_CAR + B_TIME_RND_MINUS * CAR_TT_SCALED + B_COST * CAR_CO_SCALED

# Associate utility functions with the numbering of alternatives
V = {1: V1,
     2: V2,
     3: V3}

V_MINUS = {1: V1_MINUS,
           2: V2_MINUS,
           3: V3_MINUS}

# Associate the availability conditions with the alternatives

CAR_AV_SP =  DefineVariable('CAR_AV_SP',CAR_AV  * (  SP   !=  0  ))
TRAIN_AV_SP =  DefineVariable('TRAIN_AV_SP',TRAIN_AV  * (  SP   !=  0  ))

av = {1: TRAIN_AV_SP,
      2: SM_AV,
      3: CAR_AV_SP}

# The choice model is a logit, with availability conditions
integrand_plus = bioLogit(V,av,CHOICE)
integrand_minus = bioLogit(V_MINUS,av,CHOICE)
integrand = 0.5 * (integrand_plus + integrand_minus)
simulatedI = MonteCarlo(integrand)

trueI = 0.637849835578 

sampleVariance = \
  MonteCarlo(integrand*integrand) - simulatedI * simulatedI
stderr = (sampleVariance / 200000.0)**0.5
error = simulatedI - trueI

simulate = {'01 Simulated Integral': simulatedI,
            '02 Analytical Integral': trueI,
            '03 Sample variance': sampleVariance,
            '04 Std Error': stderr,
            '05 Error': error}

rowIterator('obsIter') 

BIOGEME_OBJECT.SIMULATE = Enumerate(simulate,'obsIter')

__rowId__ = Variable('__rowId__')
BIOGEME_OBJECT.EXCLUDE = __rowId__ >= 1

#For 2000 normals draws, you need 1000 antithetic.
BIOGEME_OBJECT.PARAMETERS['NbrOfDraws'] = "1000"
BIOGEME_OBJECT.PARAMETERS['RandomDistribution'] = "HALTON"
BIOGEME_OBJECT.DRAWS = { 'B_TIME_RND': 'NORMAL' }
