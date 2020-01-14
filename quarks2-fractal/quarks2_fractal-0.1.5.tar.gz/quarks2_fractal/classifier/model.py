import torch
import torch.nn as nn 
import torch.nn.functional as F
from ..base.model import Model
from ..encoders import get_encoder
from .cls_decoder import get_decoder


class ClsEncoderDecoder(Model):

    def __init__(self, encoder, decoder, activation):
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder

        if callable(activation) or activation is None:
            self.activation = activation
        elif activation == 'softmax':
            self.activation = torch.nn.Softmax()
        elif activation == 'sigmoid':
            self.activation = torch.nn.Sigmoid()
        else:
            raise ValueError('Activation should be "sigmoid"/"softmax"/callable/None')

    def forward(self, x):
        """Sequentially pass `x` trough model`s `encoder` and `decoder` (return logits!)
        """
        x = self.encoder(x)
        y = self.decoder(x)
        if isinstance(y, tuple):
            _, out = y 
        else:
            out = y
        return out

    def predict(self, x):
        """Inference method. Switch model to `eval` mode, call `.forward(x)`
        and apply activation function (if activation is not `None`) with `torch.no_grad()`

        Args:
            x: 4D torch tensor with shape (batch_size, channels, height, width)

        Return:
            prediction: 4D torch tensor with shape (batch_size, classes, height, width)

        """
        if self.training:
            self.eval()

        with torch.no_grad():
            x = self.forward(x)
            if self.activation:
                x = self.activation(x)

        return x
    
    def save(self, save_location, ep, max_score, config):
        encoder_weights = self.encoder.state_dict()
        decoder_weights = self.decoder.state_dict()
        meta_data = {'config': config, "max_score": max_score, "epochs": ep}
        weights = {"encoder_weights": encoder_weights, "decoder_weights": decoder_weights, "meta_data": meta_data}
        torch.save(weights, save_location) 
        print('Model saved')
        return True

    def load(self, only_encoder=False, load_location="model.pth"):
        weights = torch.load(load_location)
        self.encoder.load_state_dict(weights["encoder_weights"])
        if not only_encoder:
            print("Loading decoder too. :)")
            self.decoder.load_state_dict(weights["decoder_weights"])
        return weights["meta_data"]

 
class ClsModel(ClsEncoderDecoder):
    def __init__(
        self,
        encoder_name="resnet34", 
        encoder_pretrained="imagenet",
        num_classes=1, 
        activation="sigmoid", 
        **kwargs):
        
        encoder = get_encoder(encoder_name, encoder_weights=encoder_pretrained)
        decoder = get_decoder(num_classes, encoder, encoder_name=encoder_name, **kwargs["decoder"])
        super().__init__(encoder, decoder, activation)
        self.name = 'u-{}'.format(encoder_name)