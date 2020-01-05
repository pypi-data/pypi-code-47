'''
requirements:
'''
from flask import Flask, request, Blueprint, abort, send_file
from wpkit.web import resources,utils

def bp_fs(app, name='fs',url_prefix='/fs',host_dir='./'):
    bp=Blueprint(name=name,import_name=app.import_name,url_prefix=url_prefix)
    app.o.sitemap[name] = url_prefix

    @bp.route('/', defaults={'req_path': ''})
    @bp.route('/<path:req_path>')
    def get():
        pass

    @bp.route('/', defaults={'req_path': ''})
    @bp.route('/<path:req_path>')
    def post():
        data=request.get_json()
        print(data)
    return bp
