# This file is part of the sphinxcontrib-inherit extension.
# Please see the COPYRIGHT and README.rst files at the top level of this
# repository for full copyright notices, license terms and support information.
from collections import defaultdict
from docpath import path as docpath
from docutils import nodes
from itertools import chain
from sphinx.transforms import SphinxTransform
from sphinx.util import logging

from .nodes import (
    insert_nodes, is_indirect_target, move_to_before, remove_from, remove_node,
    inherit_hidden)

logger = logging.getLogger(__name__)


class InheritReposition(SphinxTransform):
    "Make inherit nodes the parent of the nodes they inherit"
    default_priority = 40

    def apply(self, **kwargs):
        for node in docpath('//inherit').findall(self.document):
            if not node.get('required_quantity', 0):
                continue

            next_node = docpath('following::*').find(node)
            if not next_node:
                self._remove_node(node, "inherit requires a node to inherit")
                continue

            if node.parent != next_node.parent:
                move_to_before(node, next_node)

            if docpath('ancestor::inherit').find(node):
                self._remove_node(node, "nested inherits are not allowed")
                continue

            count = node.inherit_required_quantity
            while count != 0 and next_node:
                remove_node(next_node)
                node.append(next_node)

                next_node = docpath('following_sibling::*').find(node)
                if count > 0:
                    count -= 1

    @staticmethod
    def _remove_node(node, warning):
        remove_node(node)
        logger.warning(warning, location=node.inherit_source)


class InheritExtract(SphinxTransform):
    "Extract and store any inherit nodes"
    default_priority = 50

    def __init__(self, document, startnode=None):
        super().__init__(document, startnode)
        if not getattr(self.env, 'inherit_nodes', None):
            self.env.inherit_nodes = defaultdict(list)

    def apply(self, **kwargs):
        docname = self.env.docname
        index = defaultdict(int)
        for node in docpath('//inherit').findall(self.document):
            self._clean_nodes_and_document(node)
            remove_node(node)

            node.check_number_of_children()
            if node.children_required_but_missing():
                continue

            key = node.inherit_target + (node.inherit_position,)
            self.env.inherit_nodes[key].insert(index[key], (docname, node))

            index[key] += 1

        if len(self.document.children) == 0:
            self.env.note_included(self.document['source'])

    def _clean_nodes_and_document(self, inherit_node):
        for inherited_node in docpath('.//*').findall(inherit_node):
            if not isinstance(inherited_node, nodes.Element):
                continue

            inherited_node['ids'] = []

            # Note: refid should be empty as only later transforms populate it

            for id in inherited_node.get('ids', []):
                self.document.ids.pop(id, None)

            for name in inherited_node.get('names', []):
                self.document.nameids.pop(name, None)
                self.document.nametypes.pop(name, None)
                self.document.refnames.pop(name, None)

                self.document.substitution_defs.pop(name, None)
                self.document.substitution_names.pop(name, None)

                self.document.footnote_refs.pop(name, None)
                self.document.citation_refs.pop(name, None)

            if is_indirect_target(inherited_node):
                remove_from(inherited_node, self.document.indirect_targets)

            if isinstance(inherited_node, nodes.footnote):
                remove_from(inherited_node, self.document.footnotes)
                remove_from(inherited_node, self.document.autofootnotes)
                remove_from(inherited_node, self.document.symbol_footnotes)

            if isinstance(inherited_node, nodes.footnote_reference):
                remove_from(inherited_node, self.document.autofootnote_refs)
                remove_from(inherited_node, self.document.symbol_footnote_refs)

            if isinstance(inherited_node, nodes.citation):
                remove_from(inherited_node, self.document.citations)


class InheritApply(SphinxTransform):
    "Apply inherit nodes to the document"
    default_priority = 60

    def __init__(self, document, startnode=None):
        super().__init__(document, startnode)
        if not getattr(self.env, 'inherit_applied', None):
            self.env.inherit_applied = defaultdict(set)

    def apply(self, **kwargs):
        inheritance = self._get_inheritance(self.env.docname)
        for target_node, inherit_node, position in inheritance:
            apply_inheritance = getattr(self, '_apply_{}'.format(position))
            apply_inheritance(target_node, inherit_node)

            self.env.inherit_applied[self.env.docname].add(inherit_node)

            source_docname = inherit_node.inherit_source[0]
            source_filename = self.env.doc2path(source_docname)
            self.env.note_dependency(source_filename)

    def _get_inheritance(self, document_name):
        inherit_nodes = self.env.inherit_nodes

        for (docname, path, position), parts in inherit_nodes.items():
            if docname is not None and docname != document_name:
                continue

            target_node = docpath(path).find(self.document)
            if target_node is None:
                continue

            for source_docname, inherit_node in parts:
                yield (target_node, inherit_node, position)

    def _next_node_after_any_target_nodes(self, from_node):
        after_target_nodes = docpath(
            '(descendant_or_self::node|following::node)[name() != target]')
        return after_target_nodes.find(from_node)

    def _apply_after(self, target_node, inherit_node):
        target_node = self._next_node_after_any_target_nodes(target_node)
        index = target_node.parent.index(target_node)
        insert_nodes(target_node.parent, index+1, inherit_node.inherited_nodes)
        self._register_nodes(inherit_node.inherited_nodes)

    def _apply_before(self, target_node, inherit_node):
        index = target_node.parent.index(target_node)
        insert_nodes(target_node.parent, index, inherit_node.inherited_nodes)
        self._register_nodes(inherit_node.inherited_nodes)

    def _apply_inside(self, target_node, inherit_node):
        target_node = self._next_node_after_any_target_nodes(target_node)
        if inherit_node.inherit_index is None:
            target_node.extend(inherit_node.inherited_nodes)
        else:
            insert_nodes(
                target_node, inherit_node.inherit_index,
                inherit_node.inherited_nodes)
        self._register_nodes(inherit_node.inherited_nodes)

    def _apply_hide(self, target_node, inherit_node):
        assert len(inherit_node.inherited_nodes) == 0
        target_node = self._next_node_after_any_target_nodes(target_node)

        index = target_node.parent.index(target_node)
        hidden_node = inherit_hidden(source=inherit_node['source'])
        target_node.parent.insert(index, hidden_node)

        self._register_nodes([hidden_node])

        remove_node(target_node)
        hidden_node.append(target_node)

    def _register_nodes(self, nodes):
        descendants_or_self = chain(
            *[docpath('descendant_or_self::*').findall(n) for n in nodes])
        for node in descendants_or_self:
            node_type = node.__class__.__name__
            note = getattr(self, '_note_{}'.format(node_type), None)
            if note:
                note(node)

    def _note_citation(self, node):
        self.document.note_citation(node)
        self.document.note_explicit_target(node, node)

    def _note_citation_reference(self, node):
        self.document.note_citation_ref(node)

    def _note_footnote(self, node):
        auto = str(node.get('auto', None))
        if auto == '1':
            self.document.note_autofootnote(node)
        elif auto == '*':
            self.document.note_symbol_footnote(node)
        else:
            self.document.note_footnote(node)

        if node.get('names', None):
            self.document.note_explicit_target(node, node)

    def _note_footnote_reference(self, node):
        auto = str(node.get('auto', None))
        if auto == '1':
            self.document.note_autofootnote_ref(node)
        elif auto == '*':
            self.document.note_symbol_footnote_ref(node)
        if node.get('refname', None):
            self.document.note_footnote_ref(node)

    def _note_reference(self, node):
        if node.get('refname', None):
            self.document.note_refname(node)

    def _note_section(self, node):
        self.document.note_implicit_target(node, node)

    def _note_substitution_definition(self, node):
        self.document.note_substitution_def(node, node['names'][0])

    def _note_substitution_reference(self, node):
        self.document.note_substitution_ref(node, node.astext())

    def _note_target(self, node):
        if node.get('refname', None):
            self.document.note_indirect_target(node)
        elif node.get('names'):
            self.document.note_explicit_target(node, node)
        else:
            self.document.note_anonymous_target(node)


class InheritMergeToctrees(SphinxTransform):
    "Merge inherited toctree nodes with existing toctree nodes."
    default_priority = 70

    def apply(self, **kwargs):
        for toctree in docpath('//toctree').findall(self.document):
            for node in docpath('following_sibling::toctree').findall(toctree):
                self.merge_toctrees(toctree, node)
                remove_node(node)

    def merge_toctrees(self, toctree, other):
        index = other.get('inherit_index', None)
        for attribute in ['entries', 'includefiles']:
            if index is None:
                toctree[attribute] += other[attribute]
            else:
                toctree[attribute] = (
                    toctree[attribute][:index] +
                    other[attribute] +
                    toctree[attribute][index:])

        attributes = [
            'caption', 'glob', 'hidden', 'includehidden', 'maxdepth',
            'numbered', 'titlesonly']
        for attribute in attributes:
            toctree[attribute] = other[attribute]


def check_consistency(self, env):
    applied_nodes = set()
    for inherit_nodes in env.inherit_applied.values():
        applied_nodes |= inherit_nodes

    for docname, node in chain(*env.inherit_nodes.values()):
        if node not in applied_nodes:
            logger.warning(
                "inherit not applied - target '{}' not found".format(
                    node['target']),
                location=node.inherit_source)


def purge_doc(self, env, docname):
    if getattr(env, 'inherit_nodes', None):
        for key in list(env.inherit_nodes):
            env.inherit_nodes[key] = [
                (d, n) for d, n in env.inherit_nodes[key] if d != docname]

    if getattr(env, 'inherit_applied', None):
        env.inherit_applied.pop(docname, None)


def add_transforms(app):
    app.add_transform(InheritReposition)
    app.add_transform(InheritExtract)
    app.add_transform(InheritApply)
    app.add_transform(InheritMergeToctrees)

    app.connect('env-check-consistency', check_consistency)
    app.connect('env-purge-doc', purge_doc)
