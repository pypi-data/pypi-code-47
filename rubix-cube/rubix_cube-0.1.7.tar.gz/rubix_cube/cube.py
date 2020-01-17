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

    *   :class:`Rubix Cube <Cube>` class that is capable of being parameterized
        with a custom set of 6 unique colors (`Default Color Scheme 
        <https://www.schemecolor.com/rubik-cube-colors.php>`_) and can invoke
        the following moves.

        .. figure:: ./../../misc/cube_moves.png
           :name: cube_moves
           :align: center
           :scale: 75%

           6 cube face rotations both clock-wise and 
           counter-clockwise (inverse) are considered to be the standard 
           move-set. (`How to Solve 
           <https://www.rubiks.com/en-us/blog/how-to-solve-the-rubiks-cube-stage-1>`_
           )

        .. todo::
           
           *    Need to finish implementing the ``get_num_solved_rings``.
           *    Need to finish implementing the ``are_equivalent_cubes``.


        .. figure:: ./../../misc/flattened_cube.png
           :name: flattened_cube
           :align: center
           :scale: 45%

           At this view of the cube, each face is a 3x3 array indexed with 
           [0,0] in the top-left and [2,2] in the bottom right. (`Flattened
           <https://rantonse.no/en/blog/2016-05-12>`_)

.. moduleauthor:: David Grethlein <djg329@drexel.edu>

"""

import os
import sys
import json
import copy

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
    #       CLASS CONSTRUCTOR
    #==========================================================================
    def __init__(self,
                 colors : Dict[str,str] = None,
                 faces : Dict[str,np.array] = None):
        """:class:`Cube` class constructor.

        Args:
            colors (Dict[str,str], optional): Dictionary of color HEX strings.
                Default value is ``None`` which will create a cube with default
                colors :attr:`DEFAULT_FACE_COLORS`. 

                .. code-block:: 
                   :name: init_colors_keys
                   :linenos:
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
                   :linenos:
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

        """

        # Sets private attributes via properties
        self.colors = Cube.DEFAULT_FACE_COLORS
        self.faces = Cube.DEFAULT_FACES 
        
        if isinstance(colors, dict):
            self.colors = colors

            if isinstance(faces, dict):
                self.faces = faces          


    #==========================================================================
    #      OVERLOADED OPERATOR(s)
    #==========================================================================
    def __eq__(self, other) -> bool:
        """Tests if the :class:`Rubix Cube <rubix_cube.cube.Cube>` faces are
        exactly identical between the two objects.
        
        Args:
            other (TYPE): Description
        
        Returns:
            bool: Description
        
        """
        if self.is_well_formed()\
        and isinstance(other , self.__class__)\
        and other.is_well_formed():

            for face , other_face in zip(self.faces , other.faces):
                if not np.array_equal(self.faces[face],other.faces[other_face]):
                    return False

            return True

        else:
            return False


    def __ne__(self, other) -> bool:
        """Tests if the :class:`Rubix Cube <rubix_cube.cube.Cube>` faces are
        ``NOT`` exactly identical between the two objects.
        
        Args:
            other (TYPE): Description
        
        Returns:
            bool: Description
        
        """
        return not (self == other)


    def __mod__(self, other) -> bool:
        """Tests if the :class:`Rubix Cube <rubix_cube.cube.Cube>` faces are
        exactly identical between the two objects after re-orientation. 
        Essentially are the cubes identical after rotation?
        
        Args:
            other (TYPE): Description

        Returns:
            bool: 
        
        """
        return self.is_equivalent_to(other)


    def is_equivalent_to(self, other) -> bool:
        """
        
        Args:
            other (TYPE): Description

        Returns:
            bool: 

        """
        if self.is_well_formed()\
        and isinstance(other , self.__class__)\
        and other.is_well_formed():
        
            other_test_seqs = [[Cube.rotate_roll,
                                Cube.rotate_roll,
                                Cube.rotate_roll],
                               [Cube.rotate_yaw,
                                Cube.rotate_roll,
                                Cube.rotate_roll,
                                Cube.rotate_roll],
                               [Cube.rotate_yaw,
                                Cube.rotate_yaw,
                                Cube.rotate_roll,
                                Cube.rotate_roll,
                                Cube.rotate_roll],
                               [Cube.rotate_yaw_inverse,
                                Cube.rotate_roll,
                                Cube.rotate_roll,
                                Cube.rotate_roll],
                               [Cube.rotate_pitch,
                                Cube.rotate_roll,
                                Cube.rotate_roll,
                                Cube.rotate_roll],
                               [Cube.rotate_pitch_inverse,
                                Cube.rotate_roll,
                                Cube.rotate_roll,
                                Cube.rotate_roll]]

            # Tests if exact match
            if self.__eq__(other):
                return True

            # Tests the 24 sequences of re-orientations for exact matches
            for seq in other_test_seqs:

                # Makes a local copy to manipulate
                l_other = copy.deepcopy(other)

                # Performs each move
                for mv in seq:
                    mv(l_other)

                    # Tests for exact match
                    if self.__eq__(l_other):
                        return True

        return False

    #==========================================================================
    #       PROPERTY INTERFACE(s)
    #==========================================================================
    @property
    def colors(self):
        """Can only be set to be a dictionary with 6 unique color string values
        that all return ``True`` when examined by 
        :func:`matplotlib.colors.is_color_like`. 

        .. code-block::
           :name: colors_keys
           :linenos:
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
           :linenos:
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
    #       QUALITY ASSURANCE METHOD(s)
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
        required_keys = ['UP_FACE',
                         'DOWN_FACE',
                         'FRONT_FACE',
                         'BACK_FACE',
                         'LEFT_FACE',
                         'RIGHT_FACE']

        try:
            return all([self.is_valid_face(self.faces[face]) 
                        for face in required_keys])

        except KeyError:
            return False


    def is_valid_face(self, face : np.ndarray) -> bool:
        """Checks if the provided array could be a valid face on the 
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
        and all([all([val in self.colors.values() 
                        for val in row])
                            for row in face]):

            return True

        else:

            return False


    def is_solved_face(self, face: np.ndarray) -> bool:
        """Checks if the provided array could be a valid face on the 
        currently initialized :class:`Cube`.

        Args:
            face (np.ndarray): Array to be tested for being solved in the
                context of the current :class:`Cube`.

        Returns:
            ``True`` if faces is solved 3 x 3 array of valid colors as defined
            by current instance's :attr:`colors` attribute, ``False``
            otherwise.

        .. code-block::
           :name: is_solved_face
           :linenos:
           :caption: A solved ``face`` returns ``True`` when examined by 
                :func:`is_valid_face` and only contains 1 unique value.

            return len(np.unique(face) == 1)
        
        """
        if not self.is_valid_face(face):
            return False
        
        else:
            return len(np.unique(face)) == 1


    def get_num_solved_faces(self) -> int:
        """Counts the number of solved faces by examining each one using
        :func:`is_solved_face` if the currently initialized :class:`Cube`
        :func:`is_well_formed`, 0 otherwise.

        Returns:
            int: **num_faces_solved** - The number of solved faces on the 
            currently initialized :class:`Cube`.

        """

        num_faces_solved = 0

        if self.is_well_formed():

            for face in self.faces:
                if self.is_solved_face(self.faces[faces]):
                    num_faces_solved += 1

        return num_faces_solved


    #==========================================================================
    #       MOVE METHOD(s)
    #==========================================================================
    def move_up(self):
        """Up Move
        """
        if self.is_well_formed():

            self.faces['UP_FACE'] = np.rot90(self.faces['UP_FACE'], 
                                             axes=(1,0))

            temp = self.faces['BACK_FACE'][0,:].copy()

            self.faces['BACK_FACE'][0,:] = self.faces['LEFT_FACE'][0,:]
            self.faces['LEFT_FACE'][0,:] = self.faces['FRONT_FACE'][0,:]
            self.faces['FRONT_FACE'][0,:] = self.faces['RIGHT_FACE'][0,:]

            self.faces['RIGHT_FACE'][0,:] = temp


    def move_up_inverse(self):
        """Up Inverse Move
        """
        if self.is_well_formed():

            self.faces['UP_FACE'] = np.rot90(self.faces['UP_FACE'])

            temp = self.faces['BACK_FACE'][0,:].copy()
            self.faces['BACK_FACE'][0,:] = self.faces['RIGHT_FACE'][0,:]
            self.faces['RIGHT_FACE'][0,:] = self.faces['FRONT_FACE'][0,:]
            self.faces['FRONT_FACE'][0,:] = self.faces['LEFT_FACE'][0,:]
            self.faces['LEFT_FACE'][0,:] = temp


    def move_down(self):
        """Down Move
        """
        if self.is_well_formed():

            self.faces['DOWN_FACE'] = np.rot90(self.faces['DOWN_FACE'])

            temp = self.faces['FRONT_FACE'][2,:].copy()
            self.faces['FRONT_FACE'][2,:] = self.faces['LEFT_FACE'][2,:]
            self.faces['LEFT_FACE'][2,:] = self.faces['BACK_FACE'][2,:]
            self.faces['BACK_FACE'][2,:] = self.faces['RIGHT_FACE'][2,:]
            self.faces['RIGHT_FACE'][2,:] = temp


    def move_down_inverse(self):
        """Down Inverse Move
        """
        if self.is_well_formed():

            self.faces['DOWN_FACE'] = np.rot90(self.faces['DOWN_FACE'], 
                                               axes=(1,0))

            temp = self.faces['FRONT_FACE'][2,:].copy()
            self.faces['FRONT_FACE'][2,:] = self.faces['RIGHT_FACE'][2,:]
            self.faces['RIGHT_FACE'][2,:] = self.faces['BACK_FACE'][2,:]
            self.faces['BACK_FACE'][2,:] = self.faces['LEFT_FACE'][2,:]
            self.faces['LEFT_FACE'][2,:] = temp


    def move_front(self):
        """Front Move
        """
        if self.is_well_formed():

            self.faces['FRONT_FACE'] = np.rot90(self.faces['FRONT_FACE'], 
                                                axes=(1,0))

            temp = self.faces['UP_FACE'][2,:].copy()
            self.faces['UP_FACE'][2,:] = np.flip(self.faces['LEFT_FACE'][:,2])
            self.faces['LEFT_FACE'][:,2] = self.faces['DOWN_FACE'][0,:]
            self.faces['DOWN_FACE'][0,:] = np.flip(self.faces['RIGHT_FACE'][:,0])
            self.faces['RIGHT_FACE'][:,0] = temp


    def move_front_inverse(self):
        """Front Inverse Move
        """
        if self.is_well_formed():

            self.faces['FRONT_FACE'] = np.rot90(self.faces['FRONT_FACE'])

            temp = self.faces['UP_FACE'][2,:].copy()
            self.faces['UP_FACE'][2,:] = self.faces['RIGHT_FACE'][:,0]
            self.faces['RIGHT_FACE'][:,0] = np.flip(self.faces['DOWN_FACE'][0,:])
            self.faces['DOWN_FACE'][0,:] = self.faces['LEFT_FACE'][:,2]
            self.faces['LEFT_FACE'][:,2] = np.flip(temp)


    def move_back(self):
        """Back Move
        """
        if self.is_well_formed():

            self.faces['BACK_FACE'] = np.rot90(self.faces['BACK_FACE'])

            temp = self.faces['DOWN_FACE'][2,:].copy()
            self.faces['DOWN_FACE'][2,:] = self.faces['LEFT_FACE'][:,0]
            self.faces['LEFT_FACE'][:,0] = np.flip(self.faces['UP_FACE'][0,:])
            self.faces['UP_FACE'][0,:] = self.faces['RIGHT_FACE'][:,2]
            self.faces['RIGHT_FACE'][:,2] = np.flip(temp)


    def move_back_inverse(self):
        """Back Inverse Move
        """
        if self.is_well_formed():

            self.faces['BACK_FACE'] = np.rot90(self.faces['BACK_FACE'], 
                                               axes=(1,0))

            temp = self.faces['DOWN_FACE'][2,:].copy()
            self.faces['DOWN_FACE'][2,:] = self.faces['RIGHT_FACE'][:,2]
            self.faces['RIGHT_FACE'][:,2] = self.faces['UP_FACE'][0,:]
            self.faces['UP_FACE'][0,:] = self.faces['LEFT_FACE'][:,0]
            self.faces['LEFT_FACE'][:,0] = temp


    def move_left(self):
        """Left Move
        """
        if self.is_well_formed():

            self.faces['LEFT_FACE'] = np.rot90(self.faces['LEFT_FACE'], 
                                               axes=(1,0))
            
            temp = self.faces['DOWN_FACE'][:,0].copy()
            self.faces['DOWN_FACE'][:,0] = self.faces['FRONT_FACE'][:,0]
            self.faces['FRONT_FACE'][:,0] = self.faces['UP_FACE'][:,0]
            self.faces['UP_FACE'][:,0] = np.flip(self.faces['BACK_FACE'][:,2])
            self.faces['BACK_FACE'][:,2] = np.flip(temp)


    def move_left_inverse(self):
        """Left Inverse Move
        """
        if self.is_well_formed():

            self.faces['LEFT_FACE'] = np.rot90(self.faces['LEFT_FACE'])

            temp = self.faces['DOWN_FACE'][:,0].copy()
            self.faces['DOWN_FACE'][:,0] = np.flip(self.faces['BACK_FACE'][:,2])
            self.faces['BACK_FACE'][:,2] = np.flip(self.faces['UP_FACE'][:,0])
            self.faces['UP_FACE'][:,0] = self.faces['FRONT_FACE'][:,0] 
            self.faces['FRONT_FACE'][:,0] = temp


    def move_right(self):
        """Right Move
        """
        if self.is_well_formed():

            self.faces['RIGHT_FACE'] = np.rot90(self.faces['RIGHT_FACE'], 
                                                axes=(1,0))

            temp = self.faces['UP_FACE'][:,2].copy()
            self.faces['UP_FACE'][:,2] = self.faces['FRONT_FACE'][:,2]
            self.faces['FRONT_FACE'][:,2] = self.faces['DOWN_FACE'][:,2]
            self.faces['DOWN_FACE'][:,2] = np.flip(self.faces['BACK_FACE'][:,0])
            self.faces['BACK_FACE'][:,0] = np.flip(temp)


    def move_right_inverse(self):
        """Right Inverse Move
        """
        if self.is_well_formed():

            self.faces['RIGHT_FACE'] = np.rot90(self.faces['RIGHT_FACE'])

            temp = self.faces['UP_FACE'][:,2].copy()
            self.faces['UP_FACE'][:,2] = np.flip(self.faces['BACK_FACE'][:,0])
            self.faces['BACK_FACE'][:,0] = np.flip(self.faces['DOWN_FACE'][:,2])
            self.faces['DOWN_FACE'][:,2] = self.faces['FRONT_FACE'][:,2]
            self.faces['FRONT_FACE'][:,2] = temp


    def move_middle(self):
        """Middle Slice Move
        """
        if self.is_well_formed():

            temp = self.faces['DOWN_FACE'][:,1].copy()
            self.faces['DOWN_FACE'][:,1] = self.faces['FRONT_FACE'][:,1]
            self.faces['FRONT_FACE'][:,1] = self.faces['UP_FACE'][:,1]
            self.faces['UP_FACE'][:,1] = np.flip(self.faces['BACK_FACE'][:,1])
            self.faces['BACK_FACE'][:,1] = np.flip(temp)


    def move_middle_inverse(self):
        """Middle Slice Inverse Move
        """
        if self.is_well_formed():

            temp = self.faces['DOWN_FACE'][:,1].copy()
            self.faces['DOWN_FACE'][:,1] = np.flip(self.faces['BACK_FACE'][:,1])
            self.faces['BACK_FACE'][:,1] = np.flip(self.faces['UP_FACE'][:,1])
            self.faces['UP_FACE'][:,1] = self.faces['FRONT_FACE'][:,1] 
            self.faces['FRONT_FACE'][:,1] = temp


    def move_equator(self):
        """Equator Slice Move
        """
        if self.is_well_formed():

            temp = self.faces['FRONT_FACE'][1,:].copy()
            self.faces['FRONT_FACE'][1,:] = self.faces['LEFT_FACE'][1,:]
            self.faces['LEFT_FACE'][1,:] = self.faces['BACK_FACE'][1,:]
            self.faces['BACK_FACE'][1,:] = self.faces['RIGHT_FACE'][1,:]
            self.faces['RIGHT_FACE'][1,:] = temp


    def move_equator_inverse(self):
        """Equator Slice Inverse Move
        """
        if self.is_well_formed():

            temp = self.faces['FRONT_FACE'][1,:].copy()
            self.faces['FRONT_FACE'][1,:] = self.faces['RIGHT_FACE'][1,:]
            self.faces['RIGHT_FACE'][1,:] = self.faces['BACK_FACE'][1,:]
            self.faces['BACK_FACE'][1,:] = self.faces['LEFT_FACE'][1,:]
            self.faces['LEFT_FACE'][1,:] = temp


    def move_standing(self):
        """Standing Slice Move
        """
        if self.is_well_formed():

            temp = self.faces['UP_FACE'][1,:].copy()
            self.faces['UP_FACE'][1,:] = np.flip(self.faces['LEFT_FACE'][:,1])
            self.faces['LEFT_FACE'][:,1] = self.faces['DOWN_FACE'][1,:]
            self.faces['DOWN_FACE'][1,:] = np.flip(self.faces['RIGHT_FACE'][:,1])
            self.faces['RIGHT_FACE'][:,1] = temp


    def move_standing_inverse(self):
        """Standing Slice Inverse Move
        """
        if self.is_well_formed():

            temp = self.faces['UP_FACE'][1,:].copy()
            self.faces['UP_FACE'][1,:] = self.faces['RIGHT_FACE'][:,1]
            self.faces['RIGHT_FACE'][:,1] = np.flip(self.faces['DOWN_FACE'][1,:])
            self.faces['DOWN_FACE'][1,:] = self.faces['LEFT_FACE'][:,1]
            self.faces['LEFT_FACE'][:,1] = np.flip(temp)


    def rotate_pitch(self):
        """Pitch Rotation
        """
        if self.is_well_formed():

            self.move_left_inverse()
            self.move_middle_inverse()
            self.move_right()


    def rotate_pitch_inverse(self):
        """Pitch Inverse Rotation
        """
        if self.is_well_formed():

            self.move_left()
            self.move_middle()
            self.move_right_inverse()


    def rotate_roll(self):
        """Roll Rotation
        """
        if self.is_well_formed():

            self.move_front()
            self.move_standing()
            self.move_back_inverse()


    def rotate_roll_inverse(self):
        """Roll Inverse Rotation
        """
        if self.is_well_formed():

            self.move_front_inverse()
            self.move_standing_inverse()
            self.move_back()


    def rotate_yaw(self):
        """Yaw Rotation
        """
        if self.is_well_formed():

            self.move_up()
            self.move_equator_inverse()
            self.move_down_inverse()


    def rotate_yaw_inverse(self):
        """Yaw Inverse Rotation
        """
        if self.is_well_formed():

            self.move_up_inverse()
            self.move_equator()
            self.move_down()

    #==========================================================================
    #       CONSTANTS FOR DEFAULT CUBE-COLORS
    #==========================================================================
    DEFAULT_UP_COLOR = '#ffffff'        # White
    DEFAULT_DOWN_COLOR = '#ffd500'      # Cyber Yellow
    DEFAULT_FRONT_COLOR = '#009b48'     # Green (Pigment)
    DEFAULT_BACK_COLOR = '#0045ad'      # Cobalt Blue
    DEFAULT_LEFT_COLOR = '#ff5900'      # Orange (Pantone)
    DEFAULT_RIGHT_COLOR = '#b90000'     # UE Red

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

