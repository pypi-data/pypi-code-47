from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import FieldOverride

import logging
django_log = logging.getLogger('django')

class FieldOverrideStackedInline(GenericStackedInline):
    model = FieldOverride
    extra = 0
    verbose_name_plural = 'FIELD OVERRIDE INLINE'
    
    def __init__(self, parent_model, admin_site):
        #print ("\nA: dir(self) = ", dir(self), "\n")
        #print ("\n self.form = ", self.form, '\n')
        #print ("\nB: self.model = ",self.model," dir(self.model) = ", dir(self.model), "\n")
        #print ("\nE: self.model.content_type = ", self.model.content_type, '\n')
        #print ("\nF: dir(E) = ", dir(self.model.content_type), '\n')
        #print ("\nE2: self.model.content_type.__class__ = ", self.model.content_type.__class__, '\n')
        #print ("\ndir(E2): dir(self.model.content_type.__class__) = ", dir(self.model.content_type.__class__), '\n')
        #print ("\nH: self.model.object_id = ", self.model.object_id, '\n')
        #print ("\nG: E.__class__ = ", self.model.content_type.__class_, '\n')
        #print ("\nFFF3D: content_type = ", self.model.content_type, '\n')
        return super(FieldOverrideStackedInline, self).__init__(parent_model, admin_site)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(ModelImageInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        #print (" FFFF: ", self.parent_model.__name__)
        #django_log.info("TEST: {}".format(self.parent_model.__name__))
        if db_field == 'field_name':
             my_class_name = self.parent_model.__name__ 
             #print ("FFF2: class name = ", my_class_name)
             #django_log.info("FFF2: class name = {}".format(my_class_name))
        return None
    #django_log.info('TEST: {}'.format(model.content_type.model_class().map_override_fields()))
    # How do I get to?
    # model.content_type.model_class().map_override_fields()