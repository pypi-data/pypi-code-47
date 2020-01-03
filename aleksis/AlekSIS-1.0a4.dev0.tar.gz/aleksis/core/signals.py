import os
from glob import glob

from django.conf import settings


def clean_scss(*args, **kwargs) -> None:
    for source_map in glob(os.path.join(settings.STATIC_ROOT, "*.css.map")):
        try:
            os.unlink(source_map)
        except OSError:
            # Ignore because old is better than nothing
            pass  # noqa
