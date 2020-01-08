from flask import session, request, redirect, flash
from flask_mvc_app import models, views, widgets
from sqlalchemy import exc


class Controller:
    def __init__(self, namespace, model_name):
        self.namespace = namespace
        self.model_name = str(model_name)
        self.model = models.registry[self.model_name]
        # self.model = getattr(models, model_name.capitalize())

    def index(self):
        search_term = request.args.get('search')
        if search_term:
            objects = self.model.search(search_term).all()
        else:
            objects = self.model.all()
        return views.ListView(self.model, objects).render()

    def view(self, id: int):
        obj = self.model.find_or_fail(id)
        return views.DetailView(self.model, obj).render()

    def create(self):
        if request.method == 'POST':
            try:
                print(request.form.__dict__)
                cleaned_data = self.model.get_cleaned_object(request.form)
                element = self.model.create(**cleaned_data)
                self.model.commit()
                flash('Object has been created successfully!', 'success')
                return redirect(element.get_view_url())
            except (AssertionError, exc.IntegrityError) as e:
                flash(e, 'danger')
                self.model.rollback()
        return views.CreateView(self.model).render()

    def update(self, id: int):
        obj = self.model.find_or_fail(id) # None abfangen 
        if request.method == 'POST':
            try:
                cleaned_data = self.model.get_cleaned_object(request.form)
                obj.update(**cleaned_data)
                self.model.commit()
                flash('Object has been modified successfully!', 'success')
                return redirect(obj.get_view_url())
            except (AssertionError, exc.IntegrityError) as e:
                flash(e, 'danger')
                self.model.rollback()
        return views.UpdateView(self.model, obj).render()

    def delete(self, id: int):
        obj = self.model.find_or_fail(id) # None abfangen 
        if request.method == 'POST':
            obj.delete()
            self.model.commit()
            flash('Object has been deleted successfully!', 'success')
            return redirect(self.model.get_index_url())
        else:
            return views.DeleteView(self.model, obj).render()