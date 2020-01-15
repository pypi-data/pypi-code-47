#!/usr/bin/env python
# coding: utf-8

from abc import ABC, abstractmethod

import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import torch.nn.functional as F

from napoleontoolbox.neural_net import roll_multi_layer_lstm
from napoleontoolbox.file_saver import dropbox_file_saver
from napoleontoolbox.neural_net import roll_multi_layer_perceptron
from napoleontoolbox.boosted_trees import roll_lightgbm
from napoleontoolbox.features import features_type

from napoleontoolbox.utility import weights

import torch
import torch.nn as nn


class AbstractRunner(ABC):

    def __init__(self, drop_token=None, dropbox_backup = True, supervision_npy_file_suffix='_supervision.npy', features_saving_suffix='_features.npy', features_names_saving_suffix='_features_names.npy', returns_pkl_file_name='returns.pkl', local_root_directory='../data/', user = 'napoleon', lr=0.001, n_start = 252):
        super().__init__()
        self.supervision_npy_file_suffix=supervision_npy_file_suffix
        self.features_saving_suffix=features_saving_suffix
        self.features_names_saving_suffix=features_names_saving_suffix
        self.returns_pkl_file_name=returns_pkl_file_name
        self.local_root_directory=local_root_directory
        self.user=user
        self.lr=lr
        self.n_start = n_start
        self.dbx = dropbox_file_saver.NaPoleonDropboxConnector(drop_token,dropbox_backup=dropbox_backup)

    @abstractmethod
    def runTrial(self,saver, seed, sup, layers, epochs, n_past_features, n, s, whole_history, advance_feature, advance_signal,
                 normalize, activation_string, convolution):
        pass


class SimpleRunner(AbstractRunner):
    def runTrial(self, saver, seed, sup, layers, epochs, n_past_features, n, s, feature_type, activation_string, convolution):

        if (feature_type is features_type.FeaturesType.HISTORY or feature_type is features_type.FeaturesType.HISTORY_ADVANCED) and n_past_features is None:
            return

        if (feature_type is features_type.FeaturesType.STANDARD or feature_type is features_type.FeaturesType.STANDARD_ADVANCED) and n_past_features is not None:
            return

        meArg = (
            seed, sup, layers, epochs, n_past_features, n, s, feature_type,
            activation_string, convolution)

        meArgList = list(meArg)
        meArgList = [str(it) for it in meArgList]
        savingKey = ''.join(meArgList)
        savingKey = savingKey.replace('[', '')
        savingKey = savingKey.replace(']', '')
        savingKey = savingKey.replace(',', '')
        savingKey = savingKey.replace(' ', '')
        savingKey = savingKey.replace('.', '')
        # savingKey = savingKey.replace('_','')
        savingKey = 'T_' + savingKey

        print('Launching computation with parameters : '+savingKey)

        supervisors = {}
        supervisors['f_minVar'] = 0
        supervisors['f_maxMean'] = 1
        supervisors['f_sharpe'] = 2
        supervisors['f_MeanVar'] = 3
        supervisors['f_calmar'] = 4
        supervisors['f_drawdown'] = 5

        df = self.dbx.local_overwrite_and_load_pickle( folder='', subfolder='', returns_pkl_file_name=self.returns_pkl_file_name, local_root_directory = self.local_root_directory)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.set_index('Date')
        df = df.fillna(method='ffill')
        print('size return '+str(df.shape))


        result =self.dbx.local_supervision_npy_overwrite_and_load_array(rebal = s , local_root_directory= self.local_root_directory, user = self.user, supervision_npy_file_suffix= self.supervision_npy_file_suffix)

        np.random.seed(seed)
        torch.manual_seed(seed)
        # Set data
        whole_history = (feature_type is features_type.FeaturesType.HISTORY or feature_type is features_type.FeaturesType.HISTORY_ADVANCED)

        features, features_names = self.dbx.local_features_npy_ovverwrite_and_load_array(feature_type=feature_type, n_past_features=n_past_features,
                                                    local_root_directory=self.local_root_directory, user=self.user,
                                                    features_saving_suffix=self.features_saving_suffix,
                                                    features_names_saving_suffix=self.features_names_saving_suffix)

        # X = features[s:-s]
        # y = result[s:-s, :, supervisors[sup]]
        X = features[self.n_start:]
        y = result[self.n_start:, :, supervisors[sup]]
        df = df.iloc[self.n_start:]
        print('predictors')
        print(X.shape)
        print('utility')
        print(y.shape)
        print('prices')
        print(df.shape)

        # convolution 0 : perceptron
        # convolution 1 : LSTM
        # convolution 2 : xgboost

        if whole_history:
            if convolution == 2:
                print('no whole time history with ensembling method')
                return
            if convolution == 0:
                print('no whole time history with multi layers perceptron')
                # uncomment if you want multi layers perceptron with full historical backtest
                # print('flattening predictor time series for perceptron')
                # _X = np.empty((X.shape[0], X.shape[1] * X.shape[2]), dtype=np.float32)
                # for l in range(X.shape[0]):
                #     temp = np.transpose(X[l, :, :])
                #     _X[l, :] = temp.flatten()
                # X = _X

        if not whole_history:
            if convolution == 1:
                print('only whole time history with lstm')
                # print('adding one virtual time stamp')
                # X = X[..., np.newaxis, :]
                return

        print('number of nan/infinity features')
        print(np.isnan(X).sum(axis=0).sum())
        print(np.isinf(X).sum(axis=0).sum())
        print('number of nan/infinity output')
        print(np.isnan(y).sum(axis=0).sum())
        print(np.isinf(y).sum(axis=0).sum())

        print(np.count_nonzero(~np.isnan(X)))

        X = np.float32(X)
        y = np.float32(y)

        neural_net_precision = None
        if X.dtype == np.float64:
            neural_net_precision = torch.float64
        if X.dtype == np.float32:
            neural_net_precision = torch.float32

        activation_function = None
        if activation_string == 'sigmoid':
            activation_function = torch.sigmoid
        if activation_string == 'relu':
            activation_function = F.relu

        if convolution == 1:
            # the number of figures
            input_size = X.shape[2]
            hidden_size = 32
            num_layers = 1
            num_classes = y.shape[1]
            tm = roll_multi_layer_lstm.RollMultiLayerLSTM(
                X=X,
                y=y,
                num_classes=num_classes,
                input_size=input_size,
                hidden_size=hidden_size,
                num_layers=num_layers,
                # nn.Softmax/nn.Softmin can be good activations for this problem
                x_type=neural_net_precision,
                y_type=neural_net_precision
                # activation_kwargs={'dim':1} # Parameter needed for nn.Softmax/nn.Softmin
            )
            tm.set_optimizer(nn.MSELoss, torch.optim.Adam, lr=self.lr, betas=(0.9, 0.999), amsgrad=True)
            tm = tm.set_roll_period(n, s, repass_steps=epochs)
        elif convolution == 0:
            tm = roll_multi_layer_perceptron.RollMultiLayerPerceptron(
                X=X,
                y=y,
                layers=layers,
                activation=activation_function,  # nn.Softmax/nn.Softmin can be good activations for this problem
                x_type=neural_net_precision,
                y_type=neural_net_precision,
                # activation_kwargs={'dim':1} # Parameter needed for nn.Softmax/nn.Softmin
            )
            tm.set_optimizer(nn.MSELoss, torch.optim.Adam, lr=self.lr, betas=(0.9, 0.999), amsgrad=True)
            tm = tm.set_roll_period(n, s, repass_steps=epochs)
        elif convolution == 2:
            tm = roll_lightgbm.RollLightGbm(
                X=X,
                y=y
            )
            tm = tm.set_roll_period(n, s)

        tm.unroll()
        recordings_df = tm.recorder.get_all_recordings()
        print('recordings '+str(list(recordings_df.columns)))
        tm.save_model()

        # tm.y_test[tm.t:] = tm.sub_predict(tm.X[tm.t:])
        df_ret = df.fillna(method='bfill').pct_change().fillna(0).copy()
        # Process weights
        weight_mat = weights.process_weights(w=tm.y_test, df=df_ret, s=s, n=n)
        # Compute portfolio perf
        portfolio = np.cumprod(np.prod(df_ret * weight_mat.values + 1, axis=1))

        saver.saveResults(savingKey, portfolio, weight_mat, recordings_df)
        print('saved '+ savingKey)


