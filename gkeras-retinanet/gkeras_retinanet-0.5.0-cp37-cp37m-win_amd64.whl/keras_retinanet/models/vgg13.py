"""
Copyright 2017-2018 cgratie (https://github.com/cgratie/)

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

from . import retinanet
from . import Backbone
from ..utils.image import preprocess_image
from .vgg13Model import VGG13


class VGG13Backbone(Backbone):
    """ Describes backbone information and provides utility functions.
    """

    def retinanet(self, *args, **kwargs):
        """ Returns a retinanet model using the correct backbone.
        """
        return vgg13_retinanet(*args, backbone=self.backbone, **kwargs)

    def download_imagenet(self):
        "Custom backbone, therefore no weights"
        return None

    def validate(self):
        """ Checks whether the backbone string is correct.
        """
        allowed_backbones = ['vgg13']

        if self.backbone not in allowed_backbones:
            raise ValueError('Backbone (\'{}\') not in allowed backbones ({}).'.format(self.backbone, allowed_backbones))

    def preprocess_image(self, inputs):
        """ Takes as input an image and prepares it for being passed through the network.
        """
        return preprocess_image(inputs, mode="tf")


def vgg13_retinanet(num_classes, backbone='vgg13', inputs=None, modifier=None, **kwargs):
    """ Constructs a retinanet model using a custom vgg13 backbone.

    Args
        num_classes: Number of classes to predict.
        backbone: Custom backbone to use ('vgg13')).
        inputs: The inputs to the network (defaults to a Tensor of shape (None, None, 3)).
        modifier: A function handler which can modify the backbone before using it in retinanet (this can be used to freeze backbone layers for example).

    Returns
        RetinaNet model with a VGG backbone.
    """
    # choose default input
    if inputs is None:
        inputs = keras.layers.Input(shape=(None, None, 3))
    # create the vgg backbone
    if backbone == 'vgg13':
        vgg13 = VGG13(input_tensor=inputs, include_top=False, weights=None)
        #eff = EfficientNetB4(input_tensor=inputs, include_top=False, weights=None)
    else:
        raise ValueError("Backbone '{}' not recognized.".format(backbone))

    if modifier:
        vgg13 = modifier(vgg13)

    print("Se imprimen los outputs")
    print(vgg13.summary())
    print(vgg13.outputs)
    # create the full model
    layer_names = ["block3_pool", "block4_pool", "block5_pool"]
    layer_outputs = [vgg13.get_layer(name).output for name in layer_names]
    r_model = retinanet.retinanet(inputs=inputs, num_classes=num_classes, backbone_layers=layer_outputs, **kwargs)
    plot_model(r_model, show_shapes=True, show_layer_names=True, to_file='VGG13RetinaNet.png')
    return r_model
