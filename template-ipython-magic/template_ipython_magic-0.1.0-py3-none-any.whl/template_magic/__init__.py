__version__ = '0.1.0'

from IPython.core.magic import Magics, magics_class, line_cell_magic, no_var_expand
from IPython.display import display, Markdown
from jinja2 import Template as JTemplate
from mako.template import Template as MTemplate

@magics_class
class TemplateMagics(Magics):
    
    @line_cell_magic
    @no_var_expand
    def jinja(self, line, cell=None):
        display(Markdown(JTemplate(cell or line).render(self.shell.user_ns)))
        
    @line_cell_magic
    @no_var_expand
    def mako(self, line, cell=None):
        display(Markdown(MTemplate(cell or line).render(**self.shell.user_ns)))
        
def load_ipython_extension(ipython):
    ipython.register_magics(TemplateMagics)
