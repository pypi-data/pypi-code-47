# This file is part of the sphinxcontrib-inherit extension.
# Please see the COPYRIGHT and README.rst files at the top level of this
# repository for full copyright notices, license terms and support information.
from docpath import path as docpath
from docutils import nodes
from sphinx import addnodes as sphinx_nodes
from sphinx.util import logging

logger = logging.getLogger(__name__)


class inherit(nodes.Element, nodes.Structural):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._inherited_nodes = None

    def check_number_of_children(self):
        if self.inherit_required_quantity == -1:
            return

        if len(self.children) != self.inherit_required_quantity:
            logger.warning(
                "inherit captured {} nodes instead of {}".format(
                    len(self.children), self.inherit_required_quantity),
                location=self.inherit_source)

    def children_required_but_missing(self):
        return self.inherit_required_quantity and len(self.children) == 0

    @property
    def inherit_index(self):
        return self['index']

    @property
    def inherit_position(self):
        return self['position']

    @property
    def inherit_required_quantity(self):
        return self.get('required_quantity', 0)

    @property
    def inherit_source(self):
        return tuple(self['source'].split(':', 1))

    @property
    def inherit_target(self):
        file, *docpath = self['target'].split(',', 1)
        if '[' in file or not docpath:
            file = None
            docpath = [self['target']]
        return (file, docpath[0])

    @property
    def inherited_nodes(self):
        if self._inherited_nodes is None:
            filter = self.get('filter', None)
            if filter:
                self._inherited_nodes = []
                for node in docpath(filter).findall(self):
                    self._inherited_nodes.append(node.deepcopy())
            else:
                self._inherited_nodes = self.deepcopy().children

            index = self.get('index', None)
            if index is not None:
                for node in self._inherited_nodes:
                    if isinstance(node, sphinx_nodes.toctree):
                        node['inherit_index'] = int(index)

        return self._inherited_nodes


class inherit_hidden(nodes.Element, nodes.Structural):
    pass


def _skip_node(self, node):
    raise nodes.SkipNode


def add_nodes(app):
    app.add_node(inherit)
    app.add_node(
        inherit_hidden,
        html=(_skip_node, None),
        latex=(_skip_node, None),
        man=(_skip_node, None),
        texinfo=(_skip_node, None),
        text=(_skip_node, None),
        )


def insert_nodes(element, index, nodes):
    for node in reversed(nodes):
        element.insert(index, node)


def is_indirect_target(node):
    return isinstance(node, nodes.target) and node.get('refname', None)


def move_to_before(node, target):
    index = target.parent.index(target)
    remove_node(node)
    target.parent.insert(index, node)


def remove_from(node, node_list):
    found = None
    for list_item in node_list:
        attrs = set(node.attributes) | set(list_item.attributes)
        if all(node.get(a, None) == list_item.get(a, None) for a in attrs):
            found = list_item
            break
    if found:
        node_list.remove(found)


def remove_node(node):
    node.parent.remove(node)
    node.parent = None


def _get_node_types():
    node_types = {}

    for name in dir(nodes):
        node_type = getattr(nodes, name)
        try:
            if issubclass(node_type, nodes.Node):
                node_types[name] = node_type
        except TypeError:
            pass

    for name in dir(sphinx_nodes):
        node_type = getattr(sphinx_nodes, name)
        try:
            if issubclass(node_type, nodes.Node):
                node_types[name] = node_type
        except TypeError:
            pass

    return node_types


node_types = _get_node_types()
