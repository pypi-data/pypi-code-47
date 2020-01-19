#!usr/bin/env python3

import timeit
import numpy as np
from PIL import Image, ImageDraw
import pprint
import random
import pathlib
import io

###Waypoint 2:
class Sprite:
    """Represents a sprite with all characteristics."""

    def __init__(self, label, x1, y1, x2, y2):
        """
        This function (the constructor) takes 5 arguments and 
        be executed when the class Sprite is initiated.
        """

        # Data validation
        for arg in (label, x1, y1, x2, y2):
            if not isinstance(arg, int) or arg < 0:
                raise ValueError('Label and coordinates MUST be POSITIVE INTEGERS.')
        if x1 > x2 or y1 > y2:
            raise ValueError('Invalid coordinates.')

        self.__label = label
        self.__top_left = (x1, y1)
        self.__bottom_right = (x2, y2)
        self.__width = x2 - x1 + 1
        self.__height = y2 - y1 + 1
    
    @property
    def label(self):
        """
        Returns the attribute label
        """
        return self.__label
    
    @property
    def top_left(self):
        """
        Returns the attribute top_left
        """
        return self.__top_left

    @property
    def bottom_right(self):
        """
        Returns the attribute bottom_right
        """
        return self.__bottom_right
    
    @property
    def width(self):
        """
        Returns the attribute width
        """
        return self.__width
    
    @property
    def height(self):
        """
        Returns the attribute height
        """
        return self.__height


###Waypoint 5:
class SpriteSheet:
    """Represents a sheet with its sprites."""

    def __init__(self, fd, background_color=None):
        """
        This function (the constructor) takes 2 arguments and 
        be executed when the class SpriteSheet is initiated.

        :param fd: a string represents the path of image file,
                   a pathlib.Path object,
                   a file object that MUST implement read(), seek(), and tell() methods,
                   an Image object.

        :param background_color: the color of the background depending on the image mode
        """
        
        # Check the type of the argument fd
        if isinstance(fd, Image.Image):
            self.__image = fd
        elif isinstance(fd, pathlib.Path):
            self.__image = Image.open(pathlib.Path(fd))
        elif isinstance(fd, str) or isinstance(fd, io.BufferedIOBase):
            self.__image = Image.open(fd)
        else:
            raise TypeError('Please provide the valid argument of fd.')

        self.__image_mode = self.__image.mode
        
        # Data validation for the background color
        if not background_color:
            background_color = self.find_most_common_color(self.__image)
        else:
            if self.__image_mode == 'L' or self.__image_mode == 'P':
                if not isinstance(background_color, int):
                    raise ValueError('Sorry, for grayscale the background color MUST be an INTEGER.')
            elif self.__image_mode == 'RGB' or self.__image_mode == 'RGBA':
                if not isinstance(background_color, tuple):
                    raise ValueError('Sorry, for RGB format the background color MUST be a TUPLE.')
                else:
                    if 3 <= len(background_color) <= 4:
                        for bit in background_color:
                            if bit < 0:
                                raise ValueError('Sorry, for RGB or RGBA format the background color MUST be a TUPLE of 3 or 4 positive INTEGERS.')
                    else:
                        raise ValueError('Sorry, for RGB or RGBA format the background color MUST be a TUPLE of 3 or 4 positive INTEGERS.')
            else:
                raise ValueError('Sorry, please enter the right format of the image.')
        
        self.__background_color = background_color
        
        # Get the sprites and label, create private attributes.
        sprites, label_map = self.find_sprites()
        self.__sprites = sprites
        self.__label_map = label_map

    @staticmethod
    def find_most_common_color(image):
        """This function takes 1 argument,
        and returns the most used color of the sheet.

        :param image: the Image object.

        :return: the most used color of the Image object.
        """

        try:
            # Get the mode and size of the image object
            width, height = image.size

            # Get the pixels
            pixels = image.getcolors(maxcolors=width*height)
            
            # Find the most used color
            pixels = sorted(pixels, key=lambda x: x[0], reverse=True)
            return pixels[0][1]

        except Exception as e:
            print(e)

    @property
    def background_color(self):
        """Returns the background color of the sheet."""       
        return self.__background_color

    @staticmethod
    def __get_label_sprites(labels_list, x, y, label, threshold=8):
        """
        This function takes 5 arguments, gets a label for the chosen pixel,
        and return output (the label for that pixel), label (the incremented label).

        :param labels_list: a 2-D array of integers.

        :param x, y: the location of the pixel in the image.

        :param label: the starting label (1).

        :param threshold: define the range of connectivity, default is 8.

        :return: output (the label for that pixel), label (the incremented label).
        """

        if threshold == 8:
            try:
                if labels_list[y - 1][x - 1] == 0:
                    if labels_list[y - 1][x] == 0:
                        if labels_list[y - 1][x + 1] == 0:
                            if labels_list[y][x - 1] == 0:
                                output = label
                                label += 1
                            else:
                                output = labels_list[y][x - 1]
                        else:
                            output = labels_list[y - 1][x + 1]
                    else:
                        output = labels_list[y - 1][x]
                else:
                    output = labels_list[y - 1][x - 1]
            except IndexError:
                output = label
        
        return output, label

    @staticmethod
    def __create_aux_equivalent_table(labels_list):
        """
        This function takes 1 argument and returns the dictionary of labels.

        :param labels_list: a 2-D array of integers represents the label map.

        :return: the dictionary of labels with their neighbor labels.
        """
        # Label Dictionary
        label_dict = {}

        for i in range(len(labels_list)):
            for j in range(len(labels_list[i])):
                current_pixel = labels_list[i][j]
                if current_pixel == 0:
                    continue
                else:
                    try:
                        label_dict.setdefault(current_pixel, []).append(current_pixel)
                        try:
                            if labels_list[i][j - 1] != 0:
                                if not labels_list[i][j - 1] in label_dict[current_pixel]:
                                    label_dict.setdefault(current_pixel, []).append(labels_list[i][j - 1])
                        except KeyError:
                            label_dict.setdefault(current_pixel, []).append(labels_list[i][j - 1])
                        
                        try:
                            if labels_list[i - 1][j - 1] != 0:
                                if not labels_list[i - 1][j - 1] in label_dict[current_pixel]:
                                    label_dict.setdefault(current_pixel, []).append(labels_list[i - 1][j - 1])
                        except KeyError:
                            label_dict.setdefault(current_pixel, []).append(labels_list[i - 1][j - 1])
                        
                        try:
                            if labels_list[i - 1][j] != 0:
                                if not labels_list[i - 1][j] in label_dict[current_pixel]:
                                    label_dict.setdefault(current_pixel, []).append(labels_list[i - 1][j])
                        except KeyError:
                            label_dict.setdefault(current_pixel, []).append(labels_list[i - 1][j])
                        
                        try:
                            if labels_list[i - 1][j + 1] != 0:
                                if not labels_list[i - 1][j + 1] in label_dict[current_pixel]:
                                    label_dict.setdefault(current_pixel, []).append(labels_list[i - 1][j + 1])
                        except KeyError:
                            label_dict.setdefault(current_pixel, []).append(labels_list[i - 1][j + 1])
                        
                    except IndexError:
                        continue
        return label_dict

    @staticmethod
    def __create_table_of_equivalent(label_dict):
        """
        This function takes 1 argument and return the reduced dictionary of labels.

        :param label_dict: the dictionary of labels with their neighbor labels.

        :return: the dictionary of labels with all of their neighbor labels.
        """

        sorted_label_dict = {k: label_dict[k] for k in sorted(label_dict, reverse=True)}
        # print(sorted_label_dict)
        for key, values in sorted_label_dict.items():
            min_label = min(sorted_label_dict[key])
            for value in values:
                if not min_label in sorted_label_dict[value]:
                    sorted_label_dict[value].append(min_label)
                else:
                    continue
        
        for key, values in sorted_label_dict.items():
            min_label = min(sorted_label_dict[key])
            if min_label < key:
                sorted_label_dict[min_label].extend(sorted_label_dict[key])
                sorted_label_dict[min_label] = list(set(sorted_label_dict[min_label]))
                sorted_label_dict[key] = []
        sorted_label_dict = {k: v for k, v in sorted_label_dict.items() if len(sorted_label_dict[k]) > 0}
        return sorted_label_dict

    @staticmethod
    def __find_coordinates_and_create_sprite_object(equi_dict, labels_array):
        """
        This function takes 2 arguments, find the coordinates of a sprite,
        create Sprite objects and returns a dictionary of Sprite objects with its label.

        :param equi_dict: The dictionary of labels with all of their neighbor labels.

        :param labels_array: a 2-D array of integers represents the label map.

        :return: a dictionary of Sprite objects with its label.
        """
        height, width = labels_array.shape
        sprites_infor = {}

        for key in equi_dict.keys():
            # Find the index of labels
            label_index = np.where(labels_array == key)
            list_of_label_index = list(zip(label_index[0], label_index[1]))
            sprites_infor.setdefault(key, []).append([width, height, 0, 0])
            for index in list_of_label_index:
                # Find the top_left coordinate
                if index[0] < sprites_infor[key][0][1]:
                    sprites_infor[key][0][1] = index[0]

                if index[1] < sprites_infor[key][0][0]:
                    sprites_infor[key][0][0] = index[1]

                # Find the bottom_right coordinate
                if index[0] > sprites_infor[key][0][3]:
                    sprites_infor[key][0][3] = index[0]

                if index[1] > sprites_infor[key][0][2]:
                    sprites_infor[key][0][2] = index[1]

            sprites_infor[key] =  Sprite(key, 
                                        int(sprites_infor[key][0][0]), 
                                        int(sprites_infor[key][0][1]), 
                                        int(sprites_infor[key][0][2]), 
                                        int(sprites_infor[key][0][3]))
        return sprites_infor

    def find_sprites(self):
        """
        This function takes 1 argument,
        and returns  a tuple (sprites, label_map) with:

        + sprites: a dictionary with the key is the label and value is the Sprite object
        + label_map: A 2D array of integers of equal dimension with 1 means the pixel belongs to the sprite
        and 0 means the pixel does not.

        :param image: an Image object.

        :return: a tuple (sprites, label_map).
        """
     
        # Get the mode and size of the image object
        width, height = self.__image.size

        # Create a 2D array of 0 integers
        labels_list = [[0] * (width) for i in range(height)]

        # Load the pixel data     
        pixel_data = self.__image.load()

        # Label the sheet
        label = 1
        label_dict = {}
        for y in range(height):
            for x in range(width):
                current_pixel = pixel_data[x, y]
                if current_pixel == self.__background_color:
                    continue
                else:
                    pixel_label, incremented_label = self.__get_label_sprites(labels_list, x, y, label)
                    labels_list[y][x] = pixel_label
                    label = incremented_label

        # Create a label dictionary
        label_dict = self.__create_aux_equivalent_table(labels_list)

        # Create the equivalent table as a dictionary
        equi_dict = self.__create_table_of_equivalent(label_dict)

        # Relabel all the sprites
        labels_array = np.array(labels_list, dtype=np.int16)
        for label in equi_dict.keys():
            for lab in equi_dict[label]:
                labels_array = np.where(labels_array == lab, label, labels_array)

        # Create sprites objects
        sprites = self.__find_coordinates_and_create_sprite_object(equi_dict, labels_array)

        return sprites, labels_array
    @staticmethod
    def __create_pixel_color_from_mode(image_mode):
        """
        This function takes 1 argument
        and returns the color of a pixel depending on the image mode

        :param image_mode: the mode of the image.

        :return: the color of a pixel.
        """

        if image_mode == 'L' or image_mode == 'P':
            return random.randrange(256)
        if image_mode == 'RGB':
            return random.randrange(256), random.randrange(256), random.randrange(256)
        if image_mode == 'RGBA':
            return random.randrange(256), random.randrange(256), random.randrange(256), random.randint(130, 255)


    def create_sprite_labels_image(self):
        """
        This function draws the masks (with different colors) of the sprites,
        draws a bounding box of each sprite (with the same color of the mask),
        and returns an image that contains all the masks.
        
        :return: an image that contains all the masks.
        """
                
        # Get the image size from the label_map, create an image with backfground color       
        height, width = self.__label_map.shape
        image = Image.new(self.__image_mode, (width, height), color = self.__background_color)

        for label in self.__sprites:
            # Create a random color
            mask_color = self.__create_pixel_color_from_mode(self.__image_mode)

            # Get the list of label index
            label_index = np.where(self.__label_map == label)
            list_of_index = list(zip(label_index[1], label_index[0]))

            # Draw the mask
            image_draw = ImageDraw.Draw(image)
            image_draw.point(list_of_index, fill=mask_color)

            # Draw the bounding box
            coordinates = [self.__sprites[label].top_left, self.__sprites[label].bottom_right]
            image_draw.rectangle(coordinates, outline=mask_color, width=1)
        return image 
  
