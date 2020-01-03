from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import six


from .load_backend import get_backend,get_image_backend,PrintException,if_else
from .load_backend import  get_session , get_trident_dir , epsilon , set_epsilon , floatx , set_floatx , camel2snake , snake2camel , addindent , format_time , get_time_suffix , get_function , get_class , get_terminal_size , gcd , get_divisors , isprime , next_prime , prev_prime , nearest_prime




from .load_backend import tile_rgb_images,loss_metric_curve,steps_histogram,is_notebook
from .load_backend import AbstractCallback, StoppingCriterionCallback, EarlyStoppingCriterionCallback, NumberOfEpochsStoppingCriterionCallback
from .load_backend import accuracy,psnr,mean_absolute_error,mean_squared_error,mean_squared_logarithmic_error,mae,mse,rmse,msle,get_metric
from .load_backend import max_norm, non_neg_norm, unit_norm, min_max_norm, maxnorm, nonnegnorm, unitnorm, minmaxnorm, get_constraint
from .load_backend import read_image , read_mask , save_image , save_mask , image2array , array2image , mask2array , array2mask , list_pictures , normalize , unnormalize , random_crop , resize , add_noise , backend_adaptive , random_channel_shift , random_cutout 
from ..optims.trainers import ModelBase,LRSchedulerMixin,OptimizerMixin


from ..data import *
from ..data import ImageReader,ImageThread
from ..optims import *

if get_backend()=='pytorch':
    from .pytorch_backend import to_numpy, to_tensor, print_network, plot_tensor_grid, summary, calculate_flops, \
        Layer, Sequential, Input,Combine, get_device, load

    from ..layers.pytorch_activations import Identity, Sigmoid, Tanh, Relu, Relu6, LeakyRelu, LeakyRelu6, SmoothRelu, PRelu, Swish, \
        Elu, HardSigmoid, HardSwish, Selu, LecunTanh, SoftSign, SoftPlus, HardTanh, Logit, LogLog, Mish, Softmax, \
        identity, sigmoid, tanh, relu, relu6, leaky_relu, leaky_relu6, smooth_relu, p_relu, swish, elu, hard_sigmoid, \
        hard_swish, selu, lecun_tanh, soft_sign, soft_plus, hard_tanh, logit, log_log, mish, softmax, get_activation

    from .pytorch_ops import reduce_min,reduce_max,reduce_mean,reduce_sum,argmax,expand_dims,meshgrid,element_cosine_distance
    from .load_backend import BertGelu, GptGelu, bert_gelu, gpt_gelu,total_variation_norm_reg

    from .load_backend import Model, TrainingPlan,summary
    from .load_backend import  MaxPool2d , MaxPool1d , MaxPool3d , MaxUnpool1d , MaxUnpool2d , MaxUnpool3d , AvgPool1d , AvgPool2d , AvgPool3d

    from .load_backend import adjust_learning_rate, reduce_lr_on_plateau,get_lr_scheduler
    from ..layers.pytorch_normalizations import  BatchNorm,BatchNorm2d, BatchNorm3d, GroupNorm2d, LayerNorm2d, get_normalization
    from .load_backend import MSELoss, CrossEntropyLoss, make_onehot, MS_SSIM, CrossEntropyLabelSmooth, \
        mixup_criterion, DiceLoss, FocalLoss, SoftIoULoss, LovaszSoftmax, TripletLoss, CenterLoss, make_onehot, \
        mixup_data,PerceptionLoss,TransformInvariantLoss,EdgeLoss
    from ..layers.pytorch_layers import Dense,Concatenate, Flatten, Conv1d, Conv2d, Conv3d, TransConv1d, TransConv2d, \
        TransConv3d, SeparableConv2d, GcdConv2d, GcdConv2d_1,  Lambda, Reshape, CoordConv2d, \
        UpsamplingBilinear2d, Dropout, AlphaDropout,SelfAttention

    from .load_backend import Adam, SGD,Ranger, Adadelta , Adagrad , RMSprop , RAdam , PlainRAdam , AdamW , Lookahead
    from .load_backend import mixup_data, cutout
    from ..layers.pytorch_blocks import Conv2d_Block, TransConv2d_Block, GcdConv2d_Block_1, GcdConv2d_Block, ShortCut2d, \
        Classifier1d
    from ..optims.pytorch_regularizers import l1_reg, l2_reg, orth_reg, total_variation_norm_reg,get_reg
elif get_backend()=='cntk':
    from .cntk_backend import to_numpy, to_tensor, get_device,Layer, Sequential, ConcatContainer, ShortcutContainer,Input,update_add
    from ..layers.cntk_activations import Identity, Sigmoid, Tanh, Relu, Relu6, LeakyRelu, LeakyRelu6, SmoothRelu, \
        PRelu, Swish, Elu, HardSigmoid, HardSwish, Selu, LecunTanh, SoftSign, SoftPlus, HardTanh, Logit, LogLog, Mish, \
        Softmax, identity, sigmoid, tanh, relu, relu6, leaky_relu, leaky_relu6, smooth_relu, p_relu, swish, elu, \
        hard_sigmoid, hard_swish, selu, lecun_tanh, soft_sign, soft_plus, hard_tanh, logit, log_log, mish, softmax, \
        get_activation
    from ..layers.cntk_normalizations import *
    from ..layers.cntk_layers import *
    from ..layers.cntk_blocks import Conv2d_Block, TransConv2d_Block
    from ..optims.cntk_optimizers import  Adam ,Ranger,RAdam,get_optimizer

elif get_backend()=='tensorflow':
    from .tensorflow_backend import Input,Sequential,ShortcutContainer,ConcatContainer,to_tensor,to_numpy
    from .tensorflow_ops import *
    from ..optims.tensorflow_regularizers import l1_reg, l2_reg, orth_reg, total_variation_norm_reg, get_reg
    from ..optims.tensorflow_lr_schedulers import *
    from ..optims.tensorflow_optimizers import *
    from ..optims.tensorflow_losses import *
    from ..optims.tensorflow_metrics import *
    from ..optims.tensorflow_constraints import *

    from ..optims.tensorflow_trainer import *
    from ..layers.tensorflow_activations import Identity ,  Sigmoid ,  Tanh ,  Relu ,  Relu6 ,  LeakyRelu ,  LeakyRelu6 ,  SmoothRelu ,  PRelu ,  Swish ,  Elu ,HardSigmoid ,  HardSwish ,  Selu ,  LecunTanh ,  SoftSign ,  SoftPlus ,  HardTanh ,  Logit ,  LogLog ,  Mish , Softmax ,  identity ,  sigmoid ,  tanh ,  relu ,  relu6 ,  leaky_relu ,  leaky_relu6 ,  smooth_relu ,  p_relu , swish ,  elu ,  hard_sigmoid ,  hard_swish ,  selu ,  lecun_tanh ,  soft_sign ,  soft_plus ,  hard_tanh , logit ,  log_log ,  mish ,  softmax ,  get_activation
    from ..layers.tensorflow_layers import *
    from ..layers.tensorflow_blocks import *
    from ..layers.tensorflow_normalizations import *
from .load_backend import *