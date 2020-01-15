import sys
import argparse
import configparser
import os


def get_package_namespace():
    return 'django_init'


def get_init_namespace():
    return '%s.init' % get_package_namespace()


def get_version():
    """
    Return the django-init version, which should be correct for all built-in
    commands. User-supplied commands can override this method to
    return their own version.
    """
    # root_dir = os.path.abspath(os.path.dirname(__name__))
    # config_path = os.path.join(root_dir, 'setup.cfg')
    # config = configparser.ConfigParser()
    # config.read(config_path)
    # version = config.get('metadata', 'version')
    version = '11111'
    return version