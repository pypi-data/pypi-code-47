import os


_FUGA_GITHUB_ORG_NAME = 'ayemos'  # XXX: temporary
_FUGA_DEFAULT_TEMPLATE_NAME = 'fuga-experiment-tmp'


def find_experiment_root_dir(max_depth=4):
    cur = os.getcwd()
    depth = 0

    while True:
        if 'fuga.yml' in os.listdir(cur):
            return cur

        if depth >= max_depth:
            return None
        depth += max_depth
        cur = os.path.dirname(cur)


def find_cookiecutter_template(template_name):
    pass
