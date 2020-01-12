from . import ColorMode

import tensorflow as tf
import numpy as np
import multiprocessing


def resize_and_change_color(image, labels, size, color_mode, resize_method='resize_with_pad'):

    if color_mode == ColorMode.RGB and image.shape[-1] == 1:
        image = tf.image.grayscale_to_rgb(image)

    elif color_mode == ColorMode.GRAY and image.shape[-1] != 1:
        image = tf.image.rgb_to_grayscale(image)

    if size is not None:
        # make 3dim for tf.image.resize
        labels = tf.expand_dims(labels, axis=-1)

        # augmentatations
        if resize_method == 'resize':
            image = tf.image.resize(image, size[::-1], antialias=True)
            labels = tf.image.resize(labels, size[::-1], method='nearest')  # use nearest for no interpolation

        elif resize_method == 'resize_with_pad':
            image = tf.image.resize_with_pad(image, size[1], size[0], antialias=True)
            labels = tf.image.resize_with_pad(labels, size[1], size[0], method='nearest')  # use nearest for no interpolation

        elif resize_method == 'resize_with_crop_or_pad':
            image = tf.image.resize_with_crop_or_pad(image, size[1], size[0])
            labels = tf.image.resize_with_crop_or_pad(labels, size[1], size[0])  # use nearest for no interpolation
        else:
            raise Exception("unknown resize method %s" % resize_method)

        # reduce dim added before
        labels = tf.squeeze(labels, axis=-1)
    return image, labels


def get_preprocess_fn(size, color_mode, resize_method, scale_labels=False, is_training=True):

    def map_fn(image, labels, num_classes):

        # scale between 0 and 1
        image = tf.image.convert_image_dtype(image, tf.float32)

        # resize method for image create float32 image anyway
        image, labels = resize_and_change_color(image, labels, size, color_mode, resize_method=resize_method)

        if scale_labels:
            num_classes = tf.cast(num_classes, tf.float32)
            labels = tf.cast(labels, tf.float32)
            labels = labels / (num_classes - 1.0)
        else:
            num_classes = tf.cast(num_classes, tf.int32)  # cast for onehot to accept it
            labels = tf.cast(labels, tf.int64)
            labels = tf.one_hot(labels, num_classes)

        return image, labels

    return map_fn


def prepare_dataset(dataset, batch_size, num_threads=8, buffer_size=200, repeat=0, take=0, skip=0, num_workers=1, worker_index=0, cache=False, augment_fn=None):

    if num_workers > 1:
        dataset = dataset.shard(num_workers, worker_index)

    if skip > 0:
        dataset = dataset.skip(skip)

    if take > 0:
        dataset = dataset.take(take)

    if cache:
        dataset = dataset.cache()

    if repeat > 0:
        dataset = dataset.repeat(repeat)
    else:
        dataset = dataset.repeat()

    dataset = dataset.shuffle(buffer_size=buffer_size)
    dataset = dataset.batch(batch_size)

    if augment_fn:
        dataset = dataset.map(augment_fn, num_parallel_calls=multiprocessing.cpu_count())

    # dataset = dataset.prefetch(buffer_size=buffer_size)
    dataset = dataset.prefetch(buffer_size // batch_size)
    return dataset


def random_flip(**args):
    bool_right_left = tf.random.uniform(shape=[], minval=0, maxval=1, dtype=tf.int32) == tf.constant(1, dtype=tf.int32)
    bool_up_down = tf.random.uniform(shape=[], minval=0, maxval=1, dtype=tf.int32) == tf.constant(1, dtype=tf.int32)

    for k, x in args.items():
        x = tf.cond(bool_right_left, lambda: tf.image.flip_left_right(x), lambda: x)
        x = tf.cond(bool_up_down, lambda: tf.image.flip_up_down(x), lambda: x)
        args[k] = x

    return args


def random_rot180(**args):

    angle = tf.random.uniform(shape=[], minval=0, maxval=1, dtype=tf.int32) * 2
    for k, x in args.items():
        x = tf.image.rot90(x, angle)
        args[k] = x
    return args


def random_color(**args):

    for k, x in args.items():
        x = tf.image.random_hue(x, 0.08)
        x = tf.image.random_saturation(x, 0.6, 1.6)
        x = tf.image.random_brightness(x, 0.05)
        x = tf.image.random_contrast(x, 0.7, 1.3)
        args[k] = x
    return args


def random_zoom(size, **args):

    # Generate 20 crop settings, ranging from a 1% to 20% crop.
    scales = list(np.arange(0.8, 1.0, 0.01))
    boxes = np.zeros((len(scales), 4))

    for i, scale in enumerate(scales):
        x1 = y1 = 0.5 - (0.5 * scale)
        x2 = y2 = 0.5 + (0.5 * scale)
        boxes[i] = [x1, y1, x2, y2]

    def random_crop(img):
        # Create different crops for an image
        crops = tf.image.crop_and_resize(img, boxes=boxes, box_indices=np.zeros(len(scales)), crop_size=size, method='nearest')
        # Return a random crop
        return crops[tf.random.uniform(shape=[], minval=0, maxval=len(scales), dtype=tf.int32)]

    choice = tf.random.uniform(shape=[], minval=0., maxval=1., dtype=tf.float32)
    for k, x in args.items():
        # Only apply cropping 50% of the time
        args[k] = tf.cond(choice < 0.5, lambda: x, lambda: random_crop(x))

    return args


def get_augment_fn(size):

    def augment(images, labels):

        # random rotation
        rot180 = random_rot180(images=images, labels=labels)
        images, labels = rot180['images'], rot180['labels']

        # random flipping
        flip = random_flip(images=images, labels=labels)
        images, labels = flip['images'], flip['labels']

        # random zoom
        zoom = random_zoom(size, images=images, labels=labels)
        images, labels = zoom['images'], zoom['labels']

        images = random_color(images=images)['images']
        # clip images
        images = tf.clip_by_value(images, 0, 1)
        # sizes must be def
        images = tf.reshape(images, tf.convert_to_tensor([8, size[1], size[0], 3]))
        labels = tf.reshape(labels, tf.convert_to_tensor([8, size[1], size[0], 2]))
        return (images, labels)

    return augment
