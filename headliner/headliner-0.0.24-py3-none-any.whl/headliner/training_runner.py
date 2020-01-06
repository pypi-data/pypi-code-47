import json
import logging
from typing import Tuple, List

import tensorflow as tf
from headliner.model.summarizer_transformer import SummarizerTransformer

from headliner.model import SummarizerAttention
from sklearn.model_selection import train_test_split
from tensorflow_datasets.core.features.text import SubwordTextEncoder
from transformers import BertTokenizer

from headliner.model.summarizer_bert import SummarizerBert
from headliner.preprocessing import Preprocessor, Vectorizer
from headliner.trainer import Trainer


def read_data_json(file_path: str,
                   max_sequence_length: int) -> List[Tuple[str, str]]:
    with open(file_path, 'r', encoding='utf-8') as f:
        data_out = json.load(f)
        return [d for d in zip(data_out['desc'], data_out['heads']) if len(d[0].split(' ')) <= max_sequence_length]


def read_data(file_path: str) -> List[Tuple[str, str]]:
    data_out = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for l in f.readlines():
            x, y = l.strip().split('\t')
            data_out.append((x, y))
        return data_out


if __name__ == '__main__':

    train = read_data('/Users/cschaefe/datasets/en_ger.txt')[0:1000]

    train_data, val_data = train_test_split(train, test_size=10, shuffle=True, random_state=42)
    logging.getLogger("transformers.tokenization_utils").setLevel(logging.ERROR)
    tokenizer_input = BertTokenizer.from_pretrained('bert-base-uncased')
    tokenizer_target = BertTokenizer.from_pretrained('bert-base-german-cased')



    preprocessor = Preprocessor(start_token='[CLS]',
                                end_token='[SEP]',
                                filter_pattern=None,
                                add_input_start_end=False,
                                punctuation_pattern=None)
    train_prep = [preprocessor(t) for t in train_data]


    vectorizer = Vectorizer(tokenizer_input, tokenizer_target, max_input_len=512)

    p = preprocessor(train[0])
    v = vectorizer(p)
    print(p)


    summarizer = SummarizerBert(num_heads=8,
                                num_layers_encoder=0,
                                num_layers_decoder=1,
                                feed_forward_dim=1024,
                                embedding_size_encoder=768,
                                embedding_size_decoder=768,
                                bert_embedding_encoder='bert-base-uncased',
                                bert_embedding_decoder='bert-base-german-cased',
                                dropout_rate=0,
                                max_prediction_len=30)

    pred_beam = summarizer.predict_beam_search(train_data[0][0])
    for p in pred_beam:
        print(p)

    print('pred:')
    print(summarizer.predict(train_data[0][0]))
    print('target:')
    print(train_data[0][0])
    print(train_data[0][1])
