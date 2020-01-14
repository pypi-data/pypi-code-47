# PCA of h_MCR results - choose spectra

import numpy as np
from sklearn import decomposition
from fct_pointselector import SelectFromCollection
import matplotlib.pyplot as plt

plt.close('all')

S_H = np.load('S_H.npy')
print('Hierarchical spectra: ',S_H.shape)
    
# Center and scale to unit variance
S_H_mean = np.mean(S_H,axis=0)
S_H_std = np.std(S_H,axis=0)
S_H = (S_H - S_H_mean)/S_H_std

#PCA
# Number of PCA components
nb_pc = 4
pca = decomposition.PCA(n_components=nb_pc)
pca.fit(S_H)

Spca = pca.transform(S_H)  # spectra expressed in PCA scores (t)


# Number of reference spectra to be found in PCA score space
print('\nCreate reference spectra based on the hierarchicalspectra obtained.')
print('To do so:')
print('1. Enter the number of reference spectra (n) you are looking for.'
      'This will generate n score plots - pick the components to illustrate')
print('2. Circle 1 or more spectra to be combined into a reference spectra.')


nb_pure = 3

Sselect = [SelectFromCollection(Spca, S_H)   for i in range(nb_pure)]
#Sselect[0].ind

print('\nThat\'s all folks!')