import os
import sys
import matplotlib
import platform

if platform.system() not in ['Linux', 'Darwin'] and not platform.system().startswith('CYGWIN'):
    matplotlib.use('TKAgg')
from IPython import display
import inspect
import time
import random
import string
import uuid
import torch
import torch.nn as nn
from collections import OrderedDict
from functools import partial
import numpy as np
from ..backend.common import addindent, get_time_suffix, format_time, get_terminal_size, snake2camel, PrintException, to_list,unpack_singleton,enforce_singleton
from ..backend.pytorch_backend import *
from .pytorch_optimizers import get_optimizer
from .pytorch_losses import get_loss
from .pytorch_metrics import get_metric
from .pytorch_regularizers import get_reg
from .pytorch_constraints import get_constraint
from .pytorch_lr_schedulers import get_lr_scheduler
from ..misc.visualization_utils import tile_rgb_images, loss_metric_curve

from .trainers import ModelBase,OptimizerMixin,progress_bar
from ..data.image_common import *
__all__ = ['TrainingItem', 'Model','ImageClassificationModel']

_, term_width = get_terminal_size()
term_width = int(term_width)
TOTAL_BAR_LENGTH = 65.
last_time = time.time()
begin_time = last_time

def _to_tuple(x):
    if isinstance(x, tuple):
        return x
    elif isinstance(x, list):
        return tuple(x)
    else:
        return x,


def make_deterministic(seed: int = 19260817, cudnn_deterministic: bool = False):
    r"""Make experiment deterministic by using specific random seeds across
    all frameworks and (optionally) use deterministic algorithms.
    Args:
        seed (int): The random seed to set.
        cudnn_deterministic (bool): If `True`, set CuDNN to use
            deterministic algorithms. Setting this to `True` can negatively
            impact performance, and might not be necessary for most cases.
            Defaults to `False`.
    """

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

    if cudnn_deterministic:
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False






class Model(ModelBase):
    def __init__(self, inputs=None, output=None, input_shape=None):
        super(Model, self).__init__(inputs, output, input_shape)

    def _initial_graph(self, inputs=None, output=None, input_shape=None):
        if output is None:
            raise ValueError('There is at least one output')

        if inputs is None:
            if input_shape is None:
                raise ValueError('You should assign inputs or input shape')
            else:
                input_shape = _to_tuple(input_shape)
                input_name = 'input_{0}'.format(len(self.inputs))
                input_var = Input(input_shape, name=input_name)
                self.inputs[input_name] = input_var
        elif isinstance(inputs,Input):
            input_name = inputs.name if inputs.name!='' else 'input_{0}'.format(len(self.inputs))
            input_shape=inputs.input_shape
            self.inputs[input_name] = inputs
        elif isinstance(inputs, (tuple, list)):
            for inp in inputs:
                if isinstance(inp,Input):
                    input_name = inp.name if inp.name != '' else 'input_{0}'.format(len(self.inputs))
                    self.inputs[input_name] = inp
        elif isinstance(inputs, dict):
            for k, v in inputs.items():
                if isinstance(v, Input):
                    self.inputs[k] = v
        if isinstance(output, (Layer, nn.Module)):
            output.input_shape=input_shape
            self.model = output
        elif isinstance(output, (list,tuple)):
            output_list=[]
            for op in output:
                if isinstance(op, (Layer, nn.Module)):
                    output_list.append(op)
            self.model =Combine(output_list)
        else:
            raise ValueError('Invalid output')
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.training_context['current_model'] = self.model

    @property
    def layers(self):
        return self.model._nodes

    def complie(self, optimizer, losses=None, metrics=None, loss_weights=None, sample_weight_mode=None,
                weighted_metrics=None, target_tensors=None):
        self.with_optimizer(optimizer)
        if losses is not None and isinstance(losses, (list, tuple)):
            for loss in losses:
                self.with_loss(loss)
        if metrics is not None and isinstance(metrics, (list, tuple)):
            for metric in metrics:
                self.with_metric(metric)

        return self

    def with_optimizer(self, optimizer, **kwargs):
        if isinstance(optimizer, str):
            optimizer_class = get_optimizer(optimizer)
            self.optimizer = optimizer_class(self.model.parameters(), **kwargs)

        else:
            self.optimizer = optimizer(self.model.parameters(), **kwargs)
        # self.lr_scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(self.optimizer, verbose=True, mode='min',
        #                                                                factor=0.5, patience=5, threshold=1e-4,
        #                                                                cooldown=0, min_lr=1e-10, eps=1e-8)
        self.base_lr = kwargs.get('lr', kwargs.get('learning_rate', 1e-3))
        self.training_context['optimizer'] = self.optimizer
        self.training_context['base_lr'] = self.base_lr
        self.training_context['current_lr'] = self.base_lr
        return self

    def with_loss(self, loss, loss_weight=1,output_idx=0,name='',**kwargs):
        if isinstance(loss, str):
            loss = get_loss(loss)
        alias=name
        if inspect.isclass(loss):
            alias=loss.__name__ if len(alias)==0 else alias
        if len(alias)==0 and hasattr(loss,'__name__') :
             alias=  loss.__name__
        self.loss_weights[alias]=loss_weight
        if hasattr(loss, 'forward'):
            self._losses[alias] = loss(**kwargs)
            if hasattr(self._losses[alias], 'reduction'):
                setattr(self._losses[alias], 'reduction', 'mean')
            if hasattr(self._losses[alias], 'size_average'):
                setattr(self._losses[alias], 'size_average', 'True')
        elif callable(loss):
            self._losses[alias] = partial(loss, **kwargs)
        return self

    def with_metric(self, metric, output_idx=0,name='', **kwargs):
        if isinstance(metric, str):
            metric = get_metric(metric)
        alias = name
        if inspect.isfunction(metric):
            alias = metric.__name__ if len(alias) == 0 else alias
        if len(alias) == 0 and hasattr(metric, 'name'):
            alias = metric.name
        if hasattr(metric, 'forward'):
            self._metrics[alias] = metric(**kwargs)
            # if hasattr(self._metrics[metric.__name__], 'reduction'):
            #     setattr(self._metrics[metric.__name__], 'reduction', 'mean')
        elif callable(metric):
            self._metrics[alias] = partial(metric, **kwargs)
        return self

    def with_regularizer(self, reg, **kwargs):
        if reg is None:
            return self
        reg_fn = None
        if isinstance(reg, str):
            reg_fn = get_reg(reg)
        elif reg is callable:
            reg_fn = reg
        args = reg_fn.__code__.co_varnames
        if 'reg_weight' in args:
            if 'model' in args:
                self._model_regs[reg_fn.__name__] = partial(reg_fn, **kwargs)
            elif 'output' in args:
                self._output_regs[reg_fn.__name__] = partial(reg_fn, **kwargs)
        return self

    def with_constraint(self, constraint, **kwargs):
        if constraint is None:
            return self
        constraint_fn = None
        if isinstance(constraint, str):
            constraint_fn = get_constraint(constraint)

        if hasattr(constraint_fn, 'forward') and constraint_fn.__name__[-4:] == 'norm':
            self._constraints[constraint_fn.__name__] = constraint_fn(**kwargs)

        elif callable(constraint_fn) and constraint_fn.__name__[-4:] == 'norm':
            self._constraints[constraint_fn.__name__] = partial(constraint_fn, **kwargs)

        return self

    def with_model_save_path(self, save_path, **kwargs):
        if save_path is not None and len(save_path) > 1:
            folder, filename = os.path.split(save_path)
            if not os.path.exists(folder):
                try:
                    os.makedirs(folder)
                except Exception as e:
                    PrintException()
                    raise ValueError('folder:{0} is not valid path'.format(folder))

        self.training_context['save_path'] = save_path
        return self

    def with_learning_rate_schedule(self, lr_schedule, warmup=0, **kwargs):
        if lr_schedule is None:
            return self
        if isinstance(lr_schedule,str):
            lr_schedule=get_lr_scheduler(lr_schedule)
        if callable(lr_schedule) :
           self.lr_scheduler= lr_schedule(self.optimizer,**kwargs)
        self.warmup = warmup
        if self.warmup > 0:
            self.optimizer.adjust_learning_rate(1e-5,False)
            self.training_context['current_lr'] =1e-5
        return self

    def adjust_learning_rate(self,lr):
        self.optimizer.param_groups[0]['lr']=lr
        self.training_context['current_lr']=lr

    def do_on_training_start(self):
        self.model.train()
        self.model.zero_grad()

    def do_on_training_end(self):
        self.model.eval()

    def do_on_epoch_start(self):
        if self.training_context['current_epoch'] < self.warmup:
            lr = 1e-5 * (self.training_context['current_epoch'] + 1)
            self.optimizer.param_groups[0]['lr'] = lr
            self.training_context['current_lr'] = lr
        elif self.training_context['current_epoch'] == self.warmup:
            self.optimizer.param_groups[0]['lr'] = self.base_lr
            self.training_context['current_lr'] =self.base_lr
        if self.device == 'cuda':
            torch.cuda.empty_cache()

    def do_on_epoch_end(self):
        if self.training_context['current_epoch'] > self.warmup:
            if self.lr_scheduler is not None:
                self.lr_scheduler.step(np.array(self.training_context['metrics'][list(self._metrics.keys())[0]]).mean())
                self.training_context['current_lr'] = self.optimizer.lr
            if self.optimizer.param_groups[0]['lr'] < 1e-8:
                self.optimizer.param_groups[0]['lr'] = 0.05 * self.base_lr
                self.training_context['current_lr'] =  0.05 * self.base_lr
        elif self.training_context['current_epoch'] == self.warmup:
            self.optimizer.adjust_learning_rate(self.base_lr, True)
            self.training_context['current_lr'] =self.base_lr
        elif self.training_context['current_epoch'] < self.warmup:
            self.optimizer.adjust_learning_rate(1e-5*(self.training_context['current_epoch']+1), True)
            self.training_context['current_lr'] = 1e-5*(self.training_context['current_epoch']+1)

    def do_on_batch_start(self):
        #set model as training state
        #zero grad
        pass

    def do_on_batch_end(self):
        #set model as training state
        #zero grad
        pass

    def do_on_data_received(self, input=None, target=None):
        if input is not None:
            input=to_tensor(input)
        if target is not None:
            target=to_tensor(target)
        return input,target


    def do_preparation_for_loss(self):
        self.model.zero_grad()
        self.optimizer.zero_grad()


    def do_post_loss_calculation(self):
        pass

    def get_current_loss(self):
        return self.training_context['current_loss']

    def do_gradient_update(self,log_gradients=False):
        self.training_context['current_loss'].backward()
        if log_gradients :
            self.log_gradient()
        self.optimizer.step(self.get_current_loss)

    def do_post_gradient_update(self):
        pass

    def do_on_progress_end(self):
        if self.training_context['current_epoch'] > self.warmup:
            if self.lr_scheduler is not None:
                self.lr_scheduler.step(np.array(self.training_context['metrics'][list(self._metrics.keys())[0]]).mean())
                self.training_context['current_lr'] = self.optimizer.lr

    def log_gradient(self,grads=None):
        grad_dict = {}
        for k, v in self.model.named_parameters():
            grad_dict[k] = to_numpy(v.grad)
        self.gradients_history.append(grad_dict)


    def log_weight(self,weghts=None):
        weight_dict = {}
        for k, v in self.model.named_parameters():
            weight_dict[k] = to_numpy(v.data)
        self.weights_history.append(weight_dict)


    def save_model(self,save_path=None):
        for callback in self.training_context['callbacks']:
            callback.on_start_save_model(self.training_context)
        self.model.eval()
        save_path=save_path if save_path is not None else self.training_context.get('save_path',save_path)
        if save_path is not None:
            #torch.save(self.model, file_path)
            torch.save({'state_dict': self.model.state_dict()},save_path+'.tar')
        else:
            save_full_path = 'Models/model_{0}_epoch{1}.pth'.format(self.model.name,self.training_context['current_epoch'])
            #torch.save(self.model, save_full_path)
            torch.save({'state_dict': self.model.state_dict()},save_full_path+'.tar')

        self.model.train()


    def save_onnx(self, file_path):
        import torch.onnx
        input_names = ["input_0"]
        output_names = ["output0"]
        dummy_input = torch.randn(1,*self.model.input_shape.tolist(), device='cuda')
        torch.onnx.export(self.model, dummy_input,file_path, verbose=True, input_names=input_names,
                          output_names=output_names)

    def summary(self):
        summary(self.model,tuple(self.model.input_shape))

    def extra_repr(self):
        return ''

    def __str__(self):
        self.__repr__()

    def _get_name(self):
        return self.__class__.__name__

    def __repr__(self):
        # We treat the extra repr like the sub-module, one item per line
        extra_lines = []
        extra_repr = self.extra_repr()
        # empty string will be split into list ['']
        if extra_repr:
            extra_lines = extra_repr.split('\n')
        child_lines = []
        for key, value in self.__dict__.items():
            if isinstance(value, OrderedDict):
                for subkey, subvalue in value.items():
                    mod_str = repr(subvalue)
                    mod_str = addindent(mod_str, 2)
                    child_lines.append('(' + key + '): ' + mod_str)
            else:
                mod_str = repr(value)
                mod_str = addindent(mod_str, 2)
                child_lines.append('(' + key + '): ' + mod_str)
        lines = extra_lines + child_lines

        main_str = self._get_name() + '('
        if lines:
            # simple one-liner info, which most builtin Modules will use
            if len(extra_lines) == 1 and not child_lines:
                main_str += extra_lines[0]
            else:
                main_str += '\n  ' + '\n  '.join(lines) + '\n'

        main_str += ')'
        return main_str

    def __dir__(self):
        module_attrs = dir(self.model.__class__)
        optimizer_attrs = dir(self.optimizer.__class__)
        attrs = list(self.__dict__.keys())
        losses = list(self._losses.keys())
        metrics = list(self._metrics.keys())
        output_regs = list(self._output_regs.keys())
        model_regs = list(self._model_regs.keys())
        constraints = list(self._constraints.keys())
        keys = module_attrs +optimizer_attrs+ attrs + losses + metrics+output_regs+model_regs+constraints
        # Eliminate attrs that are not legal Python variable names
        keys = [key for key in keys if not key[0].isdigit()]

        return sorted(keys)



class ImageClassificationModel(Model):
    def __init__(self, inputs=None, output=None, input_shape=None):
        super(ImageClassificationModel, self).__init__(inputs, output, input_shape)

        self._class_names=[]
        self.preprocess_flow=[]
        self._idx2lab={}
        self._lab2idx={}


    @property
    def class_names(self):
        return self._class_names

    @class_names.setter
    def class_names(self,value):
        if self._class_names!=value:
            self._class_names=value
            self._lab2idx = {v: k for k, v in enumerate(self._class_names)}
            self._idx2lab = {k: v for k, v in enumerate(self._class_names)}

    def index2label(self, idx:int):
        if self._idx2lab  is None or len(self._idx2lab .items())==0:
            raise ValueError('You dont have proper mapping class names')
        elif  idx not in self._idx2lab :
            raise ValueError('Index :{0} is not exist in class names'.format(idx))
        else:
            return self._idx2lab[idx]

    def label2index(self ,label):
        if self._lab2idx  is None or len(self._lab2idx .items())==0:
            raise ValueError('You dont have proper mapping class names')
        elif  label not in self._lab2idx :
            raise ValueError('label :{0} is not exist in class names'.format(label))
        else:
            return self._lab2idx[label]

    def infer_single_image(self,img,topk=1):
        if self.model.built:
            self.model.to(self.device)
            self.model.eval()
            img=image2array(img)
            if img.shape[-1]==4:
                img=img[:,:,:3]

            for func in self.preprocess_flow:
                if inspect.isfunction(func):
                    img=func(img)

            result=self.model(to_tensor(np.expand_dims(img,0)))
            result = torch.softmax(result,dim=1)
            result=to_numpy(result)[0]

            argresult = np.argsort(result)
            argresult1 =argresult[::-1]
            answer=OrderedDict()
            idxs = list(np.argsort(result)[::-1][:topk])
            for idx in idxs:
                prob=result[idx]
                answer[self.index2label(idx)]=(idx,prob)
            #idx=int(np.argmax(result,-1)[0])


            return answer
        else:
            raise  ValueError('the model is not built yet.')




class ImageDetectionModel(Model):
    def __init__(self, inputs=None, output=None, input_shape=None):
        super(ImageDetectionModel, self).__init__(inputs, output, input_shape)

class ImageSegmentationModel(Model):
    def __init__(self, inputs=None, output=None, input_shape=None):
        super(ImageSegmentationModel, self).__init__(inputs, output, input_shape)



class LanguageModel(Model):
    def __init__(self, inputs=None, output=None, input_shape=None):
        super(LanguageModel, self).__init__(inputs, output, input_shape)




TrainingItem=Model





