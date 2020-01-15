import os

from .models import Robots
from django.forms import ModelForm
from django.conf import settings


class RobotsAdminForm(ModelForm):
    class Meta:
        model = Robots
        fields = '__all__'

    def __init__(self, data=None, files=None, instance=None, **kwargs):
        with open(os.path.join(settings.BASE_DIR, 'templates/robots.txt'), "r") as f:
            instance.value = f.read()
        super(RobotsAdminForm, self).__init__(data=data, files=files, instance=instance, **kwargs)

    def save(self, commit=True):
        with open(os.path.join(settings.BASE_DIR, 'templates/robots.txt'), "w") as f:
            f.write(self.cleaned_data["value"])
        return super(RobotsAdminForm, self).save(commit=commit)
