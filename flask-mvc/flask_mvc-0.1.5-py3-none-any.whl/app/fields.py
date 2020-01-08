from app import db
from app import widgets


class BaseField(db.Column):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.view_widget = widgets.ModelWidget
        self.edit_widget = widgets.ModelTextWidget

    @property
    def verbose_name(self):
        return ' '.join([field.capitalize() for field in self.key.split('_')])

    @staticmethod    
    def clean(value):
        return value

    def validate(self, value):
        return value


class PrimaryKeyField(BaseField):
    def __init__(self, *args, **kwargs):
        super().__init__(db.Integer, primary_key=True, *args, **kwargs)
        self.view_widget = widgets.ModelHyperlinkWidget


class IntegerField(BaseField):
    def __init__(self, *args, **kwargs):
        super().__init__(db.Integer, *args, **kwargs)

    @staticmethod
    def clean(value):
        return int(value)


class StringField(BaseField):
    def __init__(self, *args, **kwargs):
        super().__init__(db.String(255), *args, **kwargs)

    @staticmethod
    def clean(value):
        return value.strip()


class BooleanField(BaseField):
    def __init__(self, *args, **kwargs):
        super().__init__(db.Boolean, *args, **kwargs)
        self.edit_widget = widgets.ModelBooleanWidget

    @staticmethod
    def clean(value):
        return True if value.lower() == 'on' else False


class ForeignKeyField(BaseField):
    def __init__(self, related_field:str, *args, **kwargs):
        super().__init__(db.Integer, db.ForeignKey(related_field), *args, **kwargs)
        # db.Column(db.Integer, db.ForeignKey('namespace.id')) 


class RelationshipField(db.RelationshipProperty):
    view_widget = {'ONETOMANY': widgets.ModelListWidget, 'MANYTOONE': widgets.ModelHyperlinkWidget}
    edit_widget = {'ONETOMANY': widgets.ModelWidget, 'MANYTOONE': widgets.ModelSelectWidget} 

    def __init__(self, related_model:str, *args, **kwargs):
        super().__init__(related_model, *args, **kwargs)

    @property
    def verbose_name(self):
        return ' '.join([field.capitalize() for field in self.key.split('_')])

    def get_view_widget(self):
        if self.direction.name in self.view_widget:
            return self.view_widget[self.direction.name]
        print(f'WARNING: get_view_widget: {self.direction.name} is not defined!')
        return widgets.ModelWidget

    def get_edit_widget(self):
        if self.direction.name in self.edit_widget:
            return self.edit_widget[self.direction.name]
        print(f'WARNING: get_edit_widget: {self.direction.name} is not defined!')
        return widgets.ModelTextWidget


def relationship(model:str):
    obj = db.relationship(model)
    obj.__class__ = RelationshipField # Python Cast :-)
    return obj
