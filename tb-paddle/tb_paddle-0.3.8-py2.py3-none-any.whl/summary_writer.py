# coding=utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import numpy as np
import os
import six
import time

from .logger import logger
from .file_writer import FileWriter
from .embedding import make_mat, make_sprite, make_tsv, append_pbtxt
from .utils import figure_to_image
from .summary import (
    scalar, histogram, histogram_raw, image, audio, text,
    pr_curve, pr_curve_raw, video, custom_scalars, image_boxes, mesh
)
from .paddle_graph import paddle_graph
from .hparams_summary import hparams_pb, hparams_config_pb


class SummaryWriter(object):
    """Writes entries directly to event files in the logdir to be
    consumed by TensorBoard.

    The `SummaryWriter` class provides a high-level API to create an event file
    in a given directory and add summaries and events to it. The class updates the
    file contents asynchronously.
    """

    def __init__(self, logdir=None, max_queue=1024, comment='', filename_suffix='', **kwargs):
        """Creates a `SummaryWriter` that will write out events and summaries to the event file.

        :param logdir: Save directory location. Default is runs/**CURRENT_DATETIME_HOSTNAME**,
                       which changes after each run. Use hierarchical folder structure to 
                       compare between runs easily. e.g. pass in 'runs/exp1', 'runs/exp2', etc.
                       for each new experiment to compare across them.
        :type logdir: string
        :param max_queue: Size of the queue for pending events and summaries before one of
                          the 'add' calls forces a flush to disk.
        :type max_queue: int
        :param comment: Comment logdir suffix appended to the default ``logdir``.
                        If ``logdir`` is assigned, this argument has no effect.
        :type  comment: string
        :param filename_suffix: Suffix added to all event filenames in
                                the logdir directory. More details on filename construction in
                                tensorboard.summary.writer.event_file_writer.EventFileWriter.
        :type filename_suffix: string

        Examples:
            from tb_paddle import SummaryWriter

            # create a summary writer with automatically generated folder name.
            writer = SummaryWriter()

            # create a summary writer using the specified folder name.
            writer = SummaryWriter("my_experiment")

            # create a summary writer with comment appended.
            writer = SummaryWriter(comment="LR_0.1_BATCH_16")
        """
        if not logdir:
            import socket
            from datetime import datetime
            current_time = datetime.now().strftime('%b%d_%H-%M-%S')
            logdir = os.path.join(
                'runs', current_time + '_' + socket.gethostname() + comment)
        self.logdir = logdir
        self._max_queue = max_queue
        self._filename_suffix = filename_suffix
        self.kwargs = kwargs

        # Initialize the file writers, but they can be cleared out on close and recreated later as needed.
        self.file_writer = self.all_writers = None
        self._get_file_writer()

        # Create default bins for histograms, see generate_testdata.py in tensorflow/tensorboard
        v = 1E-12
        buckets = []
        neg_buckets = []
        while v < 1E20:
            buckets.append(v)
            neg_buckets.append(-v)
            v *= 1.1
        self.default_bins = neg_buckets[::-1] + [0] + buckets

        self.scalar_dict = {}

    def __append_to_scalar_dict(self, tag, scalar_value, global_step, timestamp):
        """This adds an entry to the self.scalar_dict datastructure with format
        {writer_id : [[timestamp, step, value], ...], ...}.
        """
        from .x2num import make_np
        if tag not in self.scalar_dict.keys():
            self.scalar_dict[tag] = []
        self.scalar_dict[tag].append([timestamp, global_step, float(make_np(scalar_value))])

    def _get_file_writer(self):
        if self.all_writers is None or self.file_writer is None:
            self.file_writer = FileWriter(logdir=self.logdir,
                                          max_queue=self._max_queue,
                                          filename_suffix=self._filename_suffix,
                                          **self.kwargs)
            self.all_writers = {self.file_writer.get_logdir(): self.file_writer}
        
        return self.file_writer
    
    def flush(self):
        if self.all_writers is None:
            return  # ignore double close
        for writer in self.all_writers.values():
            writer.flush()
    
    def add_scalar(self, tag, scalar_value, global_step=None, walltime=None):
        """Add scalar data to summary.

        :param tag: Data identifier.
        :type tag: str
        :param scalar_value: Value to save.
        :type scalar_value: float
        :param global_step: Global step value to record.
        :type global_step: int
        :param walltime: Optional override current time of event.
        :type walltime: float
        """
        self._get_file_writer().add_summary(scalar(tag, scalar_value), global_step, walltime)
        self.flush()

    def add_scalars(self, main_tag, tag_scalar_dict, global_step=None, walltime=None):
        """Adds many scalar data to summary.

        Note that this function also keeps logged scalars in memory. In extreme case it explodes your RAM.

        :param main_tag: The parent name for the tags.
        :type main_tag: str
        :param tag_scalar_dict: Key-value pair storing the tag and corresponding values.
        :type tag_scalar_dict: dict
        :param global_step: Global step value to record.
        :type global_step: int
        :param walltime: Optional override current time of event.
        :type walltime: float
        """
        walltime = time.time() if walltime is None else walltime
        fw_logdir = self._get_file_writer().get_logdir()
        for tag, scalar_value in tag_scalar_dict.items():
            fw_tag = fw_logdir + "/" + main_tag + "/" + tag
            if fw_tag in self.all_writers.keys():
                fw = self.all_writers[fw_tag]
            else:
                fw = FileWriter(logdir=fw_tag)
                self.all_writers[fw_tag] = fw

            fw.add_summary(scalar(main_tag, scalar_value), global_step, walltime)
            self.__append_to_scalar_dict(fw_tag, scalar_value, global_step, walltime)
        self.flush()

    def export_scalars_to_json(self, path):
        """Exports to the given path an ASCII file containing all the scalars written
        so far by this instance, with the following format:
        {writer_id : [[timestamp, step, value], ...], ...}

        The scalars saved by ``add_scalars()`` will be flushed after export.
        """
        with open(path, "w") as f:
            json.dump(self.scalar_dict, f)
        self.scalar_dict = {}

    def add_histogram(self, tag, values, global_step=None, bins='tensorflow', walltime=None, max_bins=None):
        """Add histogram to summary.

        :param tag: Data identifier.
        :type tag: str
        :param values: Values to build histogram.
        :type values: numpy.array
        :param global_step: Global step value to record.
        :type global_step: int
        :param bins: One of {'tensorflow','auto', 'fd', ...}.
            This determines how the bins are made. You can find other options in:
            https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html
        :type bins: str
        :param walltime: Optional override current time of event.
        :type walltime: float
        """
        if isinstance(bins, six.string_types) and bins == 'tensorflow':
            bins = self.default_bins
        self._get_file_writer().add_summary(
            histogram(tag, values, bins, max_bins=max_bins), global_step, walltime)
        self.flush()

    def add_histogram_raw(self, tag, min, max, num, sum, sum_squares,
                          bucket_limits, bucket_counts, global_step=None,
                          walltime=None):
        """Adds histogram with raw data.

        :param tag: Data identifier.
        :type tag: str
        :param min: Min value.
        :type min: float or int
        :param max: Max value.
        :type max: float or int
        :param num: Number of values.
        :type num: int
        :param sum: Sum of all values.
        :type sum: float or int
        :param sum_squares: Sum of squares for all values.
        :type sum_squares: float or int
        :param bucket_limits: Upper value per bucket, note that the bucket_limits returned from
                             `np.histogram` has one more element.
        :type bucket_limits: numpy.array
        :param bucket_counts: Number of values per bucket.
        :type bucket_counts: numpy.array
        :param global_step: Global step value to record.
        :type global_step: int
        :param walltime: Optional override current time of event.
        :type walltime: float
        """
        if len(bucket_limits) != len(bucket_counts):
            raise ValueError('len(bucket_limits) != len(bucket_counts), see the document.')
        self._get_file_writer().add_summary(
            histogram_raw(tag, min, max, num, sum, sum_squares, bucket_limits, bucket_counts),
            global_step,
            walltime)
        self.flush()

    def add_image(self, tag, input_image, global_step=None, walltime=None, dataformats='CHW'):
        """Add image data to summary.

        Note that this requires the `pillow` package.

        :param tag: Data identifier.
        :type tag: str
        :param input_image: An `uint8` or `float` Tensor of shape `[channel, height, width]` where
            `channel` is 1, 3, or 4. The elements in input_image can either have values
             in [0, 1] (float32) or [0, 255] (uint8).
             Users are responsible to scale the data in the correct range/type.
        :type input_image: numpy.array
        :param global_step: Global step value to record.
        :type global_step: int
        :param walltime: Optional override current time of event.
        :type walltime: float
        :param dataformats: This parameter specifies the dataformats of input_image
        :type dataformats: str

        input_image.shape: Default is :math:`(3, H, W)`,
            :math:`(1, H, W)`, :math:`(H, W)`, :math:`(H, W, 3)` is also suitible 
            as long as corresponding ``dataformats`` argument is passed. e.g. CHW, HWC, HW.
        """
        self._get_file_writer().add_summary(
            image(tag, input_image, dataformats=dataformats), global_step, walltime)
        self.flush()

    def add_images(self, tag, input_images, global_step=None, walltime=None, dataformats='NCHW'):
        """Add batched (4D) image data to summary.

        Besides passing 4D (NCHW) numpy.array, you can also pass a list of images of the same size.
        In this case, the ``dataformats`` should be `CHW` or `HWC`.
        Note that this requires the ``pillow`` package.

        :param tag: Data identifier.
        :type tag: str
        :param input_images: Image data. The elements in input_images can either have
                 values in [0, 1] (float32) or [0, 255] (uint8).
                 Users are responsible to scale the data in the correct range/type.
        :type input_images: numpy.array
        :param global_step: Global step value to record.
        :type global_step: int
        :param walltime: Optional override current time of event.
        :type walltime: float

        input_images.shape: Default is :math:`(N, 3, H, W)`, If ``dataformats`` is specified,
            other shape will be accepted. e.g. NCHW or NHWC.
        """
        if isinstance(input_images, list):  # a list of images in CHW or HWC
            if dataformats.upper() != 'CHW' and dataformats.upper() != 'HWC':
                print('A list of image is passed, but the dataformat is neither CHW nor HWC.')
                print('Nothing is written.')
                return

            input_images = np.stack(input_images, 0)
            dataformats = 'N' + dataformats

        self._get_file_writer().add_summary(
            image(tag, input_images, dataformats=dataformats), global_step, walltime)
        self.flush()

    def add_image_with_boxes(self, tag, input_image, input_box, global_step=None,
                             walltime=None, dataformats='CHW', labels=None, 
                             box_color='red', text_color='white', box_thickness=1, **kwargs):
        """Add image and draw bounding boxes on the image.

        :param tag: Data identifier.
        :type tag: str
        :param input_image: Image data.
        :type input_image: numpy.array
        :param input_box: Box data (for detected objects),
                           box should be represented as [x1, y1, x2, y2].
        :type input_box: numpy.array
        :param global_step: Global step value to record.
        :type global_step: int
        :param walltime: Optional override current time of event.
        :type walltime: float
        :param labels: The strings to be shown on each bounding box.
        :type labels: list of string
        :param box_color: The color of box.
        :param text_color: The color of text
        :param box_thickness: The thickness of box edge.
        :type box_thickness: int

        input_image.shape: Default is :math:`(3, H, W)`.
            it can be specified with `dataformat` agrument, e.g. CHW or HWC.

        input_box.shape: N * 4,  where N is the number of boxes and
            each 4 elememts in a row represents (xmin, ymin, xmax, ymax).
        """
        if labels is not None:
            if isinstance(labels, str):
                labels = [labels]
            if len(labels) != input_box.shape[0]:
                logger.warning('Number of labels do not equal to number of box, skip the labels.')
                labels = None

        self._get_file_writer().add_summary(image_boxes(
            tag, input_image, input_box, dataformats=dataformats, labels=labels, 
            box_color=box_color, text_color=text_color, box_thickness=box_thickness, **kwargs),
            global_step, walltime)
        
        self.flush()

    def add_figure(self, tag, figure, global_step=None, close=True, walltime=None):
        """Render matplotlib figure into an image and add it to summary.

        Note that this requires the ``matplotlib`` package.

        :param tag: Data identifier.
        :type tag: str
        :param figure: Figure or a list of figures.
        :type figure: matplotlib.pyplot.figure or list of matplotlib.pyplot.figure
        :param global_step: Global step value to record.
        :type global_step: int
        :param close: Flag to automatically close the figure.
        :type close: bool
        :param walltime: Optional override current time of event.
        :type walltime: float
        """
        if isinstance(figure, list):
            self.add_image(tag, figure_to_image(figure, close), global_step, walltime, dataformats='NCHW')
        else:
            self.add_image(tag, figure_to_image(figure, close), global_step, walltime, dataformats='CHW')
        self.flush()

    def add_video(self, tag, input_video, global_step=None, fps=4, walltime=None):
        """Add video data to summary.

        Note that this requires the ``moviepy`` package.

        :param tag: Data identifier.
        :type tag: str
        :param input_video: Video data.
        :type input_video: numpy.array
        :param global_step: Global step value to record.
        :type global_step: int
        :param fps: Frames Per Second.
        :type fps: float or int
        :param walltime: Optional override current time of event.
        :type walltime: float

        Shape:
            input_video: :math:`(N, T, C, H, W)`. The values should lie
                        in [0, 255] for type `uint8` or [0, 1] for type `float`.
        """
        self._get_file_writer().add_summary(video(tag, input_video, fps), global_step, walltime)
        self.flush()

    def add_audio(self, tag, input_audio, global_step=None, sample_rate=44100, walltime=None):
        """Add audio data to summary.

        :param tag: Data identifier.
        :type tag: str
        :param input_audio: Sound data.
        :type input_audio: numpy.array
        :param global_step: Global step value to record.
        :type global_step: int
        :param sample_rate: sample rate in Hz.
        :type sample_rate: int
        :param walltime: Optional override current time of event.
        :type walltime: float

        Shape:
          input_audio: :math:`(1, L)`. The values should lie between [-1, 1].
        """
        self._get_file_writer().add_summary(
            audio(tag, input_audio, sample_rate=sample_rate), global_step, walltime)
        self.flush()

    def add_text(self, tag, input_text, global_step=None, walltime=None):
        """Add text data to summary.

        :param tag: Data identifier.
        :type tag: str
        :param input_text: String to save.
        :type input_text: str
        :param global_step: Global step value to record
        :type global_step: int
        :param walltime: Optional override current time of event
        :type walltime: float
        """
        self._get_file_writer().add_summary(text(tag, input_text), global_step, walltime)
        self.flush()

    def add_paddle_graph(self, fluid_program, echo_vars=True, **kwargs):
        """ Add paddle graph to summary.

        :param fluid_program: the instance of class paddle.fluid.Program
        :type fluid_program: paddle.fluid.Program
        :param echo_vars: whether to add input/output variables to the graph.
        :type echo_vars: bool
        """
        self._get_file_writer().add_graph(paddle_graph(fluid_program, echo_vars, **kwargs))
        self.flush()

    @staticmethod
    def _encode(rawstr):
        # I'd use urllib but, I'm unsure about the differences from python3 to python2, etc.
        retval = rawstr
        retval = retval.replace("%", "%%%02x" % (ord("%")))
        retval = retval.replace("/", "%%%02x" % (ord("/")))
        retval = retval.replace("\\", "%%%02x" % (ord("\\")))
        return retval

    def add_embedding(self, mat, metadata=None, label_img=None, global_step=None, tag='default', metadata_header=None):
        """Add embedding projector data to summary.

        :param mat: A matrix which each row is the feature vector of the data point.
        :type mat: numpy.array
        :param metadata: A list of labels, each element will be convert to string.
        :type metadata: list.
        :param label_img: Images correspond to each data point.
        :type label_img: numpy.array
        :param global_step: Global step value to record.
        :type global_step: int
        :param tag: Name for the embedding.
        :type tag: str

        Shape:
            mat: :math: (N, D), where N is number of data and D is feature dimension.
            label_img: :math: (N, C, H, W)
        """
        from .x2num import make_np
        mat = make_np(mat)

        if global_step is None:
            global_step = 0

        subdir = "%s/%s" % (str(global_step).zfill(5), self._encode(tag))
        save_path = os.path.join(self._get_file_writer().get_logdir(), subdir)

        try:
            os.makedirs(save_path)
        except OSError:
            print('warning: Embedding dir exists, did you set global_step for add_embedding()?')

        if metadata is not None:
            assert mat.shape[0] == len(metadata), '#labels should equal with #data points'
            make_tsv(metadata, save_path, metadata_header=metadata_header)

        if label_img is not None:
            assert mat.shape[0] == label_img.shape[0], '#images should equal with #data points'
            make_sprite(label_img, save_path)

        assert mat.ndim == 2, 'mat should be 2D, where mat.size(0) is the number of data points'
        make_mat(mat, save_path)
        append_pbtxt(metadata, label_img, self._get_file_writer().get_logdir(), subdir, global_step, tag)
        self.flush()

    def add_pr_curve(self, 
                     tag, 
                     labels, 
                     predictions,
                     global_step=None,
                     num_thresholds=127, 
                     weights=None,
                     walltime=None):
        """Adds precision recall curve.

        Plotting a precision-recall curve lets you understand your model's 
        performance under different threshold settings.
        With this function, you provide the ground truth labeling (T/F)
        and prediction confidence (usually the output of your model) for each target.
        The TensorBoard UI will let you choose the threshold interactively.

        :param tag: Data identifier.
        :type tag: str
        :param labels: Ground truth data. Each element is 0 or 1.
        :type labels: numpy.array
        :param predictions: The probability that an element be classified as true, Value should in [0, 1]
        :type predictions: numpy.array
        :param global_step: Global step value to record.
        :type global_step: int
        :param num_thresholds: Number of thresholds used to draw the curve.
        :type num_thresholds: int
        :param walltime: Optional override current time of event
        :type walltime: float
        """
        from .x2num import make_np
        labels, predictions = make_np(labels), make_np(predictions)
        self._get_file_writer().add_summary(
            pr_curve(tag, labels, predictions, num_thresholds, weights), global_step, walltime)
        self.flush()

    def add_pr_curve_raw(self, 
                         tag, 
                         true_positive_counts,
                         false_positive_counts,
                         true_negative_counts,
                         false_negative_counts,
                         precision,
                         recall,
                         global_step=None,
                         num_thresholds=127,
                         weights=None,
                         walltime=None):
        """Adds precision recall curve with raw data.

        :param tag: Data identifier.
        :type tag: str
        :param true_positive_counts: true positive counts.
        :type true_positive_counts: numpy.array
        :param false_positive_counts: false positive counts.
        :type false_positive_counts: numpy.array
        :param true_negative_counts: true negative counts.
        :type true_negative_counts: numpy.array
        :param false_negative_counts: false negative counts.
        :type false_negative_counts: numpy.array
        :param precision: precision
        :type precision: numpy.array
        :param recall: recall
        :type recall: numpy.array
        :param global_step: Global step value to record
        :type global_step: int
        :param num_thresholds: Number of thresholds used to draw the curve.
        :type num_thresholds: int
        :param walltime: Optional override current time of event
        :type walltime: float
        """
        self._get_file_writer().add_summary(
            pr_curve_raw(
                tag,
                true_positive_counts,
                false_positive_counts,
                true_negative_counts,
                false_negative_counts,
                precision,
                recall,
                num_thresholds,
                weights
                ), global_step, walltime)
        self.flush()

    def add_custom_scalars_multilinechart(self, tags, category='default', title='untitled'):
        """Shorthand for creating multilinechart.

        Similar to ``add_custom_scalars()``, but the only necessary argument is *tags*.

        :param tags: list of tags that have been used in ``add_scalar()``
        :type tags: list of string.
        """
        layout = {category: {title: ['Multiline', tags]}}
        self._get_file_writer().add_summary(custom_scalars(layout))
        self.flush()

    def add_custom_scalars_marginchart(self, tags, category='default', title='untitled'):
        """Shorthand for creating marginchart.
         
        Similar to ``add_custom_scalars()``, but the only necessary argument is *tags*, 
        which should have exactly 3 elements.
          
        :param tags: list of tags that have been used in ``add_scalar()``
        :type tags: list of string.
        """
        assert len(tags) == 3
        layout = {category: {title: ['Margin', tags]}}
        self._get_file_writer().add_summary(custom_scalars(layout))
        self.flush()

    def add_custom_scalars(self, layout):
        """Create special chart by collecting charts tags in 'scalars'.
         
        Note that this function can only be called once for each SummaryWriter() object.
        Because it only provides metadata to tensorboard, the function can be called 
        before or after the training loop.
         
        :param layout: {categoryName: *charts*}, where *charts* is also a dictionary
              {chartName: *ListOfProperties*}. The first element in *ListOfProperties* 
              is the chart's type (one of **Multiline** or **Margin**) and the second 
              element should be a list containing the tags you have used in add_scalar 
              function, which will be collected into the new chart.
        :type layout: dict
        """
        self._get_file_writer().add_summary(custom_scalars(layout))
        self.flush()
         
    def add_mesh(self, tag, vertices, colors=None, faces=None, config_dict=None, global_step=None, walltime=None):
        """Add meshes or 3D point clouds to TensorBoard. 
          
        The visualization is based on Three.js, so it allows users to interact with 
        the rendered object. Besides the basic definitions such as vertices, faces, 
        users can further provide camera parameter, lighting condition, etc.
        Note that currently this depends on tb-nightly to show.
         
        :param tag: Data identifier.
        :type tag: str
        :param vertices: List of the 3D coordinates of vertices.
        :type vertices: numpy.array
        :param colors:  Colors for each vertex
        :type colors: numpy.array
        :param faces: Indices of vertices within each triangle.(Optional)
        :type faces: numpy.array
        :param config_dict: Dictionary with ThreeJS classes names and configuration.
        :type config_dict: dict
        :param global_step: Global step value to record.
        :type global_step: int
        :param walltime: Optional override current time
        :type walltime: float

        Shape:
            vertices: :math:`(B, N, 3)`. (batch, number_of_vertices, channels).
                      If you see nothing on tensorboard, try normalizing the values to [-1, 1].
            colors: :math:`(B, N, 3)`. The values should lie in [0, 255].
            faces: :math:`(B, N, 3)`. The values should lie in [0, number_of_vertices] for type `uint8`.
        """
        self._get_file_writer().add_summary(
            mesh(tag, vertices, colors, faces, config_dict), global_step, walltime
            )
        self.flush()

    def add_hparams(self, hparams, trial_id=None, start_time_secs=None):
        """Write hyperparameter values for a single trial.
         
        :param hparams: A `dict` mapping hyperparameters to the values used in 
            this trial. Keys should be the names of `HParam` objects used in an
            experiment, or the `HParam` objects themselves. Values should be
            Python `bool`, `int`, `float`, or `string` values, depending on
            the type of the hyperparameter.
        :param trial_id: string ID for the set of hyperparameter values used in 
            this trial. Defaults to a hash of the hyperparameters.
        :type trial_id: str, optional
        :param start_time_secs: The time that this trial started training, as
            seconds since epoch. Defaults to the current time.

        Returns:
            A tensor whose value is `True` on success, or `False` if no summary
            was written because no default summary writer was available.
        """
        hparams_summary = hparams_pb(
            hparams=hparams, trial_id=trial_id, start_time_secs=start_time_secs
            )
        self._get_file_writer().add_summary(hparams_summary) 
        self.flush()

    def add_hparams_config(self, hparams, metrics, time_created_secs=None):
        """Write a top-level experiment configuration.

        This configuration describes the hyperparameters and metrics that will
        be tracked in the experiment, but does not record any actual values of
        those hyperparameters and metrics. It can be created before any models
        are actually trained.

        :param hparams: A list of `HParam` object.
        :param metrics: A list of `Metric` object.
        :param time_created_secs: The time that this experiment was created, as
            seconds since epoch. Defaults to the current time.

        Returns:
            A tensor whose value is `True` on success, or `False` if no summary
            was written because no default summary writer was available.
        """
        hparams_config_summary = hparams_config_pb(
            hparams=hparams, metrics=metrics, time_created_secs=time_created_secs
            )
        self._get_file_writer().add_summary(hparams_config_summary)
        self.flush() 

    def close(self):
        if self.all_writers is None:
            return
        for writer in self.all_writers.values():
            writer.flush()
            writer.close()
        self.file_writer = self.all_writers = None
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

