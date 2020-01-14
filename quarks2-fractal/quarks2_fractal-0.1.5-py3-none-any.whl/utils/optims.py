import torch 

def get_optim(config, model):
    params = [{'params': model.decoder.parameters(), 'lr': config.lr[0]}, 
    {'params': model.encoder.parameters(), 'lr': config.lr[1]}]
    if config.optimizer_name == "adam":
        optim = torch.optim.Adam(params)
    elif config.optimizer_name == "sgd":
        optim = torch.optim.SGD(params)
    else:
        raise NotImplementedError("This optimizer is not implemented")
    return optim