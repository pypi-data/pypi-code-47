import pkg_resources
import os, glob, uuid
from .resources import default_templates, get_default_template_string, default_static_dir
from .utils import piu, render, pkg_info, join_path
from . import utils
from jinja2 import Environment
from flask import Flask, request, Blueprint, abort, send_file
class App(Flask):
    def __init__(self, import_name ,dbpath='./data/db',add_pkg_resources=True):
        super().__init__(import_name)
        self.default_templates = default_templates
        self.db=piu.Piu(dbpath)
        self.o=utils.IterObject()
        self.sitemap=utils.IterObject()
        if add_pkg_resources:
            self.add_static(url_prefix='/pkg-resource', static_dir=default_static_dir)
    def add_blueprint(self,bp,url_prefix=None,*args,**kwargs):
        url_prefix=url_prefix or bp.url_prefix
        self.register_blueprint(bp,url_prefix=url_prefix)
        self.sitemap[bp.name]=url_prefix
    def add_multi_static(self, dic):
        for k, v in dic.items():
            self.add_static(k, v)
    def add_static(self, url_prefix, static_dir, template=None, name=None):
        name = 'bp_static_' + uuid.uuid4().hex if not name else name
        bp = self.bp_static(url_prefix=url_prefix,static_dir=static_dir, template=template, name=name)
        self.register_blueprint(bp)
    def bp_static(self,url_prefix='/fs', static_dir='./', template=None, name='None'):
        name = 'bp_static_' + uuid.uuid4().hex if not name else name
        template = self.default_templates['files'] if not template else template
        bp = Blueprint(name=name, import_name=self.import_name,url_prefix=url_prefix)

        @bp.route('/', defaults={'req_path': ''})
        @bp.route(join_path('/', '<path:req_path>'))
        def dir_listing(req_path):
            BASE_DIR = static_dir
            abs_path = os.path.join(BASE_DIR, req_path)
            if not os.path.exists(abs_path):
                return abort(404)
            if os.path.isfile(abs_path):
                return send_file(abs_path)
            if os.path.isdir(abs_path):
                fns = os.listdir(abs_path)
                fps = [join_path(url_prefix, req_path, f) for f in fns]
                return render(open(template, 'r', encoding='utf-8').read(), files=zip(fps, fns))
        return bp


def get_default_app(import_name,static_dir_dic=None):
    from wpkit.web import bps
    app = App(import_name=import_name)
    app.add_blueprint(bps.BlueWelcomePage(app=app,import_name=import_name,name='welcome',url_prefix='/'))
    app.add_blueprint(bps.BlueStatic(import_name=import_name,name='files',url_prefix='/files',static_dir='../'))
    app.add_multi_static(static_dir_dic) if static_dir_dic else None
    app.add_blueprint(bps.BlueBoard(import_name=import_name,name='board',url_prefix='/board'))
    if pkg_info.is_linux():
        app.add_blueprint(bps.BluePostAndDownload(import_name=import_name,name='PostAndDownload', url_prefix='/post_and_download'))
    app.add_blueprint(bps.BlueSitemap(import_name=import_name,name='sitemap',url_prefix='/sitemap',sitemap=app.sitemap))
    return app
def start_simple_http_server(import_name,host='127.0.0.1',port=80,static_dir_dic=None):
    app=get_default_app(import_name=import_name,static_dir_dic=static_dir_dic)
    print(app.url_map)
    app.run(host=host,port=port)

if __name__ == '__main__':
    start_simple_http_server(__name__)