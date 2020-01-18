import pkg_resources, os
from .utils import SecureDirPath, PointDict, pkg_info, Path, DirPath
from jinja2 import Environment, PackageLoader
import jinja2
from jinja2 import Environment, \
        BaseLoader, FileSystemLoader, \
        ChoiceLoader, DictLoader, PrefixLoader

data_path = pkg_info.pkg_data_dir
pkg_templates_dir = DirPath(data_path) / 'templates'
pkg_js_dir = DirPath(data_path) / 'static' / 'js'
default_templates = PointDict.from_dict({
    'welcome': pkg_resources.resource_filename('wpkit', 'data/templates/welcome.html'),
    'files': pkg_resources.resource_filename('wpkit', 'data/templates/files.html'),
    'board': pkg_resources.resource_filename('wpkit', 'data/templates/board.html'),
    'sitemap': pkg_resources.resource_filename('wpkit', 'data/templates/sitemap.html'),
    'post': pkg_resources.resource_filename('wpkit', 'data/templates/post.html'),
    'outsite': pkg_resources.resource_filename('wpkit', 'data/templates/outsite.html')
})
default_static_dir = SecureDirPath(pkg_info.pkg_dir) / 'data' / 'static'


def get_default_template_string(tem):
    return open(default_templates[tem], 'r', encoding='utf-8').read()


env = Environment(loader=PackageLoader('wpkit.data', 'templates'))


def get_template_by_name(fn='base'):
    if not fn.endswith('.html'): fn += '.html'
    return env.get_template(fn)


def get_template_string_by_name(fn):
    if not fn.endswith('.html'): fn += '.html'
    return (pkg_templates_dir / fn)()


def get_js_string_by_name(fn):
    if not fn.endswith('.js'): fn += '.js'
    return (pkg_js_dir / fn)()


def get_env(path=None):
    path=path or './'


    _loader = ChoiceLoader([
        FileSystemLoader(path),
        PrefixLoader({
            'sys': ChoiceLoader([
                FileSystemLoader(data_path + '/static'),
                FileSystemLoader(data_path + '/templates')
            ]),
            'user': ChoiceLoader([
                FileSystemLoader('data/templates'),
                FileSystemLoader('data/blogs'),
            ])
        }),
        ChoiceLoader([
            FileSystemLoader(data_path + '/static'),
            FileSystemLoader(data_path + '/templates'),
            FileSystemLoader('data/templates'),
            FileSystemLoader('data/blogs'),
        ])
    ])
    env = Environment(
        loader=_loader
    )
    return env
pkg_tem_loader=ChoiceLoader([
                FileSystemLoader(data_path + '/static'),
                FileSystemLoader(data_path + '/templates')
            ])
pkg_env=Environment(
    loader=pkg_tem_loader
)
class Pages:
    links=get_template_by_name('links')
    view_text_file=pkg_env.get_template('view_file.tem')
    view_markdown_file=pkg_env.get_template('view_md.tem')