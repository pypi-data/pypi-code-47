class Model:
    @staticmethod
    def validate_set_property(value, prop, type_str, options=[]):
        if not isinstance(value, type_str):
            raise TypeError("{} property must be set to a {}".format(prop, type_str))
        if options:
            try:
                options.index(value)
            except ValueError:
                raise ValueError("{} value is not acceptable".format(value))
