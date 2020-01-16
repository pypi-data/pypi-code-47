# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

import os

from spot_motion_monitor.utils import getLutFromColorMap, readYamlFile, writeYamlFile

class TestGetLutFromColorMap:

    def test_getLutFromColorMap(self):
        lut = getLutFromColorMap('viridis')
        assert lut.shape == (256, 3)
        assert lut[0].tolist() == [68, 1, 84]

class TestYamlFiles:

    def setup_class(cls):
        cls.content = {'version': '1.0.0', 'camera': {'fps': 40},
                       'data': {'buffer_size': 1024, 'accumulation_time': 25.60}}

    def test_writeYamlFile(self):
        output = 'test_write.yaml'
        writeYamlFile(output, self.content)
        assert os.path.exists(output) is True
        os.remove(output)

    def test_readYamlFile(self):
        output = 'test2_write.yaml'
        writeYamlFile(output, self.content)
        new_content = readYamlFile(output)
        assert new_content == self.content
        os.remove(output)

    def test_getNoneContentforNoneFile(self):
        new_content = readYamlFile(None)
        assert new_content is None
