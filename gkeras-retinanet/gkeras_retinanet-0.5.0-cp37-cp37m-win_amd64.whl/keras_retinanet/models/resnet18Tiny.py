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
from .resnet18TinyModels import ResNet2D18, BatchNormalization


custom_objects = {
    'BatchNormalization': BatchNormalization,
}

class ResNet18TinyBackbone(Backbone):
    """ Describes backbone information and provides utility functions.
    """
    def __init__(self, backbone):
        super(ResNet18TinyBackbone, self).__init__(backbone)
        self.custom_objects.update(custom_objects)

    def retinanet(self, *args, **kwargs):
        """ Returns a retinanet model using the correct backbone.
        """
        return resnet18tiny_retinanet(*args, backbone=self.backbone, **kwargs)

    def download_imagenet(self):
        "Custom backbone, therefore no weights"
        return None

    def validate(self):
        """ Checks whether the backbone string is correct.
        """
        allowed_backbones = ['resnet18tiny']

        if self.backbone not in allowed_backbones:
            raise ValueError('Backbone (\'{}\') not in allowed backbones ({}).'.format(self.backbone, allowed_backbones))

    def preprocess_image(self, inputs):
        """ Takes as input an image and prepares it for being passed through the network.
        """
        return preprocess_image(inputs, mode="tf")


def resnet18tiny_retinanet(num_classes, backbone='resnet18tiny', inputs=None, modifier=None, **kwargs):
    """ Constructs a retinanet model using a curstom ResNet18Tiny backbone.

    Args
        num_classes: Number of classes to predict.
        backbone: Custom backbone to use ('resnet18tiny').
        inputs: The inputs to the network (defaults to a Tensor of shape (None, None, 3)).
        modifier: A function handler which can modify the backbone before using it in retinanet (this can be used to freeze backbone layers for example).

    Returns
        RetinaNet model with a custom ResNet18Tiny backbone.
    """
    # choose default input
    if inputs is None:
        inputs = keras.layers.Input(shape=(None, None, 3))
    # create the backbone
    if backbone == 'resnet18tiny':
        resnet18tiny = ResNet2D18(inputs, include_top=False, freeze_bn=False)
        plot_model(resnet18tiny, show_shapes=True, show_layer_names=True, to_file='ResNet18Tiny.png')
    else:
        raise ValueError("Backbone '{}' not recognized.".format(backbone))

    if modifier:
        resnet18tiny = modifier(resnet18tiny)

    print("Se imprimen los outputs")
    print(resnet18tiny.summary())
    print(resnet18tiny.outputs)
    # create the full model
    layer_names = ["res3b1_relu", "res4b1_relu", "res5b1_relu"]
    layer_outputs = [resnet18tiny.get_layer(name).output for name in layer_names]
    r_model = retinanet.retinanet(inputs=inputs, num_classes=num_classes, backbone_layers=layer_outputs, **kwargs)
    plot_model(r_model, show_shapes=True, show_layer_names=True, to_file='ResNet18TinyRetinaNet.png')
    return r_model
