from datetime import datetime
import graphene as g
from metamorphosis import Microservice, EventMutation
from metamorphosis.events import BaseEventMixin
from metamorphosis.example.models import Form, LegacyForm, FormType
from uuid import uuid4

from metamorphosis.mutations import MutationTimings

_forms = {}


# an exception class that we'll use later
class BadWordException(Exception):
    pass


# declare the service
forms_service = Microservice('forms')


#
# Create GraphQL object types and register them
#
class FormCreatedEvent(g.ObjectType, BaseEventMixin):
    form = g.Field(Form)


class CreateFormEvent(g.ObjectType, BaseEventMixin):
    timing = g.Field(MutationTimings)
    name = g.String()
    template = g.String()
    creator = g.Int()
    request_ts = g.DateTime()

forms_service.register_type(FormCreatedEvent)
forms_service.register_type(CreateFormEvent)


# this is the "async case" of a mutation. In the async case, we really only return the request event back to the caller.
# that event should have an ID so that the caller can find out elsewhere the status of the event. In the synchronous
# one, we publish asynchronously and wait for the consumer to put the new object into a store we have access to.  In
# the production case, this would probably be redis and the resulting key would have a TTL and map to a serialized
# version of the newly created object.
class CreateForm(EventMutation):
    microservice = forms_service
    mutation_event_type = CreateFormEvent
    allowed_timings = [MutationTimings.synchronous, MutationTimings.asynchronous]
    consequent_objecttypes = (FormCreatedEvent,)

    # the arguments that will be needed to name the form
    class Arguments:
        timing = g.Argument(MutationTimings, default_value=MutationTimings.asynchronous)
        name = g.String()
        template = g.String()

    @classmethod
    def mutate_event(cls, root, info, **kwargs):
        timing, name, template = kwargs['timing'], kwargs['name'], kwargs['template']

        return CreateFormEvent(
            timing=timing,
            name=name,  # the name of the form
            template=template,  # the form template
            creator=0,  # current_user.person_id in a real system
            request_ts=datetime.now()  # the current timestamp
        )


class CreateFormAsync(EventMutation):
    microservice = forms_service
    mutation_event_type = CreateFormEvent

    # the arguments that will be needed to name the form
    class Arguments:
        name = g.String()
        template = g.String()

    @classmethod
    def mutate_event(cls, root, info, **kwargs):
        name, template = kwargs['name'], kwargs['template']

        return CreateFormEvent(
            timing=MutationTimings.asynchronous,
            name=name,  # the name of the form
            template=template,  # the form template
            creator=0,  # current_user.person_id in a real system
            request_ts=datetime.now()  # the current timestamp
        )


class CreateFormSync(EventMutation):
    microservice = forms_service
    mutation_event_type = CreateFormEvent
    allowed_timings = [MutationTimings.synchronous]
    consequent_objecttypes = (FormCreatedEvent,)

    # the arguments that will be needed to name the form
    class Arguments:
        name = g.String()
        template = g.String()

    @classmethod
    def mutate_event(cls, root, info, **kwargs):
        name, template = kwargs['name'], kwargs['template']

        return CreateFormEvent(
            timing=MutationTimings.synchronous,
            name=name,  # the name of the form
            template=template,  # the form template
            creator=0,  # current_user.person_id in a real system
            request_ts=datetime.now()  # the current timestamp
        )


# this is an example of something that would perhaps create Form objects. To have two different consumers consume
# the same set of events, they need different group_ids. That way for example you could have one consumer for working
# with refactored forms and one consumer for working with legacy forms.  You could also have a consumer for sending
# webhook messages and one for websockets, etc.
@forms_service.event_consumer(CreateFormEvent, save_result_for_sync_mutation=True)
def create_form(evt):
    forms_service.logger.info("Creating form %s", evt.id)

    if evt.name == 'poop':
        raise BadWordException(f'you used a bad word: {evt.name}')
    else:
        # this is where we *would* create a database record
        now = datetime.now()
        form = Form(
            id=uuid4(),
            name=evt.name,
            template=evt.template,
            created_by=evt.creator,
            updated_by=evt.creator,
            form_type=FormType.quick,
            created_date=now,
            updated_date=now
        )
        _forms[str(form.id)] = form

        return FormCreatedEvent(id=evt.id, form=form)


# my legacy form consdeumer. Note that it has a different group_id
@forms_service.event_consumer(CreateFormEvent, save_result_for_sync_mutation=False)
def legacy_create_form(evt):
    forms_service.logger.info("Creating legacy form %s", evt.id)

    # this is where we *would* create a database record
    if evt.name == 'poop':
        raise BadWordException(f'you used a bad word: {evt.name}')
    else:
        # this is where we *would* create a database record
        now = datetime.now()
        form = Form(
            id=uuid4(),
            name=evt.name,
            template=evt.template,
            created_by=evt.creator,
            updated_by=evt.creator,
            created_date=now,
            updated_date=now
        )
        _forms[str(form.id)] = form

    # return nothing because this consumer doesn't produce new events


class FormsQuery(g.ObjectType):
    all_forms = g.List(Form)

    @classmethod
    def resolve_all_forms(root, info, context, **kwargs):
        return _forms

