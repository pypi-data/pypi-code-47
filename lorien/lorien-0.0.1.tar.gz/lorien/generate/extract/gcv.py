"""
The base module of workload extraction from models.
"""
import argparse
from typing import Any, Dict, List, Tuple

import yaml

from tvm import relay

from ...configs import create_config_parser, register_config_parser
from ...logger import get_logger
from ...workload import Workload
from ..generator import gen
from .extract import extract_from_model

log = get_logger('Extract-GCV')


def extract_from_gcv(configs: argparse.Namespace) -> List[Workload]:
    """Extract workloads with Gluon CV model zoo.

    Parameters
    ----------
    configs: argparse.Namespace
        The system configure of generate.extract.gcv.
    Returns
    -------
    workloads: List[Workload]
        A list of collected workloads.
    """
    import gluoncv as gcv

    # Process models.
    mod_n_params: List[Tuple[relay.Module, Dict[str, Any]]] = []
    for model_desc in configs.model:
        model = yaml.load(model_desc, Loader=yaml.Loader)
        if isinstance(model, str):  # No shape specified. Use default
            model_name = model
            shape = {'data': (1, 3, 224, 224)}
        elif (isinstance(model, dict) and len(model) == 1
              and isinstance(list(model.values())[0], dict)):
            model_name = list(model.keys())[0]
            shape = model[model_name]
        else:
            raise RuntimeError('Unrecognized model description: %s' % model)

        try:
            net = gcv.model_zoo.get_model(model_name, pretrained=True)
            mod_n_params.append(relay.frontend.from_mxnet(net, shape=shape))
        except Exception as err:  # pylint:disable=broad-except
            log.error('Failed to load the Gluon CV model: %s', str(err))
            continue

    log.info('Collecting workloads from %d Gluon CV models', len(mod_n_params))
    return extract_from_model(configs, mod_n_params)


@register_config_parser('top.generate.extract.gcv')
def define_config() -> argparse.ArgumentParser:
    """Define the command line interface for extracting Gluon CV models.

    Returns
    -------
    parser: argparse.ArgumentParser
        The defined argument parser.
    """
    parser = create_config_parser('Extract workloads from Gluon CV model zoo')
    parser.add_argument('--model',
                        action='append',
                        default=[],
                        required=True,
                        help='A Gluon CV model name with input shape in YAML format: '
                        '"<model-name>: {<input-name>: [<input-shape>]}". When shape is ignored, '
                        'the default shape (1, 3, 224, 224) will be applied')
    parser.add_argument('--target',
                        action='append',
                        default=[],
                        required=True,
                        help='A TVM target (e.g., llvm, cuda, etc). '
                        'Note that the device tag (e.g., -model=v100) is not required.')
    parser.add_argument('-o',
                        '--output',
                        default='gcv_workloads.yaml',
                        help='The output file path')
    parser.set_defaults(entry=gen(extract_from_gcv), validate_task=False)
    return parser
