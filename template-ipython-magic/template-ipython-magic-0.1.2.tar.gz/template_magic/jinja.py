from IPython.core.magic import Magics, magics_class, line_cell_magic, no_var_expand
from IPython.display import display, Markdown
from jinja2 import Template as JTemplate

@magics_class
class JinjaMagics(Magics):

    @line_cell_magic
    @no_var_expand
    def jinja(self, line, cell=None):
        display(Markdown(JTemplate(cell or line).render(self.shell.user_ns)))
