"""File 01oneLatentRegression.py

Measurement equation where the indicators are assumed continuous.
Linear regression.

:author: Michel Bierlaire, EPFL
:date: Mon Sep  9 16:30:04 2019

"""
import pandas as pd
import numpy as np
import biogeme.database as db
import biogeme.biogeme as bio
from biogeme.models import piecewise
import biogeme.loglikelihood as ll
import biogeme.optimization as opt
from biogeme.expressions import Beta, DefineVariable, log, Elem, bioMultSum

# Read the data
df = pd.read_csv("optima.dat",sep='\t')
database = db.Database("optima",df)

# The following statement allows you to use the names of the variable
# as Python variable.
globals().update(database.variables)

# Exclude observations such that the chosen alternative is -1
exclude = (Choice == -1)
database.remove(exclude)

# Piecewise linear definition of income
ScaledIncome = DefineVariable('ScaledIncome',\
                              CalculatedIncome / 1000,database)

thresholds = [4,6,8,10]
ContIncome = piecewise(ScaledIncome,thresholds)
ContIncome_0_4000 = ContIncome[0]
ContIncome_4000_6000 = ContIncome[1]
ContIncome_6000_8000 = ContIncome[2]
ContIncome_8000_10000 = ContIncome[3]
ContIncome_10000_more = ContIncome[4]

# Definition of other variables
age_65_more = DefineVariable('age_65_more',age >= Numeric(65),database)
moreThanOneCar = DefineVariable('moreThanOneCar',NbCar > 1,database)
moreThanOneBike = DefineVariable('moreThanOneBike',NbBicy > 1,database)
individualHouse = DefineVariable('individualHouse',\
                                 HouseType == 1,database)
male = DefineVariable('male',Gender == 1,database)
haveChildren = DefineVariable('haveChildren',\
                              ((FamilSitu == 3)+(FamilSitu == 4)) > 0,database)
haveGA = DefineVariable('haveGA',GenAbST == 1,database)
highEducation = DefineVariable('highEducation', Education >= 6,database)

# Parameters to be estimated
coef_intercept = Beta('coef_intercept',0.0,None,None,0)
coef_age_65_more = Beta('coef_age_65_more',0.0,None,None,0)
coef_age_unknown = Beta('coef_age_unknown',0.0,None,None,0)
coef_haveGA = Beta('coef_haveGA',0.0,None,None,0)
coef_ContIncome_0_4000 = \
 Beta('coef_ContIncome_0_4000',0.0,None,None,0)
coef_ContIncome_4000_6000 = \
 Beta('coef_ContIncome_4000_6000',0.0,None,None,0)
coef_ContIncome_6000_8000 = \
 Beta('coef_ContIncome_6000_8000',0.0,None,None,0)
coef_ContIncome_8000_10000 = \
 Beta('coef_ContIncome_8000_10000',0.0,None,None,0)
coef_ContIncome_10000_more = \
 Beta('coef_ContIncome_10000_more',0.0,None,None,0)
coef_moreThanOneCar = \
 Beta('coef_moreThanOneCar',0.0,None,None,0)
coef_moreThanOneBike = \
 Beta('coef_moreThanOneBike',0.0,None,None,0)
coef_individualHouse = \
 Beta('coef_individualHouse',0.0,None,None,0)
coef_male = Beta('coef_male',0.0,None,None,0)
coef_haveChildren = Beta('coef_haveChildren',0.0,None,None,0)
coef_highEducation = Beta('coef_highEducation',0.0,None,None,0)

### Latent variable: structural equation

# Note that the expression must be on a single line. In order to 
# write it across several lines, each line must terminate with 
# the \ symbol

CARLOVERS = \
            coef_intercept +\
            coef_age_65_more * age_65_more +\
            coef_ContIncome_0_4000 * ContIncome_0_4000 +\
            coef_ContIncome_4000_6000 * ContIncome_4000_6000 +\
            coef_ContIncome_6000_8000 * ContIncome_6000_8000 +\
            coef_ContIncome_8000_10000 * ContIncome_8000_10000 +\
            coef_ContIncome_10000_more * ContIncome_10000_more +\
            coef_moreThanOneCar * moreThanOneCar +\
            coef_moreThanOneBike * moreThanOneBike +\
            coef_individualHouse * individualHouse +\
            coef_male * male +\
            coef_haveChildren * haveChildren +\
            coef_haveGA * haveGA +\
            coef_highEducation * highEducation

sigma_s = Beta('sigma_s',1,None,None,1)

### Measurement equations
INTER_Envir01 = Beta('INTER_Envir01',0,None,None,1)
INTER_Envir02 = Beta('INTER_Envir02',0,None,None,0)
INTER_Envir03 = Beta('INTER_Envir03',0,None,None,0)
INTER_Mobil11 = Beta('INTER_Mobil11',0,None,None,0)
INTER_Mobil14 = Beta('INTER_Mobil14',0,None,None,0)
INTER_Mobil16 = Beta('INTER_Mobil16',0,None,None,0)
INTER_Mobil17 = Beta('INTER_Mobil17',0,None,None,0)

B_Envir01_F1 = Beta('B_Envir01_F1',-1,None,None,1)
B_Envir02_F1 = Beta('B_Envir02_F1',-1,None,None,0)
B_Envir03_F1 = Beta('B_Envir03_F1',1,None,None,0)
B_Mobil11_F1 = Beta('B_Mobil11_F1',1,None,None,0)
B_Mobil14_F1 = Beta('B_Mobil14_F1',1,None,None,0)
B_Mobil16_F1 = Beta('B_Mobil16_F1',1,None,None,0)
B_Mobil17_F1 = Beta('B_Mobil17_F1',1,None,None,0)

MODEL_Envir01 = INTER_Envir01 + B_Envir01_F1 * CARLOVERS
MODEL_Envir02 = INTER_Envir02 + B_Envir02_F1 * CARLOVERS
MODEL_Envir03 = INTER_Envir03 + B_Envir03_F1 * CARLOVERS
MODEL_Mobil11 = INTER_Mobil11 + B_Mobil11_F1 * CARLOVERS
MODEL_Mobil14 = INTER_Mobil14 + B_Mobil14_F1 * CARLOVERS
MODEL_Mobil16 = INTER_Mobil16 + B_Mobil16_F1 * CARLOVERS
MODEL_Mobil17 = INTER_Mobil17 + B_Mobil17_F1 * CARLOVERS

# We force the SIGMA to be positive by taking the exp.
SIGMA_STAR_Envir01 = exp(Beta('SIGMA_STAR_Envir01',1,None,None,0))
SIGMA_STAR_Envir02 = exp(Beta('SIGMA_STAR_Envir02',1,None,None,0))
SIGMA_STAR_Envir03 = exp(Beta('SIGMA_STAR_Envir03',1,None,None,0))
SIGMA_STAR_Mobil11 = exp(Beta('SIGMA_STAR_Mobil11',1,None,None,0))
SIGMA_STAR_Mobil14 = exp(Beta('SIGMA_STAR_Mobil14',1,None,None,0))
SIGMA_STAR_Mobil16 = exp(Beta('SIGMA_STAR_Mobil16',1,None,None,0))
SIGMA_STAR_Mobil17 = exp(Beta('SIGMA_STAR_Mobil17',1,None,None,0))

# We build a dict with each contribution to the loglikelihood if (var
# > 0) and (var < 6). If not, 0 is returned.
F = {}
F['Envir01'] = Elem({0:0, \
 1:ll.loglikelihoodregression(Envir01,MODEL_Envir01,SIGMA_STAR_Envir01)},\
  (Envir01 > 0)*(Envir01 < 6))
F['Envir02'] = Elem({0:0, \
 1:ll.loglikelihoodregression(Envir02,MODEL_Envir02,SIGMA_STAR_Envir02)},\
  (Envir02 > 0)*(Envir02 < 6))
F['Envir03'] = Elem({0:0, \
 1:ll.loglikelihoodregression(Envir03,MODEL_Envir03,SIGMA_STAR_Envir03)},\
  (Envir03 > 0)*(Envir03 < 6))
F['Mobil11'] = Elem({0:0, \
 1:ll.loglikelihoodregression(Mobil11,MODEL_Mobil11,SIGMA_STAR_Mobil11)},\
  (Mobil11 > 0)*(Mobil11 < 6))
F['Mobil14'] = Elem({0:0, \
 1:ll.loglikelihoodregression(Mobil14,MODEL_Mobil14,SIGMA_STAR_Mobil14)},\
  (Mobil14 > 0)*(Mobil14 < 6))
F['Mobil16'] = Elem({0:0, \
 1:ll.loglikelihoodregression(Mobil16,MODEL_Mobil16,SIGMA_STAR_Mobil16)},\
  (Mobil16 > 0)*(Mobil16 < 6))
F['Mobil17'] = Elem({0:0, \
 1:ll.loglikelihoodregression(Mobil17,MODEL_Mobil17,SIGMA_STAR_Mobil17)},\
  (Mobil17 > 0)*(Mobil17 < 6))

# The log likelihood is the sum of the elements of the above dict
loglike = bioMultSum(F)

# Define level of verbosity
import biogeme.messaging as msg
logger = msg.bioMessage()
#logger.setSilent()
#logger.setWarning()
logger.setGeneral()
#logger.setDetailed()

# Create the Biogeme object
biogeme  = bio.BIOGEME(database,loglike)
biogeme.modelName = "01oneLatentRegression"

# Estimate the parameters
results = biogeme.estimate(algorithm=opt.newtonTrustRegionForBiogeme)

print(f"Estimated betas: {len(results.data.betaValues)}")
print(f"final log likelihood: {results.data.logLike:.3f}")
print(f"Output file: {results.data.htmlFileName}")
results.writeLaTeX()
print(f"LaTeX file: {results.data.latexFileName}")


