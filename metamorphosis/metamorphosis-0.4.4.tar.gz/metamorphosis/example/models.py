import graphene as g

class FormType(g.Enum):
    quick = 0
    ds = 1

# this is in the place of a database record type.  in normal usage, this would be a SQLAlchemyObjectType
class Form(g.ObjectType):
    id = g.String()
    name = g.String()
    template = g.String()
    form_type = g.Field(FormType)
    created_by = g.Int()
    updated_by = g.Int()
    created_date = g.DateTime()
    updated_date = g.DateTime()


# this is in the place of a database record type.  in normal usage, this would be a SQLAlchemyObjectType
class LegacyForm(g.ObjectType):
    id = g.String()
    name = g.String()
    template = g.String()
    created_by = g.Int()
    updated_by = g.Int()
    created_date = g.DateTime()
    updated_date = g.DateTime()


