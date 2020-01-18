from wpkit.web.base import MyBlueprint
from wpkit.web import utils,resources

class BlueWelcomePage(MyBlueprint):
    def __init__(self,import_name=None,name='welcome',url_prefix='/sitemap',**kwargs):
        super().__init__(name=name,import_name=import_name,url_prefix=url_prefix,**kwargs)
        @self.route('/')
        def do_root():
            temf = resources.default_templates['welcome']
            return utils.render(open(temf, 'r', encoding='utf-8').read(),context=self.app)
    def register(self, app, *args,**kwargs):
        self.app=app
        super().register(app,*args,**kwargs)