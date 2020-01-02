'''
requirements:
Linux with wget installed.
'''
from flask import Flask, request, Blueprint, abort, send_file,g
from wpkit.web.utils import join_path,render,piu
from wpkit.web import resources
import uuid
from wpkit.web import utils

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
