"""File 05nestedElasticitiesCI_bootstrap.py

:author: Michel Bierlaire, EPFL
:date: Wed Sep 11 15:57:46 2019

 We use a previously estimated nested logit model.
 Three alternatives: public transporation, car and slow modes.
 RP data.

 We calculate disaggregate and aggregate direct arc elasticities, and
 the confidence intervals. The difference with
 05nestedElasticitiesConfidenceIntervals is that the simulated betas
 used to calculated the confidence intervals are drawn from a normal
 distribution based on the bootstrap estimate of the variance
 covariance matrix.
"""

import sys
import numpy as np
import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
import biogeme.results as res
from biogeme.expressions import Beta, DefineVariable

""" Calculate confidence intervals for elasticities requires interval 
    arithmetics 
    Use 'pip install pyinterval' if not available on your system.
    Warning: other types of interval packages are also available.
"""
try:
    import interval as ia
except:
    print("Use 'pip install pyinterval' to install a requested package")
    exit()
    
# Read the data
df = pd.read_csv("optima.dat",sep='\t')
database = db.Database("optima",df)

# The Pandas data structure is available as database.data. Use all the
# Pandas functions to invesigate the database
#print(database.data.describe())

# The following statement allows you to use the names of the variable
# as Python variable.
globals().update(database.variables)

# Exclude observations such that the chosen alternative is -1
exclude = (Choice == -1.0)
database.remove(exclude)

# Normalize the weights
sumWeight = database.data['Weight'].sum()
normalizedWeight = Weight * 1906 / 0.814484

# Calculate the number of accurences of a value in the database
numberOfMales = database.count("Gender",1)
print("Number of males: ",numberOfMales)
numberOfFemales = database.count("Gender",2)
print("Number of females: ",numberOfFemales)

# For more complex conditions, using directly Pandas
unreportedGender = database.data[(database.data["Gender"] != 1) & (database.data["Gender"] != 2)].count()["Gender"]
print("Unreported gender: ",unreportedGender)

# List of parameters. Their value will be set later.
ASC_CAR = Beta('ASC_CAR',0,None,None,0)
ASC_PT = Beta('ASC_PT',0,None,None,1)
ASC_SM = Beta('ASC_SM',0,None,None,0)
BETA_TIME_FULLTIME = Beta('BETA_TIME_FULLTIME',0,None,None,0)
BETA_TIME_OTHER = Beta('BETA_TIME_OTHER',0,None,None,0)
BETA_DIST_MALE = Beta('BETA_DIST_MALE',0,None,None,0)
BETA_DIST_FEMALE = Beta('BETA_DIST_FEMALE',0,None,None,0)
BETA_DIST_UNREPORTED = Beta('BETA_DIST_UNREPORTED',0,None,None,0)
BETA_COST = Beta('BETA_COST',0,None,None,0)

# Definition of variables:
# For numerical reasons, it is good practice to scale the data to
# that the values of the parameters are around 1.0.

# The following statements are designed to preprocess the data.
# It is like creating a new columns in the data file. This
# should be preferred to the statement like
# TimePT_scaled = Time_PT / 200.0
# which will cause the division to be reevaluated again and again,
# throuh the iterations. For models taking a long time to
# estimate, it may make a significant difference.

TimePT_scaled = TimePT / 200
TimeCar_scaled = TimeCar / 200
MarginalCostPT_scaled = MarginalCostPT / 10
CostCarCHF_scaled = CostCarCHF / 10
distance_km_scaled = distance_km / 5

# We investigate a scenario where the distance increases by one kilometer.
delta_dist = 1.0
distance_km_scaled_after = (distance_km + delta_dist) / 5

male = (Gender == 1)
female = (Gender == 2)
unreportedGender = (Gender == -1)

fulltime = (OccupStat == 1)
notfulltime = (OccupStat != 1)

# Definition of utility functions:
V_PT = ASC_PT + BETA_TIME_FULLTIME * TimePT_scaled * fulltime + \
       BETA_TIME_OTHER * TimePT_scaled * notfulltime + \
       BETA_COST * MarginalCostPT_scaled
V_CAR = ASC_CAR + \
        BETA_TIME_FULLTIME * TimeCar_scaled * fulltime + \
        BETA_TIME_OTHER * TimeCar_scaled * notfulltime + \
        BETA_COST * CostCarCHF_scaled
V_SM = ASC_SM + \
       BETA_DIST_MALE * distance_km_scaled * male + \
       BETA_DIST_FEMALE * distance_km_scaled * female + \
       BETA_DIST_UNREPORTED * distance_km_scaled * unreportedGender

# Utility of the slow mode whem the distance increases by 1 kilometer.
V_SM_after = ASC_SM + \
       BETA_DIST_MALE * distance_km_scaled_after * male + \
       BETA_DIST_FEMALE * distance_km_scaled_after * female + \
       BETA_DIST_UNREPORTED * distance_km_scaled_after * unreportedGender

# Associate utility functions with the numbering of alternatives
V = {0: V_PT,
     1: V_CAR,
     2: V_SM}

V_after = {0: V_PT,
           1: V_CAR,
           2: V_SM_after}

# Associate the availability conditions with the alternatives.
# In this example all alternatives are available for each individual.
av = {0: 1,
      1: 1,
      2: 1}

# Definition of the nests:
# 1: nests parameter
# 2: list of alternatives

MU_NOCAR = Beta('MU_NOCAR',1.0,1.0,None,0)

CAR_NEST = 1.0 , [ 1]
NO_CAR_NEST = MU_NOCAR , [ 0, 2]
nests = CAR_NEST, NO_CAR_NEST

# The choice model is a nested logit
prob_sm = models.nested(V,av,nests,2)
prob_sm_after = models.nested(V_after,av,nests,2)

direct_elas_sm_dist = (prob_sm_after - prob_sm) * distance_km / (prob_sm * delta_dist)

simulate = {'weight': normalizedWeight,
            'Prob. slow modes':prob_sm,
            'direct_elas_sm_dist':direct_elas_sm_dist}

biogeme  = bio.BIOGEME(database,simulate)
biogeme.modelName = "05nestedElasticitiesConfidenceIntervals"

# Retrieve the values of the parameters
# First, extract the names of parameters needed for the simulation
betas = biogeme.freeBetaNames

# Read the estimation results from the file
results = res.bioResults(pickleFile='01nestedEstimation.pickle')

# Extract the values that are necessary
betaValues = results.getBetaValues(betas)

# simulatedValues is a Panda dataframe with the same number of rows as
# the database, and as many columns as formulas to simulate.
simulatedValues = biogeme.simulate(betaValues)

# We calculate the elasticities
simulatedValues['Weighted prob. slow modes'] = simulatedValues['weight'] * simulatedValues['Prob. slow modes']

denominator_sm = simulatedValues['Weighted prob. slow modes'].sum()

direct_elas_sm_dist = (simulatedValues['Weighted prob. slow modes'] * simulatedValues['direct_elas_sm_dist'] / denominator_sm).sum()
print("Aggregate direct elasticity of slow modes wrt distance: {:.7f}".format(direct_elas_sm_dist))


print("Calculating confidence interval...")

# Calculate confidence intervals
# Draw values of betas from the distribution of the estimator. The
# bootstrap estimate of the variance-covariance matrix is used.

size=100

# All betas are simulated
simulatedBetas = np.random.multivariate_normal(results.data.betaValues, results.data.bootstrap_varCovar, size, check_valid='warn')

# Only those necessary for the simulation are selected.
index = [results.data.betaNames.index(b) for b in betas]
b = simulatedBetas[:,index]

# Returns data frame containing, for each simulated value, the left
# and right bounds of the confidence interval calculated by
# simulation.
left,right = biogeme.confidenceIntervals(b,0.9)

left['Weighted prob. slow modes'] = left['weight'] * left['Prob. slow modes']
right['Weighted prob. slow modes'] = right['weight'] * right['Prob. slow modes']
denominator_left = left['Weighted prob. slow modes'].sum()
denominator_right = right['Weighted prob. slow modes'].sum()

# Build an interval object for the denominator 
denominator_interval = ia.interval[(denominator_left,denominator_right)]

# Build a list of interval objects, one for each disaggregate elasticity
elas_interval =  [ia.interval([l,r]) for l,r in zip(left['direct_elas_sm_dist'],right['direct_elas_sm_dist'])]

# Build a list of interval objects, one for each term of the numerator
numerator_interval = [ia.interval([l,r]) for l,r in zip(left['Weighted prob. slow modes'],right['Weighted prob. slow modes'])]

# Build a list of interval objects, one for each term of the sum
terms_of_the_sum_interval = [e * wp / denominator_interval for e,wp in zip(elas_interval,numerator_interval)]

# The interval package apparently does not provide a tool to sum a
# list of intervals. We do it manually. Note that the object interval
# contains a list of ranges (to allow the modeling of disconnected
# intervals). The first of these ranges is x[0], and we access the inf
# and sup values of this range.
sum_interval_left = sum(x[0].inf for x in terms_of_the_sum_interval)
sum_interval_right = sum(x[0].sup for x in terms_of_the_sum_interval)

print("[{},{}]".format(sum_interval_left,sum_interval_right))
