import foolbox.ext.native as fbn
import numpy as np

def _get_module_name(x):
    # splitting is necessary for TensorFlow tensors
    return x.__class__.__module__.split(".")[0]

def convert_cleverhans_model(model_fn, inputs, clip_min=None, clip_max=None):
    # extract bounds
    min_ = -np.inf if clip_min is None else clip_min
    max_ = np.inf if clip_max is None else clip_max
    bounds = (min_, max_)

    # convert model to Foolbox model
    module = _get_module_name(inputs)
    if module == "torch":
        fmodel = fbn.models.PyTorchModel(model_fn, bounds=bounds)
    elif module == "tensorflow":
        fmodel = fbn.models.TensorFlowModel(model_fn, bounds=bounds)
    elif module == "jax":
        fmodel = fbn.models.JAXModel(model_fn, bounds=bounds)
    else:
        raise ValueError(f"Unknown type: {type(x)}")
        
    return fmodel

def convert_foolbox_attack(FoolboxAttack):
    def attack(model_fn, inputs, clip_min=None, clip_max=None, **kwargs):
        # convert model
        fmodel = convert_cleverhans_model(model_fn, inputs, clip_min, clip_max)
        
        # initiate attack
        foolbox_attack = FoolboxAttack(fmodel)
        
        # run attack
        adv_x = foolbox_attack(inputs, **kwargs)
        
        return adv_x
    
    return attack