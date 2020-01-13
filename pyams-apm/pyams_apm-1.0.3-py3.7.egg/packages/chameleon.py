#
# Copyright (c) 2008-2018 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_apm.packages.chameleon module

This module adds APM instrumentation for Chameleon package
"""

from elasticapm.instrumentation.packages.base import AbstractInstrumentedModule
from elasticapm.traces import capture_span


__docformat__ = 'restructuredtext'


class ChameleonCookingInstrumentation(AbstractInstrumentedModule):
    """Chameleon cooking instrumentation"""

    name = "chameleon_cooking"

    instrument_list = [("chameleon.template", "BaseTemplate.cook")]

    def call(self, module, method, wrapped, instance, args, kwargs):
        # pylint: disable=too-many-arguments
        """Wrapped method call"""
        with capture_span('COOK',
                          span_type='template',
                          span_subtype='chameleon',
                          span_action='cook',
                          extra={'filename': instance.filename},
                          leaf=False):
            return wrapped(*args, **kwargs)


class ChameleonRenderingInstrumentation(AbstractInstrumentedModule):
    """Chameleon rendering instrumentation"""

    name = "chameleon_rendering"

    instrument_list = [("chameleon.template", "BaseTemplate.render")]

    def call(self, module, method, wrapped, instance, args, kwargs):
        # pylint: disable=too-many-arguments
        """Wrapped method call"""
        with capture_span('RENDER',
                          span_type='template',
                          span_subtype='chameleon',
                          span_action='render',
                          extra={'filename': instance.filename},
                          leaf=False):
            return wrapped(*args, **kwargs)
