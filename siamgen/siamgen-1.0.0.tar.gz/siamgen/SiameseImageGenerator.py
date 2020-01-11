import numpy as np

from sklearn.utils import shuffle
from tensorflow.keras.utils import Sequence
from tensorflow.keras.utils import to_categorical

from .options import OUTPUT_TYPE, GENERATION_TYPE


class SiameseImageGenerator(Sequence):

    def __init__(self, x_set, y_set, batch_size=128, num_classes=None,
                 generation_type=GENERATION_TYPE.CONSIDERATE,
                 output_type: str or tuple = OUTPUT_TYPE.CATEGORICAL):
        self.batch_size = batch_size
        self.x, self.y = x_set, y_set
        self.output_type = output_type
        self.generation_type = generation_type
        self.n_cls = \
            len(np.unique(y_set)) if num_classes == None else num_classes
        assert self.n_cls > 1, 'You must have at least two classes.'
        self.indices = [np.where(self.y == i)[0] for i in range(self.n_cls)]
        self.min_len = [self.indices[i].size for i in range(self.n_cls)]

    def __len__(self):
        return int(np.ceil(len(self.x) / float(self.batch_size)))

    def __getitem__(self, idx):
        if self.output_type == OUTPUT_TYPE.CATEGORICAL:
            return self.__get_categorical_batch__()
        elif isinstance(self.output_type, tuple):
            return self.__get_customized_batch__()
        else:
            raise NotImplementedError('Undefined output type.')

    def on_epoch_end(self):
        self.x, self.y = shuffle(self.x, self.y)
        self.indices = [np.where(self.y == i)[0] for i in range(self.n_cls)]

    def __get_random_indices__(self):
        permuted_classes = np.apply_along_axis(
            np.random.permutation, 1, np.tile(range(self.n_cls), (self.batch_size, 1)))

        n_cls = permuted_classes[:, 1]
        a_cls = p_cls = permuted_classes[:, 0]

        a_smp = [np.random.randint(self.min_len[_]) for _ in a_cls]
        p_smp = [np.random.randint(self.min_len[_]) for _ in p_cls]
        n_smp = [np.random.randint(self.min_len[_]) for _ in n_cls]

        return (a_cls, a_smp), (p_cls, p_smp), (n_cls, n_smp)

    def __get_categorical_batch__(self):
        (a_cls, a_smp), (p_cls, p_smp),\
            (n_cls, n_smp) = self.__get_random_indices__()

        if self.generation_type == GENERATION_TYPE.CONSIDERATE:
            a_instances = [self.x[self.indices[i][j]]
                           for i, j in zip(a_cls, a_smp)]
            p_instances = [self.x[self.indices[i][j]]
                           for i, j in zip(p_cls, p_smp)]
            a_classes = [to_categorical(_, self.n_cls) for _ in a_cls]
            p_classes = [to_categorical(_, self.n_cls) for _ in p_cls]
            return [np.stack(a_instances), np.stack(p_instances)],\
                np.stack((a_classes, p_classes), axis=1)
        elif self.generation_type == GENERATION_TYPE.PARADOXICAL:
            a_instances = [self.x[self.indices[i][j]]
                           for i, j in zip(a_cls, a_smp)]
            n_instances = [self.x[self.indices[i][j]]
                           for i, j in zip(n_cls, n_smp)]
            a_classes = [to_categorical(_, self.n_cls) for _ in a_cls]
            n_classes = [to_categorical(_, self.n_cls) for _ in n_cls]
            return [np.stack(a_instances), np.stack(n_instances)],\
                np.stack((a_classes, n_classes), axis=1)
        else:
            raise NotImplementedError('Undefined generation type.')

    def __get_customized_batch__(self):
        (a_cls, a_smp), (p_cls, p_smp),\
            (n_cls, n_smp) = self.__get_random_indices__()

        if self.generation_type == GENERATION_TYPE.CONSIDERATE:
            a_instances = [self.x[self.indices[i][j]]
                           for i, j in zip(a_cls, a_smp)]
            p_instances = [self.x[self.indices[i][j]]
                           for i, j in zip(p_cls, p_smp)]
            return [np.stack(a_instances), np.stack(p_instances)],\
                np.broadcast_to(self.output_type,
                                (self.batch_size, len(self.output_type)))
        elif self.generation_type == GENERATION_TYPE.PARADOXICAL:
            a_instances = [self.x[self.indices[i][j]]
                           for i, j in zip(a_cls, a_smp)]
            n_instances = [self.x[self.indices[i][j]]
                           for i, j in zip(n_cls, n_smp)]
            return [np.stack(a_instances), np.stack(n_instances)],\
                np.broadcast_to(self.output_type,
                                (self.batch_size, len(self.output_type)))
        else:
            raise NotImplementedError('Undefined generation type.')


if __name__ == "__main__":
    np.random.seed(0)

    from tensorflow.keras.datasets import cifar10

    (x_train, y_train), (x_test, y_test) = cifar10.load_data()

    datagen = SiameseImageGenerator(x_train, y_train)
