# This file is part of the sphinxcontrib-inherit extension.
# Please see the COPYRIGHT and README.rst files at the top level of this
# repository for full copyright notices, license terms and support information.
from .directives import add_directives
from .nodes import add_nodes
from .path import Path, path_contains, path_subdir_contains
from .transforms import add_transforms

version = '0.1.0'


def inherit_config(app, config):
    "Configure Sphinx to exclude modules that are not required."
    try:
        config.inherit_modules = config.inherit_modules(app, config)
    except TypeError:
        pass
    if config.inherit_modules is None:
        config.inherit_modules = []

    src_dir = Path(app.srcdir)
    module_dir = src_dir / config.inherit_modules_dir
    modules = config.inherit_modules

    config.exclude_patterns += [
        str(d.relative_to(src_dir)) for d in module_dir.iterdir()
        if d.is_dir() and str(d.relative_to(module_dir)) not in modules]


def inherit_sort_docnames(app, env, docnames):
    "Sort docnames so they are processed in reverse inheritance order"
    modules_dir = Path(env.srcdir) / app.config.inherit_modules_dir
    modules = list(app.config.inherit_modules)
    modules.reverse()
    if not modules:
        return

    sorted_docnames = []

    # docnames in reverse order of their modules
    sorted_docnames += [
        d for m in modules for d in docnames
        if path_contains(modules_dir / m, env.doc2path(d))]

    # docnames that aren't in any module
    sorted_docnames += [
        d for d in docnames
        if not path_subdir_contains(modules_dir, env.doc2path(d))]

    docnames[:] = sorted_docnames


def setup(app):
    app.add_config_value('inherit_modules_dir', '', 'env')
    app.add_config_value('inherit_modules', None, 'env')

    app.connect('config-inited', inherit_config)
    app.connect('env-before-read-docs', inherit_sort_docnames)

    add_nodes(app)
    add_directives(app)
    add_transforms(app)

    return {
        'version': version,
        'env_version': 1,
        }
