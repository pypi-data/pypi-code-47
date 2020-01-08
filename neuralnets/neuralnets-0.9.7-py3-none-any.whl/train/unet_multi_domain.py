"""
    This is a script that illustrates training a U-Net
"""

"""
    Necessary libraries
"""
import argparse
import datetime
import os

import numpy as np
import torch
import torch.optim as optim
from torch.utils.data import DataLoader

from neuralnets.data.datasets import StronglyLabeledMultiVolumeDataset
from neuralnets.networks.unet import UNet2D
from neuralnets.util.losses import CrossEntropyLoss
from neuralnets.util.preprocessing import get_augmenter2d
from neuralnets.util.tools import set_seed
from neuralnets.util.validation import validate

"""
    Parse all the arguments
"""
print('[%s] Parsing arguments' % (datetime.datetime.now()))
parser = argparse.ArgumentParser()

# logging parameters
parser.add_argument("--seed", help="Seed for randomization", type=int, default=0)
parser.add_argument("--log_dir", help="Logging directory", type=str, default="unet_multi_domain")
parser.add_argument("--print_stats", help="Number of iterations between each time to log training losses",
                    type=int, default=50)

# network parameters
parser.add_argument("--data_dir", help="Data directory", type=str, default="../../../data")
parser.add_argument("--input_size", help="Size of the blocks that propagate through the network",
                    type=str, default="256,256")
parser.add_argument("--sample_size", help="Size of the blocks that are extracted",
                    type=str, default="448,448")
parser.add_argument("--fm", help="Number of initial feature maps in the segmentation U-Net", type=int, default=16)
parser.add_argument("--levels", help="Number of levels in the segmentation U-Net (i.e. number of pooling stages)",
                    type=int, default=4)
parser.add_argument("--dropout", help="Dropout", type=float, default=0.25)
parser.add_argument("--norm", help="Normalization in the network (batch or instance)", type=str, default="instance")
parser.add_argument("--activation", help="Non-linear activations in the network", type=str, default="relu")

# optimization parameters
parser.add_argument("--lr", help="Learning rate of the optimization", type=float, default=1e-3)
parser.add_argument("--step_size", help="Number of epochs after which the learning rate should decay",
                    type=int, default=10)
parser.add_argument("--gamma", help="Learning rate decay factor", type=float, default=0.9)
parser.add_argument("--epochs", help="Total number of epochs to train", type=int, default=200)
parser.add_argument("--len_epoch", help="Number of iteration in each epoch", type=int, default=1000)
parser.add_argument("--test_freq", help="Number of epochs between each test stage", type=int, default=1)
parser.add_argument("--train_batch_size", help="Batch size in the training stage", type=int, default=2)
parser.add_argument("--test_batch_size", help="Batch size in the testing stage", type=int, default=2)

args = parser.parse_args()
args.input_size = [int(item) for item in args.input_size.split(',')]
args.sample_size = [int(item) for item in args.sample_size.split(',')]
loss_fn = CrossEntropyLoss()

"""
Fix seed (for reproducibility)
"""
set_seed(args.seed)

"""
    Setup logging directory
"""
print('[%s] Setting up log directories' % (datetime.datetime.now()))
if not os.path.exists(args.log_dir):
    os.mkdir(args.log_dir)

"""
    Load the data
"""
print('[%s] Loading data' % (datetime.datetime.now()))
input_shape = (1, args.input_size[0], args.input_size[1])
sample_shape = (1, args.sample_size[0], args.sample_size[1])
augmenter = get_augmenter2d(input_shape[1:], sample_shape[1:], include_segmentation=True)
train_data_paths = [os.path.join(args.data_dir, 'EM/EPFL/training.tif'),
                    os.path.join(args.data_dir, 'EM/VNC/data_train.tif')]
train_label_paths = [os.path.join(args.data_dir, 'EM/EPFL/training_groundtruth.tif'),
                     os.path.join(args.data_dir, 'EM/VNC/mito_labels_train.tif')]
test_data_paths = [os.path.join(args.data_dir, 'EM/EPFL/testing.tif'),
                   os.path.join(args.data_dir, 'EM/VNC/data_test.tif')]
test_label_paths = [os.path.join(args.data_dir, 'EM/EPFL/testing_groundtruth.tif'),
                    os.path.join(args.data_dir, 'EM/VNC/mito_labels_test.tif')]
res_epfl = (1, 5, 5)
res_vnc = (1, 4.6, 4.6)
# res_mira = (1, 2, 2)
scaling = [np.divide(res_epfl, res_epfl),
           np.divide(res_vnc, res_epfl)]
train = StronglyLabeledMultiVolumeDataset(train_data_paths, train_label_paths, scaling=scaling,
                                          input_shape=sample_shape, len_epoch=args.len_epoch)
test = StronglyLabeledMultiVolumeDataset(test_data_paths, test_label_paths, scaling=scaling,
                                         input_shape=sample_shape, len_epoch=args.len_epoch)
train_loader = DataLoader(train, batch_size=args.train_batch_size)
test_loader = DataLoader(test, batch_size=args.train_batch_size)

"""
    Build the network
"""
print('[%s] Building the network' % (datetime.datetime.now()))
net = UNet2D(feature_maps=args.fm, levels=args.levels, dropout_enc=args.dropout, norm=args.norm,
             activation=args.activation)

"""
    Setup optimization for training
"""
print('[%s] Setting up optimization for training' % (datetime.datetime.now()))
optimizer = optim.Adam(net.parameters(), lr=args.lr)
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=args.step_size, gamma=args.gamma)

"""
    Train the network
"""
print('[%s] Starting training' % (datetime.datetime.now()))
net.train_net(train_loader, test_loader, loss_fn, optimizer, args.epochs, scheduler=scheduler,
              augmenter=augmenter, print_stats=args.print_stats, log_dir=args.log_dir)

"""
    Validate the trained network
"""
validate(net, test.data, test.labels, args.input_size, batch_size=args.test_batch_size,
         write_dir=os.path.join(args.write_dir, 'segmentation_final'),
         val_file=os.path.join(args.log_dir, 'validation_final.npy'))
net = torch.load(os.path.join(args.log_dir, 'best_checkpoint.pytorch'))
validate(net, test.data, test.labels, args.input_size, batch_size=args.test_batch_size,
         write_dir=os.path.join(args.write_dir, 'segmentation_best'),
         val_file=os.path.join(args.log_dir, 'validation_best.npy'))

print('[%s] Finished!' % (datetime.datetime.now()))
