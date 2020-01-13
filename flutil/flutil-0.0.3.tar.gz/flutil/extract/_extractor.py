from typing import List, Union, Iterable
import logging
from pathlib import Path
import pandas as pd
from tqdm import tqdm
import numpy as np
from PIL import Image
from ..shape import Box


class Extractor:
    """An extractor that extracts descriptor(s) from an image.

    Either `_get_descriptor()` or `_get_batch_descrs()` should be implemented
    by child classes.
    """

    def __init__(self, imgs: Iterable[Union[str, Path, Image.Image,
                                            np.ndarray]],
                 bs: int = 1,
                 dets: Iterable[Iterable[Box]] = None,
                 aois: Iterable[Iterable[Box]] = None,
                 include_original=False,
                 include_input=False):
        """
        :param Iterable[Union[str, Path, Image.Image, np.ndarray]] imgs: an
        iterable of paths (type `str` or `pathlib.Path`) pointing to image
        files or an iterable of image objects (type `PIL.Image.Image` or
        `np.ndarray`).  When using a numpy array, The different color
        bands/channels should be stored in the third dimension, such that a
        gray-image is MxN, an RGB-image MxNx3 and an RGBA-image MxNx4.

        :param int bs: (optional) batch size to process the images

        :param Iterable[Iterable[Box]] dets: the detections per image. More
        generally, the regions for which features will be extracted.

        :param Iterable[Iterable[Box]] aois: the areas of interest (AOIs) for
        each image. If a detection does not lie in an AOI, it will be
        discarded.

        :param bool include_original: whether to include the column `original`
        in the returned `DataFrame`. Default: `False`.

        :param bool include_input: include the `PIL.Image` that was used as
        input for the extractor and yielded the descriptor, e.g. the original
        image cropped to the detection region. It will be included in the
        column `input` of the returned `DataFrame`. Default: `False`.
        """
        if hasattr(imgs, '__len__') and hasattr(dets, '__len__'):
            if len(imgs) != len(dets):
                logging.warning('Lengths of imgs and dets are not equal.')

        self.imgs = imgs
        self.img_counter = 0
        self.dets = dets
        self.aois = aois
        self.bs = bs
        self.include_input = include_input
        self.include_original = include_original

    @property
    def imgs(self):
        return self._imgs

    @imgs.setter
    def imgs(self, value):
        self._wip = {'image': None, 'img_counter': None,
                     'nd_img': None, 'detection': None,
                     'aoi': None}
        self._crnt_batch = 0
        self._itsover = False
        self._imgs = value
        self._imgiter = iter(value)

    @property
    def dets(self):
        return self._dets

    @dets.setter
    def dets(self, value):
        self._dets = value
        self._detiter = iter(value) if value is not None else None

    @property
    def aois(self):
        return self._aois

    @aois.setter
    def aois(self, value):
        self._aois = value
        self._aoiiter = iter(value) if value is not None else None

    def _get_descriptor(self, im: np.array) -> np.array:
        """Return the descriptor for an image.

        Either `_get_descriptor` or `_get_batch_descrs` should be implemented
        by child classes.

        :param np.array im: the image array obtained by calling
        ``skimage.io.imread()`` with the image file path as an argument.
        """
        raise NotImplementedError

    def _get_batch_descrs(self, batch: pd.DataFrame) -> List[np.array]:
        """Return the descriptors for a batch of images.

        Either `_get_descriptor` or `_get_batch_descrs` should be implemented
        by child classes.

        :param pd.DataFrame batch: a `DataFrame` representing a batch. Its
        images as nd arrays are in a column named `nd_img`. The column `image`
        contains the path to the original image. Optionally the batch
        `DataFrame` can also contain columns `detection` and `aoi`.
        :returns: a list of descriptors for all the images in the batch
        """
        return [self._get_descriptor(im) for im in batch['nd_img']]

    def _get_ndarray_image(self, img):
        if isinstance(img, np.ndarray):
            return np.array(Image.fromarray(img).convert('RGB'))
        elif isinstance(img, str) or isinstance(img, Path):
            return np.array(Image.open(img).convert('RGB'))
        elif isinstance(img, Image.Image):
            return np.array(img.convert('RGB'))
        else:
            return img

    def _next_batch(self) -> pd.DataFrame:
        """Return a DataFrame representing the next batch.

        The returned `DataFrame` will have these columns:
        - `image`: containing (a reference to) the image
        - `nd_img`: the numpy array from which a descriptor should be extracted

        Optionally, it can have these columns as well:
        - `detection`: the detection region in the image, i.e. the region from
        which `nd_img` was cropped
        - `aoi`: the area of interest in the image. Other parts of the image
        are ignored.
        - `original`: a `PIL.Image` that contains the full, original image
        """
        batch = {k: [] for k in self._wip}

        # If there are detections that belong to the last image of the
        # previous batch, add them to the lists first
        if self._wip['image'] is not None:
            batch = {k: [v] for k, v in self._wip.items()}
            n_dets = len(batch['detection'])
            self._wip = {k: None for k in self._wip}
        else:
            n_dets = 0

        # Add detections until we have at least a batch size of detections
        while n_dets < self.bs:
            try:
                img = next(self._imgiter)
                self.img_counter += 1
                nd_img = self._get_ndarray_image(img)

                if self.aois is not None:
                    img_aois = next(self._aoiiter)
                else:
                    # Use full image region as AOI
                    h, w, _ = nd_img.shape
                    img_aois = [Box.from_width_height(width=w, height=h)]

                if self.dets is not None:
                    img_dets = next(self._detiter)
                else:
                    # We should use the AOI regions as region for extraction
                    img_dets = img_aois
            except StopIteration:
                self._itsover = True
                break

            df_det_aoi = pd.DataFrame([
                {'detection': det, 'aoi': aoi}
                for det in img_dets
                for aoi in img_aois
                if det in aoi and det is not None])

            if not df_det_aoi.empty:
                # Keep the best-fitting AOI per detection, i.e. the AOI with the
                # smallest area
                df_det_aoi['aoi_area'] = (df_det_aoi['aoi']
                                          .apply(lambda aoi: aoi.area))
                df_det_aoi['det_hash'] = (df_det_aoi['detection']
                                          .apply(hash))
                df_det_aoi = (df_det_aoi
                              .sort_values(by='aoi_area')
                              .groupby('det_hash')
                              .first()
                              .reset_index())
                img_dets = list(df_det_aoi['detection'])
                img_aois = list(df_det_aoi['aoi'])

                n_dets += len(img_dets)
            else:
                img_dets = [None]
                img_aois = [None]

            batch['detection'].append(img_dets)
            batch['nd_img'].append(nd_img)
            batch['image'].append(img)
            batch['img_counter'].append(self.img_counter)
            batch['aoi'].append(img_aois)

        # If we have more than a batch size of detections, add the excess of
        # detections to the "work in progress" dict and remove the excess from
        # the list of detections
        # NOTE: we should only remove the excess of detections and should keep
        # the last image, as the last non-excess detections belong to the last
        # image, which should still be in the batch.
        if n_dets > self.bs:
            self._wip['image'] = batch['image'][-1]
            self._wip['img_counter'] = batch['img_counter'][-1]
            self._wip['nd_img'] = batch['nd_img'][-1]

            excess = n_dets - self.bs
            for col in ['detection', 'aoi']:
                if col in batch:
                    self._wip[col] = batch[col][-1][-excess:]
                    batch[col][-1] = batch[col][-1][:-excess]

        # To avoid creating new PIL Image objects for the same image
        def get_pil_img(img, im):
            if isinstance(img, Image.Image):
                return img
            elif isinstance(img, str) or isinstance(img, Path):
                if img not in originals:
                    originals[img] = Image.fromarray(im)
                return originals[img]
            else:
                return Image.fromarray(im)
        originals = {}
        df = pd.DataFrame([{'image': (img
                                      if (isinstance(img, str) or
                                          isinstance(img, Path))
                                      else img_counter),
                            'nd_img': (self.prep_nd_img(im, det)
                                       if det is not None
                                       else im),
                            'detection': det,
                            'original': (get_pil_img(img, im)
                                         if self.include_original
                                         else None),
                            'aoi': aoi}
                           for i, (im,
                                   img,
                                   img_counter,
                                   img_dets,
                                   img_aois) in
                           enumerate(zip(batch['nd_img'],
                                         batch['image'],
                                         batch['img_counter'],
                                         batch['detection'],
                                         batch['aoi']))
                           for det, aoi in zip(img_dets, img_aois)],
                          columns=['image', 'nd_img', 'detection', 'original',
                                   'aoi'])

        return df

    @staticmethod
    def prep_nd_img(nd_img, det):
        """Crop the detection out of the numpy image, keeping the boundary of
        the image into account.

        :param nd.array nd_img: The image as a numpy array
        :param Box det: The detection to crop out of the image

        :returns: The cropped version of the image
        :rtype: nd.array
        """
        def clipx(x, nd_img):
            w = nd_img.shape[1]
            return 0 if x < 0 else w if x > w else int(x)

        def clipy(y, nd_img):
            h = nd_img.shape[0]
            return 0 if y < 0 else h if y > h else int(y)

        return nd_img[clipy(det.y_min, nd_img):clipy(det.y_max,
                                                     nd_img),
                      clipx(det.x_min, nd_img):clipx(det.x_max,
                                                     nd_img)]

    def clean_row(self, row):
        if not self.aois and 'aoi' in row.index:
            row.drop(index='aoi', inplace=True)
        if not self.dets and 'detection' in row.index:
            row.drop(index='detection', inplace=True)
        if not self.include_original and 'original' in row.index:
            row.drop(index='original', inplace=True)
        if not self.include_input and 'input' in row.index:
            row.drop(index='input', inplace=True)
        return row

    def get_descriptors(self) -> pd.DataFrame:
        """Return the descriptors for all images and their detections.

        :returns: a pandas DataFrame with the descriptors for the given images,
        optionally with the aois and detections that were used, and the columns
        `original` and/or `input`, depending on the values of
        `self.include_original` and `self.include_input`.
        :rtype: pd.DataFrame
        """
        return (pd.DataFrame([*tqdm(self,
                                    total=len(self))])
                .reset_index(drop=True))

    def __len__(self):
        if self.dets is not None:
            return (sum(1 for imdets in self.dets for _ in imdets)
                    if hasattr(self.dets, '__len__') else None)
        else:
            return len(self.imgs) if hasattr(self.imgs, '__len__') else None

    def _raw_iter(self):
        while not self._itsover:
            batch = self._next_batch()
            if len(batch) == 0:
                break

            with_dets_mask = batch[batch['detection'].notna()].index
            descrs = self._get_batch_descrs(batch.loc[with_dets_mask])

            # Clean up columns
            if 'nd_img' in batch.columns:
                if self.include_input:
                    batch['input'] = (batch['nd_img']
                                      .apply(Image.fromarray))
                batch.drop(columns='nd_img', inplace=True)
            else:
                logging.warning('Batch does not include a column named '
                                '"nd_img".')

            gen_descrs = (d for d in descrs)
            batch['descriptor'] = [next(gen_descrs)
                                   if idx in with_dets_mask
                                   else None
                                   for idx, row in batch.iterrows()]

            for _, row in batch.iterrows():
                yield row

            self._crnt_batch += 1

    def __iter__(self):
        for row in self._raw_iter():
            yield self.clean_row(row)
