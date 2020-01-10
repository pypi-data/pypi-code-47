import SimpleITK as sitk
import numpy as np
from skimage.measure import find_contours, label, regionprops
from skimage import exposure
import cv2


class MaskCheck(object):
    def __init__(self, path, maskpath, percent=1, win=None, label=None):
        raw = self._get_arr(path)
        raw = MedicalImageDeal(raw, percent=percent).valid_img
        if win is not None:
            raw = np.clip(raw, win[0], win[1])
        mask = self._get_arr(maskpath)
        if label is not None:
            mask = (mask == label).astype(np.uint8)
        self.raw_crop, self.mask_crop, pad, self.cropsize = self._crop(raw, mask)



    @staticmethod
    def _get_arr(path):
        arr = sitk.GetArrayFromImage(sitk.ReadImage(path))
        return arr

    @staticmethod
    def _crop(raw, mask):
        props = regionprops(label(mask))
        """
        get crop size
        """
        prop = regionprops(mask)[0]
        tmp = prop['bbox']
        d = max(tmp[3] - tmp[0], tmp[4] - tmp[1], tmp[5] - tmp[2])
        d = d // 2 * 2 + 2
        cs = max(d, 96)

        centerzyx = np.array(prop['centroid']) + 0.5
        centerzyx = centerzyx.astype(np.int)
        shapez, shapey, shapex = mask.shape
        cz, cy, cx = centerzyx
        crop_raw = raw[max(0, cz - cs // 2):min(cz + cs // 2, shapez),
                   max(0, cy - cs // 2):min(cy + cs // 2, shapey),
                   max(0, cx - cs // 2):min(cx + cs // 2, shapex)]

        crop_mask = mask[max(0, cz - cs // 2):min(cz + cs // 2, shapez),
                    max(0, cy - cs // 2):min(cy + cs // 2, shapey),
                    max(0, cx - cs // 2):min(cx + cs // 2, shapex)]

        padding_left = []
        padding_right = []
        for i in [cz, cy, cs]:
            left = i - cs // 2
            if left < 0:
                padding_left.append(np.abs(left))
            else:
                padding_left.append(0)

        for i, j in zip([cz, cy, cs], mask.shape):
            right = i + cs // 2 - j
            if right > 0:
                padding_right.append(np.abs(right))
            else:
                padding_right.append(0)

        crop_raw_pad = np.pad(crop_raw, ((padding_left[0], padding_right[0]),
                                         (padding_left[1], padding_right[1]),
                                         (padding_left[2], padding_right[2])), "minimum")

        crop_mask_pad = np.pad(crop_mask, ((padding_left[0], padding_right[0]),
                                           (padding_left[1], padding_right[1]),
                                           (padding_left[2], padding_right[2])), "minimum")

        """
        assert
        """
        pad = np.sum(padding_left) + np.sum(padding_right)
        assert crop_raw_pad.shape == (cs, cs, cs)
        assert crop_mask_pad.shape == (cs, cs, cs)
        return crop_raw_pad, crop_mask_pad, pad, cs

    def _plot(self):
        crop_raw = self.normalize(self.raw_crop)
        crop_mask = self.mask_crop
        crop_size = self.cropsize
        mask_indexes = np.where(crop_mask.sum(axis=(1, 2)))[0]
        w = int(np.sqrt(len(mask_indexes))) + 1
        png = np.zeros((crop_size * w,) * 2 + (3,))
        for index, mask_i in enumerate(mask_indexes):
            divide, remain = np.divmod(index, w)
            img = cv2.cvtColor(crop_raw[mask_i], cv2.COLOR_GRAY2BGR)
            contours = find_contours(crop_mask[mask_i], level=0.5)
            contours = [c.astype(np.int)[:, [1, 0]] for c in contours]
            cv2.drawContours(img, contours, -1, (0, 255, 0), thickness=1)
            png_w = divide * crop_size
            png_h = remain * crop_size
            png[png_w:png_w + crop_size, png_h:png_h + crop_size] = img
        return png

    @staticmethod
    def normalize(arr):
        image = (arr - arr.min()) / (arr.max() - arr.min())
        return (image * 255).astype(np.uint8)


class MedicalImageDeal(object):
    def __init__(self, img, percent=1):
        self.img = img
        self.percent = percent

    @property
    def valid_img(self):
        cdf = exposure.cumulative_distribution(self.img)
        watershed = cdf[1][cdf[0] >= self.percent][0]
        return np.clip(self.img, self.img.min(), watershed)

    @property
    def norm_img(self):
        return (self.img - self.img.min()) / (self.img.max() - self.img.min())


# __name__ = ['MaskCheck']


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    fnii = "/data/qingqing1/50634/2000137/50634_2000137_Ax_fs_T2_FRFSE_RT__2_0_0_axial.nii"
    fnrrd = "/data/qingqing1/50634/2000137/50634_2000137_Ax_fs_T2_FRFSE_RT__2_0_0_axialfs_T2.nrrd"
    mask = MaskCheck(fnii, fnrrd)
    png = mask._plot()
    print(png.shape)
    plt.imshow(png.astype(np.uint8))
    plt.show()
    pass


