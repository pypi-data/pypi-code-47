# -*- coding: UTF-8 -*-
# Copyright 2015-2017 Luc Saffre
# License: BSD (see file COPYING for details)

"""Defines a set of user roles and fills
:class:`lino.modlib.users.choicelists.UserTypes`.

This is used as the :attr:`user_types_module
<lino.core.site.Site.user_types_module>` for
:mod:`lino_care.projects.team`.

Note that :mod:`lino_care.projects.care` does not use this module at
all.

"""


from lino.core.roles import UserRole, SiteAdmin
from lino_xl.lib.excerpts.roles import ExcerptsUser, ExcerptsStaff
from lino_xl.lib.contacts.roles import ContactsUser, ContactsStaff
#from lino_xl.lib.courses.roles import CoursesUser
from lino.modlib.office.roles import OfficeStaff, OfficeUser
# from lino.modlib.comments.roles import CommentsReader
from lino.modlib.comments.roles import CommentsUser, CommentsStaff
#from lino_xl.lib.tickets.roles import TicketsUser, Searcher, Triager, TicketsStaff
#from lino_xl.lib.working.roles import Worker
#from lino_xl.lib.cal.roles import CalendarReader
#from lino_xl.lib.votes.roles import VotesStaff, VotesUser

from lino.modlib.users.choicelists import UserTypes
from django.utils.translation import ugettext_lazy as _


class User(OfficeUser, CommentsUser, ExcerptsUser, ContactsUser):
    pass


class Staff(User, ExcerptsStaff, CommentsStaff):
    pass


class SiteAdmin(Staff, SiteAdmin, OfficeStaff, ContactsStaff):
    """Can do everything."""


# class Anonymous(CommentsReader, CalendarReader):
class Anonymous(UserRole):
    pass

UserTypes.clear()
add = UserTypes.add_item
add('000', _("Anonymous"),        Anonymous, 'anonymous',
    readonly=True, authenticated=False)
add('100', _("User"),             User, 'user')
# add('200', _("Consultant"),       Consultant, 'consultant')
# add('300', _("Hoster"),           Consultant, 'hoster')
# add('400', _("Developer"),        Developer, 'developer')
add('490', _("Staff"), Staff, 'staff')
add('900', _("Administrator"),    SiteAdmin, 'admin')


