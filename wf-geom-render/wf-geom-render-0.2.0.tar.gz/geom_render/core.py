import cv_utils
import numpy as np
import copy
import matplotlib.pyplot as plt
import tqdm
import json
import datetime
import logging
from uuid import uuid4

logger = logging.getLogger(__name__)

class GeomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Geom):
            obj_dict = obj.__dict__
            obj_dict['geom_type'] = obj.__class__.__name__
            return obj_dict
        if isinstance(obj, np.ndarray):
            try:
                obj = np.where(np.isnan(obj), None, obj)
            except:
                pass
            return obj.tolist()
        if isinstance(obj, datetime.datetime):
            return(obj.astimezone(datetime.timezone.utc).isoformat())
        return json.JSONEncoder.default(self, obj)

class Geom:
    def __init__(
        self,
        coordinates=None,
        coordinate_indices=None,
        time_index=None,
        start_time=None,
        frames_per_second=None,
        num_frames=None,
        frame_width=None,
        frame_height=None,
        id=None
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
        if time_index is not None and start_time is None and frames_per_second is None and num_frames is None:
            # Ragged time index
            try:
                time_index = np.array(time_index)
            except:
                raise ValueError('Time index must be array-like')
            if time_index.ndim != 1:
                raise ValueError('Time index must be one-dimensional')
            time_index_sort_order = np.argsort(time_index)
            time_index = time_index[time_index_sort_order]
            calculated_num_frames = time_index.shape[0]
            if coordinates is not None:
                if coordinates.shape[0] != calculated_num_frames:
                    raise ValueError('First dimension of coordinates array must be of same length as time index')
                coordinates = coordinates.take(time_index_sort_order, axis=0)
        elif time_index is None and start_time is not None and frames_per_second is not None and num_frames is not None:
            # Regular time index
            frames_per_second = float(frames_per_second)
            num_frames = int(round(num_frames))
        elif time_index is None and start_time is None and frames_per_second is None and num_frames is None:
            # No time index
            pass
        else:
            raise ValueError('Must specify time index or all of start time/fps/number of frames or neither')
        if id is None:
            id = uuid4().hex
        self.coordinates = coordinates
        self.coordinate_indices = coordinate_indices
        self.time_index = time_index
        self.start_time = start_time
        self.frames_per_second = frames_per_second
        self.num_frames = num_frames
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.id = id

    def to_json(self, indent=None):
        return json.dumps(self, cls=GeomJSONEncoder, indent=indent)

    def get_time_slice(self, index):
        new_geom = copy.deepcopy(self)
        new_geom.coordinates = np.expand_dims(self.coordinates[index], axis=0)
        new_geom.time_index = None
        new_geom.start_time = None
        new_geom.frames_per_second = None
        new_geom.num_frames = None
        return new_geom

    def resample(
        self,
        new_time_index=None,
        new_start_time=None,
        new_frames_per_second=None,
        new_num_frames=None,
        method='interpolate',
        progress_bar=False
    ):
        if method not in ['interpolate', 'fill']:
            raise ValueError('Available resampling methods are \'interpolate\' and \'fill\'')
        if new_time_index is not None and new_start_time is None and new_frames_per_second is None and new_num_frames is None:
            # New ragged time index
            try:
                new_time_index = np.array(new_time_index)
            except:
                raise ValueError('New time index must be array-like')
            if new_time_index.ndim != 1:
                raise ValueError('New time index must be one-dimensional')
            new_time_index.sort()
            calculated_new_num_frames = new_time_index.shape[0]
            calculated_new_time_index = new_time_index
        elif new_time_index is None and new_start_time is not None and new_frames_per_second is not None and new_num_frames is not None:
            # New regular time index
            new_frames_per_second = float(new_frames_per_second)
            new_num_frames = int(round(new_num_frames))
            new_time_between_frames = datetime.timedelta(microseconds = int(round(10**6/new_frames_per_second)))
            calculated_new_time_index = [new_start_time + i*new_time_between_frames for i in range(new_num_frames)]
            calculated_new_num_frames = new_num_frames
        else:
            raise ValueError('Must specify time index or all of start time/fps/number of frames')
        if self.time_index is None and self.start_time is None and self.frames_per_second is None and self.num_frames is None:
            # No old time index
            new_geom = copy.deepcopy(self)
            new_geom.time_index = new_time_index
            new_geom.start_time = new_start_time
            new_geom.frames_per_second = new_frames_per_second
            new_geom.num_frames = new_num_frames
            new_geom.coordinates = np.tile(
                self.coordinates,
                (calculated_new_num_frames, 1, 1)
            )
            return new_geom
        elif self.time_index is None and self.start_time is not None and self.frames_per_second is not None and self.num_frames is not None:
            old_time_between_frames = datetime.timedelta(microseconds = int(round(10**6/self.frames_per_second)))
            old_time_index = [self.start_time + i*old_time_between_frames for i in range(self.num_frames)]
        elif self.time_index is not None and self.start_time is None and self.frames_per_second is None and self.num_frames is None:
            old_time_index = self.time_index
        else:
            raise ValueError('Current time index is malformed. Must include time index or all of start time/fps/number of frames or neither.')
        coordinates_time_slice_shape = self.coordinates.shape[1:]
        new_coordinates_shape = (calculated_new_num_frames,) + coordinates_time_slice_shape
        new_coordinates = np.full(new_coordinates_shape, np.nan)
        old_time_index_pointer = 0
        new_time_index_iterable = range(calculated_new_num_frames)
        if progress_bar:
            new_time_index_iterable = tqdm.tqdm_notebook(new_time_index_iterable)
        for new_time_index_pointer in new_time_index_iterable:
            if calculated_new_time_index[new_time_index_pointer] < old_time_index[old_time_index_pointer]:
                continue
            if calculated_new_time_index[new_time_index_pointer] > old_time_index[-1]:
                continue
            while calculated_new_time_index[new_time_index_pointer] > old_time_index[old_time_index_pointer + 1]:
                old_time_index_pointer += 1
            if method == 'interpolate':
                later_slice_weight = (
                    (calculated_new_time_index[new_time_index_pointer] - old_time_index[old_time_index_pointer])/
                    (old_time_index[old_time_index_pointer + 1] - old_time_index[old_time_index_pointer])
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
        new_geom.start_time = new_start_time
        new_geom.frames_per_second = new_frames_per_second
        new_geom.num_frames = new_num_frames
        new_geom.coordinates = new_coordinates
        return new_geom

class Geom2D(Geom):
    def __init__(
        self,
        **kwargs
    ):
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
        if self.time_index is not None or self.start_time is not None or self.frames_per_second is not None or self.num_frames is not None:
            video_start_time = video_input.video_parameters.start_time
            video_fps = video_input.video_parameters.fps
            video_frame_count = video_input.video_parameters.frame_count
            if video_start_time is None or video_fps is None or video_frame_count is None:
                raise ValueError('Video must have start time, FPS, and frame count info to overlay geom sequence')
            resampled_geom = self.resample(
                new_start_time=video_start_time,
                new_frames_per_second=video_fps,
                new_num_frames=video_frame_count
            )
            video_output = cv_utils.VideoOutput(
                output_path,
                video_parameters=video_input.video_parameters
            )
            if progress_bar:
                t = tqdm.tqdm_notebook(total=video_frame_count)
            for frame_index in range(video_frame_count):
                frame = video_input.get_frame()
                if frame is None:
                    raise ValueError('Input video ended unexpectedly at frame number {}'.format(frame_index))
                overlay_geom = resampled_geom.get_time_slice(frame_index)
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
        frame_width = geom_list[0].frame_width
        frame_height = geom_list[0].frame_height
        new_num_points = 0
        new_timestamp_set = set()
        for geom in geom_list:
            if geom.coordinates.shape[-1] != num_spatial_dimensions:
                raise ValueError('All geoms in list must have the same number of spatial_dimensions')
            if geom.frame_width is not None and geom_frame_width != frame_width:
                raise ValueError('All geoms in list must have the same frame width (if specified)')
            if geom.frame_height is not None and geom_frame_height != frame_height:
                raise ValueError('All geoms in list must have the same frame height (if specified)')
            if geom.time_index is not None and geom.start_time is None and geom.frames_per_second is None and geom.num_frames is None:
                new_timestamp_set = new_timestamp_set.union(geom.time_index)
            elif geom.time_index is None and geom.start_time is not None and geom.frames_per_second is not None and geom.num_frames is not None:
                time_between_frames = datetime.timedelta(microseconds = int(round(10**6/geom.frames_per_second)))
                calculated_time_index = [geom.start_time + i*time_between_frames for i in range(geom.num_frames)]
                new_timestamp_set = new_timestamp_set.union(calculated_time_index)
            elif geom.time_index is None and geom.start_time is None and geom.frames_per_second is None and geom.num_frames is None:
                pass
            else:
                raise ValueError('One of the geoms in the list has a malformed time index. Must include time index or all of start time/fps/number of frames or neither')
            new_num_points += geom.coordinates.shape[1]
        new_time_index = None
        new_start_time = None
        new_frames_per_second = None
        new_num_frames = None
        new_calculated_num_frames = 1
        if len(new_timestamp_set) > 0:
            new_time_index = np.sort(np.array(list(new_timestamp_set)))
            new_calculated_num_frames = new_time_index.shape[0]
        new_coordinates = np.full((new_calculated_num_frames, new_num_points, num_spatial_dimensions), np.nan)
        new_geom_list = list()
        new_coordinate_index = 0
        if progress_bar:
            geom_list = tqdm.tqdm_notebook(geom_list)
        for geom in geom_list:
            if new_time_index is not None:
                new_geom = geom.resample(
                    new_time_index=new_time_index,
                    method=method,
                    progress_bar=progress_bar
                )
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
                new_geom.start_time = None
                new_geom.frames_per_second = None
                new_geom.num_frames = None
                new_geom.frame_width = None
                new_geom.frame_height = None
                new_geom.coordinate_indices = [
                    new_coordinate_index + coordinate_index
                    for coordinate_index in range(num_points)
                ]
                new_geom_list.append(new_geom)
            new_coordinate_index += num_points
        return cls(
            time_index=new_time_index,
            coordinates=new_coordinates,
            geom_list=new_geom_list,
            frame_width=frame_width,
            frame_height=frame_height
        )

class Circle(Geom):
    def __init__(
        self,
        radius=6,
        line_width=1.5,
        color='#00ff00',
        fill=True,
        alpha=1.0,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.radius = radius
        self.line_width = line_width
        self.color=color
        self.fill = fill
        self.alpha=alpha

class Point(Geom):
    def __init__(
        self,
        marker='.',
        size=6,
        color='#00ff00',
        alpha=1.0,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.marker = marker
        self.size = size
        self.color=color
        self.alpha=alpha

class Line(Geom):
    def __init__(
        self,
        line_width=1.5,
        color='#00ff00',
        alpha=1.0,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.line_width = line_width
        self.color=color
        self.alpha=alpha

class Text(Geom):
    def __init__(
        self,
        text=None,
        color='#00ff00',
        alpha=1.0,
        horizontal_alignment='center',
        vertical_alignment='bottom',
        **kwargs
    ):
        super().__init__(**kwargs)
        self.text = text
        self.color = color
        self.alpha = alpha
        self.horizontal_alignment = horizontal_alignment
        self.vertical_alignment = vertical_alignment

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
        distortion_coefficients,
        frame_width=None,
        frame_height=None
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
            time_index=self.time_index,
            start_time=self.start_time,
            frames_per_second=self.frames_per_second,
            num_frames=self.num_frames,
            frame_width=frame_width,
            frame_height=frame_height
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
            edgecolor=self.color,
            fill=self.fill,
            facecolor=self.color,
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
        distortion_coefficients,
        frame_width=None,
        frame_height=None
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
            start_time=self.start_time,
            frames_per_second=self.frames_per_second,
            num_frames=self.num_frames,
            radius=self.radius,
            line_width=self.line_width,
            color=self.color,
            fill=self.fill,
            alpha=self.alpha,
            id=self.id,
            frame_width=frame_width,
            frame_height=frame_height
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
            edgecolors=self.color,
            color=self.color,
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
            color=self.color,
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
        distortion_coefficients,
        frame_width=None,
        frame_height=None
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
            start_time=self.start_time,
            frames_per_second=self.frames_per_second,
            num_frames=self.num_frames,
            marker=self.marker,
            size=self.size,
            color=self.color,
            alpha=self.alpha,
            id=self.id,
            frame_width=frame_width,
            frame_height=frame_height
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
        distortion_coefficients,
        frame_width=None,
        frame_height=None
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
            start_time=self.start_time,
            frames_per_second=self.frames_per_second,
            num_frames=self.num_frames,
            line_width=self.line_width,
            color=self.color,
            alpha=self.alpha,
            id=self.id,
            frame_width=frame_width,
            frame_height=frame_height
        )

class Text2D(Geom2D, Text):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def draw_matplotlib(self, axis):
        if self.coordinates.shape != (1, 1, 2):
            raise ValueError('Draw method for Text2D requires coordinates to be of shape (1, 1, 2)')
        if np.any(np.isnan(self.coordinates)):
            return
        axis.text(
            self.coordinates[0, 0, 0],
            self.coordinates[0, 0, 1],
            self.text,
            color=self.color,
            alpha=self.alpha,
            horizontalalignment=self.horizontal_alignment,
            verticalalignment=self.vertical_alignment,
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
            color=self.color,
            alpha=self.alpha
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
        distortion_coefficients,
        frame_width=None,
        frame_height=None
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
            start_time=self.start_time,
            frames_per_second=self.frames_per_second,
            num_frames=self.num_frames,
            text=self.text,
            color=self.color,
            alpha=self.alpha,
            horizontal_alignment=self.horizontal_alignment,
            vertical_alignment=self.vertical_alignment,
            id=self.id,
            frame_width=frame_width,
            frame_height=frame_height
        )
