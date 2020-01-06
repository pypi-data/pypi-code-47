# -*- coding: UTF-8 -*-
# Copyright 2013-2018 Rumma & Ko Ltd

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from django.conf import settings

from lino.api import dd, rt

from lino_xl.lib.notes.models import *
from lino.modlib.office.roles import OfficeUser, OfficeOperator
from lino_xl.lib.contacts.roles import ContactsUser

class Note(Note):
    class Meta:
        verbose_name = _("Note")
        verbose_name_plural = _("Notes")

    def after_ui_save(self, ar, cw):
        super(Note, self).after_ui_save(ar, cw)
        if self.project_id:
            self.project.touch()
            self.project.save()


dd.update_field(Note, 'body', textfield_format='plain', verbose_name=_("Detailed description"))
dd.update_field(Note, 'subject', verbose_name=_("Short description"))
dd.update_field(Note, 'type', verbose_name=_("Note type"))

class NoteDetail(NoteDetail):

    main = """
    date:10 time type:25 user:10
    project  subject 
    # company contact_person #contact_role
    # language:8 build_time id
    body
    """


Notes.column_names = "date time type project subject user *"
MyNotes.column_names = "date time type project subject *"
Notes.insert_layout = """
project
type:25
subject
"""


class NotesByProject(NotesByProject):
    # required_roles = dd.login_required(OfficeUser)
    # required_roles = dd.login_required()
    column_names = ("date:8 time:5 event_type:10 type:10 "
                    "subject:40 user:10 *")
    auto_fit_column_widths = True


class NotesByCompany(NotesByCompany):
    # required_roles = dd.login_required(NotesUser)
    # required_roles = dd.login_required()
    column_names = "date time project event_type type subject user *"


