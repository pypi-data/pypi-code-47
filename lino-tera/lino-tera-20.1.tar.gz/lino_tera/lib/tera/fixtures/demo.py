# -*- coding: UTF-8 -*-
# Copyright 2017-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""Demo data for Lino Tera.

- Create a client MTI child for most persons.

"""
from __future__ import unicode_literals

import datetime
from django.conf import settings

from lino.utils import ONE_DAY
from lino.utils.mti import mtichild
from lino.utils.ssin import generate_ssin
from lino.api import dd, rt, _
from lino.utils import Cycler
from lino.utils.mldbc import babel_named as named, babeld
from lino.modlib.users.utils import create_user
from lino_xl.lib.cal.choicelists import EntryStates, GuestStates
from lino_tera.lib.courses.choicelists import InvoicingPolicies, HouseholdCompositions

# from django.conf import settings

# courses = dd.resolve_app('courses')
# cal = dd.resolve_app('cal')
# users = dd.resolve_app('users')

AMOUNTS = Cycler("5.00", None, None, "15.00", "20.00", None, None)


def person2clients():
    Person = rt.models.contacts.Person
    Client = rt.models.tera.Client
    ClientStates = rt.models.clients.ClientStates

    count = 0
    for person in Person.objects.all():
        count += 1
        if count % 7 and person.gender and not person.birth_date:
            # most persons, but not those from humanlinks and those
            # with empty gender field, become clients. Youngest client
            # is 16; 170 days between each client
            
            birth_date = settings.SITE.demo_date(-170 * count - 16 * 365)
            national_id = generate_ssin(birth_date, person.gender)

            client = mtichild(
                person, Client, 
                national_id=national_id,
                birth_date=birth_date)

            if count % 2:
                client.client_state = ClientStates.active
            elif count % 5:
                client.client_state = ClientStates.newcomer
            else:
                client.client_state = ClientStates.closed
            yield client

        

def enrolments():
    # Person = rt.models.contacts.Person
    # Pupil = dd.plugins.courses.pupil_model
    Client = rt.models.tera.Client
    Teacher = dd.plugins.courses.teacher_model
    Line = rt.models.courses.Line
    EventType = rt.models.cal.EventType
    GuestRole = rt.models.cal.GuestRole
    Course = rt.models.courses.Course
    Enrolment = rt.models.courses.Enrolment
    DurationUnits = rt.models.cal.DurationUnits
    SalesRule = rt.models.invoicing.SalesRule
    UserTypes = rt.models.users.UserTypes
    Company = rt.models.contacts.Company
    Product = rt.models.products.Product
    Tariff = rt.models.invoicing.Tariff
    ProductTypes = rt.models.products.ProductTypes
    Topic = rt.models.topics.Topic
    Interest = rt.models.topics.Interest
    ProductCat = rt.models.products.ProductCat
    Account = rt.models.ledger.Account
    CommonItems = rt.models.sheets.CommonItems
    CourseAreas = rt.models.courses.CourseAreas
    PriceRule = rt.models.products.PriceRule

    # yield skills_objects()

    presence = ProductCat(**dd.str2kw('name', _("Fees")))
    yield presence

    cash = ProductCat(**dd.str2kw('name', _("Cash daybooks")))
    yield cash

    obj = Company(
        name="Tough Thorough Thought Therapies",
        country_id="BE", vat_id="BE12 3456 7890")
    yield obj
    settings.SITE.site_config.update(site_company=obj)

    indacc = named(
        Account, _("Sales on therapies"),
        sheet_item=CommonItems.sales.get_object(), ref="7010")
    yield indacc

    t1 = babeld(Tariff, _("By presence"), number_of_events=1)
    yield t1

    t10 = babeld(Tariff, _("Maximum 10"), number_of_events=1, max_asset=10)
    yield t10

    group_therapy = named(
        Product, _("Group therapy"), sales_account=indacc,
        tariff=t1,
        sales_price=30, cat=presence,
        product_type=ProductTypes.default)
    yield group_therapy

    # group_therapy.tariff.number_of_events = 1
    # yield group_therapy.tariff
    
    ind_therapy = named(
        Product, _("Individual therapy"),
        tariff=t1,
        sales_price=20, sales_account=indacc, cat=presence,
        product_type=ProductTypes.default)
    yield ind_therapy

    ind_therapy10 = named(
        Product, _("Individual therapy"),
        tariff=t10,
        sales_price=20, sales_account=indacc, cat=presence,
        product_type=ProductTypes.default)
    yield ind_therapy10

    # ind_therapy.tariff.number_of_events = 1
    # yield ind_therapy.tariff
   
    yield named(Product, _("Other"), sales_price=35)
    prepayment = named(
        Product, _("Cash daybook Daniel"), cat=cash,
        product_type=ProductTypes.daybooks)
    yield prepayment

    attendee = GuestRole(**dd.str2kw('name', _("Attendee")))
    yield attendee
    colleague = GuestRole(**dd.str2kw('name', _("Colleague"), is_teacher=True))
    yield colleague

    ind_et = EventType(
        force_guest_states=True,
        **dd.str2kw('name', _("Individual appointment")))
    yield ind_et
    group_et = EventType(
        force_guest_states=False,
        **dd.str2kw('name', _("Group meeting")))
    yield group_et

    yield create_user("daniel", UserTypes.therapist,
                      cash_daybook=prepayment, event_type=ind_et)
    yield create_user("elmar", UserTypes.therapist, event_type=group_et)
    yield create_user("lydia", UserTypes.secretary)

    yield named(Topic, _("Alcoholism"), ref="A")
    yield named(Topic, _("Phobia"), ref="P")
    yield named(Topic, _("Insomnia"), ref="I")

    yield PriceRule(seqno=1, event_type=ind_et,
                    pf_composition=HouseholdCompositions.more_children,
                    fee=ind_therapy10)
    yield PriceRule(seqno=2, event_type=group_et, fee=group_therapy)
    yield PriceRule(seqno=3, event_type=ind_et, fee=ind_therapy)

    for a in CourseAreas.get_list_items():
        kw = dict(
            name=a.text, course_area=a, guest_role=attendee)
        # kw.update(fees_cat=presence)
        kw.update(guest_role=attendee)
        # if a.name in('therapies', 'life_groups'):
        #     kw.update(fee=ind_therapy, event_type=ind_et)
        # else:
        #     kw.update(fee=group_therapy, event_type=group_et)
        a.line_obj = Line(**kw)
        yield a.line_obj  # temporary cache used below
        
    invoice_recipient = None
    for n, p in enumerate(Client.objects.all()):
        if n % 10 == 0:
            yield SalesRule(
                partner=p, invoice_recipient=invoice_recipient)
            # p.salesrule.invoice_recipient = invoice_recipient
            # yield p
        else:
            invoice_recipient = p

    # LINES = Cycler(Line.objects.all())
    USERS = Cycler(rt.models.users.User.objects.all())
    PLACES = Cycler(rt.models.cal.Room.objects.all())
    TEACHERS = Cycler(Teacher.objects.all())
    SLOTS = Cycler(rt.models.courses.Slot.objects.all())
    TOPICS = Cycler(rt.models.topics.Topic.objects.all())
    # TARIFFS = Cycler(rt.models.invoicing.Tariff.objects.all())
    # FEES = Cycler(rt.models.products.Product.objects.filter(product_type=ProductTypes.default))

    date = settings.SITE.demo_date(-200)
    qs = Client.objects.all()
    if qs.count() == 0:
        raise Exception("Oops, no clients!")
    PUPILS = Cycler(qs)
    kw = dict(state='active', line=CourseAreas.therapies.line_obj)
    for i, obj in enumerate(qs):
        if i % 6:
            kw.update(
                user=USERS.pop(),
                # client=obj,
                partner=obj,
                teacher=TEACHERS.pop(),
                # line=LINES.pop(),
                room=PLACES.pop(),
                start_date=date,
                every=2,
                max_events=10,
                every_unit=DurationUnits.weeks,
                slot=SLOTS.pop())
            # kw.update(product=FEES.pop())
            c = Course(**kw)
            yield c
            yield Interest(partner=c, topic=TOPICS.pop())
            if i % 3:  # some have a second topic
                yield Interest(partner=c, topic=TOPICS.pop())
            yield Enrolment(pupil=obj, course=c, state='confirmed')
            c.save()  # fill presences
            ar = rt.login(c.user.username)
            c.update_reminders(ar)
            date += ONE_DAY
            
    date = settings.SITE.demo_date(-200)
    kw = dict(state='active', line=CourseAreas.default.line_obj)
    grsizes = Cycler(5, 7, 12, 6)
    group_names = (_("Alcohol"), _("Burnout"), _("Women"), _("Children"))
    for name in group_names:
        kw.update(
            user=USERS.pop(),
            # client=obj,
            name=name,
            teacher=TEACHERS.pop(),
            # line=LINES.pop(),
            room=PLACES.pop(),
            start_date=date,
            max_events=10,
            every=1,
            every_unit=DurationUnits.weeks,
            slot=SLOTS.pop())
        # kw.update(product=FEES.pop())
        # kw.update(tariff=TARIFFS.pop())
        c = Course(**kw)
        yield c
        for i in range(grsizes.pop()):
            yield Enrolment(
                pupil=PUPILS.pop(), course=c, state='confirmed')
        c.save()  # fill presences
        ar = rt.login(c.user.username)
        c.update_reminders(ar)
        date += ONE_DAY
    qs = rt.models.cal.Event.objects.filter(
        start_date__lt=dd.today(-10))
    for e in qs:
        if e.id % 5:
            e.state = EntryStates.took_place
        else:
            e.state = EntryStates.missed
        if e.user and e.user.cash_daybook_id:
            if e.project.line.invoicing_policy == \
               InvoicingPolicies.by_event:
                e.amount = AMOUNTS.pop()
        yield e
    for g in rt.models.cal.Guest.objects.filter(
            event__start_date__lt=dd.today(-10)):
        if g.id % 5:
            g.state = GuestStates.present
            e = g.event
            if e.user and e.user.cash_daybook_id:
                if e.project.line.invoicing_policy == \
                   InvoicingPolicies.by_event:
                    g.amount = AMOUNTS.pop()
        else:
            g.state = GuestStates.missing
        yield g

    # for course in Course.objects.all():
    #     pp = course.

    # for obj in Course.objects.all():

            
def objects():
    yield person2clients()
    yield enrolments()
