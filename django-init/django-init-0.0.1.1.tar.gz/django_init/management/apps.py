import argparse
import os
from distutils.dir_util import copy_tree
from functools import wraps
from importlib import import_module
from shutil import copyfile

from django.core.management.base import BaseCommand

from django_init.utils.config import get_version, get_apps_namespace


def yes_or_no(func):
    @wraps(func)
    def wrapper(*args, yes=False, **kwargs):
        action, name, subject = kwargs.get('action'), kwargs.get('name'), kwargs.get('subject')
        if yes:
            func(*args, **kwargs)
        else:
            while True:
                query = input('Would you like to %s the %r %s? [Y/n]' % (action, name, subject))
                if query == '' or not query.lower() in ['yes', 'y', 'no', 'n']:
                    print('Please answer with yes or no!')
                else:
                    if query.lower()[0] == 'y':
                        func(*args, **kwargs)
                    break

    return wrapper


class AppsManagement:
    def import_app(self, namespace):
        try:
            app = import_module(namespace)
        except ImportError as e:
            print(e)
        else:
            return app

    def copy_dir(self, app_name, from_dir, to_dir):
        copy_tree(from_dir, to_dir)
        print('Successfully created %r application' % app_name)

    def copy_file(self, file, to_dir):
        file_name = os.path.split(file)[1]
        # pass __init__.py
        if file_name[:2] == '__':
            return
        # change _.gitignore
        if file_name[:2] == '_.':
            file_name = file_name[1:]
        new_file = os.path.join(to_dir, file_name)
        if os.path.isfile(new_file):
            print('File %r exist' % new_file)
        else:
            copyfile(file, new_file)

    @yes_or_no
    def create_app(self, app_name):
        app = self.import_app('%s.%s' % (get_apps_namespace(), app_name))
        from_dir = os.path.dirname(app.__file__)
        to_dir = os.path.join(os.getcwd(), app_name)
        self.copy_dir(app_name, from_dir, to_dir)

    def create_project(self, app_name):
        self.create_app(app_name)
        app = self.import_app('%s' % get_apps_namespace())
        from_dir = os.path.dirname(app.__file__)
        to_dir = os.getcwd()

        for item in os.listdir(from_dir):
            item_path = os.path.join(from_dir, item)
            if os.path.isfile(item_path):
                self.copy_file(item_path, to_dir)

    def create_all(self):
        app = self.import_app('%s' % get_apps_namespace())
        from_dir = os.path.dirname(app.__file__)
        to_dir = os.getcwd()

        for item in os.listdir(from_dir):
            item_path = os.path.join(from_dir, item)
            if os.path.isfile(item_path):
                self.copy_file(item_path, to_dir)
            else:
                to_dir = os.path.join(os.getcwd(), item)
                self.copy_dir(item, from_dir, to_dir)
