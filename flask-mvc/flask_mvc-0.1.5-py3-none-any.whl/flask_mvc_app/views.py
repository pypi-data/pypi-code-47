from flask import render_template
from flask_mvc_app import widgets
from flask_mvc_app.models import registry


class View:
    def get_template_name(self):
        raise NotImplementedError('No template given!')

    def get_context(self):
        return {}

    def render(self, context={}):
        merged_context = {**self.get_context(), **context}
        return render_template(self.get_template_name(), **merged_context)


class ModelView(View):
    def __init__(self, model, obj=None):
        self.model = model
        self.obj = obj

    def get_context(self):
        return {'nav_models': registry, 'model': self.model, 'object': self.obj}

    def render(self, context={}):
        merged_context = {**self.get_context(), **context}
        return render_template(self.get_template_name(), **merged_context)


class ListView(ModelView):
    def get_template_name(self):
        return 'list_view.html'


class DetailView(ModelView):
    def get_template_name(self):
        return 'detail_view.html'


class ModelUpdatelView(ModelView):
    def get_template_name(self):
        return 'detail_view.html'


class CreateView(ModelUpdatelView):
    def __init__(self, model, obj=None):
        super().__init__(model, obj)

    def get_template_name(self):
        return 'create_view.html'


class UpdateView(ModelUpdatelView):
    def __init__(self, model, obj=None):
        super().__init__(model, obj)
        
    def get_template_name(self):
        return 'update_view.html'


class DeleteView(ModelUpdatelView):
    def __init__(self, model, obj=None):
        super().__init__(model, obj)

    def get_template_name(self):
        return 'delete_view.html'