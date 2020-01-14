# Hierarchical MCRLLM (3 steps)
# 
# MCR takes an input X spectral matrix to obtain:
# C : composition map or n components
# S : spectra of the n components
#
# STEP 1. 
# Call raw X data and repeatedly it subdivided it into n=2
# components. This generates multiple spectra (S=2 for each)
# subdivision.
#
# STEP 2.
# PCA on the multiple spectra to manually identify the
# reference spectra (i.e. pure species)
#
# STEP 3.
# Use the reference spectra (step 2) to compute C. This is done using
# half_MCR: MCRLLM in which the spectra S are not evaluted anew.

import numpy as np
import matplotlib.pyplot as plt
from fct_H_MCR_LLM import h_MCR_LLM
plt.close('all')

X = np.load('data1.npy')

s1,s2,s3 = X.shape
X = np.reshape(X,[s1*s2,s3])

# Keep a random subset of the data
#r = np.random.rand(s1*s2,1)
#X = np.concatenate((r,X),axis=1)
#X = X[X[:,0].argsort()]
#X = X[:,1:]
#X = X[:10000,:]

#%% H MCRLLM

#analysis parameters - hiearchical init
nb_imcr = 1         # Number of itteration of mcrllm in hierarchical
min_pixels = 5     # Minimum of pixel in a division (should be about one percent of total pixels)
max_pixels = 20     # Maximum of pixels in a division (should be 3 to 10 times bigger than min pixels)
Max_level = 5      # Maximum of subdivision

S_H = h_MCR_LLM.h_mcr_llm(nb_imcr, min_pixels, max_pixels, Max_level, X)

np.save('S_H.npy', S_H)

print('\nThat\'s all folks!')