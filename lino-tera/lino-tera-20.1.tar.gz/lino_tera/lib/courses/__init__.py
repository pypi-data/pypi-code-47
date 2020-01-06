# Copyright 2013-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""Extends :mod:`lino_xl.lib.courses` for :ref:`tera`.

.. autosummary::
   :toctree:

    fixtures.demo

"""


from lino_xl.lib.courses import Plugin
from lino.api import _


class Plugin(Plugin):

    verbose_name = _("Therapies")

    teacher_model = 'users.User'
    """The name of the model to be used for "teachers" (i.e. the person
    who is responsible for a course).

    """
    teacher_label = _("Therapist")
    
    # pupil_model = 'tera.Client'
    pupil_model = 'contacts.Person'
    """
    The model to be used for "pupils" (i.e. the persons who participate
    in a course).
    """
    # pupil_name_fields = "pupil__client__name"
    extends_models = ['Enrolment', 'Course', 'Line']
    
    # remove dependencies so that courses can come as the first item
    # in main menu:
    needs_plugins = []

    def setup_main_menu(self, site, user_type, m):
        sm = m.add_menu(self.app_label, self.verbose_name)
        sm.add_action('courses.MyCoursesGiven')
        # sm.add_action('courses.Pupils')
        # sm.add_action('courses.Teachers')
        sm.add_separator()
        for ca in site.models.courses.CourseAreas.objects():
            sm.add_action(ca.courses_table)
        # sm.add_action('courses.Courses')
        # sm.add_separator()
        # sm.add_action('courses.DraftCourses')
        # sm.add_action('courses.InactiveCourses')
        # sm.add_action('courses.ActiveCourses')
        # sm.add_action('courses.ClosedCourses')
        sm.add_separator()
        # sm.add_action('courses.PendingRequestedEnrolments')
        # sm.add_action('courses.PendingConfirmedEnrolments')
        sm.add_action('tera.MyClients')

        # o = site.plugins.office
        # sm = m.add_menu(o.app_label, o.verbose_name)
        # sm.add_action('courses.MyCourses')

    def setup_config_menu(self, site, user_type, m):
        m1 = m.add_menu(self.app_label, self.verbose_name)
        # m.add_action('courses.CourseTypes')
        # m.add_separator()
        m1.add_action('courses.Lines')
        m1.add_action('courses.Topics')

        # m.add_action('courses.TeacherTypes')
        # m.add_action('courses.PupilTypes')
        # m.add_action('courses.Slots')

    def setup_reports_menu(self, site, user_type, m):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action('courses.StatusReport')

    def get_dashboard_items(self, user):
        # we don't want to see any therapies on the dashboard
        return []
