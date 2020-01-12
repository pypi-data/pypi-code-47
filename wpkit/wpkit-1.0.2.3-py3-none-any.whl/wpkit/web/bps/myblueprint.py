from flask import Blueprint
class MyBlueprint(Blueprint):
    def __init__(self, name, import_name=None, url_prefix=None,**kwargs):
        super().__init__(name=name,import_name=import_name,url_prefix=url_prefix,**kwargs)