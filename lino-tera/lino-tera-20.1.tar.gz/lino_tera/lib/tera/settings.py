# -*- coding: UTF-8 -*-
# Copyright 2014-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""
Base Django settings for Lino Tera applications.

"""

from __future__ import print_function
from __future__ import unicode_literals

from lino.projects.std.settings import *
from lino.api.ad import _
from lino_tera import SETUP_INFO

class Site(Site):

    verbose_name = "Lino Tera"
    version = SETUP_INFO['version']
    url = "http://tera.lino-framework.org/"

    demo_fixtures = 'std minimal_ledger demo demo2'.split()
    # demo_fixtures = 'std demo minimal_ledger euvatrates demo2'.split()

    # project_model = 'tera.Client'
    project_model = 'courses.Course'
    # project_model = 'contacts.Partner'
    textfield_format = 'html'
    user_types_module = 'lino_tera.lib.tera.user_types'
    workflows_module = 'lino_tera.lib.tera.workflows'
    custom_layouts_module = 'lino_tera.lib.tera.layouts'
    obj2text_template = "**{0}**"

    default_build_method = 'appypdf'

    # experimental use of rest_framework:
    # root_urlconf = 'lino_book.projects.team.urls'

    migration_class = 'lino_tera.lib.tera.migrate.Migrator'

    auto_configure_logger_names = "atelier django lino lino_xl lino_tera"

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.gfks'
        yield 'lino_xl.lib.excerpts'  # must come before any plugin that updates
                                      # the ExcerptType for Certifiable
        yield 'lino_tera.lib.courses'
        yield 'lino_tera.lib.users'
        yield 'lino.modlib.dashboard'
        yield 'lino_xl.lib.countries'
        # yield 'lino_xl.lib.properties'
        yield 'lino_tera.lib.contacts'
        yield 'lino_tera.lib.households'
        yield 'lino_xl.lib.clients'
        yield 'lino_xl.lib.healthcare'
        # yield 'lino_xl.lib.phones'
        # yield 'lino_tera.lib.lists'
        # yield 'lino_xl.lib.beid'
        # yield 'lino_xl.lib.addresses'
        # yield 'lino_xl.lib.humanlinks',
        yield 'lino_tera.lib.products'
        yield 'lino_tera.lib.sales'
        yield 'lino_tera.lib.cal'
        yield 'lino_tera.lib.invoicing'
        # yield 'lino_xl.lib.vat'
        yield 'lino_xl.lib.sepa'
        yield 'lino_xl.lib.finan'
        yield 'lino_xl.lib.bevats'
        yield 'lino_xl.lib.ana'
        yield 'lino_xl.lib.sheets'
        # 'lino_xl.lib.projects',
        # yield 'lino_xl.lib.blogs'
        yield 'lino_xl.lib.topics'
        yield 'lino_tera.lib.notes'
        # yield 'lino_tera.lib.tickets'
        # yield 'lino_xl.lib.skills'
        # yield 'lino_xl.lib.votes'
        # yield 'lino_tera.lib.working'
        # yield 'lino_xl.lib.deploy'
        # yield 'lino_presto.lib.working'
        # yield 'lino.modlib.uploads'
        # yield 'lino_xl.lib.extensible'
        # yield 'lino_xl.lib.outbox'
        yield 'lino_xl.lib.appypod'
        # yield 'lino_xl.lib.postings'
        # yield 'lino_xl.lib.pages'

        yield 'lino.modlib.export_excel'
        yield 'lino.modlib.checkdata'
        yield 'lino.modlib.tinymce'
        # yield 'lino.modlib.wkhtmltopdf'
        yield 'lino.modlib.weasyprint'

        yield 'lino_tera.lib.tera'
        yield 'lino_tera.lib.teams'
        yield 'lino_xl.lib.lists'

    def get_plugin_configs(self):
        yield super(Site, self).get_plugin_configs()
        yield ('countries', 'country_code', 'BE')
        yield ('countries', 'hide_region', True)
        yield ('vat', 'declaration_plugin', 'lino_xl.lib.bevats')
        yield ('ledger', 'use_pcmn', True)
        yield ('ledger', 'start_year', 2015)
        yield ('topics', 'partner_model', 'courses.Course')
        yield ('clients', 'client_model', 'contacts.Partner')

    def setup_quicklinks(self, user, tb):
        super(Site, self).setup_quicklinks(user, tb)
        # tb.add_action(
        #     self.models.cal.MyEntries.insert_action,
        #     label=_("New appointment"))
        tb.add_action(
            self.models.notes.MyNotes.insert_action,
            label=_("New note"))
        tb.add_action(self.models.notes.MyNotes)

    # def setup_actions(self):
    #     from lino.core.merge import MergeAction
    #     lib = self.models
    #     for m in (lib.contacts.Company, lib.tera.Client,
    #               lib.contacts.Person,
    #               lib.households.Household,
    #               lib.countries.Place):
    #         m.define_action(merge_row=MergeAction(m))
    #     super(Site, self).setup_actions()

# the following line should not be active in a checked-in version
#~ DATABASES['default']['NAME'] = ':memory:'

USE_TZ = True
# TIME_ZONE = 'Europe/Brussels'
# TIME_ZONE = 'Europe/Tallinn'
TIME_ZONE = 'UTC'
