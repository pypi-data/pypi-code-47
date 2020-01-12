import torch
from collections import OrderedDict

__all__ = ["load_models"]


# https://pytorch.org/tutorials/beginner/saving_loading_models.html#saving-loading-model-across-devices

def load_tar_models(model_path, model):
    # TODO : load more models info: ['iter', 'best_top1_acc', 'optimizer', 'state_dict']
    # not necessary?
    assert model_path.endswith(".tar")
    state_dict = torch.load(model_path)

    # create new OrderedDict that does not contain `module.`
    new_state_dict = OrderedDict()

    # multi-gpu pretrain models
    if "module." in list(state_dict['state_dict'].keys())[0]:
        for k, v in state_dict['state_dict'].items():
            name = k[7:]  # remove `module.`
            new_state_dict[name] = v

    state_dict['state_dict'] = new_state_dict

    if isinstance(state_dict, dict) and 'state_dict' in state_dict:
        # load params
        model.load_state_dict(state_dict['state_dict'])
    else:
        # load params
        model.load_state_dict(state_dict)

    return model


def load_models2gpu(model_path, model):
    state_dict = torch.load(model_path)
    model.cuda()
    # load params
    model.load_state_dict(state_dict)
    return model


def load_multi_gpu_models2_single_gpu(model_path, model):
    state_dict = torch.load(model_path)
    model.cuda()

    # create new OrderedDict that does not contain `module.`
    from collections import OrderedDict
    new_state_dict = OrderedDict()
    for k, v in state_dict["state_dict"].items():
        name = k[7:]  # remove `module.`
        new_state_dict[name] = v
    # load params
    model.load_state_dict(new_state_dict)
    return model


def load_models2cpu(model_path, model):
    state_dict = torch.load(model_path, map_location=lambda storage, loc: storage)
    # load params
    model.load_state_dict(state_dict)
    return model


def load_models(model_path, model, use_gpu=False):
    if model_path.endswith("pth.tar"):
        if torch.cuda.is_available() and use_gpu:
            model = model.cuda()
            load_tar_models(model_path, model)
        else:
            load_tar_models(model_path, model)
        return model

    if use_gpu and torch.cuda.is_available():
        model = model.cuda()
        try:
            model = load_models2gpu(model_path, model)
        except:
            model = load_multi_gpu_models2_single_gpu(model_path, model)
        else:
            print("Success load model to GPU!")
    else:
        print("No GPU or load model to CPU")
        model = model.to("cpu")
        try:
            model = load_models2cpu(model_path, model)
        except:
            print("Load model to CPU error!")
        else:
            print("Success load model to CPU!")

    return model


if __name__ == "__main__":
    from examples.models.tar.mobilenet_v2 import MobileNetV2

    model = MobileNetV2()
    model_path = "../examples/models/tar/checkpoint.pth.tar"
    # load_multi_gpu_models2_single_gpu(model_path, model)
    load_models(model_path, model)
    print(model)
    #
    import torchvision.models as models
    #
    # model = models.MobileNetV2()
    # model_path = "../examples/models/pth/mobilenet_v2-b0353104.pth"
    # load_models2gpu(model_path, model)
    # print(model)
    #
    #

    import os

    os.environ["CUDA_VISIBLE_DEVICES"] = ""

    model = models.MobileNetV2()
    model_path = "../examples/models/pth/mobilenet_v2-b0353104.pth"
    load_models(model_path, model, use_gpu=True)
    print(model)
    print(type(model))

    # model = models.MobileNetV2()
    # model_path = "../examples/models/pth/mobilenet_v2-b0353104.pth"
    # load_models2cpu(model_path, model)
    # print(model)
    # print("load_gpu_models2cpu test pass")
