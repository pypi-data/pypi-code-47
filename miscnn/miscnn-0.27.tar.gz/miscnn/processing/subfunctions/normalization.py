#==============================================================================#
#  Author:       Dominik Müller                                                #
#  Copyright:    2019 IT-Infrastructure for Translational Medical Research,    #
#                University of Augsburg                                        #
#                                                                              #
#  This program is free software: you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation, either version 3 of the License, or           #
#  (at your option) any later version.                                         #
#                                                                              #
#  This program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#==============================================================================#
#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
# External libraries
import numpy as np
# Internal libraries/scripts
from miscnn.processing.subfunctions.abstract_subfunction import Abstract_Subfunction

#-----------------------------------------------------#
#          Subfunction class: Normalization           #
#-----------------------------------------------------#
""" A Normalization Subfunction class which normalizes the intensity pixel values of an image using
    the Z-Score technique (default setting) or through scaling to [0,1].

Methods:
    __init__                Object creation function
    preprocessing:          Pixel intensity value normalization the imaging data
    postprocessing:         Do nothing
"""
class Normalization(Abstract_Subfunction):
    #---------------------------------------------#
    #                Initialization               #
    #---------------------------------------------#
    def __init__(self, z_score=True):
        self.z_score = z_score

    #---------------------------------------------#
    #                Preprocessing                #
    #---------------------------------------------#
    def preprocessing(self, sample, training=True):
        # Access image
        image = sample.img_data
        # Perform z-score normalization
        if self.z_score:
            # Compute mean and standard deviation
            mean = np.mean(image)
            std = np.std(image)
            # Scaling
            image_normalized = (image - mean) / std
        # Perform scaling normalization between [0,1]
        else:
            # Identify minimum and maximum
            max_value = np.max(image)
            min_value = np.min(image)
            # Scaling
            image_normalized = (image - min_value) / (max_value - min_value)
        # Update the sample with the normalized image
        sample.img_data = image_normalized

    #---------------------------------------------#
    #               Postprocessing                #
    #---------------------------------------------#
    def postprocessing(self, prediction):
        return prediction
