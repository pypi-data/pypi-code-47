# Use selected spectra to finalize MCR

from fct_half_LLM import HyperspectralSegmentation_Demi_LLM   
plt.close('all')

#%% User Input

#analysis parameters - mcrllm 
nb_i = 3                        # Number of iterations in mcr_llm


#%% code

import matplotlib.pyplot as plt
import numpy as np

#Load spectrum
Si = np.zeros((nb_pure,s3))

for i in range(nb_pure): 
    Si[i,:] = np.copy(Sselect[i].selectedSpectra)
    
S = Si    

plt.figure()
plt.plot(S.T)


C = HyperspectralSegmentation_Demi_LLM.mcr_llm(S, X)


plt.figure()
plt.plot(C)

print('\nThat\'s all folks!')