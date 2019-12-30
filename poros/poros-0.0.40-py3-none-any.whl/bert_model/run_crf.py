#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Copyright 2018 The Google AI Language Team Authors.
BASED ON Google_BERT.
reference from :zhoukaiyin/
@Author:Macan
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import codecs
import collections
import json
import logging
import os
import pickle

import tensorflow as tf
from tensorflow.contrib.layers.python.layers import initializers

from poros.bert_model import modeling
from poros.bert_model import optimization
from poros.bert_model import tokenization
from poros.metrics import tf_metrics
from poros.sequence.lstm_crf_layer import BLSTM_CRF

logger = logging.getLogger('tensorflow')
fh = logging.FileHandler('this_crf.log')
logger.addHandler(fh)

flags = tf.flags

flags.DEFINE_string("data_dir", None, "The input datadir.")

flags.DEFINE_string("bert_config_file", None, "The config json file corresponding to the pre-trained BERT model.")

flags.DEFINE_string("task_name", 'ner', "The name of the task to train.")

flags.DEFINE_string("output_dir", None,
                    "The output directory where the model checkpoints will be written.")

## Other parameters
flags.DEFINE_string("init_checkpoint", None, "Initial checkpoint (usually from a pre-trained BERT model).")

flags.DEFINE_bool("do_lower_case", True, "Whether to lower case the input text.")

flags.DEFINE_integer(
    "max_seq_length", 128,
    "The maximum total input sequence length after WordPiece tokenization."
)

flags.DEFINE_boolean('clean', True, 'remove the files which created by last training')

flags.DEFINE_bool("do_train", False, "Whether to run training."
                  )
flags.DEFINE_bool("use_tpu", False, "Whether to use TPU or GPU/CPU.")

flags.DEFINE_bool("do_eval", True, "Whether to run eval on the dev set.")

flags.DEFINE_bool("do_predict", True, "Whether to run the model in inference mode on the test set.")

flags.DEFINE_integer("train_batch_size", 32, "Total batch size for training.")

flags.DEFINE_integer("eval_batch_size", 8, "Total batch size for eval.")

flags.DEFINE_integer("predict_batch_size", 8, "Total batch size for predict.")

flags.DEFINE_float("learning_rate", 5e-5, "The initial learning rate for Adam.")

flags.DEFINE_integer("num_train_epochs", 10, "Total number of training epochs to perform.")
flags.DEFINE_float('droupout_rate', 0.5, 'Dropout rate')
flags.DEFINE_float('clip', 5, 'Gradient clip')
flags.DEFINE_float(
    "warmup_proportion", 0.1,
    "Proportion of training to perform linear learning rate warmup for. "
    "E.g., 0.1 = 10% of training.")

flags.DEFINE_integer("save_checkpoints_steps", 1000,
                     "How often to save the model checkpoint.")

flags.DEFINE_integer("iterations_per_loop", 1000,
                     "How many steps to make in each estimator call.")

flags.DEFINE_string("vocab_file", None,
                    "The vocabulary file that the BERT model was trained on.")

tf.flags.DEFINE_string("master", None, "[Optional] TensorFlow master URL.")
flags.DEFINE_integer(
    "num_tpu_cores", 8,
    "Only used if `use_tpu` is True. Total number of TPU cores to use.")
flags.DEFINE_string('data_config_path', None,
                    'data config file, which save train and dev config')
# lstm parame
flags.DEFINE_integer('lstm_size', 128, 'size of lstm units')
flags.DEFINE_integer('num_layers', 1, 'number of rnn layers, default is 1')
flags.DEFINE_string('cell', 'lstm', 'which rnn cell used')

# 移除模型中的Adam相关参数，使得最终模型文件为300-400M， 不会是原来的1.2G， 移除后的模型可以用于预测阶段。
# Add code to remove the adam related parameters in the model,
# and reduce the size of the model file from 1.3GB to 400MB.
# https://github.com/google-research/bert/issues/99
# If  True last model'adam related parameters will be removed, False not
flags.DEFINE_boolean('filter_adam_var', True, 'remove all the adam variables of model')

FLAGS = flags.FLAGS


class InputExample(object):
    """A single training/test example for simple sequence classification."""

    def __init__(self, guid, text, label=None):
        """Constructs a InputExample.
        Args:
          guid: Unique id for the example.
          text_a: string. The untokenized text of the first sequence. For single
            sequence tasks, only this sequence must be specified.
          label: (Optional) string. The label of the example. This should be
            specified for train and dev examples, but not for test examples.
        """
        self.guid = guid
        self.text = text
        self.label = label


class InputFeatures(object):
    """A single set of features of data."""

    def __init__(self, input_ids, input_mask, segment_ids, label_ids, ):
        self.input_ids = input_ids
        self.input_mask = input_mask
        self.segment_ids = segment_ids
        self.label_ids = label_ids
        # self.label_mask = label_mask


class DataProcessor(object):
    """Base class for data converters for sequence classification data sets."""

    def get_train_examples(self, data_dir):
        """Gets a collection of `InputExample`s for the train set."""
        raise NotImplementedError()

    def get_dev_examples(self, data_dir):
        """Gets a collection of `InputExample`s for the dev set."""
        raise NotImplementedError()

    def get_labels(self):
        """Gets the list of labels for this data set."""
        raise NotImplementedError()

    @classmethod
    def _read_data(cls, input_file):
        """Reads a BIO data."""
        with codecs.open(input_file, 'r', encoding='utf-8') as f:
            lines = []
            words = []
            labels = []
            for line in f:
                contends = line.strip()
                tokens = contends.split('\t')
                if len(tokens) == 2:
                    word = line.strip().split('\t')[0]
                    label = line.strip().split('\t')[-1]
                else:
                    if len(contends) == 0:
                        l = ' '.join([label for label in labels if len(label) > 0])
                        w = ' '.join([word for word in words if len(word) > 0])
                        lines.append([l, w])
                        words = []
                        labels = []
                        continue
                if contends.startswith("-DOCSTART-"):
                    words.append('')
                    continue
                words.append(word)
                labels.append(label)
            return lines


class NerProcessor(DataProcessor):
    def get_train_examples(self, data_dir):
        return self._create_example(
            self._read_data(os.path.join(data_dir, "train.txt")), "train"
        )

    def get_dev_examples(self, data_dir):
        return self._create_example(
            self._read_data(os.path.join(data_dir, "dev.txt")), "dev"
        )

    def get_test_examples(self, data_dir):
        return self._create_example(
            self._read_data(os.path.join(data_dir, "test.txt")), "test")

    def get_labels(self):
        # return ["O", "B-PER", "I-PER", "B-ORG", "I-ORG", "B-LOC", "I-LOC", "X", "[CLS]", "[SEP]"]
        return ['O', "X", "[CLS]", "[SEP]",
                'B-Amount', 'B-Anatomy', 'B-Disease', 'B-Drug', 'B-Duration', 'B-Frequency', 'B-Level', 'B-Method',
                'B-Operation', 'B-Reason', 'B-SideEff', 'B-Symptom', 'B-Test', 'B-Test_Value', 'B-Treatment',
                'E-Amount', 'E-Anatomy', 'E-Disease', 'E-Drug', 'E-Duration', 'E-Frequency', 'E-Level', 'E-Method',
                'E-Operation', 'E-Reason', 'E-SideEff', 'E-Symptom', 'E-Test', 'E-Test_Value', 'E-Treatment',
                'I-Amount', 'I-Anatomy', 'I-Disease', 'I-Drug', 'I-Duration', 'I-Frequency', 'I-Level', 'I-Method',
                'I-Operation', 'I-Reason', 'I-SideEff', 'I-Symptom', 'I-Test', 'I-Test_Value', 'I-Treatment',
                'S-Amount', 'S-Anatomy', 'S-Disease', 'S-Drug', 'S-Duration', 'S-Frequency', 'S-Level', 'S-Method',
                'S-Operation', 'S-Reason', 'S-SideEff', 'S-Symptom', 'S-Test', 'S-Test_Value', 'S-Treatment'
                ]

    def _create_example(self, lines, set_type):
        examples = []
        for (i, line) in enumerate(lines):
            guid = "%s-%s" % (set_type, i)
            text = tokenization.convert_to_unicode(line[1])
            label = tokenization.convert_to_unicode(line[0])
            if i == 0:
                print(label)
            examples.append(InputExample(guid=guid, text=text, label=label))
        return examples


def write_tokens(tokens, mode):
    """
    将序列解析结果写入到文件中
    只在mode=test的时候启用
    :param tokens:
    :param mode:
    :return:
    """
    if mode == "test":
        path = os.path.join(FLAGS.output_dir, "token_" + mode + ".txt")
        wf = codecs.open(path, 'a', encoding='utf-8')
        for token in tokens:
            if token != "**NULL**":
                wf.write(token + '\n')
        wf.close()


def convert_single_example(ex_index, example, label_list, max_seq_length, tokenizer, mode):
    """
    将一个样本进行分析，然后将字转化为id, 标签转化为id,然后结构化到InputFeatures对象中
    :param ex_index: index
    :param example: 一个样本
    :param label_list: 标签列表
    :param max_seq_length:
    :param tokenizer:
    :param mode:
    :return:
    """
    label_map = {}
    # 1表示从1开始对label进行index化
    for (i, label) in enumerate(label_list, 1):
        label_map[label] = i
    # 保存label->index 的map
    if not os.path.exists(os.path.join(FLAGS.output_dir, 'label2id.pkl')):
        with codecs.open(os.path.join(FLAGS.output_dir, 'label2id.pkl'), 'wb') as w:
            pickle.dump(label_map, w)

    textlist = example.text.split(' ')
    labellist = example.label.split(' ')
    tokens = []
    labels = []
    for i, word in enumerate(textlist):
        # 分词，如果是中文，就是分字
        token = tokenizer.tokenize(word)
        tokens.extend(token)
        try:
            label_1 = labellist[i]
        except:
            print(i, word)
        for m in range(len(token)):
            if m == 0:
                labels.append(label_1)
            else:  # 一般不会出现else
                labels.append("X")
    # tokens = tokenizer.tokenize(example.text)
    # 序列截断
    if len(tokens) >= max_seq_length - 1:
        tokens = tokens[0:(max_seq_length - 2)]  # -2 的原因是因为序列需要加一个句首和句尾标志
        labels = labels[0:(max_seq_length - 2)]
    ntokens = []
    segment_ids = []
    label_ids = []
    ntokens.append("[CLS]")  # 句子开始设置CLS 标志
    segment_ids.append(0)
    # append("O") or append("[CLS]") not sure!
    label_ids.append(label_map["[CLS]"])  # O OR CLS 没有任何影响，不过我觉得O 会减少标签个数,不过拒收和句尾使用不同的标志来标注，使用LCS 也没毛病
    for i, token in enumerate(tokens):
        ntokens.append(token)
        segment_ids.append(0)
        label_ids.append(label_map[labels[i]])
    ntokens.append("[SEP]")  # 句尾添加[SEP] 标志
    segment_ids.append(0)
    # append("O") or append("[SEP]") not sure!
    label_ids.append(label_map["[SEP]"])
    input_ids = tokenizer.convert_tokens_to_ids(ntokens)  # 将序列中的字(ntokens)转化为ID形式
    input_mask = [1] * len(input_ids)
    # label_mask = [1] * len(input_ids)
    # padding, 使用
    while len(input_ids) < max_seq_length:
        input_ids.append(0)
        input_mask.append(0)
        segment_ids.append(0)
        # we don't concerned about it!
        label_ids.append(0)
        ntokens.append("**NULL**")
        # label_mask.append(0)
    # print(len(input_ids))
    assert len(input_ids) == max_seq_length
    assert len(input_mask) == max_seq_length
    assert len(segment_ids) == max_seq_length
    assert len(label_ids) == max_seq_length
    # assert len(label_mask) == max_seq_length

    # 打印部分样本数据信息
    if ex_index < 5:
        tf.logging.info("*** Example ***")
        tf.logging.info("guid: %s" % (example.guid))
        tf.logging.info("tokens: %s" % " ".join(
            [tokenization.printable_text(x) for x in tokens]))
        tf.logging.info("input_ids: %s" % " ".join([str(x) for x in input_ids]))
        tf.logging.info("input_mask: %s" % " ".join([str(x) for x in input_mask]))
        tf.logging.info("segment_ids: %s" % " ".join([str(x) for x in segment_ids]))
        tf.logging.info("label_ids: %s" % " ".join([str(x) for x in label_ids]))
        # tf.logging.info("label_mask: %s" % " ".join([str(x) for x in label_mask]))

    # 结构化为一个类
    feature = InputFeatures(
        input_ids=input_ids,
        input_mask=input_mask,
        segment_ids=segment_ids,
        label_ids=label_ids,
        # label_mask = label_mask
    )
    # mode='test'的时候才有效
    write_tokens(ntokens, mode)
    return feature


def filed_based_convert_examples_to_features(
        examples, label_list, max_seq_length, tokenizer, output_file, mode=None
):
    """
    将数据转化为TF_Record 结构，作为模型数据输入
    :param examples:  样本
    :param label_list:标签list
    :param max_seq_length: 预先设定的最大序列长度
    :param tokenizer: tokenizer 对象
    :param output_file: tf.record 输出路径
    :param mode:
    :return:
    """
    writer = tf.python_io.TFRecordWriter(output_file)
    # 遍历训练数据
    for (ex_index, example) in enumerate(examples):
        if ex_index % 5000 == 0:
            tf.logging.info("Writing example %d of %d" % (ex_index, len(examples)))
        # 对于每一个训练样本,
        feature = convert_single_example(ex_index, example, label_list, max_seq_length, tokenizer, mode)

        def create_int_feature(values):
            f = tf.train.Feature(int64_list=tf.train.Int64List(value=list(values)))
            return f

        features = collections.OrderedDict()
        features["input_ids"] = create_int_feature(feature.input_ids)
        features["input_mask"] = create_int_feature(feature.input_mask)
        features["segment_ids"] = create_int_feature(feature.segment_ids)
        features["label_ids"] = create_int_feature(feature.label_ids)
        tf_example = tf.train.Example(features=tf.train.Features(feature=features))
        writer.write(tf_example.SerializeToString())


def file_based_input_fn_builder(input_file, seq_length, is_training, drop_remainder):
    name_to_features = {
        "input_ids": tf.FixedLenFeature([seq_length], tf.int64),
        "input_mask": tf.FixedLenFeature([seq_length], tf.int64),
        "segment_ids": tf.FixedLenFeature([seq_length], tf.int64),
        "label_ids": tf.FixedLenFeature([seq_length], tf.int64),
    }

    def _decode_record(record, name_to_features):
        example = tf.parse_single_example(record, name_to_features)
        for name in list(example.keys()):
            t = example[name]
            if t.dtype == tf.int64:
                t = tf.to_int32(t)
            example[name] = t
        return example

    def input_fn(params):
        batch_size = params.get('batch_size') or FLAGS.train_batch_size
        d = tf.data.TFRecordDataset(input_file)
        if is_training:
            d = d.repeat()
            d = d.shuffle(buffer_size=100)
        d = d.apply(tf.contrib.data.map_and_batch(
            lambda record: _decode_record(record, name_to_features),
            batch_size=batch_size,
            drop_remainder=drop_remainder
        ))
        return d

    return input_fn


def create_model(bert_config, is_training, input_ids, input_mask,
                 segment_ids, labels, num_labels, use_one_hot_embeddings):
    """
    创建X模型
    :param bert_config: bert 配置
    :param is_training:
    :param input_ids: 数据的idx 表示
    :param input_mask:
    :param segment_ids:
    :param labels: 标签的idx 表示
    :param num_labels: 类别数量
    :param use_one_hot_embeddings:
    :return:
    """
    # 使用数据加载BertModel,获取对应的字embedding
    model = modeling.BertModel(
        config=bert_config,
        is_training=is_training,
        input_ids=input_ids,
        input_mask=input_mask,
        token_type_ids=segment_ids,
        use_one_hot_embeddings=use_one_hot_embeddings
    )
    # 获取对应的embedding 输入数据[batch_size, seq_length, embedding_size]
    embedding = model.get_sequence_output()
    max_seq_length = embedding.shape[1].value

    used = tf.sign(tf.abs(input_ids))
    lengths = tf.reduce_sum(used, reduction_indices=1)  # [batch_size] 大小的向量，包含了当前batch中的序列长度

    blstm_crf = BLSTM_CRF(embedded_chars=embedding,
                          hidden_unit=FLAGS.lstm_size,
                          cell_type=FLAGS.cell,
                          num_layers=FLAGS.num_layers,
                          dropout_rate=FLAGS.droupout_rate,
                          initializers=initializers,
                          num_labels=num_labels,
                          sequence_max_length=max_seq_length,
                          labels=labels,
                          real_lengths=lengths,
                          is_training=is_training)
    rst = blstm_crf.add_blstm_crf_layer(crf_only=True)
    return rst


def model_fn_builder(bert_config, num_labels, init_checkpoint, learning_rate,
                     num_train_steps, num_warmup_steps, use_tpu,
                     use_one_hot_embeddings):
    """
    构建模型
    :param bert_config:
    :param num_labels:
    :param init_checkpoint:
    :param learning_rate:
    :param num_train_steps:
    :param num_warmup_steps:
    :param use_tpu:
    :param use_one_hot_embeddings:
    :return:
    """

    def model_fn(features, labels, mode, params):
        tf.logging.info("*** Features ***")
        for name in sorted(features.keys()):
            tf.logging.info("  name = %s, shape = %s" % (name, features[name].shape))
        input_ids = features["input_ids"]
        input_mask = features["input_mask"]
        segment_ids = features["segment_ids"]
        label_ids = features["label_ids"]

        print('shape of input_ids', input_ids.shape)
        # label_mask = features["label_mask"]
        is_training = (mode == tf.estimator.ModeKeys.TRAIN)

        # 使用参数构建模型,input_idx 就是输入的样本idx表示，label_ids 就是标签的idx表示
        (total_loss, logits, trans, pred_ids) = create_model(
            bert_config, is_training, input_ids, input_mask, segment_ids, label_ids,
            num_labels, use_one_hot_embeddings)

        tvars = tf.trainable_variables()
        scaffold_fn = None
        # 加载BERT模型
        if init_checkpoint:
            (assignment_map, initialized_variable_names) = modeling.get_assignment_map_from_checkpoint(tvars,
                                                                                                       init_checkpoint)
            tf.train.init_from_checkpoint(init_checkpoint, assignment_map)
            if use_tpu:
                def tpu_scaffold():
                    tf.train.init_from_checkpoint(init_checkpoint, assignment_map)
                    return tf.train.Scaffold()

                scaffold_fn = tpu_scaffold
            else:
                tf.train.init_from_checkpoint(init_checkpoint, assignment_map)

        tf.logging.info("**** Trainable Variables ****")

        output_spec = None
        if mode == tf.estimator.ModeKeys.TRAIN:
            train_op = optimization.create_optimizer(
                total_loss, learning_rate, num_train_steps, num_warmup_steps, use_tpu)
            output_spec = tf.estimator.EstimatorSpec(
                mode=mode,
                loss=total_loss,
                train_op=train_op,
                scaffold=scaffold_fn
            )
        elif mode == tf.estimator.ModeKeys.EVAL:

            # label 从 O:1 开始， 0 = pad 的 id
            pos_indices = [ind for ind in range(4, num_labels)]
            weights = tf.sequence_mask(
                tf.reduce_sum(tf.cast(tf.greater(label_ids, 0), tf.int32), axis=1),
                maxlen=FLAGS.max_seq_length)
            precision = tf_metrics.precision(label_ids, pred_ids, num_labels, pos_indices=pos_indices, weights=weights,
                                             average='macro')
            recall = tf_metrics.recall(label_ids, pred_ids, num_labels, pos_indices=pos_indices, weights=weights,
                                       average='macro')
            f = tf_metrics.f1(label_ids, pred_ids, num_labels, pos_indices=pos_indices, weights=weights,
                              average='macro')

            accuracy = tf.metrics.accuracy(labels=label_ids, predictions=pred_ids, weights=weights)

            eval_metric_ops = {
                "eval_precision": precision,
                "eval_recall": recall,
                "eval_f": f,
                "eval_accuracy": accuracy,
            }

            output_spec = tf.estimator.EstimatorSpec(
                mode=mode,
                loss=total_loss,
                eval_metric_ops=eval_metric_ops,
                scaffold=scaffold_fn
            )
        else:
            output_spec = tf.estimator.EstimatorSpec(
                mode=mode,
                predictions=pred_ids,
                scaffold=scaffold_fn
            )
        return output_spec

    return model_fn


def main(_):
    tf.logging.set_verbosity(tf.logging.INFO)
    for k, v in FLAGS.flag_values_dict().items():
        print('{}:{}'.format(k, v))
    processors = {
        "ner": NerProcessor
    }

    bert_config = modeling.BertConfig.from_json_file(FLAGS.bert_config_file)

    if FLAGS.max_seq_length > bert_config.max_position_embeddings:
        raise ValueError(
            "Cannot use sequence length %d because the BERT model "
            "was only trained up to sequence length %d" %
            (FLAGS.max_seq_length, bert_config.max_position_embeddings))

    # 在train 的时候，才删除上一轮产出的文件，在predicted 的时候不做clean
    if FLAGS.clean and FLAGS.do_train:
        clean_output_dir()
    task_name = FLAGS.task_name.lower()
    if task_name not in processors:
        raise ValueError("Task not found: %s" % (task_name))
    processor = processors[task_name]()

    label_list = processor.get_labels()
    if not os.path.exists(os.path.join(FLAGS.output_dir, 'label_list.pkl')):
        with open(os.path.join(FLAGS.output_dir, 'label_list.pkl'), 'wb') as fd:
            pickle.dump(label_list, fd)

    tokenizer = tokenization.FullTokenizer(
        vocab_file=FLAGS.vocab_file, do_lower_case=FLAGS.do_lower_case)

    run_config = tf.estimator.RunConfig(model_dir=FLAGS.output_dir,
                                        save_checkpoints_steps=FLAGS.save_checkpoints_steps)

    train_examples = None
    num_train_steps = None
    num_warmup_steps = None

    if os.path.exists(FLAGS.data_config_path):
        with codecs.open(FLAGS.data_config_path) as fd:
            data_config = json.load(fd)
    else:
        data_config = {}

    if FLAGS.do_train:
        # 加载训练数据
        if len(data_config) == 0:
            train_examples = processor.get_train_examples(FLAGS.data_dir)
            num_train_steps = int(
                len(train_examples) / FLAGS.train_batch_size * FLAGS.num_train_epochs)
            num_warmup_steps = int(num_train_steps * FLAGS.warmup_proportion)

            data_config['num_train_steps'] = num_train_steps
            data_config['num_warmup_steps'] = num_warmup_steps
            data_config['num_train_size'] = len(train_examples)
        else:
            num_train_steps = int(data_config['num_train_steps'])
            num_warmup_steps = int(data_config['num_warmup_steps'])

    model_fn = model_fn_builder(
        bert_config=bert_config,
        num_labels=len(label_list) + 1,  # 加 1 是为了 加入 pad
        init_checkpoint=FLAGS.init_checkpoint,
        learning_rate=FLAGS.learning_rate,
        num_train_steps=num_train_steps,
        num_warmup_steps=num_warmup_steps,
        use_tpu=FLAGS.use_tpu,
        use_one_hot_embeddings=FLAGS.use_tpu)

    estimator = tf.estimator.Estimator(
        model_fn=model_fn,
        config=run_config,
    )

    if FLAGS.do_train:
        # 1. 将数据转化为tf_record 数据
        if data_config.get('train.tf_record_path', '') == '':
            train_file = os.path.join(FLAGS.output_dir, "train.tf_record")
            filed_based_convert_examples_to_features(
                train_examples, label_list, FLAGS.max_seq_length, tokenizer, train_file)
        else:
            train_file = data_config.get('train.tf_record_path')
        num_train_size = int(data_config['num_train_size'])
        tf.logging.info("***** Running training *****")
        tf.logging.info("  Num examples = %d", num_train_size)
        tf.logging.info("  Batch size = %d", FLAGS.train_batch_size)
        tf.logging.info("  Num steps = %d", num_train_steps)

        # 2.读取record 数据，组成batch
        train_input_fn = file_based_input_fn_builder(
            input_file=train_file,
            seq_length=FLAGS.max_seq_length,
            is_training=True,
            drop_remainder=True)

        eval_input_fn = get_eval_fn(data_config, label_list, processor, tokenizer)

        seq_length = FLAGS.max_seq_length
        name_to_features = {
            "input_ids": tf.FixedLenFeature([seq_length], tf.int64),
            "input_mask": tf.FixedLenFeature([seq_length], tf.int64),
            "segment_ids": tf.FixedLenFeature([seq_length], tf.int64),
            "label_ids": tf.FixedLenFeature([seq_length], tf.int64),
        }

        serving_input_receiver_fn = tf.estimator.export.build_parsing_serving_input_receiver_fn(name_to_features)

        def _f1_greater(best_eval_result, current_eval_result):
            """Compares two evaluation results and returns true if the 2nd one is smaller.

            Both evaluation results should have the values for MetricKeys.LOSS, which are
            used for comparison.

            Args:
              best_eval_result: best eval metrics.
              current_eval_result: current eval metrics.

            Returns:
              True if the loss of current_eval_result is smaller; otherwise, False.

            Raises:
              ValueError: If input eval result is None or no loss is available.
            """
            # default_key = metric_keys.MetricKeys.LOSS
            default_key = 'eval_f'
            if not best_eval_result or default_key not in best_eval_result:
                raise ValueError(
                    'best_eval_result cannot be empty or no loss is found in it.')

            if not current_eval_result or default_key not in current_eval_result:
                raise ValueError(
                    'current_eval_result cannot be empty or no loss is found in it.')

            return best_eval_result[default_key] < current_eval_result[default_key]

        exporter = tf.estimator.BestExporter(serving_input_receiver_fn=serving_input_receiver_fn,
                                             compare_fn=_f1_greater)

        train_spec = tf.estimator.TrainSpec(input_fn=train_input_fn, max_steps=num_train_steps)
        eval_spec = tf.estimator.EvalSpec(input_fn=eval_input_fn, exporters=exporter, steps=None, throttle_secs=60)

        tf.estimator.train_and_evaluate(estimator, train_spec, eval_spec)

        # estimator.train(input_fn=train_input_fn, max_steps=num_train_steps)
    if FLAGS.do_eval:
        eval_input_fn = get_eval_fn(data_config, label_list, processor, tokenizer)
        result = estimator.evaluate(input_fn=eval_input_fn)
        output_eval_file = os.path.join(FLAGS.output_dir, "eval_results.txt")
        with codecs.open(output_eval_file, "w", encoding='utf-8') as writer:
            tf.logging.info("***** Eval results *****")
            for key in sorted(result.keys()):
                tf.logging.info("  %s = %s", key, str(result[key]))
                writer.write("%s = %s\n" % (key, str(result[key])))

    # 保存数据的配置文件，避免在以后的训练过程中多次读取训练以及测试数据集，消耗时间
    if not os.path.exists(FLAGS.data_config_path):
        with codecs.open(FLAGS.data_config_path, 'a', encoding='utf-8') as fd:
            json.dump(data_config, fd)

    if FLAGS.do_predict:
        token_path = os.path.join(FLAGS.output_dir, "token_test.txt")
        if os.path.exists(token_path):
            os.remove(token_path)

        with codecs.open(os.path.join(FLAGS.output_dir, 'label2id.pkl'), 'rb') as rf:
            label2id = pickle.load(rf)
            id2label = {value: key for key, value in label2id.items()}

        predict_examples = processor.get_test_examples(FLAGS.data_dir)

        predict_file = os.path.join(FLAGS.output_dir, "predict.tf_record")
        filed_based_convert_examples_to_features(predict_examples, label_list,
                                                 FLAGS.max_seq_length, tokenizer,
                                                 predict_file, mode="test")

        tf.logging.info("***** Running prediction*****")
        tf.logging.info("  Num examples = %d", len(predict_examples))
        tf.logging.info("  Batch size = %d", FLAGS.predict_batch_size)
        if FLAGS.use_tpu:
            # Warning: According to tpu_estimator.py Prediction on TPU is an
            # experimental feature and hence not supported here
            raise ValueError("Prediction in TPU not supported")
        predict_drop_remainder = True if FLAGS.use_tpu else False
        predict_input_fn = file_based_input_fn_builder(
            input_file=predict_file,
            seq_length=FLAGS.max_seq_length,
            is_training=False,
            drop_remainder=predict_drop_remainder)

        predictions = estimator.predict(input_fn=predict_input_fn)

        # (FLAGS.max_seq_length-2) 是因为sequence转成 ids 后， 第一个是[CLS],最后一个是[SEP]所以最多有max_seq_length - 2有效字符
        sentences = [example.text.split()[:(FLAGS.max_seq_length - 2)] for example in predict_examples]
        ground_truths = [example.label.split()[:(FLAGS.max_seq_length - 2)] for example in predict_examples]
        prediction_labels = []
        for idx, prediction in enumerate(predictions):
            ground_truth_length = len(ground_truths[idx])
            prediction = prediction[1:(ground_truth_length + 1)]
            prediction = [id2label.get(_id, 'O') for _id in prediction]
            prediction_labels.append(prediction)
            if idx < 5:
                print('sentence {}, {}'.format(idx, sentences[idx]))
                print('ground_truth {}, {}'.format(idx, ground_truths[idx]))
                print('predition {}, {}'.format(idx, prediction_labels[idx]))

        # print(metrics.classification_report(ground_truths, prediction_labels))

        output_predict_file = os.path.join(FLAGS.output_dir, "label_test.txt")
        write_to_file(output_predict_file, sentences, ground_truths, prediction_labels)


def get_eval_fn(data_config, label_list, processor, tokenizer):
    if data_config.get('eval.tf_record_path', '') == '':
        eval_examples = processor.get_dev_examples(FLAGS.data_dir)
        eval_file = os.path.join(FLAGS.output_dir, "eval.tf_record")
        filed_based_convert_examples_to_features(
            eval_examples, label_list, FLAGS.max_seq_length, tokenizer, eval_file)
        data_config['eval.tf_record_path'] = eval_file
        data_config['num_eval_size'] = len(eval_examples)
    else:
        eval_file = data_config['eval.tf_record_path']
    # 打印验证集数据信息
    num_eval_size = data_config.get('num_eval_size', 0)
    tf.logging.info("***** Running evaluation *****")
    tf.logging.info("  Num examples = %d", num_eval_size)
    tf.logging.info("  Batch size = %d", FLAGS.eval_batch_size)
    eval_drop_remainder = True if FLAGS.use_tpu else False
    eval_input_fn = file_based_input_fn_builder(
        input_file=eval_file,
        seq_length=FLAGS.max_seq_length,
        is_training=False,
        drop_remainder=eval_drop_remainder)
    return eval_input_fn


def write_to_file(file_path, sentences, ground_truths, prediction_labels):
    with open(file_path, 'w') as f:
        for idx, (sentence, ground_truth, prediction) in enumerate(zip(sentences, ground_truths, prediction_labels)):
            if idx < 1:
                print(ground_truth, prediction)
            for word, truth, tag in zip(sentence, ground_truth, prediction):
                f.write('{}\t{}\t{}\n'.format(word, truth, tag))
            f.write('\n')


def clean_output_dir():
    if os.path.exists(FLAGS.output_dir):
        def del_file(path):
            ls = os.listdir(path)
            for i in ls:
                c_path = os.path.join(path, i)
                if os.path.isdir(c_path):
                    del_file(c_path)
                else:
                    os.remove(c_path)

        try:
            del_file(FLAGS.output_dir)
        except Exception as e:
            print(e)
            print('pleace remove the files of output dir and data.conf')
            exit(-1)
    if os.path.exists(FLAGS.data_config_path):
        try:
            os.remove(FLAGS.data_config_path)
        except Exception as e:
            print(e)
            print('pleace remove the files of output dir and data.conf')
            exit(-1)


def get_last_checkpoint(model_path):
    if not os.path.exists(os.path.join(model_path, 'checkpoint')):
        tf.logging.info('checkpoint file not exits:'.format(os.path.join(model_path, 'checkpoint')))
        return None
    last = None
    with codecs.open(os.path.join(model_path, 'checkpoint'), 'r', encoding='utf-8') as fd:
        for line in fd:
            line = line.strip().split(':')
            if len(line) != 2:
                continue
            if line[0] == 'model_checkpoint_path':
                last = line[1][2:-1]
                break
    return last


def adam_filter(model_path):
    """
    去掉模型中的Adam相关参数，这些参数在测试的时候是没有用的
    :param model_path:
    :return:
    """
    last_name = get_last_checkpoint(model_path)
    if last_name is None:
        return
    sess = tf.Session()
    imported_meta = tf.train.import_meta_graph(os.path.join(model_path, last_name + '.meta'))
    imported_meta.restore(sess, os.path.join(model_path, last_name))
    need_vars = []
    for var in tf.global_variables():
        if 'adam_v' not in var.name and 'adam_m' not in var.name:
            need_vars.append(var)
    saver = tf.train.Saver(need_vars)
    saver.save(sess, os.path.join(model_path, 'bert_model.ckpt'))


if __name__ == "__main__":
    tf.logging.set_verbosity(tf.logging.DEBUG)
    flags.mark_flag_as_required('data_dir')
    flags.mark_flag_as_required('vocab_file')
    flags.mark_flag_as_required('bert_config_file')
    flags.mark_flag_as_required('output_dir')

    tf.app.run()
    # filter model
    if FLAGS.filter_adam_var:
        adam_filter(FLAGS.output_dir)
