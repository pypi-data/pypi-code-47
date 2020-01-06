# -*- coding: UTF-8 -*-
# Copyright 2013-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from __future__ import unicode_literals

from atelier.utils import last_day_of_month
from lino.api import _
#from lino_xl.lib.invoicing.mixins import InvoiceGenerator
from lino_xl.lib.cal.models import *
#from lino_xl.lib.cal.choicelists import EntryStates, GuestStates
#from lino_xl.lib.courses.choicelists import CourseStates
from lino_tera.lib.courses.choicelists import InvoicingPolicies
from lino_xl.lib.ledger.utils import ZERO
from lino.mixins import Referrable


# class PaymentModes(dd.ChoiceList):
#     verbose_name = _("Payment mode")
#     verbose_name_plural = _("Payment modes")

# add = PaymentModes.add_item
# add('10', _("Cash"), "default")
# add('20', _("Card"))



# class Event(Event, InvoiceGenerator):
class Event(Event):

    # invoiceable_date_field = 'start_date'

    class Meta(Event.Meta):
        abstract = dd.is_abstract_model(__name__, 'Event')
        
    amount = dd.PriceField(_("Amount"), blank=True, null=True)
    # payment_mode = PaymentModes.field(blank=True)
    
    # def get_invoiceable_partner(self):
    #     course = self.project
    #     p = course.partner
    #     if hasattr(p, 'salesrule'):
    #         return p.salesrule.invoice_recipient or p
    #     return p

    # @classmethod
    # def get_generators_for_plan(cls, plan, partner=None):
    #     qs = cls.objects.filter(**{
    #         cls.invoiceable_date_field + '__lte':
    #         plan.max_date or plan.today})
    #     invoiceable_states = (EntryStates.took_place, EntryStates.missed)
    #     qs = qs.filter(project__isnull=False)
    #     qs = qs.filter(state__in=invoiceable_states)
    #     qs = qs.filter(event_type__force_guest_states=True)
    #     if plan.course is not None:
    #         qs = qs.filter(project__id=plan.course.id)
    #     else:
    #         pass
    #         # qs = qs.filter(event__project__state=CourseStates.active)
    #     if partner is None:
    #         partner = plan.partner
    #     if partner is not None:
    #         q1 = models.Q(
    #             project__partner__salesrule__invoice_recipient__isnull=True, project__partner=partner)
    #         q2 = models.Q(project__partner__salesrule__invoice_recipient=partner)
    #         qs = qs.filter(models.Q(q1 | q2))
                
    #     # dd.logger.info("20180923 %s (%d rows)", qs.query, qs.count())
    #     for obj in qs.order_by(cls.invoiceable_date_field, 'id'):
    #         # dd.logger.info('20160223 %s', obj)
    #         yield obj
            
    # def get_invoiceable_product(self, plan):
    #     course = self.project
    #     if course is None:
    #         return
    #     fee = course.fee
    #     if fee is None and course.line_id is not None:
    #         fee = course.line.fee
    #     return fee
    
    # def get_invoiceable_amount(self):
    #     fee = self.get_invoiceable_product(None)
    #     # course = self.event.project
    #     # fee = course.fee
    #     # if fee is None and course.line_id is not None:
    #     #     fee = course.line.fee
    #     return getattr(fee, 'sales_price', ZERO)
    #     # return self.amount

    # @dd.virtualfield(dd.PriceField(_("Amount")))
    # def amount(self, ar=None):
    #     return self.get_invoiceable_amount()

    def compute_amount(self):
        # for a group therapy the amount of the event is disabled and
        # automatically computed each time a guest's amount is
        # modified.
        course = self.project
        if course and course.line and \
           course.line.invoicing_policy != InvoicingPolicies.by_event:
            amount = ZERO
            for g in self.guest_set.all():
                amount += g.amount
            self.amount = amount
            self.full_clean()
            self.save()

    def after_ui_save(self, ar, cw):
        super(Event, self).after_ui_save(ar, cw)
        if self.project_id:
            self.project.touch()
            self.project.save()

    def disabled_fields(self, ar):
        fields = super(Event, self).disabled_fields(ar)
        if ar.get_user().cash_daybook_id is not None:
            # if ar.bound_action.action.window_type == 'i':
            #     # don't disable amount in insert window
            #     return fields
            if self.can_have_amount():
                return fields
        fields.add('amount')
        return fields

    def can_have_amount(self):
        if self.id is None:
            # when inserting, the following conditions cannot yet verified, so
            # we allow entering an amount
            return True
        course = self.project
        if course is None or course.line is None or \
           course.line.invoicing_policy != InvoicingPolicies.by_event:
            return False
        if course is not None:
            li = course.get_last_invoicing()
            if li and li.voucher.voucher_date >= self.start_date:
                return False
        return True

    def force_guest_states(self):  #TODO: is this stil used?
        if self.project and self.project.line:
            return self.project.line.course_area.force_guest_states
        return False

dd.update_field(Event, 'start_date', verbose_name=_("Date"))
dd.update_field(Event, 'start_time', verbose_name=_("Time"))
# dd.update_field(Event, 'project', blank=False)
dd.update_field(Event, 'event_type', blank=False)


Event.submit_insert.label = _("Insert [Ctrl+S]")

EventType._meta.verbose_name = _("Service type")
EventType._meta.verbose_name_plural = _("Service types")


# The default value can remain "invited" as defined in xl because we have force_guest_states
# dd.update_field(Guest, 'state', default=GuestStates.present) # fails because GuestStates is not yet populated
# dd.update_field(Guest, 'state', default=GuestStates.as_callable('present'))

# class GuestRole(Referrable, GuestRole):

#     class Meta(GuestRole.Meta):
#         abstract = dd.is_abstract_model(__name__, 'GuestRole')

# class GuestRoles(GuestRoles):
#     order_by = ['ref', 'name']
#     column_names = "ref name id *"
#     detail_layout = """
#     ref name id
#     cal.GuestsByRole #courses.EnrolmentsByGuestRole
#     """

class GuestRole(GuestRole):

    class Meta(GuestRole.Meta):
        abstract = dd.is_abstract_model(__name__, 'GuestRole')

    is_teacher = dd.BooleanField(dd.plugins.courses.teacher_label, default=False)


class Guest(Guest):

    class Meta(Guest.Meta):
        abstract = dd.is_abstract_model(__name__, 'Guest')
        
    amount = dd.PriceField(_("Amount perceived"), blank=True, null=True)
    # payment_mode = PaymentModes.field(blank=True)
    
    def disabled_fields(self, ar):
        fields = super(Guest, self).disabled_fields(ar)
        # if self.event_id:
        #     course = self.event.project
        # else:
        #     course = None
        if ar.get_user().cash_daybook_id is not None:
            if self.event_id and self.event.can_have_amount():
                return fields
        fields.add('amount')
        return fields

    def after_ui_save(self, ar, cw):
        super(Guest, self).after_ui_save(ar, cw)
        self.event.compute_amount()


class GuestDetail(dd.DetailLayout):
    window_size = (60, 'auto')
    main = """
    event partner role
    state workflow_buttons 
    remark amount #payment_mode
    """

class EventDetail(EventDetail):
    start = "start_date start_time"
    end = "end_date end_time"
    main = """
    event_type summary user
    start end #all_day assigned_to #duration #state
    #room project owner amount workflow_buttons 
    # owner created:20 modified:20
    description GuestsByEvent #outbox.MailsByController
    """

    
    
class EventInsert(EventInsert):
    main = """
    start_date start_time end_time
    user
    event_type
    project
    summary
    amount #payment_mode
    """

MyEntries.column_names = 'when_html project event_type summary  *'
MyUnconfirmedAppointments.column_names = 'when_html project summary amount workflow_buttons *'

GuestsByEvent.column_names = 'partner role workflow_buttons amount #payment_mode *'
GuestsByPartner.column_names = 'event__when_html #event__overview #event_summary ' \
                               'event__user event__event_type #event__owner #role workflow_buttons *'

GuestRoles.column_names = "ref name is_teacher *"

# class MyGuestsPayments(MyGuests):
    
#     @classmethod
#     def param_defaults(self, ar, **kw):
#         kw = Guests.param_defaults(self, ar, **kw)
#         kw.update(user=ar.get_user())
#         kw.update(show_invoiced=dd.YesNo.yes)
#         return kw

from lino_xl.lib.cal.models import EventEvents
add = EventEvents.add_item
add('30', _("Perceived"), 'perceived')


class MyCashRoll(MyEntries):

    column_names = 'detail_link project amount workflow_buttons *'
    label = _("My cash roll")
    # display_mode = "html"

    @classmethod
    def get_request_queryset(cls, ar, **kwargs):
        # logger.info("20121010 Clients.get_request_queryset %s",ar.param_values)
        qs = super(MyCashRoll, cls).get_request_queryset(ar, **kwargs)
        pv = ar.param_values

        if pv.observed_event == EventEvents.perceived:
            qs = qs.filter(amount__isnull=False)
        return qs


    @classmethod
    def param_defaults(self, ar, **kw):
        offset = -10
        kw = super(MyCashRoll, self).param_defaults(ar, **kw)
        kw.update(user=ar.get_user())
        # kw.update(show_appointments=dd.YesNo.yes)
        # kw.update(assigned_to=ar.get_user())
        # logger.info("20130807 %s %s",self,kw)
        kw.update(start_date=dd.today(offset).replace(day=1))
        kw.update(end_date=last_day_of_month(dd.today(offset)))
        kw.update(observed_event=EventEvents.perceived)
        # kw.update(end_date=settings.SITE.today(14))
        return kw

