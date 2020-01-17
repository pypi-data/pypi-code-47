####################################
### This code was automatically  ###
###        generated             ###
###    on 17.01.2020 at 08:29    ###
####################################

#################################
###########  Import   ###########
#################################
import numpy as np

import synumses.one_dimension.parameters as parameters
from   synumses.one_dimension.functions import ohm_potential


#################################
########### Bernoulli ###########
#################################
def bernoulli(x):
	 if (x <  parameters.bernoulli_limit ):
	 	 return 3.30687830687831e-5*x**6 - 0.00138888888888889*x**4 + 0.0833333333333333*x**2 - 0.5*x + 1.0
	 else:
	 	 return x/(np.exp(x) - 1)


############################################
########### hole_current_density ###########
############################################
def hole_current_density():

	 j_p = np.zeros(parameters.n)

	 for i in range(0,parameters.n-1):
	 	 if (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) <= parameters.bernoulli_limit) and (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) <= parameters.bernoulli_limit):
	 	 	 j_p[i] = parameters.T*parameters.kB*parameters.mu_p[i]*(parameters.Nv[i+0]*bernoulli(-parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB))*np.exp(parameters.q*(0.5*parameters.Chi[i+0] + 0.5*parameters.Chi[i+1] + 0.5*parameters.Eg[i+0] + 0.5*parameters.Eg[i+1] + parameters.u[3*(i+1)+0] - parameters.u[3*(i+1)+1])/(parameters.T*parameters.kB)) - parameters.Nv[i+1]*(1.0 - 0.5*parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB) + 0.0833333333333333*parameters.q**2*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])**2/(parameters.T**2*parameters.kB**2) - 0.00138888888888889*parameters.q**4*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])**4/(parameters.T**4*parameters.kB**4) + 3.30687830687831e-5*parameters.q**6*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])**6/(parameters.T**6*parameters.kB**6))*np.exp(parameters.q*(0.5*parameters.Chi[i+0] + 0.5*parameters.Chi[i+1] + 0.5*parameters.Eg[i+0] + 0.5*parameters.Eg[i+1] + parameters.u[(3*i+0)+0] - parameters.u[(3*i+0)+1])/(parameters.T*parameters.kB)))*np.exp(parameters.q*(-1.0*parameters.Chi[i+0] - 1.0*parameters.Chi[i+1] - 1.0*parameters.Eg[i+0] - 1.0*parameters.Eg[i+1] - parameters.u[(3*i+0)+0] + parameters.u[(3*i+0)+1] - parameters.u[3*(i+1)+0] + parameters.u[3*(i+1)+1])/(parameters.T*parameters.kB))/parameters.dx
	 	 if (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) <= parameters.bernoulli_limit) and (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) >  parameters.bernoulli_limit):
	 	 	 j_p[i] = parameters.T*parameters.kB*parameters.mu_p[i]*(parameters.Nv[i+0]*bernoulli(-parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB))*np.exp(parameters.q*(0.5*parameters.Chi[i+0] + 0.5*parameters.Chi[i+1] + 0.5*parameters.Eg[i+0] + 0.5*parameters.Eg[i+1] + parameters.u[3*(i+1)+0] - parameters.u[3*(i+1)+1])/(parameters.T*parameters.kB)) - parameters.Nv[i+1]*parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])*np.exp(parameters.q*(0.5*parameters.Chi[i+0] + 0.5*parameters.Chi[i+1] + 0.5*parameters.Eg[i+0] + 0.5*parameters.Eg[i+1] + parameters.u[(3*i+0)+0] - parameters.u[(3*i+0)+1])/(parameters.T*parameters.kB))/(parameters.T*parameters.kB*(np.exp(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) - 1)))*np.exp(parameters.q*(-1.0*parameters.Chi[i+0] - 1.0*parameters.Chi[i+1] - 1.0*parameters.Eg[i+0] - 1.0*parameters.Eg[i+1] - parameters.u[(3*i+0)+0] + parameters.u[(3*i+0)+1] - parameters.u[3*(i+1)+0] + parameters.u[3*(i+1)+1])/(parameters.T*parameters.kB))/parameters.dx
	 	 if (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) >  parameters.bernoulli_limit) and (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) <= parameters.bernoulli_limit):
	 	 	 j_p[i] = parameters.T*parameters.kB*parameters.mu_p[i]*(parameters.Nv[i+0]*bernoulli(-parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB))*np.exp(parameters.q*(0.5*parameters.Chi[i+0] + 0.5*parameters.Chi[i+1] + 0.5*parameters.Eg[i+0] + 0.5*parameters.Eg[i+1] + parameters.u[3*(i+1)+0] - parameters.u[3*(i+1)+1])/(parameters.T*parameters.kB)) - parameters.Nv[i+1]*(1.0 - 0.5*parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB) + 0.0833333333333333*parameters.q**2*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])**2/(parameters.T**2*parameters.kB**2) - 0.00138888888888889*parameters.q**4*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])**4/(parameters.T**4*parameters.kB**4) + 3.30687830687831e-5*parameters.q**6*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])**6/(parameters.T**6*parameters.kB**6))*np.exp(parameters.q*(0.5*parameters.Chi[i+0] + 0.5*parameters.Chi[i+1] + 0.5*parameters.Eg[i+0] + 0.5*parameters.Eg[i+1] + parameters.u[(3*i+0)+0] - parameters.u[(3*i+0)+1])/(parameters.T*parameters.kB)))*np.exp(parameters.q*(-1.0*parameters.Chi[i+0] - 1.0*parameters.Chi[i+1] - 1.0*parameters.Eg[i+0] - 1.0*parameters.Eg[i+1] - parameters.u[(3*i+0)+0] + parameters.u[(3*i+0)+1] - parameters.u[3*(i+1)+0] + parameters.u[3*(i+1)+1])/(parameters.T*parameters.kB))/parameters.dx
	 	 if (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) >  parameters.bernoulli_limit) and (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) >  parameters.bernoulli_limit):
	 	 	 j_p[i] = parameters.T*parameters.kB*parameters.mu_p[i]*(parameters.Nv[i+0]*bernoulli(-parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB))*np.exp(parameters.q*(0.5*parameters.Chi[i+0] + 0.5*parameters.Chi[i+1] + 0.5*parameters.Eg[i+0] + 0.5*parameters.Eg[i+1] + parameters.u[3*(i+1)+0] - parameters.u[3*(i+1)+1])/(parameters.T*parameters.kB)) - parameters.Nv[i+1]*parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])*np.exp(parameters.q*(0.5*parameters.Chi[i+0] + 0.5*parameters.Chi[i+1] + 0.5*parameters.Eg[i+0] + 0.5*parameters.Eg[i+1] + parameters.u[(3*i+0)+0] - parameters.u[(3*i+0)+1])/(parameters.T*parameters.kB))/(parameters.T*parameters.kB*(np.exp(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) - 1)))*np.exp(parameters.q*(-1.0*parameters.Chi[i+0] - 1.0*parameters.Chi[i+1] - 1.0*parameters.Eg[i+0] - 1.0*parameters.Eg[i+1] - parameters.u[(3*i+0)+0] + parameters.u[(3*i+0)+1] - parameters.u[3*(i+1)+0] + parameters.u[3*(i+1)+1])/(parameters.T*parameters.kB))/parameters.dx

	 i = parameters.n-1
	 j_p[i] =  j_p[i-1]

	 return j_p


################################################
########### electron_current_density ###########
################################################
def electron_current_density():

	 j_n = np.zeros(parameters.n)

	 for i in range(0,parameters.n-1):
	 	 if (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) <= parameters.bernoulli_limit) and (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) <= parameters.bernoulli_limit):
	 	 	 j_n[i] = -parameters.T*parameters.kB*parameters.mu_n[i]*(parameters.Nc[i+0]*(1.0 - 0.5*parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB) + 0.0833333333333333*parameters.q**2*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])**2/(parameters.T**2*parameters.kB**2) - 0.00138888888888889*parameters.q**4*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])**4/(parameters.T**4*parameters.kB**4) + 3.30687830687831e-5*parameters.q**6*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])**6/(parameters.T**6*parameters.kB**6))*np.exp(parameters.q*(0.5*parameters.Chi[i+0] + 0.5*parameters.Chi[i+1] + parameters.u[(3*i+0)+0] - parameters.u[(3*i+0)+2])/(parameters.T*parameters.kB)) - parameters.Nc[i+1]*bernoulli(-parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB))*np.exp(parameters.q*(0.5*parameters.Chi[i+0] + 0.5*parameters.Chi[i+1] + parameters.u[3*(i+1)+0] - parameters.u[3*(i+1)+2])/(parameters.T*parameters.kB)))/parameters.dx
	 	 if (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) <= parameters.bernoulli_limit) and (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) >  parameters.bernoulli_limit):
	 	 	 j_n[i] = -parameters.T*parameters.kB*parameters.mu_n[i]*(parameters.Nc[i+0]*(1.0 - 0.5*parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB) + 0.0833333333333333*parameters.q**2*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])**2/(parameters.T**2*parameters.kB**2) - 0.00138888888888889*parameters.q**4*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])**4/(parameters.T**4*parameters.kB**4) + 3.30687830687831e-5*parameters.q**6*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])**6/(parameters.T**6*parameters.kB**6))*np.exp(parameters.q*(0.5*parameters.Chi[i+0] + 0.5*parameters.Chi[i+1] + parameters.u[(3*i+0)+0] - parameters.u[(3*i+0)+2])/(parameters.T*parameters.kB)) - parameters.Nc[i+1]*bernoulli(-parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB))*np.exp(parameters.q*(0.5*parameters.Chi[i+0] + 0.5*parameters.Chi[i+1] + parameters.u[3*(i+1)+0] - parameters.u[3*(i+1)+2])/(parameters.T*parameters.kB)))/parameters.dx
	 	 if (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) >  parameters.bernoulli_limit) and (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) <= parameters.bernoulli_limit):
	 	 	 j_n[i] = -parameters.T*parameters.kB*parameters.mu_n[i]*(parameters.Nc[i+0]*parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])*np.exp(parameters.q*(0.5*parameters.Chi[i+0] + 0.5*parameters.Chi[i+1] + parameters.u[(3*i+0)+0] - parameters.u[(3*i+0)+2])/(parameters.T*parameters.kB))/(parameters.T*parameters.kB*(np.exp(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) - 1)) - parameters.Nc[i+1]*bernoulli(-parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB))*np.exp(parameters.q*(0.5*parameters.Chi[i+0] + 0.5*parameters.Chi[i+1] + parameters.u[3*(i+1)+0] - parameters.u[3*(i+1)+2])/(parameters.T*parameters.kB)))/parameters.dx
	 	 if (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) >  parameters.bernoulli_limit) and (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) >  parameters.bernoulli_limit):
	 	 	 j_n[i] = -parameters.T*parameters.kB*parameters.mu_n[i]*(parameters.Nc[i+0]*parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])*np.exp(parameters.q*(0.5*parameters.Chi[i+0] + 0.5*parameters.Chi[i+1] + parameters.u[(3*i+0)+0] - parameters.u[(3*i+0)+2])/(parameters.T*parameters.kB))/(parameters.T*parameters.kB*(np.exp(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) - 1)) - parameters.Nc[i+1]*bernoulli(-parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB))*np.exp(parameters.q*(0.5*parameters.Chi[i+0] + 0.5*parameters.Chi[i+1] + parameters.u[3*(i+1)+0] - parameters.u[3*(i+1)+2])/(parameters.T*parameters.kB)))/parameters.dx

	 i = parameters.n-1
	 j_n[i] =  j_n[i-1]

	 return j_n


################################
########### update_b ###########
################################
def update_b(Ua, Ub):

	 for i in range(0, parameters.n):
	 	 if (i==0) :
	 	 	 #################
	 	 	 ###  left ###
	 	 	 #################
	 	 	 parameters.b[3*i+0] = (parameters.Epsilon[i]*((ohm_potential(parameters.C[0], parameters.Chi[0], parameters.Eg[0], parameters.Nc[0], parameters.Nv[0]) + Ua) - 2.0*parameters.u[(3*i+0)+0] + parameters.u[3*(i+1)+0])*np.exp(parameters.q*(parameters.Chi[i+0] + parameters.Eg[i+0] + parameters.u[(3*i+0)+0] - parameters.u[(3*i+0)+1])/(parameters.T*parameters.kB)) + parameters.dx**2*parameters.q*(parameters.Nv[i+0] + (parameters.C[i] - parameters.Nc[i+0]*np.exp(parameters.q*(parameters.Chi[i+0] + parameters.u[(3*i+0)+0] - parameters.u[(3*i+0)+2])/(parameters.T*parameters.kB)))*np.exp(parameters.q*(parameters.Chi[i+0] + parameters.Eg[i+0] + parameters.u[(3*i+0)+0] - parameters.u[(3*i+0)+1])/(parameters.T*parameters.kB))))*np.exp(-parameters.q*(parameters.Chi[i+0] + parameters.Eg[i+0] + parameters.u[(3*i+0)+0] - parameters.u[(3*i+0)+1])/(parameters.T*parameters.kB))/parameters.Epsilon[i]
	 	 	 if (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) <= parameters.bernoulli_limit) and (np.abs(parameters.q*(-(ohm_potential(parameters.C[0], parameters.Chi[0], parameters.Eg[0], parameters.Nc[0], parameters.Nv[0]) + Ua) + parameters.u[(3*i+0)+0])/(parameters.T*parameters.kB)) <= parameters.bernoulli_limit) and (np.abs(parameters.q*(-(ohm_potential(parameters.C[0], parameters.Chi[0], parameters.Eg[0], parameters.Nc[0], parameters.Nv[0]) + Ua) + parameters.u[(3*i+0)+0])/(parameters.T*parameters.kB)) <= parameters.bernoulli_limit) and (np.abs(parameters.q*(parameters.u[(3*i+0)+0] - parameters.u[3*(i+1)+0])/(parameters.T*parameters.kB)) <= parameters.bernoulli_limit):
	 	 	 	 parameters.b[3*i+1] = 