import tensorflow as tf
import os
import numpy as np
from collections import OrderedDict, defaultdict
import yaml
from dl_rank.file import wfile
try:
    from dl_rank.layer import layers
except:
    from layer import layers

class BaseParser(object):
    def __init__(self, confPath, mode, useSpark):
        self.useSpark = useSpark
        self.confPath = confPath
        self.conf_dict = LoadDict(self.load_conf_switch(mode))
        self.column_to_csv_defaults()
        self.data_file_filter = lambda f_name: f_name.split('.')[-1] == 'txt'

    @property
    def model_out_format(self):
        if hasattr(self, '_model_out_format'):
            return self._model_out_format
        else:
            _model_out_format = self.conf_dict['separator']['model_out_format']
            self._model_out_format = [item+'_' for item in _model_out_format]
            return self._model_out_format

    def load_conf_switch(self, mode):
        confPath = self.confPath
        if self.useSpark:
            from pyspark import SparkFiles
            def wrapper(filename):
                try:
                    with open(SparkFiles.get(filename+'_'+mode+'.yaml'), 'r') as f:
                        return yaml.load(f)
                except:
                    with open(SparkFiles.get(filename+'.yaml'), 'r') as f:
                        return yaml.load(f)
            return wrapper
        else:
            def wrapper(filename):
                if wfile.Exists(os.path.join(confPath, filename+'_'+mode+'.yaml')):
                    with wfile.Open(os.path.join(confPath, filename+'_'+mode+'.yaml'), 'r') as f:
                        return yaml.load(f)
                else:
                    with wfile.Open(os.path.join(confPath, filename+'.yaml'), 'r') as f:
                        return yaml.load(f)
            return wrapper

    def load_all_conf(self, *confs):
        all_conf = dict()
        for conf in confs:
            all_conf.update({conf: self.conf_dict[conf]})
        return all_conf

    def column_to_csv_defaults(self):
        """parse columns to record_defaults param in tf.decode_csv func
        Return:
            OrderedDict {'feature name': [''],...}
        """
        feature_conf = self.conf_dict['feature']
        feature_list_conf = self.conf_dict['schema']
        feature_list = [feature_list_conf[key] for key in sorted(feature_list_conf, reverse=False)]
        self.feature_unused = []
        self.column_defaults = OrderedDict()
        self.column_scope = OrderedDict()
        self.column_length = OrderedDict()
        for f in feature_list:
            if f in feature_conf and not feature_conf[f]['ignore']:  # used features
                conf = feature_conf[f]
                scope = feature_conf[f]['parameter']['scope'] if 'scope' in feature_conf[f]['parameter'] else 'embedding'
                name = feature_conf[f]['parameter']['name'] if 'name' in feature_conf[f]['parameter'] else f
                self.column_scope[f] = [scope, name]
                self.column_length[f] = abs(feature_conf[f]['multi']['num'])  if 'multi' in feature_conf[f] else 1
            else:  # unused feature
                self.feature_unused.append(f)
            self.column_defaults[f] = ['']

    def serving_parse_fn(self, pred_node_names):
        csv_scope = self.column_scope
        feature_unused = self.feature_unused
        columns_length = self.column_length
        model_out_format = self.model_out_format
        def serving_feature_receiver_fn():
            input_dict = dict()
            # scope_set = set([f[0] for f in csv_scope.values()])
            csv_scope_name = defaultdict(list)
            for feature, scope_name in csv_scope.items():
                csv_scope_name[scope_name[0]].append(feature)
            with tf.variable_scope('placeholder'):
                for scope, features in csv_scope_name.items():
                    with tf.variable_scope(scope):
                        for feature in features:
                            if feature in feature_unused:
                                continue
                            input_dict.update({feature: tf.compat.v1.placeholder(dtype=tf.int32, shape=[None, columns_length[feature]], name=feature)})

            input_dict.update({id: tf.compat.v1.placeholder(dtype=tf.string, shape=[None], name=id) for id in model_out_format if id[:-1] not in pred_node_names})
            return tf.estimator.export.ServingInputReceiver(features=input_dict, receiver_tensors=input_dict)
        return serving_feature_receiver_fn

    def parse_fn(self, data_type, isPred=False, na_value='', tail=''):
        csv_defaults = self.column_defaults
        csv_length = self.column_length
        csv_length.update({'ctr_label': 1})
        feature_unused = self.feature_unused
        primary_delim = self.conf_dict['separator']['primary_delim']
        secondary_delim = self.conf_dict['separator']['secondary_delim']
        train_data_format = self.conf_dict['separator']['train_data_format']
        infer_data_format = self.conf_dict['separator']['infer_data_format']
        data_format = self.conf_dict['separator']['data_format']
        def _parser_feature(features):
            decode_features = tf.io.decode_csv(
                records=features, record_defaults=list(csv_defaults.values()),
                field_delim=secondary_delim, use_quote_delim=False, na_value=na_value)
            decode_features = dict(zip(csv_defaults.keys(), decode_features))
            for f in feature_unused:
                decode_features.pop(f)
            features_tail = {key+tail: decode_features[key] for key in decode_features}
            return features_tail

        def tfrecord_parser(value):
            if isPred:
                field_config = {field_name: tf.FixedLenFeature([], tf.string) for field_name in infer_data_format}
                batch_data = tf.parse_example(value, features=field_config)
                features = batch_data.pop("features")
                features_tail = _parser_feature(features)
                features_tail.update({elem+'_'+tail: data for elem, data in batch_data.items() if elem != 'features'})
                return features_tail
            else:
                field_config = {field_name: tf.FixedLenFeature([csv_length[field_name]], tf.int64) for field_name in data_format}
                batch_data = tf.parse_example(value, features=field_config)
                # features = batch_data.pop("features")
                # features_tail = _parser_feature(features)
                labels = batch_data.pop("ctr_label")
                # labels = tf.concat([tf.expand_dims(batch_data[label], 1) for label in train_data_format if label != 'features'], axis=1)
                # labels = tf.strings.to_number(labels, out_type=tf.int32)
                return batch_data, labels


        def tfrecord_str_parser(value):
            if isPred:
                field_config = {field_name: tf.FixedLenFeature([], tf.string) for field_name in infer_data_format}
                batch_data = tf.parse_example(value, features=field_config)
                features = batch_data.pop("features")
                features_tail = _parser_feature(features)
                features_tail.update({elem+'_'+tail: data for elem, data in batch_data.items() if elem != 'features'})
                return features_tail
            else:
                field_config = {field_name: tf.FixedLenFeature([], tf.string) for field_name in train_data_format}
                batch_data = tf.parse_example(value, features=field_config)
                features = batch_data.pop("features")
                features_tail = _parser_feature(features)
                labels = tf.concat([tf.expand_dims(batch_data[label], 1) for label in train_data_format if label != 'features'], axis=1)
                labels = tf.strings.to_number(labels, out_type=tf.int32)
                return features_tail, labels

        def csv_parser(value):
            """Parse train and eval data with label
            Args:
                value: Tensor("arg0:0", shape=(), dtype=string)
            """
            if isPred:
                decode_data = tf.io.decode_csv(
                    records=value, record_defaults=[['']]*len(infer_data_format),
                    field_delim=primary_delim, use_quote_delim=False, na_value=na_value)
                data_container = dict(zip(infer_data_format, decode_data))
                features_tail = _parser_feature(data_container['features'])
                features_tail.update({elem+'_'+tail: data for elem, data in data_container.items() if elem != 'features'})
                return features_tail
            else:
                decode_data = tf.io.decode_csv(
                    records=value, record_defaults=[['']]*len(train_data_format),
                    field_delim=primary_delim, use_quote_delim=False, na_value=na_value)
                data_container = dict(zip(train_data_format, decode_data))
                features_tail = _parser_feature(data_container['features'])
                labels = [tf.equal(data_container[label], '1') for label in train_data_format if label != 'features']
                labels = tf.concat([tf.expand_dims(label, 1) if label.shape.ndims<2 else label for label in labels], axis=1)
                return features_tail, labels
        if data_type == 'tfrecord':
            return tfrecord_parser
        elif data_type == "tfrecord_str":
            return tfrecord_str_parser
        else:
            return csv_parser

    # def parse_fn(self, data_type, isPred=False, na_value='', tail=''):
    #     primary_delim = self.conf_dict['separator']['primary_delim']
    #     # secondary_delim = self.conf_dict['separator']['secondary_delim']
    #     train_data_format = self.conf_dict['separator']['train_data_format']
    #     infer_data_format = self.conf_dict['separator']['infer_data_format']
    #     feature_parse_fn = self.feature_parse_fn(data_type)
    #     def tfrecord_parser(value):
    #         if isPred:
    #             field_config = {field_name: tf.FixedLenFeature([], tf.string) for field_name in infer_data_format}
    #             batch_data = tf.parse_example(value, features=field_config)
    #             return batch_data["features"]
    #         else:
    #             field_config = {field_name: tf.FixedLenFeature([], tf.string) for field_name in train_data_format}
    #             batch_data = tf.parse_example(value, features=field_config)
    #             features = batch_data.pop("features")
    #             labels = tf.concat([tf.expand_dims(batch_data[label], 1) for label in train_data_format if label != 'features'], axis=1)
    #             labels = tf.strings.to_number(labels, out_type=tf.int32)
    #             return features, labels
    #
    #     def csv_parser(value):
    #         """Parse train and eval data with label
    #         Args:
    #             value: Tensor("arg0:0", shape=(), dtype=string)
    #         """
    #         if isPred:
    #             decode_data = tf.io.decode_csv(
    #                 records=value, record_defaults=[['']]*len(infer_data_format),
    #                 field_delim=primary_delim, use_quote_delim=False, na_value=na_value)
    #             data_container = dict(zip(infer_data_format, decode_data))
    #             features_tail = _parser_feature(data_container['features'])
    #             features_tail.update({elem+'_'+tail: data for elem, data in data_container.items() if elem != 'features'})
    #             return data_container['features']
    #         else:
    #             decode_data = tf.io.decode_csv(
    #                 records=value, record_defaults=[['']]*len(train_data_format),
    #                 field_delim=primary_delim, use_quote_delim=False, na_value=na_value)
    #             data_container = dict(zip(train_data_format, decode_data))
    #             labels = [tf.equal(data_container[label], '1') for label in train_data_format if label != 'features']
    #             labels = tf.concat([tf.expand_dims(label, 1) if label.shape.ndims<2 else label for label in labels], axis=1)
    #             return data_container['features'], labels
    #     if data_type == 'tfrecord':
    #         return tfrecord_parser
    #     else:
    #         return csv_parser

    def model_input_parse_fn(self, model_first_parse_fn, model_secondary_parse_fn):
        first_parser = self.first_parse_fn if model_first_parse_fn is None else model_first_parse_fn
        second_parser = self.secondary_parse_fn if hasattr(self, 'secondary_parse_fn') else model_secondary_parse_fn
        csv_defaults = self.column_defaults
        feature_unused = self.feature_unused
        secondary_delim = self.conf_dict['separator']['secondary_delim']
        teriary_delim = self.conf_dict['separator']['teriary_delim']
        def wrapper(features, params, dims, model_struct):
            sparse_emb, deep_emb, dense_emb, mask = first_parser(features, params, teriary_delim)
            features = second_parser(sparse_emb, deep_emb, dense_emb, mask, model_struct)
            return dims, features
        return wrapper

    @staticmethod
    def first_parse_fn(features, params, teriary_delim):
        '''

        :param features:
        :param params:
        :param is_input_indices: if True: input feature has been changed to index, else string
        :return:
        sparse_features: [batch, one_hot_cate_con]
        deep_features: [batch, [cate, con], embedding_size]
        dense_features: [batch, con_num]
        '''

        sparse = params['sparse']
        deep = params['deep']
        dense = params['dense']
        numeric = params['numeric']
        table = params['table']
        multi = params['multi']

        features = {key: tf.identity(features[key], name=key) for key in features}
        # batch_size = tf.shape(features[list(features.keys())[0]])[0]
        sparse_emb = OrderedDict()
        deep_emb = OrderedDict()
        dense_emb = OrderedDict()
        dense_emb_noreduce = OrderedDict()
        mask = dict()

        for f in features:
            f_type = multi[f][0]
            num = multi[f][1]
            fill_value = multi[f][6]
            features_f = tf.strings.split(features[f], sep=teriary_delim, maxsplit=num)
            if fill_value == '':
                fill_mask = tf.not_equal(features_f.values, '')
                len_mask = tf.less(features_f.indices[:, 1], abs(num))
                f_mask = tf.squeeze(tf.where(tf.logical_and(fill_mask, len_mask)), axis=1)
                features_f = tf.SparseTensor(indices=tf.gather(features_f.indices, f_mask),
                                             values=tf.gather(features_f.values, f_mask),
                                             dense_shape=(features_f.dense_shape[0], abs(num)))
            else:
                if f_type == 'category':
                    features_f_val = tf.regex_replace(features_f.values, '^$', fill_value)
                else:
                    mask_empty = tf.cast(tf.equal(features_f.values, ''), dtype=tf.float32)
                    features_f_val = tf.regex_replace(features_f.values, '^$', '0')
                    features_f_val = tf.strings.to_number(features_f_val) + fill_value * mask_empty
                f_mask = tf.squeeze(tf.where(tf.less(features_f.indices[:, 1], abs(num))), axis=1)
                features_f = tf.SparseTensor(indices=tf.gather(features_f.indices, f_mask),
                                             values=tf.gather(features_f_val, f_mask),
                                             dense_shape=(features_f.dense_shape[0], abs(num)))
            features[f] = features_f

        for f in numeric:
            f_type, num, size, combiner, same, default_value, _, null_value = multi[f]
            if combiner == 'none':
                features_f, f_mask = layers.to_dense(features[f], default_value=null_value, out_type=tf.float32)
                dense_emb_noreduce.update({f: (features_f, f_mask)})
                if f in dense:
                    dense_emb.update({f: features_f})    #chi cun shi fou wei N, 1 haishi N,
                if num < 0 and f not in mask.keys():
                    mask[f] = f_mask
            else:
                sparse_f_float, sparse_f_indice = layers.sparse_str2sparse_num(features[f], tf.float32)
                # tfprint = tf.print('sparse_f_float', sparse_f_float, summarize=1e6)
                # with tf.control_dependencies([tfprint]):
                f_input_combine = layers.sparse_reduce(sparse_f_float, reduce_type=combiner)# tf.cast(tf.expand_dims(tf.nn.embedding_lookup_sparse(tf.ones([abs(num)], dtype=tf.float32), sparse_f_indice, sparse_f_float, combiner='sqrtn'), 1), dtype=tf.float32)
                # tp = tf.print('sparse_f_indice', sparse_f_indice, 'sparse_f_float', sparse_f_float, 'combiner', f_input_combine, 'thereis f_input_combine', features[f], f, summarize=1e6)
                # with tf.control_dependencies([tp]):
                #     f_input_combine = tf.identity(f_input_combine)
                dense_emb_noreduce.update({f: (sparse_f_float if not same else f_input_combine, sparse_f_indice)})
                if f in dense:
                    dense_emb.update({f: f_input_combine})
        # all sparse only for category features
        for f in sparse:
            f_type, num, size, combiner, same, default_value, _, null_value = multi[f]
            if combiner == 'none':
                if f in table.keys():
                    features_f_indice = table[f].lookup(features[f])
                    features_f_indicator, f_mask = layers.to_dense(features_f_indice, default_value=int(null_value))
                    # f_mask = tf.not_equal(features_f_indicator, null_value)
                else:
                    features_f_indicator, f_mask = layers.to_dense(features[f], default_value=null_value, out_type=tf.int32)
                    features_f_indicator = layers.replace2default(features_f_indicator, size, default_value)
                # features_f_emb = tf.nn.embedding_lookup(sparse[f], features_f_indicator)
                features_f_emb = layers.multi_hot(features_f_indicator, num=abs(num), depth=size)
                sparse_emb.update({f: features_f_emb})
                if num < 0 and f not in mask.keys():
                    mask[f] = f_mask
            else:
                if f in table.keys():
                    features_f_indice = table[f].lookup(features[f])
                else:
                    features_f_indice, _ = layers.sparse_str2sparse_num(features[f], tf.int32)
                    features_f_indice = layers.replace2default(features_f_indice, size, default_value)
                # features_f_emb = tf.nn.embedding_lookup_sparse(sparse[f], features_f_indice, None, combiner=combiner)
                features_f_emb = layers.multi_hot(features_f_indice, depth=size, combiner=combiner)
                # _ = tf.reduce_mean(features_f_emb, axis=0, name='{}_embedding_params'.format(f))
                sparse_emb.update(
                    {f: tf.expand_dims(features_f_emb, 1)})

        for f in deep:
            f_type, num, size, combiner, same, default_value, _, null_value = multi[f]
            if f_type == 'category':
                if combiner == 'none':
                    deep_f = deep[f]
                    if f in table.keys():
                        features_f_indice = table[f].lookup(features[f])
                        features_f_indicator, f_mask = layers.to_dense(features_f_indice, default_value=null_value)
                        # f_mask = tf.not_equal(features_f_indicator, null_value)
                    else:
                        features_f_indicator, f_mask = layers.to_dense(features[f], default_value=null_value, out_type=tf.int32)
                        features_f_indicator = layers.replace2default(features_f_indicator, size, default_value)
                    features_f_emb = layers.embedding_lookup(deep_f, features_f_indicator)
                    deep_emb.update({f: features_f_emb})
                    if num < 0:
                        mask[f] = f_mask
                        _ = tf.identity(tf.multiply(tf.cast(tf.expand_dims(f_mask, -1), tf.float32), features_f_emb), name='{}_used_embedding_params'.format(f))    #bs,num.vec
                    else:
                        _ = tf.identity(features_f_emb, name='{}_used_embedding_params'.format(f))#bs,num,vec
                else:
                    if f in table.keys():
                        features_f_indice = table[f].lookup(features[f])
                    else:
                        features_f_indice, _ = layers.sparse_str2sparse_num(features[f], tf.int32)
                        features_f_indice = layers.replace2default(features_f_indice, size, default_value)
                    if same:
                        features_f_emb = tf.tile(deep[f], tf.stack(tf.shape(features_f_indice.dense_shape)[0], 1))
                        assert False, 'u cant do this（set same in category feature） 0_0'
                    else:
                        features_f_emb = tf.nn.embedding_lookup_sparse(deep[f], features_f_indice, None, combiner=combiner)
                        features_f_emb = tf.pad(features_f_emb, [[0, tf.cast(features_f_indice.dense_shape[0], tf.int32)-tf.shape(features_f_emb)[0]], [0, 0]], 'CONSTANT', constant_values=0)
                        features_f_emb = tf.identity(features_f_emb)
                    deep_emb.update(
                        {f: tf.expand_dims(features_f_emb, 1)})
                    _ = tf.identity(features_f_emb, name='{}_used_embedding_params'.format(f))
            elif f_type == 'numeric':
                features_f_value, sparse_f_indice = dense_emb_noreduce[f]
                if combiner == 'none':
                    features_f_emb = tf.multiply(tf.expand_dims(features_f_value, -1), tf.expand_dims(deep[f], 0))
                    deep_emb.update({f: features_f_emb})
                    sparse_f_indice = tf.cast(sparse_f_indice, tf.float32)
                    _ = tf.multiply(sparse_f_indice[:, :, np.newaxis], deep[f][np.newaxis, :, :], name='{}_used_embedding_params'.format(f))
                else:
                    if same:
                        features_f_combine = tf.expand_dims(tf.matmul(features_f_value, deep[f]), axis=1)
                        deep_emb.update({f: features_f_combine})
                        ###
                        _ = tf.identity(tf.expand_dims(deep[f], 0), name='{}_used_embedding_params'.format(f))#1,field_num,vec
                    else:
                        features_f_emb = layers.embedding_lookup_sparse(deep[f], sparse_f_indice, features_f_value, combiner=combiner)
                        _ = layers.embedding_lookup_sparse(deep[f], sparse_f_indice, None, combiner='mean', name='{}_used_embedding_params'.format(f))
                        # _ = tf.identity(features_f_emb, name='{}_used_embedding_params'.format(f))#bs,vec
                        features_f_combine = tf.expand_dims(features_f_emb, 1)
                        deep_emb.update({f: features_f_combine})

        return sparse_emb, deep_emb, dense_emb, mask

class LoadDict(dict):
    def __init__(self, load_fn):
        super(LoadDict, self).__init__()
        self.load_fn = load_fn

    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            try:
                value = self.load_fn(item)
            except:
                value = None
            self.__setitem__(item, value)
            return value
