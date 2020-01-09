"""
Copyright 2017-2018 Fizyr (https://fizyr.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import keras
from keras.utils import get_file, plot_model
import keras_resnet
import keras_resnet.models

from . import retinanet
from . import Backbone
from ..utils.image import preprocess_image


class ResNetBackbone(Backbone):
    """ Describes backbone information and provides utility functions.
    """

    def __init__(self, backbone):
        super(ResNetBackbone, self).__init__(backbone)
        self.custom_objects.update(keras_resnet.custom_objects)

    def retinanet(self, *args, **kwargs):
        """ Returns a retinanet model using the correct backbone.
        """
        return resnet_retinanet(*args, backbone=self.backbone, **kwargs)

    def download_imagenet(self):
        """ Downloads ImageNet weights and returns path to weights file.
        """
        resnet_filename = 'ResNet-{}-model.keras.h5'
        #resnet_resource = 'https://github.com/fizyr/keras-models/releases/download/v0.0.1/{}'.format(resnet_filename)
        depth = int(self.backbone.replace('resnet', ''))

        filename = resnet_filename.format(depth)
        #resource = resnet_resource.format(depth)
        if depth == 18:
            resource = 'https://github.com/qubvel/classification_models/releases/download/0.0.1/resnet18_imagenet_1000.h5'
            checksum = '64da73012bb70e16c901316c201d9803'
        elif depth == 50:
            resource = 'https://github.com/qubvel/classification_models/releases/download/0.0.1/resnet50_imagenet_1000.h5'
            checksum = 'd0feba4fc650e68ac8c19166ee1ba87f'
        elif depth == 101:
            resource = 'https://github.com/qubvel/classification_models/releases/download/0.0.1/resnet101_imagenet_1000.h5'
            checksum = '9489ed2d5d0037538134c880167622ad'
        elif depth == 152:
            resource = 'https://github.com/qubvel/classification_models/releases/download/0.0.1/resnet152_imagenet_1000.h5'
            checksum = '1efffbcc0708fb0d46a9d096ae14f905'

        return get_file(
            filename,
            resource,
            cache_subdir='models',
            md5_hash=checksum
        )

    def validate(self):
        """ Checks whether the backbone string is correct.
        """
        allowed_backbones = ['resnet18', 'resnet50', 'resnet101', 'resnet152']
        backbone = self.backbone.split('_')[0]

        if backbone not in allowed_backbones:
            raise ValueError('Backbone (\'{}\') not in allowed backbones ({}).'.format(backbone, allowed_backbones))

    def preprocess_image(self, inputs):
        """ Takes as input an image and prepares it for being passed through the network.
        """
        return preprocess_image(inputs, mode="tf")


def resnet_retinanet(num_classes, backbone='resnet50', inputs=None, modifier=None, **kwargs):
    """ Constructs a retinanet model using a resnet backbone.

    Args
        num_classes: Number of classes to predict.
        backbone: Which backbone to use (one of ('resnet50', 'resnet101', 'resnet152')).
        inputs: The inputs to the network (defaults to a Tensor of shape (None, None, 3)).
        modifier: A function handler which can modify the backbone before using it in retinanet (this can be used to freeze backbone layers for example).

    Returns
        RetinaNet model with a ResNet backbone.
    """
    # choose default input
    if inputs is None:
        if keras.backend.image_data_format() == 'channels_first':
            inputs = keras.layers.Input(shape=(3, None, None))
        else:
            inputs = keras.layers.Input(shape=(None, None, 3))

    # create the resnet backbone
    if backbone == 'resnet18':
        resnet = keras_resnet.models.ResNet18(inputs, include_top=False, freeze_bn=True)
        plot_model(resnet, show_shapes=True, show_layer_names=True, to_file='ResNet18.png')
    elif backbone == 'resnet50':
        resnet = keras_resnet.models.ResNet50(inputs, include_top=False, freeze_bn=True)
        plot_model(resnet, show_shapes=True, show_layer_names=True, to_file='ResNet50.png')
    elif backbone == 'resnet101':
        resnet = keras_resnet.models.ResNet101(inputs, include_top=False, freeze_bn=True)
        plot_model(resnet, show_shapes=True, show_layer_names=True, to_file='ResNet101.png')
    elif backbone == 'resnet152':
        resnet = keras_resnet.models.ResNet152(inputs, include_top=False, freeze_bn=True)
        plot_model(resnet, show_shapes=True, show_layer_names=True, to_file='ResNet152.png')
    else:
        raise ValueError('Backbone (\'{}\') is invalid.'.format(backbone))

    # invoke modifier if given
    if modifier:
        resnet = modifier(resnet)
        
    print("Se imprimen los outputs")
    print(resnet.summary())
    print(resnet.outputs)

    # create the full model
    return retinanet.retinanet(inputs=inputs, num_classes=num_classes, backbone_layers=resnet.outputs[1:], **kwargs)


def resnet18_retinanet(num_classes, inputs=None, **kwargs):
    r_model = resnet_retinanet(num_classes=num_classes, backbone='resnet18', inputs=inputs, **kwargs)
    plot_model(r_model, show_shapes=True, show_layer_names=True, to_file='ResNet18RetinaNet.png')
    return r_model


def resnet50_retinanet(num_classes, inputs=None, **kwargs):
    r_model = resnet_retinanet(num_classes=num_classes, backbone='resnet50', inputs=inputs, **kwargs)
    plot_model(r_model, show_shapes=True, show_layer_names=True, to_file='ResNet50RetinaNet.png')
    return r_model


def resnet101_retinanet(num_classes, inputs=None, **kwargs):
    r_model = resnet_retinanet(num_classes=num_classes, backbone='resnet101', inputs=inputs, **kwargs)
    plot_model(r_model, show_shapes=True, show_layer_names=True, to_file='ResNet101RetinaNet.png')
    return r_model


def resnet152_retinanet(num_classes, inputs=None, **kwargs):
    r_model = resnet_retinanet(num_classes=num_classes, backbone='resnet152', inputs=inputs, **kwargs)
    plot_model(r_model, show_shapes=True, show_layer_names=True, to_file='ResNet152RetinaNet.png')
    return r_model
