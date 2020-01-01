from ..myblueprint import MyBlueprint
from wpkit.web import utils,resources

class BlueWelcomePage(MyBlueprint):
    def __init__(self,app,import_name=None,name='sitemap',url_prefix='/sitemap',**kwargs):
        super().__init__(name=name,import_name=import_name,url_prefix=url_prefix,**kwargs)
        @self.route('/')
        def do_root():
            temf = resources.default_templates['welcome']
            return utils.render(open(temf, 'r', encoding='utf-8').read(),context=app)