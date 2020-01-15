from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

def create_field_override_choices(override_map=None):
    """
    This is a utility function that takes the output from the map_override_fields method,
    and converts it to a tuple suitable for a "choices" option to a field.
    
    The map is a list of dicts.
    We want to return a list of tuples (value_to_store, value_to_show)
    """
    if override_map:
        choices = []
        for item in override_map:
                choices.append(item['field'], "{} ({})".format(item['field'],item['field_type']))
        return choices
    return None
    
def list_field_override_choices(override_map=None,  html=True):
    """
    This returns either a list of allowable choices, or an HTML-formatted unordered list (default).
    """
    if override_map:
        if html:
            choices = '<b>These are the allowable field override choices for field name:<ul>'
        else:
            choices = []
        for item in override_map:
            if html:
                choices += '<li>{}</li>'.format(item['field'])
            else:
                choices.append(item['field'])
        return choices
    return None
    
class FieldOverride(models.Model):
    """
    What do we need here?
        - What field am I?
        - What field(s) am I overriding?
        - what is my field type
        - what is the override data?
    
    So:
        1. Use the map_override_fields method to define the set of fields
        2. Save the above four fields
        
    We'll also want a Mixin that sets context of the override fields.  Since we know the path of override,
    we can use the map_override_fields method to do that AS WELL!
    
    """
    # I need to know what my model is...?
    # So this will have to be some sort of generic foreign key...
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    
    # This is one of the 'field' values in override_fields
    field_name = models.CharField (
        _('Field Name'),
        max_length = 100,
        #choices = get_appropriate_choices_for_field_name
        ###
        ###
        #### AND HERE IS THE MISSING LINK
        ###     I WANT to use something like this:
        #choices = create_field_override_choices(override_map=None)
        ### but how do I send the override_map from the model on the other end of the content_type field?
        ###
        ###
    )
    override_value = models.TextField (
        _('Override Value'),
        null = True, blank = True
    )
    
    
    #content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    #module = importlib.import_module(content_type.app_label)
    #model = getattr(module, content_type.model)
    #fields = model._meta.get_fields()
    
class FieldOverrideAbstractModel(models.Model):
    
    override_fields = GenericRelation(FieldOverride)
    
    @classmethod 
    def map_override_fields(self):
        """
        This is where you create the structure of fields that can be overridden.
            
        FOR NOW assume that the set of fields come from the 1:1 relationships to the FieldOverride model.
        
        So I'm expecting something like:
        
        override_fields = [
            {'field': 'description', 'field_type': 'TextField',
                'overrides': ['fmp__description', 'pbsmm__description_long']},
        ]
        
        where overrides is the list of fields in order of precedence, highest to lowest.
        
        I'm assuming the x__y syntax will work because e.g., in the Admin you can use that for all of the
        admin's parameters, and in the model _meta for things like setting default ordering.
        """
        return None # This is the default;  the user is supposed to override this method.
    
    class Meta:
        abstract = True
    
"""
    def map_override_fields(self):

"""        