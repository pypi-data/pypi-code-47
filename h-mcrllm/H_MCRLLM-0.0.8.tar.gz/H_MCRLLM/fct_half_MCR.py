# DEMI MCR LLM

"""
Coded by Jeffrey Byrns
Adapted by Ryan Gosselin
"""

# import packages
import numpy as np
from scipy.optimize import minimize
from functools import partial



class HyperspectralSegmentation_Demi_LLM:

       
    
    @classmethod
    def mcr_llm(cls, s, xraw):
        
        nb_c = s.shape[0]

        
        x_sum = np.asarray([np.sum(xraw, axis=1)]).T
        x_norm = xraw / x_sum
        x_norm = np.nan_to_num(x_norm)
        
        c_pred = x_norm @ s.T @ np.linalg.inv(s @ s.T)
        
        c = cls.C_plm(s, xraw, nb_c, c_pred)



        return c   
    
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
            
            # avoid errors, should not be necessary
            yPred[yPred < 1/(10000*len(yPred))] = 1/(10000*len(yPred))
            
            
            
            
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