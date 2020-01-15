# -*- coding: utf-8 -*-

from .models import Config

def setup(request):
    context = {}
    config_options = Config.objects.filter(is_active=True)
    for config_option in config_options:
        context['cfg_' + config_option.key] = config_option.value
    return context
