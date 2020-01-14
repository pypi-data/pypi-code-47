# -*- coding: utf-8 -*-
"""
@auteurs: Hugo Caussan et Louis-Philippe Baillargeon
"""

# import packages
import numpy as np
from scipy.optimize import minimize
import scipy.stats as stats
from functools import partial
from tqdm import tqdm
import math
from scipy.special import factorial



class HyperspectralSegmentation_MCR_LLM:

       
    
    @classmethod
    def mcr_llm(cls, xraw, nb_c, init, nb_iter = 25):
    
        x_sum = np.asarray([np.sum(xraw, axis=1)]).T
        x_norm = xraw / x_sum
        x = np.nan_to_num(x_norm)
        
        s = init      
        [nb_pix,nb_lev] = np.shape(xraw)
        c = np.zeros((nb_pix, nb_c))
        
        
        c = x @ s.T @ np.linalg.inv(s @ s.T)

        
        for nb_iter in tqdm(range(nb_iter)):
            # Concentrations (with Poisson likelihood maximization)
            
            c = cls.C_plm(s, xraw, nb_c, c)
            s = cls.s_plm(x, c)
            

        return c, s    
    
    
    
    
    
    @classmethod
    def s_plm(cls,x,c):
        S2 = np.linalg.inv(c.T@c)@c.T@x# Multilinear regression
        S2[S2 <= np.spacing(1)] = np.spacing(1) # avoid 0 values
        s = S2/ (np.sum(S2, axis =1) * np.ones((np.size(S2, axis = 1),1))).T# Normalization
        
        
        return s

    
    
    
    
    @classmethod
    def C_plm(cls, s, xraw, nb_c, c_pred):
        #initialize C

        [nb_pix,nb_lev] = np.shape(xraw)
        c_new = np.zeros((nb_pix,nb_c))
        


        # on calcule les concentrations optimales pour chaque pixel par maximum likelihood 
        for pix in range(nb_pix):

                x_sum = np.sum(xraw[pix,:])      #total des counts 
                sraw = s*x_sum
                
                c_new[pix,:] = cls.pyPLM(nb_c, sraw, xraw[pix,:], c_pred[pix,:])
                
                
         # avoid errors (this part should not be necessary)
        c_new[np.isnan(c_new)] = 1/nb_c
        c_new[np.isinf(c_new)] = 1/nb_c
        c_new[c_new<0] = 0
        c_sum1 = np.array([np.sum(c_new,axis=1)])
        c_sum =c_sum1.T@np.ones((1,np.size(c_new,axis =1)))
        c_new = c_new/c_sum

        return c_new
    
    
    
    
    
    @classmethod
    def pyPLM(cls, nb_c, sraw, xrawPix, c_old):
        

        # sum of every value is equal to 1
        def con_one(c_old):
            return 1-sum(c_old) 
        

        # all values are positive
        bnds = ((0.0, 1.0),) * nb_c
        

        cons = [{'type': 'eq', 'fun': con_one}]
        
        
        
        
        def regressLLPoisson(sraw,  xrawPix, c_pred):
            
            
            
            #compute prediction of counts
            yPred = c_pred @ sraw
            
            nb_lev = len(yPred)
            
            # avoid errors, should not be necessary
            yPred[yPred < 1/1000000] = 1/1000000
            
            
            
            
            logLik = -np.sum(xrawPix*np.log(yPred)-yPred)
            
            
            return (logLik)
        
        
        
        def jacobians(nb_c, xrawPix, sraw, c_pred):

            #compute prediction of counts
            yPred = c_pred @ sraw
            
            
            #compute jacobians
            jacC = np.zeros(nb_c)
            
            for phase in range(nb_c):
                
                jacC[phase] = -np.sum(((xrawPix*sraw[phase,:])/yPred)-sraw[phase,:])
                
            return(jacC) 
        

   
                
        # Run the minimizer    
        results = minimize(partial(regressLLPoisson, sraw,  xrawPix), c_old, method='SLSQP', bounds=bnds, constraints=cons, jac = partial(jacobians, nb_c, xrawPix, sraw))
        results = results.x
        results = np.asarray(results)
        


        c_new = results.reshape(int(len(results) / nb_c), nb_c)
        
        
        return c_new
