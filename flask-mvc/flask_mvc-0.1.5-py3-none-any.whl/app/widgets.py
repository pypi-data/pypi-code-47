from flask import render_template
from flask import Markup
from flask import request


class Widget:
    template = 'widgets/default.html' 

    def __init__(self, value, params={}):
        self.value = value 
        self.params = params
        self.ctx = dict()

    def get_template_name(self):
        return self.template
        
    def render(self):
        return render_template(self.get_template_name(), **self.get_context()) # to do: Markup Safe!

    def get_context(self): 
        self.ctx['value'] = self.value
        return {**self.ctx, **self.params}

    def __str__(self):
        return self.render()


class HyperlinkWidget(Widget):
    template = 'widgets/hyperlink.html' 
        
    def __init__(self, url, value, params={}):
        super().__init__(value, params)
        self.url = url 

    def get_context(self):
        self.ctx['url'] = self.url
        return super().get_context()


class ListWidget(Widget):
    template = 'widgets/list.html' 
        
    def __init__(self, items: list, params={}):
        super().__init__(items, params)


class ModelWidget(Widget):
    def __init__(self, model_reference, field_name: str, data_object=None, params={}):
        super().__init__(None, params)
        self.model = model_reference
        self.data_object = data_object
        self.field_name = field_name

    @property
    def verbose_name(self):
        return ' '.join([field.capitalize() for field in self.field_name.split('_')])

    def get_context(self):
        if request.form:
            self.ctx['value'] = request.form.get(self.field_name)
        else:
            try:
                self.ctx['value'] = getattr(self.data_object, self.field_name)
            except AttributeError:
                self.ctx['value'] = '' # to do: default value?
        return {**self.ctx, **self.params}


class ModelListWidget(ModelWidget):
    template = 'widgets/linklist.html' 


class ModelTextWidget(ModelWidget):
    template = 'widgets/input_text.html' 

    def get_context(self):
        self.ctx['name'] = self.field_name
        self.ctx['id'] = self.field_name
        self.ctx['type'] = "text"
        self.ctx['label'] = self.verbose_name
        self.ctx['placeholder'] = self.verbose_name
        return super().get_context()


class ModelBooleanWidget(ModelWidget):
    template = 'widgets/input_checkbox.html' 

    def get_context(self):
        self.ctx['name'] = self.field_name
        self.ctx['id'] = self.field_name
        self.ctx['label'] = self.verbose_name
        self.ctx['checked'] = True
        return super().get_context()


class ModelSelectWidget(ModelWidget):
    template = 'widgets/input_select.html' 

    def get_context(self):
        try:
            self.ctx['value'] = getattr(self.data_object, self.field_name)
        except AttributeError:
            self.ctx['value'] = [] # to do: default value?

        self.ctx['name'] = f'{self.field_name}_id'
        self.ctx['id'] = self.ctx['name'] 
        self.ctx['label'] = self.verbose_name
        remote_model = self.model.__mapper__.relationships.get(self.field_name).mapper.class_
        self.ctx['items'] = remote_model.all()
        return super().get_context()


class ModelHyperlinkWidget(ModelWidget):
    template = 'widgets/hyperlink.html' 

    def get_context(self):
        remote_object = getattr(self.data_object, self.field_name)
        if isinstance(remote_object, (int, str,)):
            self.ctx['url'] = self.data_object.get_view_url() 
        elif remote_object:
            self.ctx['url'] = remote_object.get_view_url() # f'/app/admin/{model}/{field.id}'
        return super().get_context()
