from flask import Flask, request, Blueprint, abort, send_file
from wpkit.web import resources,utils
from wpkit.pan import Pan
from wpkit.web.bps.myblueprint import MyBlueprint
from wpkit.web.resources import env
import wpkit

class BluePan(MyBlueprint):
    def __init__(self,import_name=None,name='pan',datapath='./data/pan',url_prefix='/pan',github_path="git@github.com:Peiiii/MyCloudSpace.git",**kwargs):
        super().__init__(name=name,import_name=import_name,url_prefix=url_prefix,**kwargs)
        self.datapath = wpkit.basic.DirPath(datapath)
        self.db=wpkit.piu.Piu(path=self.datapath.db)
        self.panpath=self.datapath/'pan'
        if not self.db.get('initialized',None):
            self.pan= Pan.init(self.panpath, github_path=github_path)
            print('Initing Pan at %s'%(self.panpath))
            self.db.add(initialized=True)
        self.pan=Pan(self.panpath)
        self.usman=wpkit.web.utils.UserManager(dbpath=self.datapath.usman.db,home_url=self.url_prefix)
        usman = self.usman
        self.route('/login', methods=['post'])(usman.login)
        self.route('/signup', methods=['post'])(usman.signup)
        @self.route('/', methods=['get'])
        # @usman.login_required
        def do_pan_get():
            return resources.get_template_by_name('pan').render()
        @self.route('/', methods=['POST'])
        def do_pan_post():
            return
        @self.route('/cmd',methods=['post'])
        @utils.parse_json
        def do_cmd(cmd):
            print('cmd:',cmd)
            res=self.pan.execute(cmd)
            print('res:',res)
            return  utils.jsonify(res)

        @self.route('/upload',methods=['post'])
        @utils.parse_json
        def do_upload():
            f=request.files['file']
            f.save('upload.txt')
            # print(dir(a))
            print(dir(f))
            print(f)
            print({
                'content_type':f.content_type,
                'filename':f.filename,
                'headers':f.headers,
                'mimetype':f.mimetype,
                'mimetype_params':f.mimetype_params,
                'name':f.name 
            })
            res=''
            return  utils.jsonify(res)

        
