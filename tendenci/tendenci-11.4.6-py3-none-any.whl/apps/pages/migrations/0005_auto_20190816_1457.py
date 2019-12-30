# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-16 14:57
from __future__ import unicode_literals

from django.db import migrations

def remove_fb_like_from_custom_templates(apps, schema_editor):
    """
    Remove facebook like buttons from custom templates (the templates pulled down to site).
     
    1) pages/meta.html
        Remove facebook like block 
    
        {% if show_fb_connect|default:False %}
           {% fb_like_button_iframe news.get_absolute_url height=20 %}
       {% endif %}
       
    
    """
    import re
    import os
    from tendenci.apps.theme.utils import get_theme_root
    dir_path = get_theme_root()
    # pages/meta.html
    file_path = '{}/templates/pages/meta.html'.format(dir_path)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            p = r'{0}([\d\D\s\S\w\W]*?){1}'.format(re.escape('{% if show_fb_connect|default:False %}'),
                                                                re.escape('{% endif %}'))
            content = re.sub(p, '', content)
            
        with open(file_path, 'w') as f:
            f.write(content)


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20190815_1719'),
    ]

    operations = [
        migrations.RunPython(remove_fb_like_from_custom_templates),
    ]
