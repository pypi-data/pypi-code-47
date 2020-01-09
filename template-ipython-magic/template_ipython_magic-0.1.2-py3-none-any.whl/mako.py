from IPython.core.magic import Magics, magics_class, line_cell_magic, no_var_expand
from IPython.display import display, Markdown
from mako.template import Template as MTemplate

@magics_class
class MakoMagics(Magics):

    @line_cell_magic
    @no_var_expand
    def mako(self, line, cell=None):
        display(Markdown(MTemplate(cell or line).render(**self.shell.user_ns)))
