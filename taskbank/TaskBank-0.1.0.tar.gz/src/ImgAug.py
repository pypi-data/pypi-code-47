from imgaug import augmenters as iaa  # https://imgaug.readthedocs.io/en/latest/source/overview_of_augmenters.html


def img_aug(**kwargs):
    augment_keywords = ["image", "images", "heatmaps", "segmentation_maps", "keypoints", "bounding_boxes", "polygons", "line_strings"]
    f = kwargs.pop("f", "Noop")
    sometimes = kwargs.pop("sometimes", 1)
    augment_kwargs = {k: kwargs.pop(k, None) for k in augment_keywords if k in kwargs}
    for k, v in kwargs.items():
        if isinstance(v, str):
            if v.split("(")[0] == "tuple":
                v = v.replace("(", ',').replace(")", ',').split(',')
                kwargs[k] = float(v[1]), float(v[2])
    out = iaa.Sometimes(sometimes, getattr(iaa, f)(**kwargs)).augment(**augment_kwargs)
    return out
