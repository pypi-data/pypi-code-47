import os
import subprocess
import sys
from distutils.dir_util import copy_tree
from functools import wraps
from importlib import import_module
from shutil import copyfile

from django_init.utils.config import get_init_namespace


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


def git_init():
    subprocess.check_call(['git', 'init'])


# https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program
def install_package(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])


def install_requirements(dir):
    file_name = 'requirements.txt'
    file = os.path.join(dir, file_name)
    if os.path.isfile(file):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', file])


def get_requirements(dir):
    import requirements
    file_name = 'requirements.txt'
    file = os.path.join(dir, file_name)
    reqs = {}
    with open(file) as f:
        for pkg in requirements.parse(f):
            yield pkg.name, pkg.specs
        f.closed
    return reqs


def create_requirements(reqs):
    i = len(reqs)
    for req in reqs:
        pass


def import_app(namespace):
    try:
        app = import_module(namespace)
    except ImportError as e:
        print(e)
    else:
        return app


def remove_file(dir, file_name):
    file = os.path.join(dir, file_name)
    if os.path.isfile(file):
        os.remove(file)


class AppsManagement:
    def get_path_dir(self, namespace, app_name):
        app = import_app(namespace)
        base_path = os.path.dirname(app.__file__)
        path = os.path.join(base_path, app_name)
        if os.path.isdir(path):
            return path
        raise SystemExit('No module named %r' % app_name)

    def copy_dir(self, label, app_name, from_dir, to_dir):
        copy_tree(from_dir, to_dir)
        print('Successfully created %r %s' % (app_name, label))

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
            print('Successfully created %r %s' % (new_file, 'file'))

    @staticmethod
    def get_apps():
        app = import_app('%s' % get_init_namespace())
        apps_dir = os.path.dirname(app.__file__)
        for app_name in os.listdir(apps_dir):
            app_path = os.path.join(apps_dir, app_name)
            if os.path.isdir(app_path) and not app_name[:2] == '__':
                yield app_path, app_name

    def create_app(self, app_name):
        from_dir = self.get_path_dir(get_init_namespace(), app_name)
        to_dir = os.path.join(os.getcwd(), app_name)
        copy_tree(from_dir, to_dir)
        print('Successfully created %r %s' % (app_name, 'application'))

        install_requirements(from_dir)
        remove_file(to_dir, 'requirements.txt')
        get_requirements(from_dir)

    def create_project(self):
        self.create_app('app')
        app = import_app('%s' % get_init_namespace())
        from_dir = os.path.dirname(app.__file__)
        to_dir = os.getcwd()

        for item in os.listdir(from_dir):
            item_path = os.path.join(from_dir, item)
            if os.path.isfile(item_path):
                self.copy_file(item_path, to_dir)

        git_init()

    def create_all(self):
        app = import_app('%s' % get_init_namespace())
        from_dir = os.path.dirname(app.__file__)
        to_dir = os.getcwd()

        for item in os.listdir(from_dir):
            item_path = os.path.join(from_dir, item)
            if os.path.isfile(item_path):
                self.copy_file(item_path, to_dir)
            else:
                to_dir = os.path.join(os.getcwd(), item)
                self.copy_dir(item, from_dir, to_dir)


