from plone import api
#from plone.indexer.decorator import indexer
from plone.supermodel import model
from plone.dexterity.browser.view import DefaultView
from .vocabularies import PRESENTATION_DURATION_TYPES, LEVEL_TYPES, \
AUDIENCE_TYPES
from plone.event.interfaces import IEventAccessor
from plone.event.interfaces import IOccurrence
#from Products.Five.browser import BrowserView
import logging
from Products.CMFPlone.interfaces import ISelectableConstrainTypes
from plone.app.dexterity.behaviors.constrains import ENABLED
from plone.app.event.dx.behaviors import IEventContact
from collective.easyform.api import get_actions, set_actions
from plone.app.contenttypes.browser.collection import CollectionView

class IConference(model.Schema):
    model.load('models/conference.xml')


class ConferenceView(CollectionView):

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.data = IEventAccessor(context)

    def __call__(self):
        if IOccurrence.providedBy(self.context):
            # The transient Occurrence objects cannot be edited. disable the
            # edit border for them.
            self.request.set('disable_border', True)
        return self.index()  # render me.

    def duration_vocab(self):
        return PRESENTATION_DURATION_TYPES

    def level_vocab(self):
        return LEVEL_TYPES

    def audience_vocab(self):
        return AUDIENCE_TYPES

    def speakers(self):
        """ parse speaker set into something template can iterate over
        """
        speaker_set = self.context.speaker
        speakers = [api.content.get(UID=x) for x in speaker_set]
        speaker_data = []
        for x in speakers:
            scale_func = api.content.get_view(name='images', context=x, request=self.request)
            # scale choices are taken from portal_registry/edit/plone.allowed_sizes
            scaled_image = getattr(x.aq_explicit, 'headshot', False) and scale_func.scale('headshot', width=150, height=150)
            if scaled_image:
                tag = scaled_image.tag(css_class='image-left')
            else:
                tag = ''
            speaker_data.append({'url': x.absolute_url(), 'name': x.title, 'headshot': tag})
        return speaker_data

    def vocab_title(self, values, vocab):
        """ return title when given the vocabulary and the value key
        """
        if not isinstance(values, (list, set)):
            result = vocab.getTerm(values).title
            if vocab == AUDIENCE_TYPES:
                return [result] # hacky fix
            return result
        return [vocab.getTerm(x).title for x in values ]


def _set_mailer_adapter_recipient_email(conference):
    # set mailer adapter email address to be that of conference owner
    event_contact_aspect = IEventContact(conference)
    conference_contact_email = event_contact_aspect.contact_email
    conference_registration_form = getattr(conference, 'registration', None)
    if conference_registration_form:
        actions = get_actions(conference_registration_form)
        mailer = actions['mailer']
        mailer.recipient_email = conference_contact_email
        set_actions(conference_registration_form, actions)

def create_conference_content(conference, event):
    logging.getLogger(__name__).info("setting up the new conference item %s" % conference.getId())

    # set default collection constraints to list presentations
    conference.query = [
        {
            'i': 'portal_type',
            'o': 'plone.app.querystring.operation.selection.any',
            'v': ['presentation']
        }
    ]
    conference.sort_on = 'start'
    conference.sort_reversed = False

    # constrain types for conference object
    aspect = ISelectableConstrainTypes(conference)
    aspect.setConstrainTypesMode(ENABLED)
    allowed_types = ['Folder', 'Document']
    aspect.setLocallyAllowedTypes(allowed_types)
    aspect.setImmediatelyAddableTypes(allowed_types)

    # create Speakers folder and constrain types
    speakers = api.content.create(
        type='Folder',
        title='Speakers',
        container=conference)
    aspect = ISelectableConstrainTypes(speakers)
    aspect.setConstrainTypesMode(ENABLED)
    allowed_types = ['person', 'keynoter']
    aspect.setLocallyAllowedTypes(allowed_types)
    aspect.setImmediatelyAddableTypes(allowed_types)

    # create Talks folder and constrain types
    talks = api.content.create(
        type='Folder',
        title='Talks',
        container=conference)
    aspect = ISelectableConstrainTypes(talks)
    aspect.setConstrainTypesMode(ENABLED)
    allowed_types = ['presentation',]
    aspect.setLocallyAllowedTypes(allowed_types)
    aspect.setImmediatelyAddableTypes(allowed_types)

    # create Classes folder and constrain types
    classes = api.content.create(
        type='Folder',
        title='Classes',
        container=conference)
    aspect = ISelectableConstrainTypes(classes)
    aspect.setConstrainTypesMode(ENABLED)
    allowed_types = ['training_class',]
    aspect.setLocallyAllowedTypes(allowed_types)
    aspect.setImmediatelyAddableTypes(allowed_types)

    # copy registration folder from site root
    template_registration_form = api.content.get(path="/registration")
    api.content.copy(source=template_registration_form, target=conference)

    # set mailer adapter email address to be that of conference owner
    _set_mailer_adapter_recipient_email(conference)


def update_conference_content(conference, event):
    logging.getLogger(__name__).info("update modified conference item %s" % conference.getId())
    _set_mailer_adapter_recipient_email(conference)

