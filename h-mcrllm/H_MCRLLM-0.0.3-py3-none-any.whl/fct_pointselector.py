# Point selector in PCA score plot

import numpy as np

from matplotlib.widgets import LassoSelector
from matplotlib.path import Path
import matplotlib.pyplot as plt
from time import ctime

class SelectFromCollection:
    """Select indices from a matplotlib collection using `LassoSelector`.

    Selected indices are saved in the `ind` attribute. This tool fades out the
    points that are not part of the selection (i.e., reduces their alpha
    values). If your collection has alpha < 1, this tool will permanently
    alter the alpha values.

    Note that this tool selects collection objects based on their *origins*
    (i.e., `offsets`).

    Parameters
    ----------
    ax : :class:`~matplotlib.axes.Axes`
        Axes to interact with.

    collection : :class:`matplotlib.collections.Collection` subclass
        Collection you want to select from.

    alpha_other : 0 <= float <= 1
        To highlight a selection, this tool sets all selected points to an
        alpha value of 1 and non-selected points to `alpha_other`.
    """


    def __init__(self, Spca, Shier,  alpha_other=0.3):
        
        
        #Spectral attributes
        self.Spca = Spca
        self.Shier = Shier
        self.elevel = len(self.Shier[0,:])
        self.selectedSpectra = []
        
        
        # User defined input : shown components
        print('\n####################')
        print('\nSelect PCA components to project (1,2,...n)')
        
        self.PCX = int(input('Horizontal component : '))-1
        self.PCY = int(input('Vertical component : '))-1
        
        # Plot data
        subplot_kw = dict()
        fig, ax = plt.subplots(subplot_kw=subplot_kw)
        self.canvas = ax.figure.canvas
        self.collection = ax.scatter(Spca[:, self.PCX], Spca[:, self.PCY], s=10)
        
        #Plot atributes
        self.alpha_other = alpha_other
        self.xys = self.collection.get_offsets()
        self.Npts = len(self.xys)
        
         

        # Ensure that we have separate colors for each object
        self.fc = self.collection.get_facecolors()
        if len(self.fc) == 0:
            raise ValueError('Collection must have a facecolor')
        elif len(self.fc) == 1:
            self.fc = np.tile(self.fc, (self.Npts, 1))

        self.lasso = LassoSelector(ax, onselect=self.onselect)
        self.ind = []

                
        def accept(event):
            if event.key == "enter":
                print("Selected points:")
                self.disconnect()
                ax.set_title("")
                fig.canvas.draw()
        
        fig.canvas.mpl_connect("key_press_event", accept)
          
        ax.set_title("Press enter to accept selected points")
        plt.xlabel('Principal component ' + str(self.PCX+1))
        plt.ylabel('Principal component ' + str(self.PCY+1))
        
        plt.show()
        
        
        
          
        

    def onselect(self, verts):
        
        path = Path(verts)
        self.ind = np.nonzero(path.contains_points(self.xys))[0]
        #print('\n \n self ind \n \n')
        print('\n')
        print(self.ind)
        

        
        self.computeSpectra()
    
        self.fc[:, -1] = self.alpha_other
        self.fc[self.ind, -1] = 1
        self.collection.set_facecolors(self.fc)
        
        self.canvas.draw_idle()

        #count = self.ind
        #np.savetxt('data_pure_'+str(np.round(100*np.random.rand(),-1))+'.txt',count)
        #np.savetxt('data_pure_'+str(count[0])+'.txt',count)
        #np.savetxt('data_pure_'+str(ctime())+'.txt',count)




    def disconnect(self):
        self.lasso.disconnect_events()
        self.fc[:, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()
        
    
    
    
    def computeSpectra(self):
        
        Si = np.mean(self.Shier[self.ind,:], axis  = 0)
        plt.figure()
        plt.plot(Si)
        self.selectedSpectra = Si
        
        
    
    
    #return indices of selected points
    def getSelectedPoints(self):
        return self.ind
        
        