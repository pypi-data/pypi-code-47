"""File 06serialCorrelation.py

Choice model with the latent variable.
Mixture of logit, with agent effect to deal with serial correlation.
Measurement equation for the indicators.
Maximum likelihood (full information) estimation.

:author: Michel Bierlaire, EPFL
:date: Wed Sep 11 08:27:18 2019

"""
import pandas as pd
import numpy as np
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
import biogeme.distributions as dist
import biogeme.results as res
from biogeme.expressions import Beta, DefineVariable, bioDraws, MonteCarlo, Elem, bioNormalCdf

# Read the data
df = pd.read_csv("optima.dat",sep='\t')
database = db.Database("optima",df)

# The following statement allows you to use the names of the variable
# as Python variable.
globals().update(database.variables)

# Exclude observations such that the chosen alternative is -1
exclude = (Choice == -1.0)
database.remove(exclude)

### Variables

ScaledIncome = DefineVariable('ScaledIncome',\
                              CalculatedIncome / 1000,database)
thresholds = [4,6,8,10]
ContIncome = models.piecewise(ScaledIncome,thresholds)
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

### Coefficients
# Read the estimates from the previous estimation, and use
# them as starting values
results = res.bioResults(pickleFile='05latentChoiceFull.pickle')
betas = results.getBetaValues()
coef_intercept = Beta('coef_intercept',betas['coef_intercept'],None,None,0 )
coef_age_65_more = Beta('coef_age_65_more',betas['coef_age_65_more'],None,None,0 )
coef_haveGA = Beta('coef_haveGA',betas['coef_haveGA'],None,None,0)
coef_ContIncome_0_4000 = Beta('coef_ContIncome_0_4000',betas['coef_ContIncome_0_4000'],None,None,0 )
coef_ContIncome_4000_6000 = Beta('coef_ContIncome_4000_6000',betas['coef_ContIncome_4000_6000'],None,None,0 )
coef_ContIncome_6000_8000 = Beta('coef_ContIncome_6000_8000',betas['coef_ContIncome_6000_8000'],None,None,0 )
coef_ContIncome_8000_10000 = Beta('coef_ContIncome_8000_10000',betas['coef_ContIncome_8000_10000'],None,None,0 )
coef_ContIncome_10000_more = Beta('coef_ContIncome_10000_more',betas['coef_ContIncome_10000_more'],None,None,0 )
coef_moreThanOneCar = Beta('coef_moreThanOneCar',betas['coef_moreThanOneCar'],None,None,0 )
coef_moreThanOneBike = Beta('coef_moreThanOneBike',betas['coef_moreThanOneBike'],None,None,0 )
coef_individualHouse = Beta('coef_individualHouse',betas['coef_individualHouse'],None,None,0 )
coef_male = Beta('coef_male',betas['coef_male'],None,None,0 )
coef_haveChildren = Beta('coef_haveChildren',betas['coef_haveChildren'],None,None,0 )
coef_highEducation = Beta('coef_highEducation',betas['coef_highEducation'],None,None,0 )

### Latent variable: structural equation

# Note that the expression must be on a single line. In order to 
# write it across several lines, each line must terminate with 
# the \ symbol

# Define a random parameter, normally distributed, designed to be used
# for Monte-Carlo integration
omega = bioDraws('omega','NORMAL')
sigma_s = Beta('sigma_s',betas['sigma_s'],None,None,0 )

#
# Deal with serial correlation by including an error component that is individual specific
#
errorComponent = bioDraws('errorComponent','NORMAL')
ec_sigma = Beta('ec_sigma',1,None,None,0)

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
            coef_highEducation * highEducation +\
            sigma_s * omega+\
            ec_sigma * errorComponent

### Measurement equations

INTER_Envir01 = Beta('INTER_Envir01',0,None,None,1)
INTER_Envir02 = Beta('INTER_Envir02',betas['INTER_Envir02'],None,None,0 )
INTER_Envir03 = Beta('INTER_Envir03',betas['INTER_Envir03'],None,None,0 )
INTER_Mobil11 = Beta('INTER_Mobil11',betas['INTER_Mobil11'],None,None,0 )
INTER_Mobil14 = Beta('INTER_Mobil14',betas['INTER_Mobil14'],None,None,0 )
INTER_Mobil16 = Beta('INTER_Mobil16',betas['INTER_Mobil16'],None,None,0 )
INTER_Mobil17 = Beta('INTER_Mobil17',betas['INTER_Mobil17'],None,None,0 )

B_Envir01_F1 = Beta('B_Envir01_F1',-1,None,None,1)
B_Envir02_F1 = Beta('B_Envir02_F1',betas['B_Envir02_F1'],None,None,0 )
B_Envir03_F1 = Beta('B_Envir03_F1',betas['B_Envir03_F1'],None,None,0 )
B_Mobil11_F1 = Beta('B_Mobil11_F1',betas['B_Mobil11_F1'],None,None,0 )
B_Mobil14_F1 = Beta('B_Mobil14_F1',betas['B_Mobil14_F1'],None,None,0 )
B_Mobil16_F1 = Beta('B_Mobil16_F1',betas['B_Mobil16_F1'],None,None,0 )
B_Mobil17_F1 = Beta('B_Mobil17_F1',betas['B_Mobil17_F1'],None,None,0 )

MODEL_Envir01 = INTER_Envir01 + B_Envir01_F1 * CARLOVERS
MODEL_Envir02 = INTER_Envir02 + B_Envir02_F1 * CARLOVERS
MODEL_Envir03 = INTER_Envir03 + B_Envir03_F1 * CARLOVERS
MODEL_Mobil11 = INTER_Mobil11 + B_Mobil11_F1 * CARLOVERS
MODEL_Mobil14 = INTER_Mobil14 + B_Mobil14_F1 * CARLOVERS
MODEL_Mobil16 = INTER_Mobil16 + B_Mobil16_F1 * CARLOVERS
MODEL_Mobil17 = INTER_Mobil17 + B_Mobil17_F1 * CARLOVERS

SIGMA_STAR_Envir01 = Beta('SIGMA_STAR_Envir01',1,None,None,1 )
SIGMA_STAR_Envir02 = Beta('SIGMA_STAR_Envir02',betas['SIGMA_STAR_Envir02'],None,None,0 )
SIGMA_STAR_Envir03 = Beta('SIGMA_STAR_Envir03',betas['SIGMA_STAR_Envir03'],None,None,0 )
SIGMA_STAR_Mobil11 = Beta('SIGMA_STAR_Mobil11',betas['SIGMA_STAR_Mobil11'],None,None,0 )
SIGMA_STAR_Mobil14 = Beta('SIGMA_STAR_Mobil14',betas['SIGMA_STAR_Mobil14'],None,None,0 )
SIGMA_STAR_Mobil16 = Beta('SIGMA_STAR_Mobil16',betas['SIGMA_STAR_Mobil16'],None,None,0 )
SIGMA_STAR_Mobil17 = Beta('SIGMA_STAR_Mobil17',betas['SIGMA_STAR_Mobil17'],None,None,0 )

delta_1 = Beta('delta_1',betas['delta_1'],0,10,0 )
delta_2 = Beta('delta_2',betas['delta_2'],0,10,0 )
tau_1 = -delta_1 - delta_2
tau_2 = -delta_1 
tau_3 = delta_1
tau_4 = delta_1 + delta_2

Envir01_tau_1 = (tau_1-MODEL_Envir01) / SIGMA_STAR_Envir01
Envir01_tau_2 = (tau_2-MODEL_Envir01) / SIGMA_STAR_Envir01
Envir01_tau_3 = (tau_3-MODEL_Envir01) / SIGMA_STAR_Envir01
Envir01_tau_4 = (tau_4-MODEL_Envir01) / SIGMA_STAR_Envir01
IndEnvir01 = {
    1: bioNormalCdf(Envir01_tau_1),
    2: bioNormalCdf(Envir01_tau_2)-bioNormalCdf(Envir01_tau_1),
    3: bioNormalCdf(Envir01_tau_3)-bioNormalCdf(Envir01_tau_2),
    4: bioNormalCdf(Envir01_tau_4)-bioNormalCdf(Envir01_tau_3),
    5: 1-bioNormalCdf(Envir01_tau_4),
    6: 1.0,
    -1: 1.0,
    -2: 1.0
}

P_Envir01 = Elem(IndEnvir01, Envir01)


Envir02_tau_1 = (tau_1-MODEL_Envir02) / SIGMA_STAR_Envir02
Envir02_tau_2 = (tau_2-MODEL_Envir02) / SIGMA_STAR_Envir02
Envir02_tau_3 = (tau_3-MODEL_Envir02) / SIGMA_STAR_Envir02
Envir02_tau_4 = (tau_4-MODEL_Envir02) / SIGMA_STAR_Envir02
IndEnvir02 = {
    1: bioNormalCdf(Envir02_tau_1),
    2: bioNormalCdf(Envir02_tau_2)-bioNormalCdf(Envir02_tau_1),
    3: bioNormalCdf(Envir02_tau_3)-bioNormalCdf(Envir02_tau_2),
    4: bioNormalCdf(Envir02_tau_4)-bioNormalCdf(Envir02_tau_3),
    5: 1-bioNormalCdf(Envir02_tau_4),
    6: 1.0,
    -1: 1.0,
    -2: 1.0
}

P_Envir02 = Elem(IndEnvir02, Envir02)

Envir03_tau_1 = (tau_1-MODEL_Envir03) / SIGMA_STAR_Envir03
Envir03_tau_2 = (tau_2-MODEL_Envir03) / SIGMA_STAR_Envir03
Envir03_tau_3 = (tau_3-MODEL_Envir03) / SIGMA_STAR_Envir03
Envir03_tau_4 = (tau_4-MODEL_Envir03) / SIGMA_STAR_Envir03
IndEnvir03 = {
    1: bioNormalCdf(Envir03_tau_1),
    2: bioNormalCdf(Envir03_tau_2)-bioNormalCdf(Envir03_tau_1),
    3: bioNormalCdf(Envir03_tau_3)-bioNormalCdf(Envir03_tau_2),
    4: bioNormalCdf(Envir03_tau_4)-bioNormalCdf(Envir03_tau_3),
    5: 1-bioNormalCdf(Envir03_tau_4),
    6: 1.0,
    -1: 1.0,
    -2: 1.0
}

P_Envir03 = Elem(IndEnvir03, Envir03)

Mobil11_tau_1 = (tau_1-MODEL_Mobil11) / SIGMA_STAR_Mobil11
Mobil11_tau_2 = (tau_2-MODEL_Mobil11) / SIGMA_STAR_Mobil11
Mobil11_tau_3 = (tau_3-MODEL_Mobil11) / SIGMA_STAR_Mobil11
Mobil11_tau_4 = (tau_4-MODEL_Mobil11) / SIGMA_STAR_Mobil11
IndMobil11 = {
    1: bioNormalCdf(Mobil11_tau_1),
    2: bioNormalCdf(Mobil11_tau_2)-bioNormalCdf(Mobil11_tau_1),
    3: bioNormalCdf(Mobil11_tau_3)-bioNormalCdf(Mobil11_tau_2),
    4: bioNormalCdf(Mobil11_tau_4)-bioNormalCdf(Mobil11_tau_3),
    5: 1-bioNormalCdf(Mobil11_tau_4),
    6: 1.0,
    -1: 1.0,
    -2: 1.0
}

P_Mobil11 = Elem(IndMobil11, Mobil11)

Mobil14_tau_1 = (tau_1-MODEL_Mobil14) / SIGMA_STAR_Mobil14
Mobil14_tau_2 = (tau_2-MODEL_Mobil14) / SIGMA_STAR_Mobil14
Mobil14_tau_3 = (tau_3-MODEL_Mobil14) / SIGMA_STAR_Mobil14
Mobil14_tau_4 = (tau_4-MODEL_Mobil14) / SIGMA_STAR_Mobil14
IndMobil14 = {
    1: bioNormalCdf(Mobil14_tau_1),
    2: bioNormalCdf(Mobil14_tau_2)-bioNormalCdf(Mobil14_tau_1),
    3: bioNormalCdf(Mobil14_tau_3)-bioNormalCdf(Mobil14_tau_2),
    4: bioNormalCdf(Mobil14_tau_4)-bioNormalCdf(Mobil14_tau_3),
    5: 1-bioNormalCdf(Mobil14_tau_4),
    6: 1.0,
    -1: 1.0,
    -2: 1.0
}

P_Mobil14 = Elem(IndMobil14, Mobil14)

Mobil16_tau_1 = (tau_1-MODEL_Mobil16) / SIGMA_STAR_Mobil16
Mobil16_tau_2 = (tau_2-MODEL_Mobil16) / SIGMA_STAR_Mobil16
Mobil16_tau_3 = (tau_3-MODEL_Mobil16) / SIGMA_STAR_Mobil16
Mobil16_tau_4 = (tau_4-MODEL_Mobil16) / SIGMA_STAR_Mobil16
IndMobil16 = {
    1: bioNormalCdf(Mobil16_tau_1),
    2: bioNormalCdf(Mobil16_tau_2)-bioNormalCdf(Mobil16_tau_1),
    3: bioNormalCdf(Mobil16_tau_3)-bioNormalCdf(Mobil16_tau_2),
    4: bioNormalCdf(Mobil16_tau_4)-bioNormalCdf(Mobil16_tau_3),
    5: 1-bioNormalCdf(Mobil16_tau_4),
    6: 1.0,
    -1: 1.0,
    -2: 1.0
}

P_Mobil16 = Elem(IndMobil16, Mobil16)

Mobil17_tau_1 = (tau_1-MODEL_Mobil17) / SIGMA_STAR_Mobil17
Mobil17_tau_2 = (tau_2-MODEL_Mobil17) / SIGMA_STAR_Mobil17
Mobil17_tau_3 = (tau_3-MODEL_Mobil17) / SIGMA_STAR_Mobil17
Mobil17_tau_4 = (tau_4-MODEL_Mobil17) / SIGMA_STAR_Mobil17
IndMobil17 = {
    1: bioNormalCdf(Mobil17_tau_1),
    2: bioNormalCdf(Mobil17_tau_2)-bioNormalCdf(Mobil17_tau_1),
    3: bioNormalCdf(Mobil17_tau_3)-bioNormalCdf(Mobil17_tau_2),
    4: bioNormalCdf(Mobil17_tau_4)-bioNormalCdf(Mobil17_tau_3),
    5: 1-bioNormalCdf(Mobil17_tau_4),
    6: 1.0,
    -1: 1.0,
    -2: 1.0
}

P_Mobil17 = Elem(IndMobil17, Mobil17)

# Choice model


ASC_CAR = Beta('ASC_CAR',betas['ASC_CAR'],None,None,0 )
ASC_PT	 = Beta('ASC_PT',0,None,None,1)
ASC_SM = Beta('ASC_SM',betas['ASC_SM'],None,None,0 )
BETA_COST_HWH = Beta('BETA_COST_HWH',betas['BETA_COST_HWH'],None,None,0 )
BETA_COST_OTHER = Beta('BETA_COST_OTHER',betas['BETA_COST_OTHER'],None,None,0 )
BETA_DIST = Beta('BETA_DIST',betas['BETA_DIST'],None,None,0 )
BETA_TIME_CAR_REF = Beta('BETA_TIME_CAR_REF',betas['BETA_TIME_CAR_REF'],-10000,0,0 )
BETA_TIME_CAR_CL = Beta('BETA_TIME_CAR_CL',betas['BETA_TIME_CAR_CL'],-10,10,0 )
BETA_TIME_PT_REF = Beta('BETA_TIME_PT_REF',betas['BETA_TIME_PT_REF'],-10000,0,0 )
BETA_TIME_PT_CL = Beta('BETA_TIME_PT_CL',betas['BETA_TIME_PT_CL'],-10,10,0 )
BETA_WAITING_TIME = Beta('BETA_WAITING_TIME',betas['BETA_WAITING_TIME'],None,None,0 )

TimePT_scaled  = DefineVariable('TimePT_scaled', TimePT   /  200 ,database)
TimeCar_scaled  = DefineVariable('TimeCar_scaled', TimeCar   /  200 ,database)
MarginalCostPT_scaled  = \
 DefineVariable('MarginalCostPT_scaled', MarginalCostPT   /  10 ,database)
CostCarCHF_scaled  = \
 DefineVariable('CostCarCHF_scaled', CostCarCHF   /  10 ,database)
distance_km_scaled  = \
 DefineVariable('distance_km_scaled', distance_km   /  5 ,database)
PurpHWH = DefineVariable('PurpHWH', TripPurpose == 1,database)
PurpOther = DefineVariable('PurpOther', TripPurpose != 1,database)



### DEFINITION OF UTILITY FUNCTIONS:

BETA_TIME_PT = BETA_TIME_PT_REF * exp(BETA_TIME_PT_CL * CARLOVERS)

V0 = ASC_PT + \
     BETA_TIME_PT * TimePT_scaled + \
     BETA_WAITING_TIME * WaitingTimePT + \
     BETA_COST_HWH * MarginalCostPT_scaled * PurpHWH  +\
     BETA_COST_OTHER * MarginalCostPT_scaled * PurpOther +\
     ec_sigma * errorComponent

BETA_TIME_CAR = BETA_TIME_CAR_REF * exp(BETA_TIME_CAR_CL * CARLOVERS)

V1 = ASC_CAR + \
      BETA_TIME_CAR * TimeCar_scaled + \
      BETA_COST_HWH * CostCarCHF_scaled * PurpHWH  + \
      BETA_COST_OTHER * CostCarCHF_scaled * PurpOther+\
      ec_sigma * errorComponent 

V2 = ASC_SM + BETA_DIST * distance_km_scaled

# Associate utility functions with the numbering of alternatives
V = {0: V0,
     1: V1,
     2: V2}

# Associate the availability conditions with the alternatives.
# In this example all alternatives are available for each individual.
av = {0: 1,
      1: 1,
      2: 1}

# Conditional to the random parameters, we have a logit model (called
# the kernel) for the choice
condprob = models.logit(V,av,Choice)

# Conditional to the random parameters, we have the product of ordered
# probit for the indicators.
condlike = P_Envir01 * \
          P_Envir02 * \
          P_Envir03 * \
          P_Mobil11 * \
          P_Mobil14 * \
          P_Mobil16 * \
          P_Mobil17 * \
          condprob

# We integrate over omega using Monte-Carlo integration
loglike = log(MonteCarlo(condlike))

# Define level of verbosity
import biogeme.messaging as msg
logger = msg.bioMessage()
#logger.setSilent()
#logger.setWarning()
logger.setGeneral()
#logger.setDetailed()

# Create the Biogeme object
biogeme  = bio.BIOGEME(database,loglike,numberOfDraws=10)
biogeme.modelName = "06serialCorrelation"

# Estimate the parameters
results = biogeme.estimate()
print(f"Estimated betas: {len(results.data.betaValues)}")
print(f"Final log likelihood: {results.data.logLike:.3f}")
print(f"Output file: {results.data.htmlFileName}")
results.writeLaTeX()
print(f"LaTeX file: {results.data.latexFileName}")


