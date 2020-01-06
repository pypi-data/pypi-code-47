# -*- coding: UTF-8 -*-
# Copyright 2017-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)


from __future__ import unicode_literals
from __future__ import print_function

from builtins import str
from collections import OrderedDict

from django.utils.translation import pgettext_lazy as pgettext
from django.db import models

from etgen.html import E, tostring

from lino.api import dd, rt, gettext, _
from lino.utils import join_elems
from lino.utils.mti import get_child
from lino.mixins import Referrable, Modified

from lino_xl.lib.invoicing.mixins import InvoiceGenerator
from lino_xl.lib.ledger.utils import DEBIT
from lino_xl.lib.cal.workflows import TaskStates
from lino_xl.lib.healthcare.mixins import HealthcareSubject
from lino_xl.lib.topics.models import AddInterestField
from lino_xl.lib.products.choicelists import ProductTypes

from .choicelists import EndingReasons, TranslatorTypes
from .choicelists import PartnerTariffs, TherapyDomains
from .choicelists import InvoicingPolicies, PriceFactors
from .choicelists import HouseholdCompositions, Residences, IncomeCategories

from lino_xl.lib.courses.models import *
# from .choicelists import *

from lino_xl.lib.cal.utils import day_and_month

# from lino.utils.media import TmpMediaFile

from lino.modlib.printing.utils import CustomBuildMethod

contacts = dd.resolve_app('contacts')


class Line(Line):

    class Meta(Line.Meta):
        app_label = 'courses'
        abstract = dd.is_abstract_model(__name__, 'Line')
        verbose_name = _("Dossier type")
        verbose_name_plural = _('Dossier types')

    ref_max_length = 4

    # course_type = dd.ForeignKey(
    #     'courses.CourseType', blank=True, null=True)
    invoicing_policy = InvoicingPolicies.field(default='by_event')

class TeraInvoiceable(InvoiceGenerator): 
    
    class Meta(object):
        abstract = True
        
    # tariff = dd.ForeignKey('invoicing.Tariff', blank=True, null=True)
    # product = dd.ForeignKey('products.Product',
    #                         blank=True, null=True, verbose_name=_("Participation fee"))

    # def get_invoiceable_event_date(self, ie):
    #     course = self.get_invoiceable_course()
    #     if course.line.invoicing_policy == InvoicingPolicies.by_event:
    #         return ie.start_date
    #     else:
    #         return ie.event.start_date

    # @dd.virtualfield(dd.ForeignKey('products.Product', verbose_name=_("Invoiceable fee")))
    @dd.displayfield(_("Invoiceable fee"))
    def invoiceable_fee(self, ar):
        partner = self.get_invoiceable_partner()
        if partner is None:
            return None
        event_type = self.update_cal_event_type()
        fee = rt.models.products.Product.get_rule_fee(partner, event_type)
        elems = []
        if fee is None:
            elems.append(gettext("No fee"))
        else:
            elems.append(fee.obj2href(ar))
        elems.append(" ")
        elems.append(gettext("for"))
        elems.append(" ")
        elems.append(partner.obj2href(ar))
        return E.span(*elems)

    def get_invoiceable_product(self, max_date=None):
        partner = self.get_invoiceable_partner()
        if partner is None:
            return None
        event_type = self.update_cal_event_type()
        return rt.models.products.Product.get_rule_fee(partner, event_type)

    def get_invoiceable_start_date(self, max_date):
        # invoicing period is always one month
        return max_date.replace(day=1)
        
    # def get_invoiceable_product(self, max_date=None):
    #     return self.product

    # def get_invoiceable_event_class(self):
    #     course = self.get_invoiceable_course()
    #     if course.line.invoicing_policy == InvoicingPolicies.by_event:
    #         return rt.models.cal.Event
    #     return rt.models.cal.Guest
        
            
    # def get_invoiceable_tariff(self, product=None):
    #     # course = self.get_invoiceable_course()
    #     # return rt.models.invoicing.Tariff.objects.first()
    #     return self.tariff

    def get_invoiceable_event_formatter(self):
        course = self.get_invoiceable_course()
        if course.line.invoicing_policy == InvoicingPolicies.by_event:
            ev2entry = lambda ie: ie
        else:
            ev2entry = lambda ie: ie.event

        def fmt(ie, ar=None):
            event = ev2entry(ie)
            txt = dd.fds(event.start_date)
            # txt = _("{} with {} on {}").format(
            #     event.event_type, event.user, dd.fds(event.start_date))
            if ar is None:
                return txt
            return ar.obj2html(event, txt)
        return fmt
    
    def get_cash_daybook(self, ie):
        course = self.get_invoiceable_course()
        if course.line.invoicing_policy == InvoicingPolicies.by_event:
            u = ie.user
        else:
            u = ie.event.user
        return u.cash_daybook
    
    def get_invoiceable_events(self, start_date, max_date):
        course = self.get_invoiceable_course()
        if course is None:
            return []
        elif course.line.invoicing_policy == InvoicingPolicies.by_event:
            # flt = dict(
            #     state=rt.models.cal.EntryStates.took_place)
            invoiceable_states = (rt.models.cal.EntryStates.took_place,
                                  rt.models.cal.EntryStates.missed)
            flt = dict(state__in=invoiceable_states)

            if start_date:
                flt.update(start_date__gte=start_date)
            if max_date:
                flt.update(start_date__lte=max_date)
            qs = course.events_by_course(**flt).order_by("start_date")
        else:
            flt = dict()
            ct = rt.models.contenttypes.ContentType.objects.get_for_model(
                course.__class__)
            flt.update(
                event__owner_type=ct, event__owner_id=course.id)

            invoiceable_states = (rt.models.cal.GuestStates.present,
                                  rt.models.cal.GuestStates.absent)
            flt.update(state__in=invoiceable_states)

            if start_date:
                flt.update(event__start_date__gte=start_date)
            if max_date:
                flt.update(event__start_date__lte=max_date)
            
            qs = rt.models.cal.Guest(*flt).order_by(
                "event__start_date")
        # dd.logger.info(
        #     "20181116 get_invoiceable_events() for %s (%s) "
        #     "returns %d rows", course, qs.query, qs.count())
        return qs


    def get_invoice_items(self, info, invoice, ar):
        # dd.logger.info("20181116a %s", self)
        if info.used_events is None:
            dd.logger.debug("20181126 no used_events for %s", self)
            return
        Product = rt.models.products.Product
        course = self.get_invoiceable_course()
        collector = OrderedDict()
        for ev in info.used_events:
            # dd.logger.info("20181116b %s", ev)
            if course.line.invoicing_policy == InvoicingPolicies.by_event:
                entry = ev
            else:
                entry = ev.event
            product = Product.get_rule_fee(self.get_invoiceable_partner(), entry.event_type)
            if product is None:
                raise Exception("20181128 no price rule for {}".format(self))
            else:
                events = collector.setdefault(product, [])
                events.append(ev)

        fmt = self.get_invoiceable_event_formatter()

        for product, events in collector.items():
            tariff = self.get_invoiceable_tariff(product)
            desc = _("{product} on {dates}").format(
                product=product,
                dates=', '.join([fmt(ev, None) for ev in events]))
            title = _("{} appointments").format(len(events))
            kwargs = dict(
                invoiceable=self,
                product=product,
                description=desc,
                title=title)
            if tariff and tariff.max_asset:
                # qty=self.get_invoiceable_qty())
                kwargs.update(qty=min(len(events), tariff.max_asset))
            else:
                kwargs.update(qty=len(events))
            # print(20181117, kwargs)
            yield invoice.add_voucher_item(**kwargs)
            # yield model(**kwargs)

        for ev in info.used_events:
            if ev.amount:
                pp = self.get_cash_daybook(ev)
                if not pp:
                    raise Exception(_("No cash daybook defined"))
                kwargs = dict(
                    invoiceable=self, product=pp)
                    # total_incl=-ev.amount)
                # kwargs.update(title=gettext("Prepayment"))
                i = invoice.add_voucher_item(**kwargs)
                # i = model(**kwargs)
                i.set_amount(ar, -ev.amount)
                yield i
                
    def get_invoiceable_amount(self, ie):
        prod = self.get_invoiceable_product()
        return prod.sales_price or 5
        # return ie.amount
    



class Course(Referrable, Course, TeraInvoiceable, HealthcareSubject, Modified):
    """
    Extends the standard model by adding a field :attr:`fee`.

    Also adds a :attr:`ref` field and defines a custom :meth:`__str__`
    method.

    The custom :meth:`__str__` method defines how to textually
    represent a course e.g. in the dropdown list of a combobox or in
    reports. Rules:

    - If :attr:`ref` is given, it is shown, but see also the two
      following cases.

    - If :attr:`name` is given, it is shown (possibly behind the
      :attr:`ref`).

    - If a :attr:`line` (series) is given, it is shown (possibly
      behind the :attr:`ref`).

    - If neither :attr:`ref` nor :attr:`name` nor :attr:`line` are
      given, show a simple "Course #".


    .. attribute:: partner
    
        When this is empty, the course is considered a group therapy
        and invoicing is done per enrolment.  Invoice recipient is
        the pupil of every enrolment.

        Otherwise it is considered an individual or life group therapy
        and invoicing is done per course.

    .. attribute:: ref
    
        An identifying public course number to be used by both
        external and internal partners for easily referring to a given
        course.

    .. attribute:: name

        A short designation for this course. An extension of the
        :attr:`ref`.

    .. attribute:: line

        Pointer to the course series.


    .. attribute:: fee

        The default attendance fee to apply for new enrolments.

    .. attribute:: payment_term

        The payment term to use when writing an invoice. If this is
        empty, Lino will use the partner's default payment term.

    .. attribute:: paper_type

        The paper_type to use when writing an invoice. If this is
        empty, Lino will use the site's default paper type.
    """
    class Meta(Course.Meta):
        app_label = 'courses'
        abstract = dd.is_abstract_model(__name__, 'Course')
        verbose_name = _("Dossier")
        verbose_name_plural = _('Dossiers')

    ref_max_length = 8
    
    # allow_cascaded_delete = "client household"
    allow_cascaded_delete = "partner"

    # fee = dd.ForeignKey('products.Product',
    #                     blank=True, null=True,
    #                     verbose_name=_("Attendance fee"),
    #                     related_name='courses_by_fee')

    payment_term = dd.ForeignKey(
        'ledger.PaymentTerm',
        related_name="%(app_label)s_%(class)s_set_by_payment_term",
        blank=True, null=True)    

    procurer = dd.ForeignKey('tera.Procurer', blank=True, null=True)
    mandatory = models.BooleanField(_("Mandatory"), default=False)
    ending_reason = EndingReasons.field(blank=True)
    partner_tariff = PartnerTariffs.field(
        default=PartnerTariffs.as_callable('plain'))
    translator_type = TranslatorTypes.field(blank=True)
    therapy_domain = TherapyDomains.field(blank=True)
    team = dd.ForeignKey('teams.Team', blank=True, null=True)
    add_interest = AddInterestField()
    
    partner = dd.ForeignKey(
        'contacts.Partner',
        verbose_name=_("Invoice recipient"),
        # related_name="%(app_label)s_%(class)s_set_by_client",
        blank=True, null=True)

    client = dd.ForeignKey(
        'tera.Client',
        verbose_name=_("Client"),
        blank=True, null=True)

    def get_client(self):
        return self.client

    # client = dd.ForeignKey(
    #     'tera.Client',
    #     related_name="%(app_label)s_%(class)s_set_by_client",
    #     blank=True, null=True)    

    # household = dd.ForeignKey(
    #     'households.Household',
    #     related_name="%(app_label)s_%(class)s_set_by_household",
    #     blank=True, null=True)    

    paper_type = dd.ForeignKey(
        'sales.PaperType',
        related_name="%(app_label)s_%(class)s_set_by_paper_type",
        blank=True, null=True)    

    quick_search_fields = "ref name partner__name"
    
    # @classmethod
    # def get_registrable_fields(cls, site):
    #     for f in super(Course, cls).get_registrable_fields(site):
    #         yield f
    #     yield 'fee'

    # @dd.chooser()
    # def fee_choices(cls, line):
    #     Product = rt.models.products.Product
    #     if not line or not line.fees_cat:
    #         return Product.objects.none()
    #     return Product.objects.filter(cat=line.fees_cat)

    def on_create(self, ar):
        self.teacher = ar.get_user()
        super(Course, self).on_create(ar)

    def full_clean(self):
        if not self.name:
            # self.name = str(self.household or self.client)
            # if self.partner.team and self.partner.team.ref:
            #     s = self.partner.team.ref + "/"
            # else:
            #     s = ''
            if self.partner:
                s = self.partner.name
            else:
                s = 'ZZZ'
            # if self.line_id and self.line.ref:
            #     s = "{} ({})".format(s, self.line.ref)
            self.name = s
        return super(Course, self).full_clean()
    
    def __str__(self):
        if self.name:
            s = self.name
        else:
            # Note that we cannot use super() with
            # python_2_unicode_compatible
            s = "{0} #{1}".format(self._meta.verbose_name, self.pk)
        if self.line_id and self.line.ref:
            more = self.line.ref
        else:
            more = ''
        # if self.ref:
        #     more += " " + self.ref
        if self.teacher_id and self.teacher.initials:
            more += " " + self.teacher.initials
        if more:    
            s = "{} ({})".format(s, more.strip())
        return s

    def update_cal_event_type(self):
        if self.teacher_id:
            return self.teacher.event_type

    def update_cal_summary(self, et, i):
        label = dd.babelattr(et, 'event_label')
        if self.ref:
            label = self.ref + ' ' + label
        if self.line and self.line.ref:
            label = self.line.ref + '.' + label
        return "%s %d" % (label, i)

    def get_overview_elems(self, ar):
        # we don't want to see the teacher (therapist)
        # here. Especially not in MyGivenCourses but probably nowhere
        # else either.  when a table of therapies is shown in
        # dashboard, then we want a way to open its detail with a
        # single click.
        
        # elems = super(Course, self).get_overview_elems(ar)
        elems = []
        elems.append(self.obj2href(ar))
        # if self.teacher_id:
        #     elems.append(" / ")
        #     # elems.append(ar.obj2html(self.teacher))
        #     elems.append(self.teacher.obj2href(ar))
        # elems.append(E.br())
        # elems.append(ar.get_data_value(self, 'eid_info'))
        notes = []
        for obj in rt.models.cal.Task.objects.filter(
                project=self, state=TaskStates.important):
            notes.append(E.b(ar.obj2html(obj, obj.summary)))
        if len(notes):
            notes = join_elems(notes, " / ")
            elems.append(E.p(*notes, **{'class':"lino-info-yellow"}))
        return elems

    def update_owned_instance(self, owned):
        owned.project = self
        super(Course, self).update_owned_instance(owned)

    @dd.displayfield(_("Patient"))
    def client(self, ar):
        if ar is None or self.partner_id is None:
            return
        obj = get_child(self.partner, rt.models.tera.Client)
        if obj is not None:
            return obj.obj2href(ar)

    @dd.displayfield(_("Household"))
    def household(self, ar):
        if ar is None or self.partner_id is None:
            return
        obj = get_child(self.partner, rt.models.households.Household)
        if obj is not None:
            return obj.obj2href(ar)

    @dd.displayfield(_("Organization"))
    def company(self, ar):
        if ar is None or self.partner_id is None:
            return
        obj = get_child(self.partner, rt.models.contacts.Company)
        if obj is not None:
            return obj.obj2href(ar)

    def get_invoiceable_partner(self):
        return self.partner
        # if hasattr(p, 'salesrule'):
        #     return p.salesrule.invoice_recipient or p
        # return p

    @dd.chooser()
    def product_choices(cls, partner):
        return rt.models.products.Product.get_product_choices(partner)

    # def get_invoiceable_product(self, max_date=None):
    #     return self.fee or self.line.fee
    
    def get_invoiceable_course(self):
        return self

    @classmethod
    def get_generators_for_plan(cls, plan, partner=None):
        # pre-select all Course objects that potentially will generate
        # an invoice.
        
        qs = cls.objects.all()
        # qs = cls.objects.filter(**{
        #     cls.invoiceable_date_field + '__lte':
        #       plan.max_date or plan.today})
        
        if plan.course is None:
            qs = qs.filter(state=CourseStates.active)
        else:
            qs = qs.filter(id=plan.course.id)
            
        # dd.logger.info("20181113 c %s", qs)
        
        if partner is None:
            partner = plan.partner
            
        if partner is None:
            # only courses with a partner (because only these get invoiced
            # per course).
            qs = qs.filter(partner__isnull=False)
        else:
            q1 = models.Q(
                partner__salesrule__invoice_recipient__isnull=True,
                partner=partner)
            q2 = models.Q(
                partner__salesrule__invoice_recipient=partner)
            qs = qs.filter(models.Q(q1 | q2))

        # dd.logger.info("20181113 %s (%d rows)", qs.query, qs.count())
        return qs.order_by('id')
    
        # for obj in qs.order_by(cls.invoiceable_date_field, 'id'):
        #     # dd.logger.info('20160223 %s', obj)
        #     yield obj

    # def setup_invoice_item(self, item):
    #     item.description = dd.plugins.jinja.render_from_request(
    #         None, 'courses/Course/item_description.html',
    #         obj=self, item=item)

        

# Course.set_widget_options('ref', preferred_with=6)
# dd.update_field(Course, 'ref', verbose_name=_("Legacy file number"))
# dd.update_field(Course, 'partner', verbose_name=_("Invoicing address"))
#  dd.update_field(Course, 'teacher', verbose_name=_("Therapist"))
dd.update_field(Course, 'user', verbose_name=_("Manager"))

# class CreateInvoiceForEnrolment(CreateInvoice):

#     def get_partners(self, ar):
#         return [o.pupil for o in ar.selected_rows]


class Enrolment(Enrolment, TeraInvoiceable):
    """Adds

    .. attribute:: pupil_info

        Show the name and address of the participant.  Overrides
        :attr:`lino_xl.lib.courses.models.Enrolment.pupil_info`
        in order to add (between parentheses after the name) some
        information needed to compute the price.

    .. attribute:: payment_info

        A virtual field showing a summary of due accounting movements
        (debts and payments).

    """

    
    class Meta(Enrolment.Meta):
        app_label = 'courses'
        abstract = dd.is_abstract_model(__name__, 'Enrolment')
        # verbose_name = _("Attendance")
        # verbose_name_plural = _("Attendances")

    guest_role = dd.ForeignKey(
        'cal.GuestRole', verbose_name=_("Role"), blank=True, null=True)
    # fee = dd.ForeignKey('products.Product',
    #                     blank=True, null=True,
    #                     # verbose_name=_("Attendance fee"),
    #                     related_name='enrolments_by_fee')

    # @dd.chooser()
    # def fee_choices(cls, course):
    #     Product = rt.models.products.Product
    #     if not course or not course.line or not course.line.fees_cat:
    #         return Product.objects.none()
    #     return Product.objects.filter(cat=course.line.fees_cat)

    def __str__(self):
        if self.course_id:
            return "{}/{}".format(self.pupil_id, self.course.ref or self.course_id)
        return "{}/{}".format(self.pupil_id, self.course_id)

    # def before_ui_save(self, ar):
    def before_ui_save(self, ar):
        if self.course_id is None:
            if self.pupil_id:
                line = rt.models.courses.Line.objects.order_by('id').first()
                kw = dict(line=line, partner=self.pupil)
                kw.update(name=u"{} {}".format(self.pupil.last_name.upper(),
                                               self.pupil.first_name))
                # kw.update(user=ar.get_user())
                # kw.update(teacher=ar.get_user())
                course = rt.models.courses.Course(**kw)
                course.on_create(ar)
                course.full_clean()
                course.save()
                self.course = course
        super(Enrolment, self).before_ui_save(ar)

    def full_clean(self, *args, **kwargs):
        if self.course_id:
            if self.course.line:
                self.course_area = self.course.line.course_area
                if self.guest_role_id is None:
                    self.guest_roles = self.course.line.guest_role
        # if self.fee_id is None:
        #     self.compute_fee()
        super(Enrolment, self).full_clean(*args, **kwargs)

    # def get_invoiceable_product(self, max_date=None):
    #     if self.course_id:
    #         return self.product or self.course.product
    #     return self.product

    # def get_invoiceable_tariff(self, product=None):
    #     # course = self.get_invoiceable_course()
    #     # return rt.models.invoicing.Tariff.objects.first()
    #     if self.course_id:
    #         return self.tariff or self.course.tariff
    #     return self.tariff

    # def pupil_changed(self, ar):
    #     self.compute_fee()
    #
    # def compute_fee(self):
    #     #todo: set fee according to tariff rules
    #     if self.course_id is not None:
    #         self.fee = self.course.fee
    #         if self.fee_id is None and self.course.line_id is not None:
    #             self.fee = self.course.line.fee

    @dd.virtualfield(dd.HtmlBox(_("Participant")))
    def pupil_info(self, ar):
        if not self.pupil_id:
            return ''
        elems = []
        txt = self.pupil.get_full_name(nominative=True)
        if ar is None:
            elems = [txt]
        else:
            elems = [ar.obj2html(self.pupil, txt)]
        info = self.pupil.get_enrolment_info()
        if info:
            # elems += [" ({})".format(self.pupil.pupil_type.ref)]
            elems += [" ({})".format(info)]
        elems += [', ']
        elems += join_elems(
            self.pupil.address_location_lines(), sep=', ')
        if self.pupil.phone:
            elems += [', ', _("Phone: {0}").format(self.pupil.phone)]
        if self.pupil.gsm:
            elems += [', ', _("GSM: {0}").format(self.pupil.gsm)]
        return E.p(*elems)

    @dd.displayfield(_("Payment info"))
    def payment_info(self, ar):
        if not self.pupil_id:
            return ''
        return rt.models.ledger.Movement.balance_info(
            DEBIT, partner=self.pupil, cleared=False)
        
    def get_guest_role(self):
        return self.guest_role or super(Enrolment, self).get_guest_role()
        
    def get_invoiceable_partner(self):
        # if hasattr(self.pupil, 'salesrule'):
        #     return self.pupil.salesrule.invoice_recipient or self.pupil
        return self.pupil

    @dd.chooser()
    def product_choices(cls, pupil):
        return rt.models.products.Product.get_product_choices(pupil)

    # def get_invoiceable_product(self, max_date=None):
    #     if self.fee:
    #         return self.fee
    #     if self.course_id:
    #         if self.course.fee:
    #             return self.course.fee
    #         if self.course.line_id:
    #             return self.course.line.fee
    
    def get_invoiceable_course(self):
        if self.course_id:
            return self.course
    
    def update_cal_event_type(self):
        if self.course_id and self.course.teacher_id:
            return self.course.teacher.event_type

    @classmethod
    def get_generators_for_plan(cls, plan, partner=None):
        
        qs = cls.objects.all()
        
        if plan.course is None:
            qs = qs.filter(course__state=CourseStates.active)
        else:
            qs = qs.filter(course__id=plan.course.id)

        # dd.logger.info("20181113 c %s", qs)
        
        # only enrolments whose course.partner is empty (because only
        # these get invoiced per enrolment).
        qs = qs.filter(course__partner__isnull=True)
        
        if partner is None:
            partner = plan.partner
        if partner:
            pupil = get_child(partner, dd.plugins.courses.pupil_model)
            if pupil:
                q1 = models.Q(
                    pupil__salesrule__invoice_recipient__isnull=True,
                    pupil=pupil)
                q2 = models.Q(pupil__salesrule__invoice_recipient=partner)
                qs = qs.filter(models.Q(q1 | q2))
            else:
                # if the partner is not a pupil, then it might still
                # be an invoice_recipient
                qs = qs.filter(
                    pupil__salesrule__invoice_recipient=partner)

        # dd.logger.info("20181113 %s (%d rows)", qs.query, qs.count())
        return qs.order_by('id')
    
        # for obj in qs.order_by(cls.invoiceable_date_field, 'id'):
        #     # dd.logger.info('20160223 %s', obj)
        #     yield obj

    # def setup_invoice_item(self, item):
    #     item.description = dd.plugins.jinja.render_from_request(
    #         None, 'courses/Enrolment/item_description.html',
    #         obj=self, item=item)


dd.update_field(
    Enrolment, 'overview',
    verbose_name=Course._meta.verbose_name)
