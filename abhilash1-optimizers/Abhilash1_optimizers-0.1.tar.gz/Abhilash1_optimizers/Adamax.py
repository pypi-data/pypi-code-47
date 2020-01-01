# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 14:48:18 2019

@author: 45063883
"""

import math
import numpy as np
import Abhilash1_optimizers.Activation as Activation
import Abhilash1_optimizers.hyperparameters as hyperparameters
import Abhilash1_optimizers.Moment_Initializer as Moment_Initializer
#Adamax varaiation of ADAM with L**p norm over L**2 norm(p->infinity)
class ADAMAX():
    def __init__(alpha,b_1,b_2,epsilon,noise_g):
        return hyperparameters.hyperparameter.initialise(alpha,b_1,b_2,epsilon,noise_g)
    def init(m_t,v_t,t,theta):
        return Moment_Initializer.Moment_Initializer.initialize(m_t,v_t,t,theta)
    def Adamax_optimizer(data,len_data,max_itr,alpha,b_1,b_2,epsilon,noise_g,act_func,scale):
        alpha,b_1,b_2,epsilon,noise_g=ADAMAX.__init__(alpha,b_1,b_2,epsilon,noise_g)
        m_t,v_t,t,theta_0=ADAMAX.init(0,0,0,0)
        final_weight_vector=[]
        for i in range(len_data):
            theta_0=data[i]
            for i in range(max_itr):
                t+=1
            
                if(act_func=="softPlus"):
                    g_t=Activation.Activation.softplus(theta_0)
                elif (act_func=="relu"):
                    g_t=Activation.Activation.relu(theta_0)
                elif (act_func=="elu"):
                    g_t=Activation.Activation.elu(theta_0,alpha)
                elif (act_func=="selu"):
                    g_t=Activation.Activation.selu(scale,theta_0,theta)
                elif (act_func=="tanh"):
                    g_t=Activation.Activation.tanh(theta_0)
                elif (act_func=="hardSigmoid"):
                    g_t=Activation.Activation.hard_sigmoid(theta_0)
                elif (act_func=="softSign"):
                    g_t=Activation.Activation.softsign(theta_0)
                elif (act_func=="linear"):
                    g_t=Activation.Activation.linear(theta_0)
                elif (act_func=="exponential"):
                    g_t=Activation.Activation.exponential(theta_0)
                
                m_t=b_1*m_t + (1-b_1)*g_t
                v_t=max(b_2*v_t,g_t)
                theta_prev=theta_0
        
                alpha_t=(alpha*(1.0/(1-b_1**t)))
                theta_0=theta_prev-(alpha_t)
                print("Intrermediate gradients")
                print("==========================================")
                print("Previous gradient",theta_prev)
                print("Present gradient",theta_0)
                print("==========================================")
                #if theta_0==theta_prev:
                    #    break;
                    
            final_weight_vector.append(theta_0)
            
        return final_weight_vector



    def initialize(data,max_itr,alpha,b_1,b_2,epsilon,noise_g):
        len_data=len(data)
        optimized_weights=ADAMAX.Adamax_optimizer(data,len_data,max_itr,alpha,b_1,b_2,epsilon,noise_g,act_func,scale)
        print("Optimized Weight Vector")
        print("=====================================")
        for i in range(len(optimized_weights)):
            print("=====",optimized_weights[i])

if __name__=='__main__':
    print("Verbose")
    #t_0=Adagrad_optimizer()
    #print("gradient coefficient",t_0)
    #solve_grad=poly_func(t_0)
    #print("Gradient Value",solve_grad)
    sample_data=[1,0.5,0.7,0.1]
    ADAMAX.initialize(sample_data,100)    


