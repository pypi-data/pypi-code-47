
import torch
from ..torchio import INTENSITY
from ..utils import is_image_dict
from .random_transform import RandomTransform


class RandomBias(RandomTransform):
    def __init__(self, seed=None, verbose=False):
        super().__init__(seed=seed, verbose=verbose)

    def apply_transform(self, sample):
        # params = self.get_params()
        # sample['bias'] = None
        for image_dict in sample.values():
            if not is_image_dict(image_dict):
                continue
            if image_dict['type'] != INTENSITY:
                continue
            # add_noise(image_dict['data'], std)
        return sample

    @staticmethod
    def get_params(std_range):
        std = torch.FloatTensor(1).uniform_(*std_range).item()
        return std


def add_noise(data, std):
    noise = torch.FloatTensor(*data.shape).normal_(mean=0, std=std).numpy()
    data += noise
