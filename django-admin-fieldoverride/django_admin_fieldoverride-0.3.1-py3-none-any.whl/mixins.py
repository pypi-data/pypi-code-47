from django.views.generic.detail import SingleObjectMixin

"""
We'll need a mixin to:
    - get all the override fields for a model instance
    - set the context with either the override content (if it exists), OR
    - the context from the parental fields (in order of precedence)
"""

class FieldOverrideMixin(SingleObjectMixin):
    """
    This handles setting context for all override fields.
    The override fields for a given AR5model is defined with the
        map_override_fields @classmethod.
    """
    def get_context_data(self, **kwargs):
        """
        For each field in the model's map_override_fields nethod:
           1. check to see if there's a FieldOverride record for that field
           2. If so:
               a. translate the value if necessary
               b. set context['field_name'] to that value
           3. Otherwise:
               a. go through the 'overrides' list:
               b. if the corresponding field is not None set context['field_name'] to that value
        
        If we allow Admin users to put in a field name OUTSIDE of the ones defined by the model 
            in map_override_fields()  (This is an unintended consequence of not having the drop-down
            working; it is currently possible to enter ANY field_name.  This sets up the ability for
            the Admin user to define a value for an object that is outside the model's definition,
            which wasn't INTENDED, but could be useful.)
        
            4. THEN:
                a. Go through the FieldOverride records:
                b. if a field shows up that is NOT in the list of fields from map_override_fields():
                    i. set the context['field_name']
            5. return the context
        """
        context = super(FieldOverrideMixin, self).get_context_data(**kwargs)
        
        # This is where the magic will happen.
        obj = self.get_object()
        # 1. get the map_override_fields for the parent model
        # 2. Process the FieldOverride records
        #   a. set the context for each value
        # 3. Fallback to default values from FMP or PBSMM
        # 
        # IF we allow "custom" overrides:   TBD - RAD 4/19/2019
        # 4. Go through the list of FieldOverride field_name values that are NOT in map_override_fields
        #   and set context for each of them.

        return context