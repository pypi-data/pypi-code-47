# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import rt.categorysupport


class RtCategorysupportLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=rt.categorysupport)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'rt.categorysupport:default')


RT_CATEGORYSUPPORT_FIXTURE = RtCategorysupportLayer()


RT_CATEGORYSUPPORT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(RT_CATEGORYSUPPORT_FIXTURE,),
    name='RtCategorysupportLayer:IntegrationTesting',
)


RT_CATEGORYSUPPORT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(RT_CATEGORYSUPPORT_FIXTURE,),
    name='RtCategorysupportLayer:FunctionalTesting',
)


RT_CATEGORYSUPPORT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        RT_CATEGORYSUPPORT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='RtCategorysupportLayer:AcceptanceTesting',
)
