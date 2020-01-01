from flask import Flask, request, Blueprint, abort, send_file
from wpkit.web import resources,utils
from wpkit.pan import Pan
from wpkit.web.resources import env
import wpkit


def bp_pan(app, name='pan',url_prefix='/pan',host_dir='./data/pan'):
    bp=Blueprint(name=name,import_name=app.import_name,url_prefix=url_prefix)
    bp.app=app
    app.o.sitemap[name] = url_prefix
    app.o.pan.usman=utils.UserManager(dbpath='./data/pan/user',home_url=url_prefix)
    usman=app.o.pan.usman
    bp.route('/login',methods=['post'])(usman.login)
    bp.route('/signup',methods=['post'])(usman.signup)
    @bp.route('/',methods=['get'])
    @usman.login_required
    def do_pan_get():
        return env.get_template('pan.html').render()
    @bp.route('/',methods=['POST'])
    def do_pan_post():
        pass
    return bp