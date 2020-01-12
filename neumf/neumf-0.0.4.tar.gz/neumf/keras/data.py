import tensorflow as tf, numpy as np, pickle, json, math
from .utils import (shared_shuffle, shared_sort, batch_idx)

def to_int_feature(values):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=list(values)))

def serialize_transaction_data(data:dict):
    features = {
        k: to_int_feature(v.astype(np.int64))
        for k, v in data.items()
        if type(v) is list
    }
    return tf.train.Example(features=tf.train.Features(feature=features)).SerializeToString()

class TransactionSequence(tf.keras.utils.Sequence):
    def __init__(
        self, users, items, num_users, num_items,
        batch_size=32, neg_ratio=4, pad_last=True
    ):
        self.num_users = num_users
        self.num_items = num_items
        self.batch_size = batch_size
        self.adjusted_batch_size = batch_size * (neg_ratio+1)
        self.neg_ratio = neg_ratio
        self.pad_last = pad_last

        negative_info = NegativeTransactionTable(users, items, num_users, num_items)
        negative_info.construct_table()
        self.neg = negative_info

        self.users, self.items = shared_shuffle((users, items))

    def on_epoch_end(self):
        self.users, self.items = shared_shuffle((self.users, self.items))


    def __len__(self):
        d = len(self.items) / self.batch_size
        if self.pad_last:
            return math.ceil(d)
        return math.floor(d)

    def __getitem__(self, idx):
        a, b = batch_idx(idx, self.batch_size)
        b_users = self.users[a:b]
        b_items = self.items[a:b]
        b_pos = np.ones_like(b_users)

        n_users = np.repeat(b_users, self.neg_ratio)
        n_items = self.neg.lookup_negative_items(n_users)
        b_neg = np.zeros_like(n_users)

        b_u = np.concatenate((b_users, n_users))
        b_i = np.concatenate((b_items, n_items))
        b_y = np.concatenate((b_pos, b_neg))

        # need to pad, will do so evenly with random _previously_ seen positive and negative examples
        if self.adjusted_batch_size > len(b_u):
            diff = self.adjusted_batch_size - len(b_u)
            pad_pos = round(diff / 2)
            pad_neg = diff-pad_pos

            ppu = np.random.choice(np.arange(len(self.users)), pad_pos)
            b_u = np.concatenate((
                b_u,
                self.users[ppu],
                self.users[ppu][:pad_neg]
            ))
            b_i = np.concatenate((
                b_i,
                self.items[ppu],
                self.neg.lookup_negative_items(self.users[ppu])[:pad_neg]
            ))
            b_y = np.concatenate((b_y, np.ones_like(ppu), np.zeros((pad_neg))))


        b = np.array([b_u, b_i, b_y])


        i = np.arange(self.adjusted_batch_size)
        np.random.shuffle(i)
        x, y = tuple(b[:2, i]), b[2:, i].reshape(-1)
        return x, y

class NegativeTransactionTable:
    def __init__(self, users, items, num_users, num_items):
        super(NegativeTransactionTable, self).__init__()
        self.users, self.items = shared_sort((users, items))
        self.num_users = num_users
        self.num_items = num_items

        self.negative_table = None
        self.per_user_neg_count = None

    def construct_table(self):
        inner_bounds = np.argwhere(self.users[1:] - self.users[:-1])[:, 0] + 1
        (upper_bound,) = self.users.shape
        index_bounds = [0] + inner_bounds.tolist() + [upper_bound]
        negative_table = np.zeros(shape=(self.num_users, self.num_items), dtype=np.int32) - 1
        full_set = np.arange(self.num_items)
        per_user_neg_count = np.zeros(shape=(self.num_users,), dtype=np.int32)
        for i in range(self.num_users):
            positives = self.items[index_bounds[i]:index_bounds[i+1]]
            negatives = np.delete(full_set, positives)
            per_user_neg_count[i] = self.num_items - positives.shape[0]
            negative_table[i, :per_user_neg_count[i]] = negatives

        self.negative_table = negative_table
        self.per_user_neg_count = per_user_neg_count
        return negative_table

    def lookup_negative_items(self, users, **kwargs):
        neg_choices = [
            np.random.randint(self.per_user_neg_count[user])
            for user in users
        ]
        return self.negative_table[users, neg_choices]


def preprocess_transaction_dataframe(
    dataframe,
    user_col:str='user_id',
    item_col:str='item_id',
    time_col:str=None,
    min_items:int=20,
    save_file:str=None,
    drop_duplicates:bool=True
):
    dff = dataframe
    if drop_duplicates:
        dff = dff.drop_duplicates(subset=[user_col, item_col])

    # only users with at least `min_items` iteractions
    grouped = dff.groupby(user_col)
    dff = grouped.filter(lambda x: len(x) >= min_items)

    # for reindexing
    original_users = dff[user_col].unique()
    original_items = dff[item_col].unique()

    # database index to 0-based index
    user_map = {user: index for index, user in enumerate(original_users)}
    item_map = {item: index for index, item in enumerate(original_items)}

    # apply reindexing
    dff[user_col] = dff[user_col].apply(lambda user: user_map[user])
    dff[item_col] = dff[item_col].apply(lambda item: item_map[item])

    # dimensions of rating matrix
    num_users = len(original_users)
    num_items = len(original_items)

    # sort rating interactions by recency
    if time_col is not None:
        dff.sort_values(by=time_col, inplace=True)
        dff.sort_values([user_col, time_col], inplace=True, kind="mergesort")

        # The dataframe does not reconstruct indices in the sort or filter steps.
        dff = dff.reset_index()

    grouped = dff.groupby(user_col, group_keys=False)
    eval_df, train_df = grouped.tail(1), grouped.apply(lambda x: x.iloc[:-1])

    data = {
        'train_'+user_col: train_df[user_col].values.astype(np.int32),
        'train_'+item_col: train_df[item_col].values.astype(np.int32),

        'eval_'+user_col: eval_df[user_col].values.astype(np.int32),
        'eval_'+item_col: eval_df[item_col].values.astype(np.int32),

        'user_map': user_map,
        'item_map': item_map,

        'num_users': num_users,
        'num_items': num_items
    }
    if save_file:
        with open(save_file, 'wb') as f:
            pickle.dump(data, f)
    return data
