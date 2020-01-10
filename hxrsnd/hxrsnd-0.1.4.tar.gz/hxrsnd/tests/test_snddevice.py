#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import logging
from collections import OrderedDict

import numpy as np
from ophyd.device import Device

from .conftest import get_classes_in_module, fake_device
from hxrsnd import snddevice

logger = logging.getLogger(__name__)

@pytest.mark.parametrize("dev", get_classes_in_module(snddevice, Device))
def test_sndevice_devices_instantiate_and_run_ophyd_functions(dev):
    device = fake_device(dev)
    assert(isinstance(device.read(), OrderedDict))
    assert(isinstance(device.read_configuration(), OrderedDict))
