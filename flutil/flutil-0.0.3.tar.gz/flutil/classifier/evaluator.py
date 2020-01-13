import pandas as pd
import numpy as np
import seaborn as sns
import itertools
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import precision_recall_fscore_support as prfs
from sklearn.metrics import average_precision_score
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
from concurrent.futures import ProcessPoolExecutor
from . import Classifier
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import logging
from PIL import Image, ImageDraw, ImageColor
from ..shape import Box
import copy


def split_gallery_query(df, n_gallery=1, n_query=None,
                        fmax_gallery=1.0, seed=None,
                        gallery_mask=None, query_mask=None):
    """Return a tuple of a randomly selected gallery and query DataFrame.

    :param DataFrame df: the DataFrame to select the gallery and query
    items from. It must contain a column 'label'.
    :param int n_gallery: the number of gallery items per id
    :param int n_query: the number of gallery items per id, if `None` the
    resulting
    :param float fmax_gallery: the maximal fraction of gallery items
    compared to the total amount of descriptors for an id
    :param int seed: seed for the random generator
    :param np.array gallery_mask: mask for selecting the rows in the DataFrame
    that are valid gallery items. If None, all rows are assumed to be valid.
    :param np.array query_mask: mask for selecting the rows in the DataFrame
    that are valid query items. If None, all rows are assumed to be valid.
    :returns: a tuple of a randomly selected gallery and query DataFrame.
    :rtype: tuple
    """
    df_gallery = pd.DataFrame(columns=df.columns)
    df_queries = pd.DataFrame(columns=df.columns)

    if gallery_mask is None:
        gallery_mask = np.ones(len(df.index), dtype=bool)
    if query_mask is None:
        query_mask = np.ones(len(df.index), dtype=bool)

    for name, group in df[gallery_mask].groupby('label'):
        group_len = len(group.index)

        if group_len < n_gallery:
            logging.warning(f'{name} has not enough gallery items '
                            f'(has {group_len} items, needs {n_gallery}). '
                            'It will be left out.')
            continue

        n = int(min(n_gallery, group_len*fmax_gallery))

        if group_len >= n:
            label_gallery = group.sample(n=n, random_state=seed)

            label_query = df[query_mask].copy()
            label_query = label_query[label_query['label'] == name]
            label_query = label_query.drop([i for i in label_gallery.index
                                            if i in label_query.index])
            if n_query is not None:
                if n_query > len(label_query):
                    raise ValueError(f'Not enough rows of label "{name}" '
                                     f'to create {n_gallery} gallery '
                                     f'item{"" if n_gallery == 1 else "s"} '
                                     f'and {n_query} query '
                                     f'item{"" if n_query == 1 else "s"} '
                                     f'for that label.')
                label_query = label_query.sample(n=n_query,
                                                 random_state=seed)

            df_gallery = pd.concat([df_gallery, label_gallery],
                                   ignore_index=True)
            df_queries = pd.concat([df_queries, label_query],
                                   ignore_index=True)

    # Add rows with labels that are not in gallery
    gallery_labels = df_gallery['label'].unique().tolist()
    unkown_label_rows = df[df.apply(lambda row: (row['label']
                                                 not in gallery_labels),
                                    axis=1)
                           & query_mask]
    df_queries = pd.concat([df_queries, unkown_label_rows],
                           ignore_index=True)

    return df_gallery, df_queries


def get_crop_box(focus_box: Box, crop_margin):
    size = max(focus_box.width, focus_box.height)*crop_margin
    return Box.from_width_height(width=size, height=size,
                                 center=focus_box.center).to_int()


def create_thumb(img: str, crop_box: Box, focus_box: Box, color: str = None,
                 alpha: float = 0.6) -> Image:
    """Return the thumbnail that displays the box's region on the image.

    A thumbnail displays a cropped version of the image, cropped (with a
    certain margin) around the box of the respective row. The box
    region is marked by adding a colored overlay to those parts of the image
    that do not belong to the box.

    :param str img: the image path
    :param Box box: the rectangular region of interest
    :param str color: the color to use for the overlay. If `None`, it will be
    set to 'black'.
    :param float alpha: the opacity between 0 (completely transparent) and 1
    (completely opaque) of the colored overlay.
    """
    im = Image.open(img).convert('RGBA')

    # Crop and scale the image
    im = im.crop(crop_box)

    # Add colored overlay
    if color is None:
        color = 'black'
    color = list(ImageColor.getcolor(color, 'RGBA'))
    color[3] = int(255*alpha)
    overlay = Image.new('RGBA', im.size, tuple(color))
    d = ImageDraw.Draw(overlay)

    # Transform focus box to crop box coordinates
    fbox_tf = focus_box - (crop_box.x_min, crop_box.y_min)
    # Make the focus box region transparant
    d.rectangle(tuple(fbox_tf.to_int()), fill=(0, 0, 0, 0))

    # Put it all together
    im = Image.alpha_composite(im, overlay).convert('RGB')
    return im


def get_colors_from_df(df):
    """Return
    """
    if 'color' in df.columns:
        return df['color'].values.tolist()
    elif ('label' in df.columns
          and 'pred_label' in df.columns):
        return ['green' if (label == pred_label) else 'red'
                for label, pred_label in zip(df['label'],
                                             df['pred_label'])]
    else:
        return ['black']*len(df)


def get_focus_boxes_from_df(df):
    if 'annot' in df.columns:
        return df['annot'].values.tolist()
    elif 'detection' in df.columns:
        return df['detection'].values.tolist()
    elif 'image' in df.columns:
        return (df['image']
                .apply(lambda img:
                       Box.from_width_height(*Image.open(img).size))
                .values.tolist())
    else:
        raise ValueError('Boxes could not be created from the DataFrame. '
                         'Make sure the DataFrame contains either of these '
                         'columns: annot, detection, image.')


def add_patches(ax, patchable, **kwargs):
    if 'color' in kwargs:
        color = kwargs['color']
        del kwargs['color']
    else:
        color = 'green'
    if 'linewidth' in kwargs:
        linewidth = kwargs['linewidth']
        del kwargs['linewidth']
    else:
        linewidth = 2.0

    for patch in patchable.to_patches(color=color, linewidth=linewidth,
                                      **kwargs):
        ax.add_patch(patch)

    return ax


def compose_axis(ax, im, row, crop_box, title_cols,
                 annot_kwargs={},
                 det_kwargs={}):
    ax.set_axis_off()
    ax.imshow(im)

    shift = (crop_box.x_min, crop_box.y_min)
    if 'annot' in row.index:
        add_patches(ax, row['annot'] - shift, **annot_kwargs)
    if 'detection' in row.index:
        add_patches(ax, row['detection'] - shift, **det_kwargs)

    if isinstance(title_cols, str):
        title_cols = [title_cols]
    ax.set_title(' | '.join([str(row[t])
                             for t in title_cols
                             if t in row.index]))
    return ax


def get_grid_size_from_df(df, aspect=1):
    grid_size = np.sqrt(len(df))
    ncols = int(np.ceil(grid_size / np.sqrt(aspect)))
    nrows = int(np.ceil(grid_size * np.sqrt(aspect)))
    assert ncols * nrows >= len(df)
    return ncols, nrows


def convert_callable_kwargs(kwargs_with_callables, args_for_callables) -> dict:
    """Return a copy of `kwargs_with_callables` where all callables are
    converted into their return values.

    :param dict kwargs_with_callables: a dict with kwargs where some kwargs are
    callable
    :param list args_for_callables: the args to use when calling a callable
    from the `kwargs_with_callables`
    :returns: a copy of `kwargs_with_callables` where all callables are
    converted into their return values.
    :rtype: dict
    """
    # Convert kwarg callables to values
    callables = {k: v for k, v in kwargs_with_callables.items()
                 if callable(v)}

    kwargs_copy = copy.deepcopy(kwargs_with_callables)
    if callables:
        for k, v in callables.items():
            kwargs_copy[k] = v(*args_for_callables)

    return kwargs_copy


def create_img_grid(df: pd.DataFrame, fig_size=None, crop_margin=2, alpha=0.8,
                    aspect=1,
                    ncols=None,
                    nrows=None,
                    title_cols=['label', 'pred_label', 'pred_score'],
                    njobs=None,
                    pad=(0.2, 0.2),
                    dpi=100,
                    annot_kwargs: dict = {}, det_kwargs: dict = {}):
    """Return Figure of image grid displaying the images in the `DataFrame`.

    :param `DataFrame` df: The `DataFrame` must have the column:

    - 'image': the file path of the gallery image

    Optionally, it can also have these columns:

    - 'label': the true label
    - 'pred_label': the predicted label
    - 'pred_score': the prediction score
    - 'annot': the annotation to which the true label belongs
    - 'detection': the detection from which a descriptor was extracted
    - 'color': the color to give the image overlay

    If the `DataFrame` contains a column 'box', the image will be
    cropped around this annotation region. The annotation boundaries will
    be shown in green in the grid, unless specified otherwise using the
    `annot_kwargs` dict. If the `DataFrame` also contains a column
    'detection', it will be shown in blue in the grid, unless specified
    otherwise using the `det_kwargs` dict. If the `DataFrame` only contain
    a column 'detection', the images will be cropped around the detection
    region.

    If the `DataFrame` contains a column 'label' and 'pred_label', these
    will be shown in the title of each image. Correct classifications will
    get a green border, wrong classifications will get a red border.

    If the `DataFrame` contains a column 'pred_score', the score will be
    mentioned in the title of each image.

    :param tuple fig_size: the matplotlib `Figure` size
    :param float crop_margin: the (relative) margin to leave between the image
    border and the detected or annotated region. E.g. `2` means that the width
    and height of the image will be twice as long as the width and height of
    the detection or annotation.
    :param float alpha: the alpha value of the colored overlays
    :param float aspect: the aspect ratio (width/height) of the grid
    :param int ncols: the number of columns to use, overrides `aspect`
    parameter
    :param int nrows: the number of rows to use, overrides `aspect`
    parameter
    :param list title_cols: the columns from which to use the value in the
    title
    :param int njobs: the number of jobs to use in parallel
    :param tuple pad: the relative padding around each image
    :param float dpi: the dpi of the grid
    :param dict annot_kwargs: kwargs passed to the annotation's `to_patches()`
    method. The values can be either true values or callables taking the images
    width and height as arguments and returning the desired value based on the
    with and height.
    :param dict det_kwargs: kwargs passed to the detection's `to_patches()`
    method. The values can be either true values or callables taking the images
    width and height as arguments and returning the desired value based on the
    with and height.
    :returns: matplotlib Figure with the grid
    :rtype: plt.Figure
    """
    colors = get_colors_from_df(df)
    focus_boxes = get_focus_boxes_from_df(df)
    crop_boxes = [get_crop_box(box, crop_margin)
                  for box in focus_boxes]

    if njobs == 1:
        thumbs = [create_thumb(*args)
                  for args in zip(df['image'],
                                  crop_boxes,
                                  focus_boxes,
                                  colors,
                                  [alpha]*len(df))]

    else:
        with ProcessPoolExecutor(max_workers=njobs) as executor:
            thumbs = executor.map(create_thumb,
                                  df['image'],
                                  crop_boxes,
                                  focus_boxes,
                                  colors,
                                  [alpha]*len(df))

    if 'detection' in df.columns:
        det_kwargs = [convert_callable_kwargs(det_kwargs,
                                              [det.width, det.height])
                      for det in df['detection']]
    else:
        det_kwargs = [{} for _ in range(len(df))]

    if 'annot' in df.columns:
        annot_kwargs = [convert_callable_kwargs(annot_kwargs,
                                                [annot.width, annot.height])
                        for annot in df['annot']]
    else:
        annot_kwargs = [{} for _ in range(len(df))]

    if nrows is None and ncols is None:
        nrows, ncols = get_grid_size_from_df(df, aspect)
    elif nrows is None:
        nrows = 1
    elif ncols is None:
        ncols = 1

    if fig_size is None:
        fig_size = (ncols*2.5, nrows*2.5)

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols,
                             figsize=fig_size, squeeze=False, dpi=dpi,
                             gridspec_kw={'wspace': pad[0], 'hspace': pad[1]})

    for ax, t, (_, row), c_box, a_kws, d_kws in zip(axes.flatten(),
                                                    thumbs,
                                                    df.iterrows(),
                                                    crop_boxes,
                                                    annot_kwargs,
                                                    det_kwargs):
        compose_axis(ax, t, row, c_box, title_cols, a_kws, d_kws)

    for ax in axes.flatten()[len(df):]:
        ax.remove()

    plt.close(fig)
    return fig


class Result:
    def __init__(self, query_data: pd.DataFrame, classifier: Classifier):
        """Initialize Result object.

        :param pd.DataFrame query_data: DataFrame object with columns:
        - 'descriptor': the descriptor to classify
        - 'label': the true label
        :param Classifier classifier: the `Classifier` object that will
        classify the descriptors
        """
        self.query_data = query_data
        self.gallery_data = classifier.train_data
        self.classifier = classifier
        self.true_labels = self.query_data.label.values
        self.classes = self.gallery_data.label.unique()

        self._pr = None
        self._score_mat = None
        self._gal_labels = None
        self._pred_labels = None
        self._score_mat = None
        self._gal_labels = None
        self._df_clf = None
        self._inspector = None
        self._confusion = None

    @property
    def df_clf(self):
        if self._df_clf is None:
            self._df_clf = self.classifier.classify(self.query_data)
        return self._df_clf

    @property
    def pred_labels(self):
        return self.df_clf['label'].values

    @property
    def pred_scores(self):
        return self.df_clf['score'].values

    @property
    def score_matrix(self):
        if self._score_mat is None:
            score_mat, gal_labels = (self.classifier
                                     .get_score_mat(self.query_data))
            self._score_mat = score_mat
            self._gal_labels = gal_labels
        return self._score_mat

    @property
    def gallery_labels(self):
        if self._gal_labels is None:
            score_mat, gal_labels = (self.classifier
                                     .get_score_mat(self.query_data))
            self._score_mat = score_mat
            self._gal_labels = gal_labels
        return self._gal_labels

    @property
    def pr(self):
        if self._pr is None:
            self._pr = PR(true_labels=self.true_labels,
                          score_matrix=self.score_matrix,
                          gallery_labels=self.gallery_labels,
                          pred_labels=self.pred_labels)
        return self._pr

    @property
    def inspector(self):
        if self._inspector is None:
            self._inspector = Inspector(self.query_data,
                                        self.gallery_data,
                                        self.pred_labels,
                                        self.pred_scores)
        return self._inspector

    @property
    def confusion(self):
        if self._confusion is None:
            self._confusion = Confusion(self.true_labels,
                                        self.pred_labels)
        return self._confusion


class Inspector:
    def __init__(self, query_data: pd.DataFrame, gallery_data: pd.DataFrame,
                 pred_labels: np.array, pred_scores: np.array):
        """Class to intuitively inspect a classification result.

        :param pd.DataFrame query_data: `DataFrame` object that contains the
        queries of the classification. It must have the columns:
        - 'image': the file path of the query image
        - 'label': the true label
        Optionally, it can also have these columns:
        - 'annot': the annotation to which the label belongs
        - 'detection': the detection from which a descriptor was extracted
        :param pd.DataFrame gallery_data: `DataFrame` object that contains the
        gallery items, i.e. the "reference images". The `DataFrame` must have
        the columns:

        - 'image': the file path of the gallery image
        - 'label': the true label

        Optionally, it can also have these columns:

        - 'annot': the annotation to which the label belongs
        - 'detection': the detection from which a descriptor was extracted

        Note that multiple gallery items can correspond to the same label, i.e.
        there might be multiple reference images for the same label.
        :param np.array pred_labels: the predicted label for each query
        item. The order of the labels must match the order of the rows in the
        `query_data` `DataFrame`.
        :param np.array pred_scores: the prediction scores for each
        prediction. The order of the scores must match the order of the rows in
        the `query_data` `DataFrame`.
        """
        self.query_data = query_data
        self.gallery_data = gallery_data
        self.query_data['pred_label'] = pred_labels
        self.query_data['pred_score'] = pred_scores
        self.true_labels = query_data['label'].values
        self.pred_labels = pred_labels
        self.pred_scores = pred_scores

    @staticmethod
    def _get_ordered_masked_N(df, idxs, mask, N):
        """Return the N first elements from the `DataFrame`, selected with
        `mask` and ordered with `idx`.
        """
        if not any(mask):
            logging.info('The mask contains no True value.')

        return df.iloc[idxs][mask[idxs]].iloc[:N]

    def show_query(self, true_label=None, pred_label=None,
                   correct=None, highest=None, N=9, **kwargs):
        """Return a matplotlib figure with a visualization of the query.

        :param true_label: (optional) filter on true labels, can be str of list
        of str. None means don't filter.
        :param pred_label: (optional) filter on predicted labels, can be str of
        list of str. None means don't filter.
        :param bool correct: (optional) True means: only show correct
        predictions; False means: only show wrong predictions. None means don't
        filter.
        :param bool highest: (optional) True means: sort the results from
        highest to lowest score; False means: sort the results from lowest to
        highest score. None means: use the order from the `DataFrame`.
        :param int N: (optional) the number of queries to show in the grid,
        default: 9.
        :param kwargs: kwargs passed to `create_img_grid()`
        """
        data = self.query_data

        if true_label is not None:
            if isinstance(true_label, str):
                data = data[data['label'] == true_label]
            elif isinstance(true_label, list):
                data = data[data.label.apply(lambda l: l in true_label)]

        if pred_label is not None:
            if isinstance(pred_label, str):
                data = data[data['pred_label'] == pred_label]
            elif isinstance(pred_label, list):
                data = data[data.pred_label.apply(lambda l: l in pred_label)]

        if correct is not None:
            if correct:
                data = data[data['label'] == data['pred_label']]
            else:
                data = data[data['label'] != data['pred_label']]

        if highest is not None:
            if highest:
                data = data.iloc[np.argsort(data.pred_score)[::-1]]
            else:
                data = data.iloc[np.argsort(data.pred_score)]

        return create_img_grid(data[:N], **kwargs)

    def show_gallery(self, label=None, **kwargs):
        """Return a matplotlib figure with a label's gallery.

        :param label: (optional) the label or list of labels to show the
        gallery from, if `None` show full gallery
        :param kwargs: kwargs passed to `create_img_grid()`
        """
        if label is None:
            mask = [True]*len(self.gallery_data)
        elif isinstance(label, list):
            mask = self.gallery_data['label'].apply(lambda l: l in label)
        else:
            mask = self.gallery_data['label'] == label
        return create_img_grid(self.gallery_data[mask], **kwargs)


class PR:
    def __init__(self,
                 true_labels: np.array,
                 score_matrix: np.array,
                 gallery_labels: np.array=None,
                 pred_labels: np.array=None,
                 average='weighted'):
        """PR result of a classification.

        :param np.array true_labels: the true labels of the queries
        :param np.array score_matrix: the score matrix. Each row is a query,
        each column a gallery item.
        :param np.array gallery_labels: the labels of the gallery items, i.e.
        the labels that belong to each column in the score matrix
        (`score_matrix`). If `None`, the entries will be taken by calling
        `np.unique()` with `true_labels`.
        :param np.array pred_labels: the predicted labels of the queries. If
        `None`, the label with the maximum score in `score_matrix` will be
        used.
        :param str average: how multi-class classifications should be averaged
        (see also
        https://scikit-learn.org/stable/modules\
        /model_evaluation.html\
        #from-binary-to-multiclass-and-multilabel)
        """
        if gallery_labels is None:
            gallery_labels = np.unique(true_labels)

        if pred_labels is None:
            pred_labels = gallery_labels[np.argmax(score_matrix, axis=1)]

        self._true_labels = true_labels
        self._pred_labels = pred_labels
        self._score_mat = score_matrix
        self._gal_labels = gallery_labels
        self.avg = average

        self._mAP = None
        self._prfs = None
        self._curve = None

    @property
    def mAP(self):
        """The mean of the Average Precisions (AP) of all the classes."""
        if self._mAP is None:
            y_true = (self._gal_labels == self._true_labels[:, np.newaxis])
            self._mAP = average_precision_score(y_true.ravel(),
                                                self._score_mat.ravel())
        return self._mAP

    @property
    def prfs(self):
        """Tuple of precision, recall, f1-score and support."""
        if self._prfs is None:
            self._prfs = prfs(self._true_labels,
                              self._pred_labels,
                              average=self.avg)
        return self._prfs

    @property
    def p(self):
        """The average of the Precisions of all the classes."""
        return self.prfs[0]

    @property
    def r(self):
        """The average of the Recalls of all the classes."""
        return self.prfs[1]

    @property
    def f1(self):
        """The average of the F1-scores of all the classes."""
        return self.prfs[2]

    @property
    def support(self):
        """The number of occurrences of each label in y_true."""
        return self.prfs[3]

    @property
    def curve(self):
        """
        A tuple with precisions, recalls and thresholds.

        Note: precision and recall are micro-averaged over all classes.
        """
        if self._curve is None:
            y_true = (self._gal_labels == self._true_labels[:, np.newaxis])
            self._curve = precision_recall_curve(y_true.ravel(),
                                                 self._score_mat.ravel())

        return self._curve

    def plot(self, ax=None, **kwargs) -> Axes:
        """Return a plot of precision and recall."""
        if ax is None:
            _, ax = plt.subplots()

        # Plot PR-curve
        ax.plot(self.curve[1], self.curve[0], **kwargs)
        ax.set_xlabel('Recall')
        ax.set_ylabel('Precision')
        ax.set_ylim([0.0, 1.05])
        ax.set_xlim([0.0, 1.0])
        return ax


class Grid:
    def __init__(self, df_gs):
        """Interpretation of a grid search result.

        :param pd.DataFrame df_gs: `DataFrame` containing the result of the
        grid search. The column names should be the same as the keys in the
        `cv_reslts_` attribute of `sklearn.model_selection.GridSearchCV`.
        """
        self.df_gs = df_gs

    def plot(self, param_x, param_y,
             metric='mean_test_score',
             **kwargs) -> Axes:
        """
        Return a plot of the validation accuracy for the different parameter
        values.

        :param param_x: the parameter values shown on the x-axis.
        :param param_y: the parameter values shown on the y-axis.
        :param metric: the metric shown as function of `param_x` and `param_y`
        :param kwargs: passed to `seaborn.heatmap()`
        """
        ax = sns.heatmap(self.df_gs.pivot_table(values=metric,
                                                index=f'param_{param_y}',
                                                columns=f'param_{param_x}'),
                         **kwargs)
        ax.set_xlabel(param_x.title())
        ax.set_ylabel(param_y.title())
        return ax


class Confusion:
    def __init__(self, true_labels, pred_labels):
        """Confusion matrix for a single-label multi-class classification.

        :param nd.array true_labels: the true labels
        :param nd.array pred_labels: the predicted labels
        """
        self._matrix = None
        self.true_labels = true_labels
        self.pred_labels = pred_labels
        self.labels = unique_labels(true_labels, pred_labels)

    @property
    def matrix(self):
        if self._matrix is None:
            self._matrix = confusion_matrix(self.true_labels,
                                            self.pred_labels)

        return self._matrix

    def plot(self, ax=None, normalize=False, **kwargs) -> Axes:
        if normalize:
            cm = (self.matrix.astype('float')
                  / self.matrix.sum(axis=1)[:, np.newaxis])
        else:
            cm = self.matrix

        n_classes = len(self.labels)
        if ax is None:
            _, ax = plt.subplots(figsize=(n_classes/2, n_classes/2))

        if 'cmap' in kwargs:
            cmap = kwargs['cmap']
            del kwargs['cmap']
        else:
            cmap = plt.cm.Blues

        ax.imshow(cm, cmap=cmap, **kwargs)

        tick_marks = np.arange(n_classes)
        ax.set_xticks(tick_marks)
        ax.set_xticklabels(self.labels, rotation=45)
        ax.set_yticks(tick_marks)
        ax.set_yticklabels(self.labels)

        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]),
                                      range(cm.shape[1])):
            ax.text(j, i, format(cm[i, j], fmt),
                    horizontalalignment="center",
                    color="white" if cm[i, j] > thresh else "black")

        ax.set_ylabel('True label')
        ax.set_xlabel('Predicted label')
        return ax
