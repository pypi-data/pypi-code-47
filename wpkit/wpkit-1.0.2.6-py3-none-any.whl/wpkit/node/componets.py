from wpkit.node import *

login_form=Form(action='post',target='/login')(
    Input(name='email',type='email'),
    Input(name='password',type='password'),
    Button(name='submit',type='submit')('Submit')
)
class Template:
    def __init__(self,node):
        self.node=node
    def _render(self,**kwargs):
        for k,v in kwargs:
            res=self.node.find('tem[tid=%s]' % (k))
            if res:res[0].replacewith(v)
        return self.node


