from flask import Flask, request, Blueprint, abort, send_file,g
from .utils import join_path,render,piu
from . import resources
import uuid
from . import utils
def bp_static(app,static_dir='./',name=None, template=None,url_prefix='/files'):
    import  os
    name = 'bp_static_' + uuid.uuid4().hex if not name else name
    template = resources.default_templates['files'] if not template else template
    bp = Blueprint(name=name, import_name=app.import_name, url_prefix=url_prefix)
    app.o.sitemap[name]=url_prefix
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

def bp_sitemap(app,url_prefix='/sitemap',map=None,add_map={},name='sitemap'):
    bp = Blueprint(name=name, import_name=app.import_name, url_prefix=url_prefix)
    app.o.sitemap[name] = url_prefix
    app.o.sitemap.update(add_map)
    app.o.sitemap=map if map is not None else app.o.sitemap
    @bp.route('/')
    def do_root():
        temf = resources.default_templates['sitemap']
        return render(open(temf, 'r', encoding='utf-8').read(),context=app.o)
    return bp
def bp_welcome(app,url_prefix='/',name='home'):
    bp = Blueprint(name=name, import_name=app.import_name, url_prefix=url_prefix)
    app.o.sitemap[name] = url_prefix
    @bp.route('/')
    def do_root():
        temf = resources.default_templates['welcome']
        # print(app.o)
        return render(open(temf, 'r', encoding='utf-8').read(),context=app.o)
    return bp
def bp_board(app, name='board',url_prefix='/board',db_path=None):
    bp=Blueprint(name=name,import_name=app.import_name,url_prefix=url_prefix)
    app.o.sitemap[name] = url_prefix
    db = app.db if db_path is None else piu.Piu(db_path)
    @bp.route('/')
    def do_board():
        data = db.get('board_data', '')
        return render(resources.get_default_template_string('board'), content=data)
    @bp.route('/post', methods=['POST'])
    def do_board_post():
        data = request.get_json()
        # print('board data:%s' % (data))
        db.add('board_data', data['content'])
        return 'success'
    return bp

def bp_post_and_download_by_linux_wget(app, name='post and download',url_prefix='/post_and_download',out_dir='/var/www/html',download_path=None):
    bp=Blueprint(name=name,import_name=app.import_name,url_prefix=url_prefix)
    app.o.sitemap[name] = url_prefix
    assert utils.pkg_info.is_linux()
    import wpkit.linux as pylinux
    @bp.route('/', methods=['GET'])
    def do_post_get():
        return render(resources.get_default_template_string('post'))

    @bp.route('/', methods=['POST'])
    def do_post_post():
        data = request.get_json()
        url = data['url']
        print('get url: %s'%url)
        pylinux.tools.wget_download(url, out_dir=out_dir)
        return 'seccess'
    return bp
