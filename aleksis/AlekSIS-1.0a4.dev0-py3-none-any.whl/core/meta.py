import os
from django.conf import settings

# Build path for copyright
copyright_path = os.path.abspath(os.path.join(settings.BASE_DIR, '..', 'COPYRIGHT.md'))

# Read copyright from file
with open(copyright_path, "r") as f:
    COPYRIGHT = f.read()

COPYRIGHT_SHORT = "© 2018–2019 Mitglieder der Computer-AG, Katharineum zu Lübeck"

VERSION = '1.1.4 "Aebli"'

LICENSE_APACHE_2 = "Apache 2.0 License"
LICENSE_BSD = "2-Clause BSD License"
LICENSE_BSD_3 = "3-Clause BSD License"
LICENSE_MIT = "MIT License"
LICENSE_GPL_V2 = "GNU General Public License v2.0"
LICENSE_GPL_V3 = "GNU General Public License v3.0"

OPEN_SOURCE_COMPONENTS = [
    # ("Docker (u.a. Engine, CLI, docker-compose)", "https://github.com/docker", LICENSE_APACHE_2,
    #  "https://github.com/docker/docker/blob/master/LICENSE"),
    ("Django", "https://www.djangoproject.com/", "Django BSD License",
     "https://github.com/django/django/blob/master/LICENSE"),
    ("Python 3", "https://www.python.org/", "PSF LICENSE AGREEMENT FOR PYTHON",
     "https://docs.python.org/3/license.html"),
    ("jQuery", "https://jquery.com/", LICENSE_MIT, "https://github.com/jquery/jquery/blob/master/LICENSE.txt"),
    ("pip", "https://pypi.org/project/pip/", LICENSE_MIT, "https://github.com/pypa/pip/blob/master/LICENSE.txt"),
    ("Requests", "https://requests.kennethreitz.org/", LICENSE_APACHE_2,
     "https://github.com/psf/requests/blob/master/LICENSE"),
    ("django-widget-tweaks", "https://github.com/jazzband/django-widget-tweaks", LICENSE_MIT,
     "https://github.com/jazzband/django-widget-tweaks/blob/master/LICENSE"),
    ("Materialize CSS", "https://materializecss.com/", LICENSE_MIT,
     "https://github.com/Dogfalo/materialize/blob/master/LICENSE"),
    ("Material Design Icons", "http://google.github.io/material-design-icons/", LICENSE_APACHE_2,
     "https://github.com/google/material-design-icons/blob/master/LICENSE"),
    ("highlight.js", "https://highlightjs.org/", LICENSE_BSD_3,
     "https://github.com/highlightjs/highlight.js/blob/master/LICENSE"),
    ("React", "https://reactjs.org/", LICENSE_MIT, "https://github.com/facebook/react/blob/master/LICENSE"),
    ("mysqlclient", "https://github.com/PyMySQL/mysqlclient-python", LICENSE_GPL_V2,
     "https://github.com/PyMySQL/mysqlclient-python/blob/master/LICENSE"),
    ("django-auth-ldap", "https://github.com/django-auth-ldap/django-auth-ldap", LICENSE_BSD,
     "https://github.com/django-auth-ldap/django-auth-ldap/blob/master/LICENSE"),
    ("django-dbsettings", "https://github.com/zlorf/django-dbsettings", LICENSE_BSD_3,
     "https://github.com/zlorf/django-dbsettings/blob/master/LICENSE"),
    ("Django PDB", "https://github.com/HassenPy/django-pdb", "Public Domain", ""),
    ("Django Material", "https://github.com/viewflow/django-material", LICENSE_BSD_3,
     "https://github.com/viewflow/django-material/blob/master/LICENSE.txt"),
    ("Django Filter", "https://github.com/carltongibson/django-filter", LICENSE_BSD_3,
     "https://github.com/carltongibson/django-filter/blob/master/LICENSE"),
    ("django-react-templatetags", "https://github.com/Frojd/django-react-templatetags", LICENSE_MIT,
     "https://github.com/Frojd/django-react-templatetags/blob/develop/LICENSE"),
    ("martor", "https://github.com/agusmakmun/django-markdown-editor", LICENSE_GPL_V3,
     "https://github.com/agusmakmun/django-markdown-editor/blob/master/LICENSE"),
    ("Babel", "https://babeljs.io/", LICENSE_MIT, "https://github.com/babel/babel/blob/master/LICENSE")
]
OPEN_SOURCE_COMPONENTS.sort(key=lambda elem: elem[0].lower())


# Provide vars to all templates via processor
def meta_processor(request):
    return {'COPYRIGHT': COPYRIGHT, "COPYRIGHT_SHORT": COPYRIGHT_SHORT, "VERSION": VERSION}
