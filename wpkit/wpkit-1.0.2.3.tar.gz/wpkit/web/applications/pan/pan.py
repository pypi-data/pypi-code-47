from flask import Flask, request, Blueprint, abort, send_file, redirect
from wpkit.web import resources, utils
from wpkit.pan import Pan, LocalFSHandle
from wpkit.web.base import MyBlueprint
from wpkit.web.resources import env, get_template_by_name
from wpkit.web.utils import parse_json_and_form
from wpkit.basic import Status,StatusError,StatusSuccess
import logging, functools
import wpkit


class BluePan(MyBlueprint):
    def __init__(self, import_name=None, name='pan', datapath='./data/pan', url_prefix='/pan',
                  **kwargs):
        # github_path = "git@github.com:Peiiii/MyCloudSpace.git",
        super().__init__(name=name, import_name=import_name, url_prefix=url_prefix, **kwargs)
        self.datapath = wpkit.basic.DirPath(datapath)
        self.db = wpkit.piu.Piu(path=self.datapath.db)
        # print("db:",self.db.dic)
        self.panpath = self.datapath / 'pan'
        self.pan = None
        self.config_statics({
            "/files": self.panpath
        })
        if self.db.get('initialized', None):
            try:
                self.pan=Pan(self.panpath)
            except:
                self.db.add('initialized',False)
        rd_post_github_path=redirect(location=self.url_prefix+'/post_github_path')


        def check_pan(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if not self.db.get('initialized', None):
                    github_path=None
                    try:
                        github_path = self.db.get('github_path', None)
                        print("get github_path:",github_path)
                        if not github_path:
                            return rd_post_github_path
                        self.pan = Pan.init(self.panpath, github_path=github_path)
                    except:
                        # raise
                        Pan(self.panpath).destroy()
                        print("error occured when init pan, github_path:",github_path or None)
                        return redirect(location=self.url_prefix+'/post_github_path')
                    print('Initializing Pan at %s' % (self.panpath))
                    self.db.add(initialized=True)

                self.pan = Pan(self.panpath)
                def getUrl(location, name):
                    # print("getUrlK")
                    res = 'http://%s:%s' % (
                        self.app.host, self.app.port) + self.url_prefix + '/files/' + self.pan.local_path(
                        location + '/' + name)
                    print("res", res)
                    return res

                self.pan.add_cmd('getUrl', getUrl)
                return func(*args,**kwargs)
            return wrapper

        def check_github_path(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if not self.db.get('github_path'):
                    return redirect(location=self.url_prefix+'/post_github_path')
                return func(*args, **kwargs)

            return wrapper

        self.usman = wpkit.web.utils.UserManager(dbpath=self.datapath.usman.db, home_url=self.url_prefix)
        usman = self.usman

        self.route('/login', methods=['post'])(usman.login(redirect_to=redirect(location=self.url_prefix)))
        self.route('/signup', methods=['post'])(usman.signup)

        @self.route('/post_github_path',methods=['GET'])
        def do_get_post_github_path():
            # print("hello")
            # return abort(404)
            return get_template_by_name('form').render(
                action=self.url_prefix + '/post_github_path',
                method='POST',
                name='github_path',
                msg='Input github path'
            )
        @self.route('/post_github_path', methods=['POST'])
        @parse_json_and_form
        def do_post_github_path(github_path):
            print("github_path:", github_path)
            if github_path:
                self.db.add(github_path=github_path)
                return redirect(location=self.url_prefix)
            else:
                return "error"

        @self.route('/', methods=['get'])
        @usman.login_required
        @check_pan
        @check_github_path
        def do_pan_get():
            return resources.get_template_by_name('pan').render()

        @self.route('/', methods=['POST'])
        def do_pan_post():
            return

        @self.route('/cmd', methods=['post'])
        @utils.parse_json
        def do_cmd(cmd):

            print('cmd:', cmd)
            try:
                res = self.pan.execute(cmd)
                res=StatusSuccess(data=res)
            except:
                # raise
                res=StatusError()
            print('res:', res)
            return utils.jsonify(res)

        @self.route('/upload', methods=['post'])
        @utils.parse_json
        def do_upload():
            f = request.files['file']
            f.save('upload.txt')
            # print(dir(a))
            print(dir(f))
            print(f)
            print({
                'content_type': f.content_type,
                'filename': f.filename,
                'headers': f.headers,
                'mimetype': f.mimetype,
                'mimetype_params': f.mimetype_params,
                'name': f.name
            })
            res = ''
            return utils.jsonify(res)
