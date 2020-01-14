import easydict
import yaml

from quarks2_fractal.classifier.model import ClsModel

def get_config(conf_file: str):
    """
    parse and load the provided configuration
    :param conf_file: configuration file
    :return: conf => parsed configuration
    """
    from easydict import EasyDict as edict

    with open(conf_file, "r") as file_descriptor:
        data = yaml.load(file_descriptor)

    # convert the data into an easyDictionary
    return edict(data)


def get_model(config: dict):
    if config.type == "classification":
        # model = ClsModel(encoder_name=config.encoder, encoder_weights=config.encoder_pretrained, classes=config.num_classes, activation=config.activation, *config.decoder)
        print("Loading model")
        model = ClsModel(**config)
    else:
        raise ValueError("type of the model is not defined")
    return model


def get_params_count(config: str, only_trainable=False):
    config = get_config(config)
    model = get_model(config)
    param_count = 0
    for _, param in model.named_parameters():
        if only_trainable:
            if param.requires_grad:
                param_count+= param.size().numel()
            else:
                continue
        else:
            param_count+= param.size().numel()
    return param_count