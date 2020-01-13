# This file is part of the sphinxcontrib-inherit extension.
# Please see the COPYRIGHT and README.rst files at the top level of this
# repository for full copyright notices, license terms and support information.
from docpath import path as docpath
from docutils.parsers.rst.directives import nonnegative_int
from sphinx.util.docutils import SphinxDirective

from .nodes import inherit


def _get_quantity(position, option_value):
    result = option_value

    if result is None:
        default = 1
        result = {
            'hide': 0,
            }.get(position, default)

    if result == 'all':
        result = -1

    return result


def docpath_path(argument):
    docpath(argument)
    return argument


def int_or_end(argument):
    if argument == 'end':
        return None
    return int(argument)


def nonnegative_int_or_all(argument):
    if argument == 'all':
        return
    return nonnegative_int(argument)


class Inherit(SphinxDirective):
    required_arguments = 2
    final_argument_whitespace = True
    option_spec = {
        'filter': docpath_path,
        'index': int_or_end,
        'quantity':  nonnegative_int_or_all,
    }

    def run(self):
        position = self.arguments[0]
        quantity = _get_quantity(position, self.options.get('quantity', None))
        return [inherit(
            filter=self.options.get('filter', []),
            index=self.options.get('index', None),
            position=position,
            required_quantity=quantity,
            source='{}:{}'.format(self.env.docname, self.lineno),
            target=self.arguments[1],
            )]


def add_directives(app):
    app.add_directive('inherit', Inherit)
