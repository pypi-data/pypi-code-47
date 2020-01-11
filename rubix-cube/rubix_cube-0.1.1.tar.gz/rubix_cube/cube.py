# -*- coding: utf-8 -*-
"""Rubix :class:`Cube` class data-structure Module

Module Description
==================

Collection of methods that define the main Rubix :class:`Cube` class data
structure and how it is interacted with by other modules.

Note:
	Using `Western Color Scheme 
	<https://ruwix.com/the-rubiks-cube/japanese-western-color-schemes/>`_ as
	default Rubix Cube coloring scheme.

Module Contents
===============

	*	:class:`Rubix Cube <Cube>` class that is capable of being parameterized
		with a custom set of 6 unique colors (`Default Color Scheme 
		<https://www.schemecolor.com/rubik-cube-colors.php>`_) and can invoke
		the following moves.

		.. figure:: ./../../misc/cube_moves.png
		   :name: cube_moves
		   :align: center
		   :scale: 75%

		   6 cube face rotations both clock-wise and 
		   counter-clockwise (inverse) are considered to be the standard 
		   move-set.

.. moduleauthor:: David Grethlein <djg329@drexel.edu>

"""

import os
import sys
import json

import warnings

from typing import List, Tuple, Dict

import numpy as np
from matplotlib.colors import is_color_like


class Cube(object):
	"""Data structure for representing a 3x3x3 rubix-cube.

	Attributes:
		__colors (Dict[str,str]): Dictionary of HEX colors that define the 
			rendering of the :class:`Cube`'s tile coloring.
		__faces (Dict[str,np.ndarray]): Dictionary of 
			:class:`numpy arrays <numpy.ndarray>` that define the rendering of
			the :class:`Cube`'s tile configuration.

	"""

	#==========================================================================
	#		CLASS CONSTRUCTOR
	#==========================================================================
	def __init__(self,
				 colors : Dict[str,str] = None,
				 faces : Dict[str,np.array] = None,
				 verbose : bool = False):
		""":class:`Cube` class constructor.

		Args:
			colors (Dict[str,str], optional): Dictionary of color HEX strings.
				Default value is ``None`` which will create a cube with default
				colors :attr:`DEFAULT_FACE_COLORS`. 

				.. code-block:: 
				   :name: init_colors_keys
				   :caption: Required ``colors`` dictionary keys.

			   	   colors = {'UP_COLOR' : ...,
				             'DOWN_COLOR' : ...,
				             'FRONT_COLOR' : ...,
				             'BACK_COLOR' : ...,
				             'LEFT_COLOR' : ...,
				             'RIGHT_COLOR' : ...
				            }

				All colors passed as values must return ``True`` when examined
				by :func:`matplotlib.colors.is_color_like`.

			faces (Dict[str,np.array], optional): Dictionary of face names to
				3x3 arrays of the the tile face values. Default value is 
				``None`` which will create a solved cube with default colors.

				.. code-block::
				   :name: init_faces_keys 
				   :caption: Required ``faces`` dictionary keys.

			   	   faces = {'UP_FACE' : ...,
				            'DOWN_FACE' : ...,
				            'FRONT_FACE' : ...,
				            'BACK_FACE' : ...,
				            'LEFT_FACE' : ...,
				            'RIGHT_FACE' : ...
				           }

				All faces passed as value must be 3x3 
				:class:`numpy arrays <numpy.ndarray>` with each element 
				returning ``True`` when examined by 
				:func:`matplotlib.colors.is_color_like`.

			verbose (bool, optional): [DEBUG]-style console output.
				Default value is ``False``.

		"""

		# Sets private attributes via properties
		if not isinstance(colors, dict):
			self.colors = Cube.DEFAULT_FACE_COLORS
		else:
			self.colors = colors

		if not isinstance(faces, dict):
			self.faces = Cube.DEFAULT_FACES	
		else:
			self.faces = faces			

		if verbose:
			if self.is_well_formed():
				print("\n[DEBUG]\tCube successfully initialized!\n")
			else:
				print("\n[ERROR]\tCube initialization failure!\n")

	#==========================================================================
	#		PROPERTY INTERFACE(s)
	#==========================================================================
	@property
	def colors(self):
		"""Can only be set to be a dictionary with 6 unique color string values
		that all return ``True`` when examined by 
		:func:`matplotlib.colors.is_color_like`. 

		.. code-block::
		   :name: colors_keys
		   :caption: Required ``colors`` dictionary keys.
		   
		   colors = {'UP_COLOR' : ...,
		             'DOWN_COLOR' : ...,
		             'FRONT_COLOR' : ...,
		             'BACK_COLOR' : ...,
		             'LEFT_COLOR' : ...,
		             'RIGHT_COLOR' : ...
		            }
		"""
		return self.__colors

	
	@colors.setter
	def colors(self, colors : Dict[str,str]):

		required_keys = ['UP_COLOR',
						 'DOWN_COLOR',
						 'FRONT_COLOR',
						 'BACK_COLOR',
						 'LEFT_COLOR',
						 'RIGHT_COLOR']

		if isinstance(colors, dict)\
		and all([key in colors for key in required_keys]):

			set_colors = np.array([colors[key] for key in required_keys])

			if all([is_color_like(color) for color in set_colors]):

				self.__colors = dict(zip(required_keys , set_colors))


	@property
	def faces(self) -> Dict[str,np.ndarray]:
		"""Can only be set to be a dictionary of 6 strings mapped to the faces
		of a Rubix Cube. Each value must be a 3x3 
		:class:`numpy array <numpy.ndarray>` of values all of which are valid
		colors that can be found within the :attr:`colors` attribute.
		
		.. code-block::
		   :name: faces_keys
		   :caption: Required ``faces`` dictionary keys.
		   
		   faces = {'UP_FACE' : ...,
		            'DOWN_FACE' : ...,
		            'FRONT_FACE' : ...,
		            'BACK_FACE' : ...,
		            'LEFT_FACE' : ...,
		            'RIGHT_FACE' : ...
		           }
		"""
		return self.__faces


	@faces.setter
	def faces(self, faces : Dict[str,np.ndarray]):

		required_keys = ['UP_FACE',
						 'DOWN_FACE',
						 'FRONT_FACE',
						 'BACK_FACE',
						 'LEFT_FACE',
						 'RIGHT_FACE']
		
		if isinstance(faces, dict)\
		and all([key in faces for key in required_keys]):

			set_faces = np.array([faces[key] for key in required_keys])

			if all([self.is_valid_face(face) for face in set_faces]):

				self.__faces = dict(zip(required_keys , set_faces))

	#==========================================================================
	#		QUALITY ASSURANCE METHOD(s)
	#==========================================================================	
	def is_well_formed(self) -> bool:
		"""Quality control method to ensure class has been properly
		initialized by examining all :attr:`faces` via the quality control
		method :func:`is_valid_face`.
		
		Returns:
			``True`` if all faces are 3 x 3 arrays of valid colors
			as defined by :func:`matplotlib.colors.is_color_like`,
			``False`` otherwise.

		"""
		return all([self.is_valid_face(self.faces[face]) 
						for face in self.faces])


	def is_valid_face(self, face : np.ndarray) -> bool:
		"""Checks if the provided array could be a valid face on a the 
		currently initialized :class:`Cube`.
			
		Args:
			face (np.ndarray): Array to be tested for being valid in the
				context of the current :class:`Cube`.

		Returns:
			``True`` if faces is 3 x 3 array of valid colors as defined by
			current instance's :attr:`colors` attribute, ``False`` otherwise.
		"""
		if isinstance(face, np.ndarray)\
		and face.shape == (3,3)\
		and all([
				all([val in self.colors.values() for val in row])
					for row in face]):

			return True

		else:

			False

	#==========================================================================
	#		MOVE METHOD(s)
	#==========================================================================
	def up(self):
		"""Up Move
		"""
		if self.is_well_formed():

			self.faces['UP_FACE'] = np.rot90(self.faces['UP_FACE'], 
											 axes=(1,0))

			temp = self.faces['BACK_FACE'][0,:]
			self.faces['BACK_FACE'][0,:] = self.faces['LEFT_FACE'][0,:]
			self.faces['LEFT_FACE'][0,:] = self.faces['FRONT_FACE'][0,:]
			self.faces['FRONT_FACE'][0,:] = self.faces['RIGHT_FACE'][0,:]
			self.faces['RIGHT_FACE'][0,:] = temp


	def up_inverse(self):
		"""Up Inverse Move
		"""
		if self.is_well_formed():

			self.faces['UP_FACE'] = np.rot90(self.faces['UP_FACE'])

			temp = self.faces['BACK_FACE'][0,:]
			self.faces['BACK_FACE'][0,:] = self.faces['RIGHT_FACE'][0,:]
			self.faces['RIGHT_FACE'][0,:] = self.faces['FRONT_FACE'][0,:]
			self.faces['FRONT_FACE'][0,:] = self.faces['LEFT_FACE'][0,:]
			self.faces['LEFT_FACE'][0,:] = temp


	def down(self):
		"""Down Move
		"""
		if self.is_well_formed():

			self.faces['DOWN_FACE'] = np.rot90(self.faces['DOWN_FACE'])

			temp = self.faces['FRONT_FACE'][2,:]
			self.faces['FRONT_FACE'][2,:] = self.faces['LEFT_FACE'][2,:]
			self.faces['LEFT_FACE'][2,:] = self.faces['BACK_FACE'][2,:]
			self.faces['BACK_FACE'][2,:] = self.faces['RIGHT_FACE'][2,:]
			self.faces['RIGHT_FACE'][2,:] = temp

	def down_inverse(self):
		"""Down Inverse Move
		"""
		if self.is_well_formed():

			self.faces['DOWN_FACE'] = np.rot90(self.faces['DOWN_FACE'], 
											   axes=(1,0))

			temp = self.faces['FRONT_FACE'][2,:]
			self.faces['FRONT_FACE'][2,:] = self.faces['RIGHT_FACE'][2,:]
			self.faces['RIGHT_FACE'][2,:] = self.faces['BACK_FACE'][2,:]
			self.faces['BACK_FACE'][2,:] = self.faces['LEFT_FACE'][2,:]
			self.faces['LEFT_FACE'][2,:] = temp


	def front(self):
		"""Front Move
		"""
		if self.is_well_formed():

			self.faces['FRONT_FACE'] = np.rot90(self.faces['FRONT_FACE'], 
												axes=(1,0))

			temp = self.faces['UP_FACE'][2,:]
			self.faces['UP_FACE'][2,:] = self.faces['LEFT_FACE'][:,2]
			self.faces['LEFT_FACE'][:,2] = self.faces['DOWN_FACE'][0,:]
			self.faces['DOWN_FACE'][0,:] = self.faces['RIGHT_FACE'][:,0]
			self.faces['RIGHT_FACE'][:,0] = temp


	def front_inverse(self):
		"""Front Inverse Move
		"""
		if self.is_well_formed():

			self.faces['FRONT_FACE'] = np.rot90(self.faces['FRONT_FACE'])

			temp = self.faces['UP_FACE'][2,:]
			self.faces['UP_FACE'][2,:] = self.faces['RIGHT_FACE'][:,0]
			self.faces['RIGHT_FACE'][:,0] = self.faces['DOWN_FACE'][0,:]
			self.faces['DOWN_FACE'][0,:] = self.faces['LEFT_FACE'][:,2]
			self.faces['LEFT_FACE'][:,2] = temp


	def back(self):
		"""Back Move
		"""
		if self.is_well_formed():

			self.faces['BACK_FACE'] = np.rot90(self.faces['BACK_FACE'])

			temp = self.faces['DOWN_FACE'][2,:]
			self.faces['DOWN_FACE'][2,:] = self.faces['LEFT_FACE'][:,0]
			self.faces['LEFT_FACE'][:,0] = self.faces['UP_FACE'][0,:]
			self.faces['UP_FACE'][0,:] = self.faces['RIGHT_FACE'][:,2]
			self.faces['RIGHT_FACE'][:,2] = temp


	def back_inverse(self):
		"""Back Inverse Move
		"""
		if self.is_well_formed():

			self.faces['BACK_FACE'] = np.rot90(self.faces['BACK_FACE'], 
											   axes=(1,0))

			temp = self.faces['DOWN_FACE'][2,:]
			self.faces['DOWN_FACE'][2,:] = self.faces['RIGHT_FACE'][:,2]
			self.faces['RIGHT_FACE'][:,2] = self.faces['UP_FACE'][0,:]
			self.faces['UP_FACE'][0,:] = self.faces['LEFT_FACE'][:,0]
			self.faces['LEFT_FACE'][:,0] = temp


	def left(self):
		"""Left Move
		"""
		if self.is_well_formed():

			self.faces['LEFT_FACE'] = np.rot90(self.faces['LEFT_FACE'], 
											   axes=(1,0))
			
			temp = self.faces['DOWN_FACE'][:,0]
			self.faces['DOWN_FACE'][:,0] = self.faces['FRONT_FACE'][:,0]
			self.faces['FRONT_FACE'][:,0] = self.faces['UP_FACE'][:,0]
			self.faces['UP_FACE'][:,0] = self.faces['BACK_FACE'][:,2]
			self.faces['BACK_FACE'][:,2] = temp


	def left_inverse(self):
		"""Left Inverse Move
		"""
		if self.is_well_formed():

			self.faces['LEFT_FACE'] = np.rot90(self.faces['LEFT_FACE'])

			temp = self.faces['DOWN_FACE'][:,0]
			self.faces['DOWN_FACE'][:,0] = self.faces['BACK_FACE'][:,2]
			self.faces['BACK_FACE'][:,2] = self.faces['UP_FACE'][:,0]
			self.faces['UP_FACE'][:,0] = self.faces['FRONT_FACE'][:,0] 
			self.faces['FRONT_FACE'][:,0] = temp


	def right(self):
		"""Right Move
		"""
		if self.is_well_formed():

			self.faces['RIGHT_FACE'] = np.rot90(self.faces['RIGHT_FACE'], 
												axes=(1,0))

			temp = self.faces['UP_FACE'][:,2]
			self.faces['UP_FACE'][:,2] = self.faces['FRONT_FACE'][:,2]
			self.faces['FRONT_FACE'][:,2] = self.faces['DOWN_FACE'][:,2]
			self.faces['DOWN_FACE'][:,2] = self.faces['BACK_FACE'][:,0]
			self.faces['BACK_FACE'][:,0] = temp


	def right_inverse(self):
		"""Right Inverse Move
		"""
		if self.is_well_formed():

			self.faces['RIGHT_FACE'] = np.rot90(self.faces['RIGHT_FACE'])

			temp = self.faces['UP_FACE'][:,2]
			self.faces['UP_FACE'][:,2] = self.faces['BACK_FACE'][:,0]
			self.faces['BACK_FACE'][:,0] = self.faces['DOWN_FACE'][:,2]
			self.faces['DOWN_FACE'][:,2] = self.faces['FRONT_FACE'][:,2]
			self.faces['FRONT_FACE'][:,2] = temp


	#def middle(self):
	#	if self.is_well_formed():

	#def middle_inverse(self):
	#	if self.is_well_formed():

	#def equator(self):
	#	if self.is_well_formed():

	#def equator_inverse(self):
	#	if self.is_well_formed():

	#def standing(self):
	#	if self.is_well_formed():

	#def standing_inverse(self):
	#	if self.is_well_formed():

	#==========================================================================
	#		CONSTANTS FOR DEFAULT CUBE-COLORS
	#==========================================================================
	DEFAULT_UP_COLOR = '#ffffff'		# White
	DEFAULT_DOWN_COLOR = '#ffd500'		# Cyber Yellow
	DEFAULT_FRONT_COLOR = '#009b48'		# Green (Pigment)
	DEFAULT_BACK_COLOR = '#0045ad'		# Cobalt Blue
	DEFAULT_LEFT_COLOR = '#ff5900'		# Orange (Pantone)
	DEFAULT_RIGHT_COLOR = '#b90000'		# UE Red

	DEFAULT_FACE_COLORS = {
		'UP_COLOR' : DEFAULT_UP_COLOR,
		'DOWN_COLOR' : DEFAULT_DOWN_COLOR,
		'FRONT_COLOR' : DEFAULT_FRONT_COLOR,
		'BACK_COLOR' : DEFAULT_BACK_COLOR,
		'LEFT_COLOR' : DEFAULT_LEFT_COLOR,
		'RIGHT_COLOR' : DEFAULT_RIGHT_COLOR
	}

	DEFAULT_UP_FACE = np.full((3,3), DEFAULT_UP_COLOR)
	DEFAULT_DOWN_FACE = np.full((3,3), DEFAULT_DOWN_COLOR)
	DEFAULT_FRONT_FACE = np.full((3,3), DEFAULT_FRONT_COLOR)
	DEFAULT_BACK_FACE = np.full((3,3), DEFAULT_BACK_COLOR)
	DEFAULT_LEFT_FACE = np.full((3,3), DEFAULT_LEFT_COLOR)
	DEFAULT_RIGHT_FACE = np.full((3,3), DEFAULT_RIGHT_COLOR)

	DEFAULT_FACES = {
		'UP_FACE' : DEFAULT_UP_FACE,
		'DOWN_FACE' : DEFAULT_DOWN_FACE,
		'FRONT_FACE' : DEFAULT_FRONT_FACE,
		'BACK_FACE' : DEFAULT_BACK_FACE,
		'LEFT_FACE' : DEFAULT_LEFT_FACE,
		'RIGHT_FACE' : DEFAULT_RIGHT_FACE
	}

