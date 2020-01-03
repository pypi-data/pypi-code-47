#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 18:55:26 2019

@author: sven
"""

def constraints_pso(x,**kwargs):
    
    return([np.linalg.norm(x) -1 + 1e-3,-np.linalg.norm(x) +1 + 1e-3]) 
    
    
def dicomo_max_pso(x,**kwargs): #works
    
    est = kwargs.pop('est')
    X = kwargs.pop('X')
    return(-est.fit(np.matmul(X,x)))
    
    
# before dicomo_max:
    wi = minimize(lambda x: -self.most.fit(np.matmul(E,x),**opt_args),
                                    E[0,:].transpose(), 
                                    method=self.optimizer,
                                    constraints=constraint,
                                    options=self.optimizer_options).x


def dicomo_max(x,est,X,opt_args): #works
    
    n = len(x)
    x = np.matrix(x).reshape((n,1))
    return(-est.fit(np.matmul(X,x),**opt_args))
    
def dicomo_max(x,): #works
    
    
    return(-est.fit(np.matmul(X,x)))
    
def var_max(x,X): # works
    
    return(-np.var(np.matmul(X,x)))
    
def trimmcov_max(x,X): # works
    
    return(-trim_mom(np.matmul(X,x),np.matmul(X,x),trim_mean,2,0,1,fscorr=False))
    
def trimmvar_max(x,X): # works
    
    return(-trimvar(np.matmul(X,x),0))
    
def trimmvar_dir_max(x,X): #does not work
    
    w = np.matmul(X,x)
    return(-sps.trim_mean(np.square(w - sps.trim_mean(w,0)),0)[0])
    
def var_dir_max(x,X): #works
    
    w = np.matmul(X,x)
    return(-np.mean(np.square(w - np.mean(w))))
    
def dicomo_dir_max(x,X): #works di
    
    est = dicomo()
    return(-est.fit(np.matmul(X,x)))