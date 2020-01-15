# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import sandia.conferencetheme


class SandiaConferencethemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=sandia.conferencetheme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sandia.conferencetheme:default')


SANDIA_CONFERENCETHEME_FIXTURE = SandiaConferencethemeLayer()


SANDIA_CONFERENCETHEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SANDIA_CONFERENCETHEME_FIXTURE,),
    name='SandiaConferencethemeLayer:IntegrationTesting'
)


SANDIA_CONFERENCETHEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SANDIA_CONFERENCETHEME_FIXTURE,),
    name='SandiaConferencethemeLayer:FunctionalTesting'
)


SANDIA_CONFERENCETHEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SANDIA_CONFERENCETHEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='SandiaConferencethemeLayer:AcceptanceTesting'
)
