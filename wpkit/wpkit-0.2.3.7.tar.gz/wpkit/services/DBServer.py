
from wpkit.piu import BackupDB
from flask import Flask,jsonify
from wpkit.web.utils import parse_json,parse_json_and_form
from wpkit.basic import PointDict,Status,StatusSuccess,StatusError
from flask_cors import CORS
class DBServer(Flask):
    def __init__(self,import_name,dbpath="./",url='/db/cmd',*args,**kwargs):
        super().__init__(import_name=import_name,*args,**kwargs)
        self.url = url
        self.db=BackupDB(path=dbpath)
        self.add_handlers()
        CORS(self,resources=r'/*')

    def add_handlers(self):
        @self.route(self.url,methods=['POST'])
        @parse_json_and_form
        def do_cmd(cmd):
            print("cmd:",cmd)
            try:
                res=self.db.execute(cmd)
                res=StatusSuccess(data=res)
            except:
                res=StatusError()
            return jsonify(res)






