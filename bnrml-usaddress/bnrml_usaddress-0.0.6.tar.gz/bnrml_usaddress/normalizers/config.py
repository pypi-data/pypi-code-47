#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by pat on 9/2/19
"""
.. currentmodule:: bnrml_usaddress.normalizers
.. moduleauthor:: Pat Daburu <pat@daburu.net>

Say something descriptive about the 'normalizers' module.
"""
from functools import lru_cache
import os
from pathlib import Path
from bnrml import Normalizer
from bnrml.mappings import SUPPORTED_MAPPING_FILE_EXTS

#: the paths in which `Normals` definitions may be found for usaddress
#: components
NORMALS_DIR_PATHS = [
    Path(path).expanduser().resolve() for path in (
        os.environ.get('NORMALS_DIR_PATH'),
        Path.cwd() / 'normals',
        '~/.bnrml-usaddress/normals',
        '/etc/bnrml-usaddress/normals',
        Path(__file__).parent / 'normals'
    ) if path is not None
]


@lru_cache()
def by_component(component: str) -> Normalizer or None:
    """
    Retrieve the configured `Normalizer` for an address component.

    :param component: the component
    :return: the normalizer
    """
    # Lowercase the component name (for simpler matching).
    _component = component.lower()
    # Look at the paths that may contain normals in the order they're defined.
    for path in NORMALS_DIR_PATHS:
        # Establish the full path (by using the directory and the component
        # name).
        component_base_path = path / _component
        # The file will have a suffix, so we'll check for files with the
        # component name and all the supported suffixes.
        for ext in SUPPORTED_MAPPING_FILE_EXTS:
            # What's the path if we consider this suffix?
            component_path = component_base_path.with_suffix(ext)
            # If there a file at this path?
            if component_path.is_file():
                # Great!  Assume it's a normalizer configuration and load it.
                return Normalizer.loadf(path=component_path)
    # If we haven't returned before now, there is nothing defined for this
    # component.
    return None
