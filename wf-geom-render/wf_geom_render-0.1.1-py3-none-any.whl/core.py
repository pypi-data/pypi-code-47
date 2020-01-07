import cv_utils
import numpy as np
import copy
import matplotlib.pyplot as plt
import tqdm
import json
import datetime
import logging

logger = logging.getLogger(__name__)

class GeomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Geom):
            obj_dict = obj.__dict__
            obj_dict['geom_type'] = obj.__class__.__name__
            return obj_dict
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, datetime.datetime):
            return(obj.astimezone(datetime.timezone.utc).isoformat())
        return json.JSONEncoder.default(self, obj)

class Geom:
    def __init__(
        self,
        coordinates=None,
        coordinate_indices=None,
        time_index=None
    ):
        if coordinates is not None:
            try:
                coordinates = np.array(coordinates)
            except:
                raise ValueError('Coordinates for geom must be array-like')
            if coordinates.ndim > 3:
                raise ValueError('Coordinates for geom must be of dimension 3 or less')
            while coordinates.ndim < 3:
                coordinates = np.expand_dims(coordinates, axis=0)
        if time_index is not None:
            try:
                time_index = np.array(time_index)
            except:
                raise ValueError('Time index must be array-like')
            if time_index.ndim != 1:
                raise ValueError('Time index must be one-dimensional')
            num_time_slices = time_index.shape[0]
            time_index_sort_order = np.argsort(time_index)
            time_index = time_index[time_index_sort_order]
            if coordinates is not None:
                if coordinates.shape[0] != num_time_slices:
                    raise ValueError('First dimension of coordinates array must be of same length as time index')
                coordinates = coordinates.take(time_index_sort_order, axis=0)
        self.coordinates = coordinates
        self.coordinate_indices = coordinate_indices
        self.time_index = time_index

    def to_json(self, indent=None):
        return json.dumps(self, cls=GeomJSONEncoder, indent=indent)

    def get_time_slice(self, index):
        new_geom = copy.deepcopy(self)
        new_geom.coordinates = np.expand_dims(self.coordinates[index], axis=0)
        new_geom.time_index = None
        return new_geom

    def resample(
        self,
        new_time_index,
        method='interpolate',
        progress_bar=False
    ):
        if method not in ['interpolate', 'fill']:
            raise ValueError('Available resampling methods are \'interpolate\' and \'fill\'')
        try:
            new_time_index = np.array(new_time_index)
        except:
            raise ValueError('New time index must be array-like')
        if new_time_index.ndim != 1:
            raise ValueError('New time index must be one-dimensional')
        new_time_index.sort()
        num_new_time_slices = new_time_index.shape[0]
        if self.time_index is None:
            new_geom = copy.deepcopy(self)
            new_geom.time_index = new_time_index
            print(self.coordinates)
            print(num_new_time_slices)
            new_geom.coordinates = np.tile(
                self.coordinates,
                (num_new_time_slices, 1, 1)
            )
            return new_geom
        coordinates_time_slice_shape = self.coordinates.shape[1:]
        new_coordinates_shape = (num_new_time_slices,) + coordinates_time_slice_shape
        new_coordinates = np.full(new_coordinates_shape, np.nan)
        old_time_index_pointer = 0
        logger.debug('Resampling from {} time slices to {} time slices'.format(
            self.time_index.shape[0],
            num_new_time_slices
        ))
        new_time_index_iterable = range(num_new_time_slices)
        if progress_bar:
            new_time_index_iterable = tqdm.tqdm_notebook(new_time_index_iterable)
        for new_time_index_pointer in new_time_index_iterable:
            if new_time_index[new_time_index_pointer] < self.time_index[old_time_index_pointer]:
                continue
            if new_time_index[new_time_index_pointer] > self.time_index[-1]:
                continue
            while new_time_index[new_time_index_pointer] > self.time_index[old_time_index_pointer + 1]:
                old_time_index_pointer += 1
            if method == 'interpolate':
                later_slice_weight = (
                    (new_time_index[new_time_index_pointer] - self.time_index[old_time_index_pointer])/
                    (self.time_index[old_time_index_pointer + 1] - self.time_index[old_time_index_pointer])
                )
                earlier_slice_weight = 1.0 - later_slice_weight
            else:
                earlier_slice_weight = 1.0
                later_slice_weight = 0.0
            if earlier_slice_weight == 0.0:
                new_coordinates[new_time_index_pointer] = self.coordinates[old_time_index_pointer + 1]
            elif later_slice_weight == 0.0:
                new_coordinates[new_time_index_pointer] = self.coordinates[old_time_index_pointer]
            else:
                new_coordinates[new_time_index_pointer] = (
                    earlier_slice_weight*self.coordinates[old_time_index_pointer] +
                    later_slice_weight*self.coordinates[old_time_index_pointer + 1]
                )
        new_geom = copy.deepcopy(self)
        new_geom.time_index = new_time_index
        new_geom.coordinates = new_coordinates
        return new_geom

class Geom2D(Geom):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.coordinates is not None and self.coordinates.shape[-1] != 2:
            raise ValueError('For 2D geoms, size of last dimension must be 2')

    def plot_matplotlib(
        self,
        image_size=None,
        background_image=None,
        background_alpha=None,
        show_axes=True,
        show=True
    ):
        if image_size is None and background_image is not None:
            image_size = np.array([
                background_image.shape[1],
                background_image.shape[0]]
        )
        fig, axes = plt.subplots()
        self.draw_matplotlib(axes)
        cv_utils.format_2d_image_plot(image_size, show_axes)
        if background_image is not None:
            cv_utils.draw_background_image(
                background_image,
                background_alpha
            )
        if show:
            plt.show()

    def overlay_video(
        self,
        input_path,
        output_path,
        start_time=None,
        progress_bar=False
    ):
        video_input = cv_utils.VideoInput(
            input_path=input_path,
            start_time=start_time
        )
        if self.time_index is not None:
            video_time_index = video_input.video_parameters.time_index
            if video_time_index is None:
                raise ValueError('Video must have time index to overlay geom sequence')
            if self.time_index[0] > video_time_index[-1]:
                logger.warning('Beginning of geom sequence is after end of video')
            if self.time_index[-1] < video_time_index[0]:
                logger.warning('End of geom sequence is before beginning of video')
            num_timestamps = len(video_time_index)
            resampled_geom = self.resample(video_time_index)
            video_output = cv_utils.VideoOutput(
                output_path,
                video_parameters=video_input.video_parameters
            )
            if progress_bar:
                t = tqdm.tqdm_notebook(total=num_timestamps)
            for sequence_index in range(num_timestamps):
                frame = video_input.get_frame()
                if frame is None:
                    raise ValueError('Input video ended unexpectedly at frame number {}'.format(sequence_index))
                overlay_geom = resampled_geom.get_time_slice(sequence_index)
                frame = overlay_geom.draw_opencv(frame)
                video_output.write_frame(frame)
                if progress_bar:
                    t.update()
        else:
            video_output = cv_utils.VideoOutput(
                output_path,
                video_parameters=video_input.video_parameters
            )
            if progress_bar:
                t = tqdm.tqdm_notebook(total=video_input.video_parameters.frame_count)
            frame_count_stream = 0
            while(video_input.is_opened()):
                frame = video_input.get_frame()
                if frame is not None:
                    frame_count_stream += 1
                    frame = self.draw_opencv(frame)
                    video_output.write_frame(frame)
                    if progress_bar:
                        t.update()
                else:
                    break
            if video_input.video_parameters.frame_count is not None and int(frame_count_stream) != int(video_input.video_parameters.frame_count):
                logger.warning('Expected {} frames but got {} frames'.format(
                    int(frame_count),
                    int(frame_count_stream)
                ))
        video_input.close()
        video_output.close()
        if progress_bar:
            t.close()

class Geom3D(Geom):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.coordinates is not None and self.coordinates.shape[-1] != 3:
            raise ValueError('For 3D geoms, size of last dimension must be 3')

    def project_coordinates(
        self,
        rotation_vector,
        translation_vector,
        camera_matrix,
        distortion_coefficients
    ):
        new_coordinates = np.apply_along_axis(
            lambda points: cv_utils.project_points(
                points,
                rotation_vector,
                translation_vector,
                camera_matrix,
                distortion_coefficients,
                remove_behind_camera=True
            ),
            axis=-1,
            arr=self.coordinates
        )
        return new_coordinates

class GeomCollection(Geom):
    def __init__(
        self,
        geom_list=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.geom_list = geom_list

    @classmethod
    def from_geom_list(
        cls,
        geom_list,
        method='interpolate',
        progress_bar=False
    ):
        num_spatial_dimensions = geom_list[0].coordinates.shape[-1]
        new_num_points = 0
        new_timestamp_set = set()
        for geom in geom_list:
            if geom.coordinates.shape[-1] != num_spatial_dimensions:
                raise ValueError('All geoms in list must have the same number of spatial_dimensions')
            if geom.time_index is not None:
                new_timestamp_set = new_timestamp_set.union(geom.time_index)
            new_num_points += geom.coordinates.shape[1]
        new_time_index = None
        new_num_time_slices = 1
        if len(new_timestamp_set) > 0:
            new_time_index = np.sort(np.array(list(new_timestamp_set)))
            new_num_time_slices = new_time_index.shape[0]
        new_coordinates = np.full((new_num_time_slices, new_num_points, num_spatial_dimensions), np.nan)
        new_geom_list = list()
        new_coordinate_index = 0
        if progress_bar:
            geom_list = tqdm.tqdm_notebook(geom_list)
        for geom in geom_list:
            if new_time_index is not None:
                new_geom = geom.resample(new_time_index, method, progress_bar)
            else:
                new_geom = copy.deepcopy(geom)
            num_points = new_geom.coordinates.shape[1]
            new_coordinates[:, new_coordinate_index : new_coordinate_index + num_points, :] = new_geom.coordinates
            if isinstance(geom, GeomCollection):
                for sub_geom in geom.geom_list:
                    new_sub_geom = copy.deepcopy(sub_geom)
                    new_sub_geom.coordinate_indices = [
                        coordinate_index + new_coordinate_index
                        for coordinate_index in new_sub_geom.coordinate_indices
                    ]
                    new_geom_list.append(new_sub_geom)
            else:
                new_geom.coordinates = None
                new_geom.time_index = None
                new_geom.coordinate_indices = [
                    new_coordinate_index + coordinate_index
                    for coordinate_index in range(num_points)
                ]
                new_geom_list.append(new_geom)
            new_coordinate_index += num_points
        return cls(
            time_index=new_time_index,
            coordinates=new_coordinates,
            geom_list=new_geom_list
        )

class Circle(Geom):
    def __init__(
        self,
        radius=6,
        line_width=1.5,
        line_style='solid',
        line_color='#00ff00',
        fill=True,
        fill_color='#00ff00',
        alpha=1.0,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.radius = radius
        self.line_width = line_width
        self.line_style = line_style
        self.line_color=line_color
        self.fill = fill
        self.fill_color=fill_color
        self.alpha=alpha

class Point(Geom):
    def __init__(
        self,
        marker='.',
        size=6,
        line_width=1.5,
        line_color='#00ff00',
        fill_color='#00ff00',
        alpha=1.0,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.marker = marker
        self.size = size
        self.line_width=line_width
        self.line_color=line_color
        self.fill_color=fill_color
        self.alpha=alpha

class Line(Geom):
    def __init__(
        self,
        line_width=1.5,
        line_style='solid',
        color='#00ff00',
        alpha=1.0,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.line_width = line_width
        self.line_style = line_style
        self.color=color
        self.alpha=alpha

class Text(Geom):
    def __init__(
        self,
        text=None,
        font_family=None,
        font_style=None,
        font_weight=None,
        font_size=None,
        text_color='#00ff00',
        text_alpha=1.0,
        horizontal_alignment='center',
        vertical_alignment='bottom',
        box=False,
        box_line_width=1.5,
        box_line_style='solid',
        box_line_color='#000000',
        box_fill=False,
        box_fill_color='#ffff00',
        box_alpha=1.0,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.text = text
        self.font_family = font_family
        self.font_style = font_style
        self.font_weight = font_weight
        self.font_size = font_size
        self.text_color = text_color
        self.text_alpha = text_alpha
        self.horizontal_alignment = horizontal_alignment
        self.vertical_alignment = vertical_alignment
        self.box = box
        self.box_line_color = box_line_color
        self.box_fill = box_fill
        self.box_fill_color = box_fill_color
        self.box_alpha = box_alpha
        self.box_line_width = box_line_width
        self.box_line_style = box_line_style

class GeomCollection2D(Geom2D, GeomCollection):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def draw_matplotlib(self, axis):
        for geom_index, geom in enumerate(self.geom_list):
            geom_copy = copy.deepcopy(geom)
            geom_copy.coordinates = self.coordinates.take(geom_copy.coordinate_indices, 1)
            geom_copy.draw_matplotlib(axis)

    def draw_opencv(self, image):
        new_image = image.copy()
        for geom_index, geom in enumerate(self.geom_list):
            geom_copy = copy.deepcopy(geom)
            geom_copy.coordinates = self.coordinates.take(geom_copy.coordinate_indices, 1)
            new_image = geom_copy.draw_opencv(new_image)
        return new_image

class GeomCollection3D(Geom3D, GeomCollection):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def project(
        self,
        rotation_vector,
        translation_vector,
        camera_matrix,
        distortion_coefficients
    ):
        new_coordinates=None
        if self.coordinates is not None:
            new_coordinates = self.project_coordinates(
                rotation_vector,
                translation_vector,
                camera_matrix,
                distortion_coefficients
            )

        new_geom_list = [
            geom.project(
                rotation_vector,
                translation_vector,
                camera_matrix,
                distortion_coefficients
            ) for geom in self.geom_list]
        return GeomCollection2D(
            coordinates=new_coordinates,
            geom_list=new_geom_list,
            time_index=self.time_index
        )

class Circle2D(Geom2D, Circle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def draw_matplotlib(self, axis):
        if self.coordinates.shape != (1, 1, 2):
            raise ValueError('Draw method for Circle2D requires coordinates to be of shape (1, 1, 2)')
        axis.add_artist(plt.Circle(
            xy=self.coordinates[0, 0, :],
            radius=self.radius,
            linewidth=self.line_width,
            linestyle=self.line_style,
            edgecolor=self.line_color,
            fill=self.fill,
            facecolor=self.fill_color,
            alpha=self.alpha
        ))

    def draw_opencv(self, image):
        if self.coordinates.shape != (1, 1, 2):
            raise ValueError('Draw method for Circle2D requires coordinates to be of shape (1, 1, 2)')
        if np.any(np.isnan(self.coordinates)):
            return image
        new_image = cv_utils.draw_circle(
            image,
            coordinates=self.coordinates[0, 0],
            radius=self.radius,
            line_width=self.line_width,
            color=self.line_color,
            fill=self.fill,
            alpha=self.alpha
        )
        return new_image

class Circle3D(Geom3D, Circle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def project(
        self,
        rotation_vector,
        translation_vector,
        camera_matrix,
        distortion_coefficients
    ):
        new_coordinates=None
        if self.coordinates is not None:
            new_coordinates = self.project_coordinates(
                rotation_vector,
                translation_vector,
                camera_matrix,
                distortion_coefficients
            )
        return Circle2D(
            coordinates=new_coordinates,
            coordinate_indices=self.coordinate_indices,
            time_index=self.time_index,
            radius=self.radius,
            line_width=self.line_width,
            line_style=self.line_style,
            line_color=self.line_color,
            fill=self.fill,
            fill_color=self.fill_color,
            alpha=self.alpha
        )


class Point2D(Geom2D, Point):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def draw_matplotlib(self, axis):
        if self.coordinates.shape != (1, 1, 2):
            raise ValueError('Draw method for Point2D requires coordinates to be of shape (1, 1, 2)')
        s = None
        if self.size is not None:
            s=self.size**2
        axis.scatter(
            self.coordinates[0, 0, 0],
            self.coordinates[0, 0, 1],
            marker=self.marker,
            s=s,
            linewidths=self.line_width,
            edgecolors=self.line_color,
            color=self.fill_color,
            alpha=self.alpha
        )

    def draw_opencv(self, image):
        if self.coordinates.shape != (1, 1, 2):
            raise ValueError('Draw method for Point2D requires coordinates to be of shape (1, 1, 2)')
        if np.any(np.isnan(self.coordinates)):
            return image
        new_image = cv_utils.draw_point(
            image,
            coordinates=self.coordinates[0, 0],
            marker=self.marker,
            marker_size=self.size,
            line_width=self.line_width,
            color=self.line_color,
            alpha=self.alpha
        )
        return new_image

class Point3D(Geom3D, Point):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def project(
        self,
        rotation_vector,
        translation_vector,
        camera_matrix,
        distortion_coefficients
    ):
        new_coordinates=None
        if self.coordinates is not None:
            new_coordinates = self.project_coordinates(
                rotation_vector,
                translation_vector,
                camera_matrix,
                distortion_coefficients
            )
        return Point2D(
            coordinates=new_coordinates,
            coordinate_indices=self.coordinate_indices,
            time_index=self.time_index,
            marker=self.marker,
            size=self.size,
            line_width=self.line_width,
            line_color=self.line_color,
            fill_color=self.fill_color,
            alpha=self.alpha
        )


class Line2D(Geom2D, Line):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def draw_matplotlib(self, axis):
        if self.coordinates.shape != (1, 2, 2):
            raise ValueError('Draw method for Line2D requires coordinates to be of shape (1, 2, 2)')
        axis.add_artist(plt.Line2D(
            (self.coordinates[0, 0, 0], self.coordinates[0, 1,0]),
            (self.coordinates[0, 0, 1], self.coordinates[0, 1, 1]),
            linewidth=self.line_width,
            linestyle=self.line_style,
            color=self.color,
            alpha=self.alpha
        ))

    def draw_opencv(self, image):
        if self.coordinates.shape != (1, 2, 2):
            raise ValueError('Draw method for Line2D requires coordinates to be of shape (1, 2, 2)')
        if np.any(np.isnan(self.coordinates)):
            return image
        new_image = cv_utils.draw_line(
            image,
            coordinates=self.coordinates[0],
            line_width=self.line_width,
            color=self.color,
            alpha=self.alpha
        )
        return new_image

class Line3D(Geom3D, Line):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def project(
        self,
        rotation_vector,
        translation_vector,
        camera_matrix,
        distortion_coefficients
    ):
        new_coordinates=None
        if self.coordinates is not None:
            new_coordinates = self.project_coordinates(
                rotation_vector,
                translation_vector,
                camera_matrix,
                distortion_coefficients
            )
        return Line2D(
            coordinates=new_coordinates,
            coordinate_indices=self.coordinate_indices,
            time_index=self.time_index,
            line_width=self.line_width,
            line_style=self.line_style,
            color=self.color,
            alpha=self.alpha
        )

class Text2D(Geom2D, Text):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def draw_matplotlib(self, axis):
        if self.coordinates.shape != (1, 1, 2):
            raise ValueError('Draw method for Text2D requires coordinates to be of shape (1, 1, 2)')
        if np.any(np.isnan(self.coordinates)):
            return
        bbox = None
        if self.box:
            bbox = {
                'edgecolor': self.box_line_color,
                'fill': self.box_fill,
                'facecolor': self.box_fill_color,
                'alpha': self.box_alpha,
                'linewidth': self.box_line_width,
                'linestyle': self.box_line_style
            }
        axis.text(
            self.coordinates[0, 0, 0],
            self.coordinates[0, 0, 1],
            self.text,
            fontfamily=self.font_family,
            fontstyle=self.font_style,
            fontweight=self.font_weight,
            fontsize=self.font_size,
            color=self.text_color,
            alpha=self.text_alpha,
            horizontalalignment=self.horizontal_alignment,
            verticalalignment=self.vertical_alignment,
            bbox=bbox,
            clip_on=True
        )

    def draw_opencv(self, image):
        if self.coordinates.shape != (1, 1, 2):
            raise ValueError('Draw method for Text2D requires coordinates to be of shape (1, 1, 2)')
        if np.any(np.isnan(self.coordinates)):
            return image
        new_image = cv_utils.draw_text(
            image,
            coordinates=self.coordinates[0,0],
            text=self.text,
            horizontal_alignment=self.horizontal_alignment,
            vertical_alignment=self.vertical_alignment,
            color=self.text_color,
            alpha=self.text_alpha
        )
        return new_image

class Text3D(Geom3D, Text):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def project(
        self,
        rotation_vector,
        translation_vector,
        camera_matrix,
        distortion_coefficients
    ):
        new_coordinates=None
        if self.coordinates is not None:
            new_coordinates = self.project_coordinates(
                rotation_vector,
                translation_vector,
                camera_matrix,
                distortion_coefficients
            )
        return Text2D(
            coordinates=new_coordinates,
            coordinate_indices=self.coordinate_indices,
            time_index=self.time_index,
            text=self.text,
            font_family=self.font_family,
            font_style=self.font_style,
            font_weight=self.font_weight,
            font_size=self.font_size,
            text_color=self.text_color,
            text_alpha=self.text_alpha,
            horizontal_alignment=self.horizontal_alignment,
            vertical_alignment=self.vertical_alignment,
            box=self.box,
            box_line_width=self.box_line_width,
            box_line_style=self.box_line_style,
            box_line_color=self.box_line_color,
            box_fill=self.box_fill,
            box_fill_color=self.box_fill_color,
            box_alpha=self.box_alpha
        )
