import imghdr
import io
import numpy
import pathlib
import random
import sys
from PIL import Image, PngImagePlugin, ImageDraw


def _assign_label(selected_area, heigth, width, coordinate_y, coordinate_x, current_label, is_reduce=False):

    nearest_points = [
        (coordinate_x - 1, coordinate_y - 1),
        (coordinate_x, coordinate_y - 1),
        (coordinate_x + 1, coordinate_y - 1),
        (coordinate_x - 1, coordinate_y)
    ]

    current_point_label = selected_area[coordinate_y, coordinate_x]
    list_nearest_label = []

    for point in nearest_points:
        # skil useless point
        if point[0] < 0 or point[0] >= width or point[1] < 0 or point[1] >= heigth:
            continue

        label = selected_area[point[1], point[0]]

        # skip background
        if label == 0:
            continue

        # reduce number of label mode
        if is_reduce:
            # skip same label
            if label != current_point_label and label not in list_nearest_label:
                list_nearest_label.append(label)
            continue

        return label, current_label

    if is_reduce:
        return min(list_nearest_label) if list_nearest_label else []

    return current_label + 1, current_label + 1


def _get_random_color(background_color):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb = (r, g, b) if len(background_color) == 3 else (r, g, b, 255)

    return rgb if rgb != background_color else _get_random_color(background_color)


# waypoint1
def find_most_common_color(image):
    """
    Arguments:
        image {Image.Image} -- a Image object

    Raises:
        TypeError: if argument is not a Image object

    Returns:
        int -- when image mode is grayscale
        tuple of integer -- when image mode is RGB or RGBA
    """
    if not isinstance(image, Image.Image):
        raise TypeError("argument 'image' must be a Imange object")

    color_dict = {}
    width, height = image.size
    result = None

    if width >= 1000 or height >= 1000:
        width = width // 10
        height = height // 10
    else:
        width = width // 2
        height = height // 2

    image = image.resize((width, height))
    pixel = image.load()

    for i in range(width):
        # find all pixel color of image
        for j in range(height):
            if pixel[i, j] not in color_dict:
                color_dict[pixel[i, j]] = 1
            else:
                color_dict[pixel[i, j]] += 1

            # find the pixel color most use
            if not result or color_dict[result] < color_dict[pixel[i, j]]:
                result = pixel[i, j]

    return result


# waypoint2
class Sprite:
    def __init__(self, label, x1, y1, x2, y2):
        """
        Arguments:
            label {int} -- the value of labe of coordinates
            x1 {int} -- x coordinates of top_left
            y1 {int} -- y coordinates of top_left
            x2 {int} -- x coordinates of bottom_right
            y2 {int} -- y coordinates of bottom_right

        Raises:
            ValueError: if one or more arguments label, x1, y1, x2, and y2 is not positive integer,
                        or if the arguments x2 and y2 is not equal or greater respectively than x1 and y1.
        """
        attributes = [label, x1, x2, y1, y2]

        if any([not isinstance(x, int) for x in attributes]) or \
                any([x < 0 for x in attributes]) or x2 < x1 or y2 < y1:
            raise ValueError("Invalid coordinates")

        self.__label = label
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__width = self.__x2 - self.__x1 + 1
        self.__height = self.__y2 - self.__y1 + 1

    @property
    def label(self):
        return self.__label

    @property
    def top_left(self):
        return (self.__x1, self.__y1)

    @property
    def bottom_right(self):
        return (self.__x2, self.__y2)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height


# waypoint3
def find_sprites(image, background_color=None):
    """
    Arguments:
        image {Image.Image} -- an Image object

    Keyword Arguments:
        background_color {tuple or int} -- color of background of image (default: {None})

    Raises:
        TypeError: when background_color is not a tuple or int
                   when image is not an Image object

    Returns:
        dict -- a dict of sprite of image
        2D-list -- a label map of image
    """
    if not isinstance(image, Image.Image):
        raise TypeError("argument 'image' must be a Imange object")

    if background_color:
        if image.mode == 'RGB' and not isinstance(background_color, tuple)\
                and len(background_color) != 3:
            raise TypeError("Invalid background color")

        if image.mode == 'RGBA' and not isinstance(background_color, tuple)\
                and len(background_color) != 4:
            raise TypeError("Invalid background color")

        if image.mode == 'L' and not isinstance(background_color, int):
            raise TypeError("Invalid background color")

    # set background color
    if not background_color:
        background_color = find_most_common_color(image)

    width, heigth = image.size
    pixel = image.load()
    selected_area = numpy.zeros((heigth, width), dtype=int)
    current_label = 0
    label_dict = {}

    for j in range(heigth):
        for i in range(width):
            pixel_color = pixel[i, j]

            # skip pixels which are background
            if pixel_color == background_color:
                continue

            if image.mode == 'RGBA' and pixel_color[3] == 0:
                continue

            selected_area[j][i], current_label = _assign_label(
                selected_area, heigth, width, j, i, current_label)

            label_dict.setdefault(selected_area[j][i], [])

    # find equivalent label
    for j in range(heigth):
        i = 0 if j % 2 == 0 else (width - 1)
        while i >= 0 and i < width:

            # skip background and label 1
            if selected_area[j][i] == 0 or selected_area[j][i] == 1:
                i = (i + 1) if j % 2 == 0 else (i - 1)
                continue

            nearest_lowest_label = _assign_label(
                selected_area, heigth, width, j, i, current_label, is_reduce=True)

            if not nearest_lowest_label or nearest_lowest_label in label_dict[selected_area[j][i]]:
                i = (i + 1) if j % 2 == 0 else (i - 1)
                continue

            label_dict[selected_area[j][i]].append(nearest_lowest_label)

            i = (i + 1) if j % 2 == 0 else (i - 1)

    list_label = list(label_dict.keys())
    list_label.reverse()

    # define group table
    for label in list_label:
        # skip not equivalent label
        if not label_dict[label]:
            continue

        min_equivalent_label = min(label_dict[label])

        # no smaller equivalent label
        if min_equivalent_label >= label:
            continue

        for other_label in label_dict[label]:
            # except min equivalent label, skip label than larger than current label
            if other_label == min_equivalent_label or other_label >= label:
                continue

            label_dict[other_label] += [min_equivalent_label]

        for other_label in label_dict:
            if other_label >= label:
                break

            if label in label_dict[other_label]:
                label_dict[other_label] += [min_equivalent_label]

        label_dict[label].remove(min_equivalent_label)
        label_dict[min_equivalent_label] += [label] + label_dict[label]

        label_dict[label] = []

    # remove duplicate
    for label in label_dict:
        label_dict[label] = list(dict.fromkeys(label_dict[label]))

    # replace label with min equivalent label
    for label, values in label_dict.items():
        if not values:
            continue

        for value in values:
            selected_area[selected_area == value] = label

    sprite_dict = {}

    # define locate of each sprite
    for j in range(heigth):
        for i in range(width):
            cur_label = selected_area[j][i]

            if cur_label == 0:
                continue

            sprite_dict.setdefault(cur_label, [width, heigth, 0, 0])

            if i < sprite_dict[cur_label][0]:
                sprite_dict[cur_label][0] = i

            if i > sprite_dict[cur_label][2]:
                sprite_dict[cur_label][2] = i

            if j < sprite_dict[cur_label][1]:
                sprite_dict[cur_label][1] = j

            if j > sprite_dict[cur_label][3]:
                sprite_dict[cur_label][3] = j

    sprites = {}

    # create dict of sprites
    for label, value in sprite_dict.items():
        sprites[label] = Sprite(
            int(label), value[0], value[1],
            value[2], value[3]
        )

    return sprites, selected_area.tolist()


def create_sprite_labels_image(sprites, label_map, background_color=(255, 255, 255)):
    """
    Arguments:
        sprites {dict} -- a dict of sprites
        label_map {2D-list} -- 2D-list of image

    Keyword Arguments:
        background_color {tuple} -- color of background (default: {(255, 255, 255)})

    Raises:
        TypeError: when sprites is not a dict of sprite
                   when label map is not a 2D-list
                   when background color is not RGB or RGBA mode

    Returns:
        Image.Image -- an Image object
    """
    if not isinstance(sprites, dict):
        raise TypeError("Invalid sprites")
    if not isinstance(label_map, list) and not(isinstance, label_map[0], list):
        raise TypeError("Invalid label map")
    if not isinstance(background_color, tuple) and 3 <= len(background_color) <= 4:
        raise TypeError("Invalid background color")

    label_color = {}
    heigth = len(label_map)
    width = len(label_map[0])
    label_map = numpy.array(label_map)
    image = Image.new('RGB', (width, heigth), background_color) if len(
        background_color) == 3 else Image.new('RGBA', (width, heigth), background_color)
    draw = ImageDraw.Draw(image)

    for label, value in sprites.items():
        color = _get_random_color(background_color)
        y, x = numpy.where(label_map == label)
        draw.point(list(zip(x, y)), fill=color)
        label_color[label] = [value.top_left, value.bottom_right, color]

    for label, value in label_color.items():
        draw.rectangle([value[0], value[1]],
                       outline=value[2], fill=None)

    return image


# waypoint5
class SpriteSheet:
    @staticmethod
    def _is_valid(fd):
        if isinstance(fd, Image.Image):
            return fd
        if isinstance(fd, str) and imghdr.what(fd):
            return Image.open(fd)
        if isinstance(fd, io.BufferedReader) and isinstance(fd, io.IOBase):
            return Image.open(fd)
        if isinstance(fd, pathlib.PosixPath):
            return Image.open(fd)

        return False

    def __init__(self, fd, background_color=None):
        """
        Arguments:
            fd {str or Image} --  
                            the name and path (a string) that references an image file in the local file system;
                            a pathlib.Path object that references an image file in the local file system ;
                            a file object that MUST implement read(), seek(), and tell() methods, and be opened in binary mode;
                            a Image object.

        Keyword Arguments:
            background_color {int or tuple} -- background color of image (default: {None})

        Raises:
            TypeError: when Argument 'fd' is invalid
        """
        if not self._is_valid(fd):
            raise TypeError("Argument 'fd' is invalid")

        if background_color:
            if not isinstance(background_color, (int, tuple)):
                raise TypeError("Argument 'background_color' is invalid")

        self.fd = self._is_valid(fd)
        self.__background_color = background_color

    @property
    def background_color(self):
        if self.__background_color == None:
            return self.find_most_common_color(self.fd)

        return self.__background_color

    @staticmethod
    def __assign_label(selected_area, heigth, width, coordinate_y, coordinate_x, current_label, is_reduce=False):

        nearest_points = [
            (coordinate_x - 1, coordinate_y - 1),
            (coordinate_x, coordinate_y - 1),
            (coordinate_x + 1, coordinate_y - 1),
            (coordinate_x - 1, coordinate_y)
        ]

        current_point_label = selected_area[coordinate_y, coordinate_x]
        list_nearest_label = []

        for point in nearest_points:
            # skil useless point
            if point[0] < 0 or point[0] >= width or point[1] < 0 or point[1] >= heigth:
                continue

            label = selected_area[point[1], point[0]]

            # skip background
            if label == 0:
                continue

            # reduce number of label mode
            if is_reduce:
                # skip same label
                if label != current_point_label and label not in list_nearest_label:
                    list_nearest_label.append(label)
                continue

            return label, current_label

        if is_reduce:
            return min(list_nearest_label) if list_nearest_label else []

        return current_label + 1, current_label + 1

    @staticmethod
    def __get_random_color(background_color):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        rgb = (r, g, b) if len(background_color) == 3 else (r, g, b, 255)

        return rgb if rgb != background_color else _get_random_color(background_color)

    @staticmethod
    def find_most_common_color(image):
        """
        Arguments:
            image {Image.Image} -- a Image object

        Raises:
            TypeError: if argument is not a Image object

        Returns:
            int -- when image mode is grayscale
            tuple of integer -- when image mode is RGB or RGBA
        """
        if not isinstance(image, Image.Image):
            raise TypeError("argument 'image' must be a Imange object")

        color_dict = {}
        width, height = image.size
        result = None

        if width >= 1000 or height >= 1000:
            width = width // 10
            height = height // 10
        else:
            width = width // 2
            height = height // 2

        image = image.resize((width, height))
        pixel = image.load()

        for i in range(width):
            # find all pixel color of image
            for j in range(height):
                if pixel[i, j] not in color_dict:
                    color_dict[pixel[i, j]] = 1
                else:
                    color_dict[pixel[i, j]] += 1

                # find the pixel color most use
                if not result or color_dict[result] < color_dict[pixel[i, j]]:
                    result = pixel[i, j]

        return result

    def find_sprites(self, image):
        """
        Arguments:
            image {Image.Image} -- an Image object

        Raises:
            TypeError: when image is not an Image object

        Returns:
            dict -- a dict of sprite of image
            2D-list -- a label map of image
        """
        if not isinstance(image, Image.Image):
            raise TypeError("argument 'image' must be a Imange object")

        # set background color
        background_color = self.background_color

        width, heigth = image.size
        pixel = image.load()
        selected_area = numpy.zeros((heigth, width), dtype=int)
        current_label = 0
        label_dict = {}

        for j in range(heigth):
            for i in range(width):
                pixel_color = pixel[i, j]

                # skip pixels which are background
                if pixel_color == background_color:
                    continue

                if image.mode == 'RGBA' and pixel_color[3] == 0:
                    continue

                selected_area[j][i], current_label = self.__assign_label(
                    selected_area, heigth, width, j, i, current_label)

                label_dict.setdefault(selected_area[j][i], [])

        # find equivalent label
        for j in range(heigth):
            i = 0 if j % 2 == 0 else (width - 1)
            while i >= 0 and i < width:

                # skip background and label 1
                if selected_area[j][i] == 0 or selected_area[j][i] == 1:
                    i = (i + 1) if j % 2 == 0 else (i - 1)
                    continue

                nearest_lowest_label = self.__assign_label(
                    selected_area, heigth, width, j, i, current_label, is_reduce=True)

                if not nearest_lowest_label or nearest_lowest_label in label_dict[selected_area[j][i]]:
                    i = (i + 1) if j % 2 == 0 else (i - 1)
                    continue

                label_dict[selected_area[j][i]].append(nearest_lowest_label)

                i = (i + 1) if j % 2 == 0 else (i - 1)

        list_label = list(label_dict.keys())
        list_label.reverse()

        # define group table
        for label in list_label:
            # skip not equivalent label
            if not label_dict[label]:
                continue

            min_equivalent_label = min(label_dict[label])

            # no smaller equivalent label
            if min_equivalent_label >= label:
                continue

            for other_label in label_dict[label]:
                # except min equivalent label, skip label than larger than current label
                if other_label == min_equivalent_label or other_label >= label:
                    continue

                label_dict[other_label] += [min_equivalent_label]

            for other_label in label_dict:
                if other_label >= label:
                    break

                if label in label_dict[other_label]:
                    label_dict[other_label] += [min_equivalent_label]

            label_dict[label].remove(min_equivalent_label)
            label_dict[min_equivalent_label] += [label] + label_dict[label]

            label_dict[label] = []

        # remove duplicate
        for label in label_dict:
            label_dict[label] = list(dict.fromkeys(label_dict[label]))

        # replace label with min equivalent label
        for label, values in label_dict.items():
            if not values:
                continue

            for value in values:
                selected_area[selected_area == value] = label

        sprite_dict = {}

        # define locate of each sprite
        for j in range(heigth):
            for i in range(width):
                cur_label = selected_area[j][i]

                if cur_label == 0:
                    continue

                sprite_dict.setdefault(cur_label, [width, heigth, 0, 0])

                if i < sprite_dict[cur_label][0]:
                    sprite_dict[cur_label][0] = i

                if i > sprite_dict[cur_label][2]:
                    sprite_dict[cur_label][2] = i

                if j < sprite_dict[cur_label][1]:
                    sprite_dict[cur_label][1] = j

                if j > sprite_dict[cur_label][3]:
                    sprite_dict[cur_label][3] = j

        sprites = {}

        # create dict of sprites
        for label, value in sprite_dict.items():
            sprites[label] = Sprite(
                int(label), value[0], value[1],
                value[2], value[3]
            )

        return sprites, selected_area.tolist()

    def create_sprite_labels_image(self, background_color=(255, 255, 255)):
        """
        Keyword Arguments:
            background_color {tuple} -- color of background (default: {(255, 255, 255)})

        Returns:
            Image.Image -- an Image object
        """
        sprites, label_map = self.find_sprites(self.fd)
        label_color = {}
        heigth = len(label_map)
        width = len(label_map[0])
        label_map = numpy.array(label_map)
        image = Image.new('RGB', (width, heigth), background_color) if len(
            background_color) == 3 else Image.new('RGBA', (width, heigth), background_color)
        draw = ImageDraw.Draw(image)

        for label, value in sprites.items():
            color = self.__get_random_color(background_color)
            y, x = numpy.where(label_map == label)
            draw.point(list(zip(x, y)), fill=color)
            label_color[label] = [value.top_left, value.bottom_right, color]

        for label, value in label_color.items():
            draw.rectangle([value[0], value[1]],
                           outline=value[2], fill=None)

        return image
