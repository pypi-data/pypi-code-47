# Use selected spectra to finalize MCR
# 
# Compute C from X using reference spectra S found in PCA

import matplotlib.pyplot as plt
import numpy as np
from fct_half_MCR import HyperspectralSegmentation_Demi_LLM   
plt.close('all')

#Load spectrum
S = np.zeros((nb_pure,s3))

for i in range(nb_pure): 
    S[i,:] = np.copy(Sselect[i].selectedSpectra) 

# Remove (center and scale to unit variance)
S = S * S_H_std + S_H_mean

C = HyperspectralSegmentation_Demi_LLM.mcr_llm(S, X)

plt.figure()
plt.plot(S.T)

plt.figure()
plt.plot(C)

print('\nThat\'s all folks!')