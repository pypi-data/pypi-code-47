# Use selected spectra to finalize MCR
# 
# Compute C from X using reference spectra S found in PCA

import matplotlib.pyplot as plt
import numpy as np
from fct_fullMCR import HyperspectralSegmentation_MCR_LLM   
plt.close('all')

#Load spectrum
S = np.zeros((nb_pure,s3))

for i in range(nb_pure): 
    S[i,:] = np.copy(Sselect[i].selectedSpectra)

plt.figure()
plt.plot(S.T)

C, S = HyperspectralSegmentation_MCR_LLM.mcr_llm(X, nb_pure, S, nb_iter = 1)

plt.figure()
plt.plot(C)

plt.figure()
plt.plot(S.T)

print('\nThat\'s all folks!')