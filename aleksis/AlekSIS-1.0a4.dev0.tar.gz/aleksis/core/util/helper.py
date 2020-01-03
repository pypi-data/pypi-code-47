import os
from uuid import uuid4

from django.template.loader_tags import register


def path_and_rename(instance, filename):
    upload_to = 'menus'
    ext = filename.split('.')[-1].lower()
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


@register.inclusion_tag("components/msgbox.html")
def msg_box(msg, status="success", icon="info"):
    return {"msg": msg, "status": status, "icon": icon}
