import sys
import time
import os
import inspect
import numpy as np
import cntk as C
from cntk import cntk_py
from cntk.internal.sanitize import *
from collections import OrderedDict
from functools import partial
from ..backend.common import addindent, format_time, get_terminal_size, snake2camel, camel2snake, floatx, \
    unpack_singleton
from ..backend.cntk_backend import to_tensor, to_numpy, Input
from .cntk_optimizers import get_optimizer
from .cntk_losses import get_loss
from .cntk_metrics import get_metric
from .cntk_regularizers import get_reg
from .cntk_constraints import get_constraint
from .trainers import ModelBase, OptimizerMixin, progress_bar

__all__ = ['Model']


def _to_tuple(x):
    if isinstance(x, tuple):
        return x
    elif isinstance(x, list):
        return tuple(x)
    else:
        return x,


class Model(ModelBase):
    def __init__(self, inputs=None, output=None, input_shape=None):
        super(Model, self).__init__(inputs, output, input_shape)

    def _initial_graph(self, inputs=None, output=None, input_shape=None):
        temp_outputs = []
        args_list = []

        self.inputs = OrderedDict()
        self.targets = OrderedDict()
        if output is None:
            raise ValueError('There is at least on eoutput')
        if isinstance(output, (C.Variable, C.Function)):
            output = output if isinstance(output, C.Function) else output.owner

        elif inspect.isfunction(output):
            pass
        elif isinstance(output, (list, tuple)):
            raise ValueError(
                'You only can assign one Function as output  if you want optimize several Functions, use combine([functions] in advance.')

        if inputs is None:
            if input_shape is None:
                raise ValueError('You should assign inputs or input shape')
            else:
                input_shape = _to_tuple(input_shape)
                input_name = 'input_{0}'.format(len(self.inputs))
                input_var = Input(input_shape, dtype=sanitize_precision(floatx), name=input_name)
                self.inputs[input_name] = input_var

                if len(output.arguments) == 1:
                    self.model = output(input_var)
                    for outout in self.model.outputs:
                        self.targets['target_{0}'.format(len(self.targets))] = Input(outout.shape,
                                                                                     dtype=sanitize_precision(floatx()),
                                                                                     name='target_{0}'.format(
                                                                                         len(self.targets)))
        else:
            if isinstance(inputs, C.Variable):
                inputs = inputs,
            elif isinstance(inputs, C.Function):
                inputs = inputs.owner,

            if isinstance(inputs, (tuple, list)):
                for inp in inputs:
                    if isinstance(inp, C.Variable):
                        self.inputs[inp.uid] = inp

                temp_args = []
                for j in range(len(output.arguments)):
                    if output.arguments[j].uid in self.inputs:
                        temp_args.append(self.inputs[output.arguments[0].uid])
                    elif output.arguments[j].name=='keep' and len(self.inputs)>j:
                        temp_args.append(list(self.inputs.values())[j])
                    elif output.arguments[j].shape == list(self.inputs.values())[0].shape or output.arguments[ j].shape == -2:
                        temp_args.append(list(self.inputs.values())[0])
                    else:
                        raise ValueError( 'Function outputs {0} cannot mapping its argments {1}'.format(j, self.model.arguments))
                if len(temp_args) == len(output.arguments):
                    self.model = output(*temp_args)
                    for outout in self.model.outputs:
                        self.targets['target_{0}'.format(len(self.targets))] = Input(outout.shape,    dtype=sanitize_precision(floatx()),  name='target_{0}'.format(  len(self.targets)))
                else:
                    raise ValueError('arguments mapping is not correct')
        self.training_context['current_model'] = self.model
        self.device = "cuda" if 'GPU' in str(C.all_devices()[0]) else "cpu"

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
            self.optimizer = optimizer_class(self.model.parameters, **kwargs)
        else:
            self.optimizer = optimizer(self.model.parameters, **kwargs)
        self.base_lr = kwargs.get('lr', 1e-3)
        self.training_context['optimizer'] = self.optimizer
        self.training_context['base_lr'] = self.base_lr
        self.training_context['current_lr'] = self.base_lr
        return self

    def with_loss(self, loss, loss_weight=1,output_idx=0,name='', **kwargs):
        if isinstance(loss, str):
            loss = get_loss(loss)
        input_var=self.model.output if output_idx==0 and output_idx>=len(self.model.outputs) else self.model.outputs[output_idx]
        target_var=list(self.targets.values())[0] if output_idx==0 and output_idx>=len(self.targets) else list(self.targets.values())[output_idx]
        if not isinstance(loss, C.Function):
            alias = loss.__name__
            if alias.lower()==alias:
                if len(kwargs)==0:
                    loss = (input_var, target_var,kwargs)
                else:
                    loss=(input_var, target_var)
            if len(kwargs)==0:
                loss = loss()(input_var, target_var)
            else:
                loss = loss(**kwargs)(input_var, target_var)
            loss.name=name if name!='' else alias
        else:
            assert len(loss.arguments) == 2
            temp_args=[]
            for arg in loss.arguments:

                if arg.uid in self.inputs :
                    temp_args.append(self.inputs[arg.uid])
                elif arg.uid not in self.inputs and arg.name!='keep':
                    temp_args.append(arg)
                else:
                    temp_args.append(self.model.output)
            loss=loss(*temp_args)
            loss.name=name if name != '' else loss.name
        self._losses[loss.name if len(loss.name)>0 else loss.uid] = loss
        return self

    def with_metric(self, metric, output_idx=0,name='',**kwargs):
        if isinstance(metric, str):
            metric = get_metric(metric)
        input_var = self.model.output if output_idx == 0 and output_idx >= len(self.model.outputs) else \
        self.model.outputs[output_idx]
        target_var = list(self.targets.values())[0] if output_idx == 0 and output_idx >= len(self.targets) else \
        list(self.targets.values())[output_idx]
        if not isinstance(metric, C.Function):
            alias = metric.__name__
            if alias.lower() == alias:
                if len(kwargs) == 0:
                    metric = (input_var, target_var, kwargs)
                else:
                    metric = (input_var, target_var)
            if len(kwargs) == 0:
                metric = metric()(input_var, target_var)
            else:
                metric = metric(**kwargs)(input_var, target_var)
            metric.name = name if name != '' else alias
        else:
            assert len(metric.arguments) == 2
            temp_args = []
            for arg in metric.arguments:

                if arg.uid in self.inputs:
                    temp_args.append(self.inputs[arg.uid])
                elif arg.uid not in self.inputs and arg.name != 'keep':
                    temp_args.append(arg)
                else:
                    temp_args.append(self.model.output)
            metric = metric(*temp_args)
            metric.name = name if name != '' else metric.name
        self._metrics[metric.name if len(metric.name) > 0 else metric.uid] = metric
        return self

    def with_regularizer(self, reg, **kwargs):
        if reg is None:
            return self
        reg_fn = None
        args = []
        if isinstance(reg, str):
            reg_fn = get_reg(reg)

        if callable(reg) and not isinstance(reg, C.Function):
            reg_fn = reg
            args = reg_fn.__code__.co_varnames
            reg_fn = C.Function._to_Function(reg_fn, make_block=False, op_name=snake2camel(reg_fn.__name__),
                                             name=reg_fn.__name__)
        reg_fn.argument_map(**kwargs)
        args = list(reg_fn.arguments.keys())
        if 'reg_weight' in args:
            if 'model' in args:
                self._model_regs[reg_fn.__name__] = reg_fn
            elif 'output' in args:
                self._output_regs[reg_fn.__name__] = reg_fn
        return self

    def with_constraint(self, constraint, **kwargs):
        if constraint is None or constraint.__name__[-4:] != 'norm':
            return self
        constraint_fn = None
        if isinstance(constraint, str):
            constraint_fn = get_constraint(constraint)
        if callable(constraint_fn) and not isinstance(constraint_fn, C.Function):
            constraint_fn = C.Function._to_Function(constraint_fn, make_block=False,
                                                    op_name=snake2camel(constraint_fn.__name__),
                                                    name=snake2camel(constraint_fn.__name__))
        constraint_fn.argument_map(**kwargs)
        self._constraints[constraint_fn.__name__] = constraint_fn
        return self

    def with_learning_rate_schedule(self, lr_schedule, warmup=0, **kwargs):
        # self.lr_schedule=partial(lr_schedule,**kwargs)
        self.warmup = warmup
        if self.warmup > 0:
            self.optimizer.adjust_learning_rate(1e-6)
            self.training_context['current_lr'] = 1e-6
        return self

    def adjust_learning_rate(self, lr):
        self.optimizer.adjust_learning_rate(lr)
        self.training_context['current_lr'] = lr

    def do_on_training_start(self):
        loss_args = []
        [loss_args.extend(list(loss.arguments)) for loss in self._losses.values()]
        loss_args = list(set(loss_args))

        metric_args = []
        [metric_args.extend(list(metric.arguments)) for metric in self._metrics.values()]
        metric_args = list(set(metric_args))
        if self.model:
            for arg in self.model.arguments:
                if arg not in loss_args and arg not in metric_args:
                    raise ValueError("model function must share its arguments with the loss function")
            for arg in loss_args:
                if arg not in self.model.arguments:
                    raise ValueError("loss function arguments is not engugh")
            for arg in metric_args:
                if arg not in self.model.arguments:
                    raise ValueError("metics function arguments is not engugh")
            if self.device is None or isinstance(self.device, str):
                self.device = C.use_default_device()

    def do_on_training_end(self):
        pass

    def do_on_epoch_start(self):
        if self.training_context['current_epoch'] < self.warmup:
            lr = 1e-5 * (self.training_context['current_epoch'] + 1)
            self.optimizer.param_groups[0]['lr'] = lr
            self.training_context['current_lr'] = lr
        elif self.training_context['current_epoch'] == self.warmup:
            self.optimizer.param_groups[0]['lr'] = self.base_lr
            self.training_context['current_lr'] = self.base_lr

    def do_on_epoch_end(self):
        if self.training_context['current_epoch'] >= self.warmup:
            if self.lr_scheduler is not None:
                self.lr_scheduler.step(np.array(self.training_context['metrics'][list(self._metrics.keys())[0]]).mean())
            if self.optimizer.lr < 1e-8:
                self.optimizer.adjust_learning_rate(0.05 * self.base_lr)

    def do_on_data_received(self, input=None, target=None):
        if input is not None:
            input = to_numpy(input)
        if target is not None:
            target = to_numpy(target)
        return input, target

    def do_preparation_for_loss(self):
        pass

    def do_post_loss_calculation(self):
        pass

    def do_gradient_update(self):
        self.optimizer.updates(self.training_context['current_loss'], self.training_context)

    def do_post_gradient_update(self):
        pass

    def save_model(self, file_path=None):
        for callback in self.training_context['callbacks']:
            callback.on_start_save_model(self.training_context)

        if file_path is not None:
            self.model.save(file_path)

        elif 'save_path' in self.training_context and self.training_context['save_path'] is not None:
            self.model.save(self.training_context['save_path'])
        else:
            save_full_path = os.path.join('Models/', 'model_{0}_epoch{1}.model'.format(self.model.__name__,
                                                                                     self.training_context[
                                                                                         'current_epoch']))
            self.model.save(save_full_path)

        self.model.train()

    def save_onnx(self, file_path):
        for callback in self.training_context['callbacks']:
            callback.on_start_save_model(self.training_context)

        if file_path is not None:
            self.model.save(file_path, C.ModelFormat.ONNX)

        elif 'save_path' in self.training_context and self.training_context['save_path'] is not None:
            self.model.save(self.training_context['save_path'], C.ModelFormat.ONNX)
        else:
            save_full_path = os.path.join('Models/', 'model_{0}_epoch{1}.onnx'.format(self.model.__name__,
                                                                                      self.training_context[
                                                                                          'current_epoch']))
            self.model.save(save_full_path, C.ModelFormat.ONNX)

        self.model.train()

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
        keys = module_attrs + optimizer_attrs + attrs + losses + metrics + output_regs + model_regs + constraints
        # Eliminate attrs that are not legal Python variable names
        keys = [key for key in keys if not key[0].isdigit()]

        return sorted(keys)
