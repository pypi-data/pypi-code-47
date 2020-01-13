# This file is part of the sphinxcontrib-inherit extension.
# Please see the COPYRIGHT and README.rst files at the top level of this
# repository for full copyright notices, license terms and support information.
from sphinx_testing import with_app
from unittest import TestCase


def with_basic_app(warnings=''):
    return with_app(
        srcdir='test/doc/basic',
        warningiserror=(warnings != 'allow-warnings'),
        write_docstring='module/index.rst')


def with_content_app(buildername='singlehtml'):
    return with_app(
        buildername=buildername,
        srcdir='test/doc/content/',
        warningiserror=True,
        write_docstring='module/index.rst')


class TestInheritDirectivePosition(TestCase):

    @with_basic_app()
    def test_inherit_after(self, app, status, warning):
        """
        .. inherit:: after //section[@names=='tests']

        Test after directive.
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
             source,
             '(?ms)<h2>Tests<a[^>]*>¶</a></h2>.?</div>.?'
             '<p>Test after directive\.</p>')

    @with_basic_app()
    def test_inherit_before(self, app, status, warning):
        """
        .. inherit:: before //section[@names=='tests']

        Test before directive.
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
             source,
             '(?ms)<p>Test before directive\.</p>.?'
             '<div[^>]*>.?<h2>Tests<a[^>]*>')

    @with_basic_app()
    def test_inherit_inside(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']

        Test inside directive.
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<h2>Tests<a[^>]*>¶</a></h2>.?<p>Test inside directive\.</p>')

    @with_basic_app()
    def test_inherit_hide(self, app, status, warning):
        """
        .. inherit:: hide //section[@names=='tests']
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertNotRegex(source, '<h2>Tests')


class TestInheritDirectiveOptions(TestCase):

    @with_basic_app()
    def test_inherit_quantity(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']
            :quantity: 2

        Subsection One
        --------------

        A paragraph in subsection 1.

        Subsection Two
        --------------

        A paragraph in subsection 2.
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<h3>Subsection One<a[^>]*>¶</a></h3>.?'
            '<p>A paragraph in subsection 1\.</p>.*'
            '<h3>Subsection Two<a[^>]*>¶</a></h3>.?'
            '<p>A paragraph in subsection 2\.</p>')

    @with_basic_app()
    def test_inherit_filter(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']
            :filter: .//paragraph

        Section
        -------

        Subsection One
        ^^^^^^^^^^^^^^

        A paragraph in subsection 1.

        Subsection Two
        ^^^^^^^^^^^^^^

        A paragraph in subsection 2.
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<p>A paragraph in subsection 1\.</p>.*'
            '<p>A paragraph in subsection 2\.</p>')
        self.assertNotRegex(source, 'Section')
        self.assertNotRegex(source, 'Subsection One')
        self.assertNotRegex(source, 'Subsection Two')

    @with_content_app()
    def test_inherit_index_start(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='paragraphs']
            :index: 0

        A paragraph to test index insertion.
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<div[^>]*>\s*'
            '<p>A paragraph to test index insertion\.</p>\s*'
            '<h[3-6]>Paragraphs')

    @with_content_app()
    def test_inherit_index_end(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='paragraphs']
            :index: end

        A paragraph to test index insertion.
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<p>The fourth paragraph\.</p>\s*'
            '<p>A paragraph to test index insertion\.</p>\s*</div>')

    @with_content_app()
    def test_inherit_index_1(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='paragraphs']
            :index: 1

        A paragraph to test index insertion.
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<h[3-6]>Paragraphs<a[^>]*>[^<]*</a></h[3-6]>\s*'
            '<p>A paragraph to test index insertion\.</p>\s*'
            '<p>The first paragraph.</p>')

    @with_content_app()
    def test_inherit_index_minus_1(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='paragraphs']
            :index: -1

        A paragraph to test index insertion.
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<p>The third paragraph\.</p>\s*'
            '<p>A paragraph to test index insertion\.</p>\s*'
            '<p>The fourth paragraph\.</p>')

    @with_content_app()
    def test_inherit_list_item_insertion(self, app, status, warning):
        """
        .. inherit:: after //bullet_list/list_item[2]
            :filter: .//list_item

        * inserted item 1
        * inserted item 2
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<ul[^>]*>\s*<li><p>first list item</p></li>\s*'
            '<li><p>second list item</p></li>\s*'
            '<li><p>inserted item 1</p></li>\s*'
            '<li><p>inserted item 2</p></li>\s*'
            '<li><p>third list item</p></li>\s*'
            '<li><p>fourth list item</p></li>\s*</ul>')

    @with_content_app('html')
    def test_inherit_toctree_insertion(self, app, status, warning):
        """
        Module
        ======

        .. inherit:: inside //compound[./toctree]
            :filter: .//toctree
            :index: 1

        .. toctree::
            :maxdepth: 1

            index
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<div[^>]*>\s*<ul>\s*'
            '<li[^>]*><a[^>]*>Build Test</a></li>\s*'
            '<li[^>]*><a[^>]*>Module</a></li>\s*'
            '<li[^>]*><a[^>]*>Build Test</a></li>\s*'
            '</ul>\s*</div>')


class TestInheritDirectiveNodeTypes(TestCase):

    @with_basic_app()
    def test_inherit_substitution(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']

        Substitution Test
        -----------------

        Test substitutions: |not substituted|.

        .. |not substituted| replace:: successfully substituted
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source, '<p>Test substitutions: successfully substituted\.</p>')

    @with_basic_app()
    def test_inherit_hyperlink_internal(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']

        Internal Hyperlink Test
        -----------------------

        .. _internal link:

        Test an `internal link`_.
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '<p[^>]*>Test an <a[^>]*href="#internal-link"[^>]*>'
            'internal link</a>\.</p>')

    @with_basic_app()
    def test_inherit_hyperlink_external(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']

        External Hyperlink Test
        -----------------------

        Test an `external link`_.

        .. _`external link`: https://external.link/
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '<p>Test an <a[^>]*href="https://external.link/"[^>]*>'
            'external link</a>\.</p>')

    @with_basic_app()
    def test_inherit_hyperlink_anonymous(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']

        Anonymous Hyperlink Test
        ------------------------

        Test an `anonymous link`__.

        __ https://anonymous.link/
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '<p>Test an <a[^>]*href="https://anonymous.link/"[^>]*>'
            'anonymous link</a>\.</p>')

    @with_basic_app()
    def test_inherit_hyperlink_indirect(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']

        Indirect Hyperlink Test
        -----------------------

        Test an `indirect link`_.

        .. _`indirect target`: https://indirect.link/
        .. _`indirect link`: `indirect target`_
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '<p>Test an <a[^>]*href="https://indirect.link/"[^>]*>'
            'indirect link</a>\.</p>')

    @with_basic_app()
    def test_inherit_citation(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']

        Citation Test
        -------------

        Test a citation [CIT1]_.

        .. [CIT1] First citation.
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<p>Test a citation '
            '<a[^>]*href="#cit1" id="id1">\[?CIT1\]?</a>\.</p>')
        self.assertRegex(
            source,
            '(?ms)<a[^>]*href="#id1">\[?CIT1\]?</a>.*>First citation\.</')

    @with_basic_app()
    def test_inherit_footnote_manual(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']

        Manual Footnote Test
        --------------------

        Test a manually numbered footnote [1]_.

        .. [1] Manually numbered footnote.
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<p>Test a manually numbered footnote '
            '<a[^>]*href="#id2" id="id1">\[?1\]?</a>\.</p>')
        self.assertRegex(
            source,
            '(?ms)<a[^>]*href="#id1">\[?1\]?</a>.*'
            '>Manually numbered footnote\.</')

    @with_basic_app()
    def test_inherit_footnote_named(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']

        Named Footnote Test
        -------------------

        Test a named footnote [#footnote-name]_.

        .. [#footnote-name] Named footnote.
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<p>Test a named footnote '
            '<a[^>]*href="#footnote-name" id="id1">\[?1\]?</a>\.</p>')
        self.assertRegex(
            source, '(?ms)<a[^>]*href="#id1">\[?1\]?</a>.*>Named footnote\.</')

    @with_basic_app()
    def test_inherit_footnote_auto_numbered(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']

        Auto Numbered Footnote Test
        ---------------------------

        Test an auto numbered footnote [#]_.

        .. [#] Auto numbered footnote.
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<p>Test an auto numbered footnote '
            '<a[^>]*href="#id2" id="id1">\[?1\]?</a>\.</p>')
        self.assertRegex(
            source,
            '(?ms)<a[^>]*href="#id1">\[?1\]?</a>.*>Auto numbered footnote\.</')

    @with_basic_app()
    def test_inherit_footnote_auto_symbol(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']

        Auto Symbol Footnote Test
        -------------------------

        Test an auto symbol footnote [*]_.

        .. [*] Auto symbol footnote.
        """
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<p>Test an auto symbol footnote '
            '<a[^>]*href="#id2" id="id1">\[?\*\]?</a>\.</p>')
        self.assertRegex(
            source,
            '(?ms)<a[^>]*href="#id1">\[?\*\]?</a>.*>Auto symbol footnote\.</')

    @with_basic_app('allow-warnings')
    def test_inherit_warning_missing_from_toc(self, app, status, warning):
        """
        Some content that is not inherited.
        """
        app.builder.build_all()
        self.assertRegex(
            warning.getvalue(),
            "WARNING: document isn't included in any toctree")

    @with_basic_app('allow-warnings')
    def test_inherit_warning_no_target(self, app, status, warning):
        """
        .. inherit:: inside //non_existent_target

        Missing Target Test
        -------------------

        A section that should go inside a non existent target.
        """
        app.builder.build_all()
        self.assertRegex(
            warning.getvalue(),
            "WARNING: inherit not applied - "
            "target '//non_existent_target' not found")

    @with_basic_app('allow-warnings')
    def test_inherit_warning_double_inherit(self, app, status, warning):
        """
        .. inherit:: before //section[@names=='tests']

        .. inherit:: after //section[@names=='tests']

        Double Inherit Test
        -------------------

        Two inherit statements one directly after the other.
        """
        app.builder.build_all()
        self.assertRegex(
            warning.getvalue(),
            "WARNING: inherit captured 0 nodes instead of 1")

    @with_basic_app('allow-warnings')
    def test_inherit_warning_too_few_nodes(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']
            :quantity: 3

        Too Few Nodes Test
        ------------------

        Trying to inherit 3 sections, when only one is available.
        """
        app.builder.build_all()
        self.assertRegex(
            warning.getvalue(),
            "WARNING: inherit captured 1 nodes instead of 3")

    @with_basic_app('allow-warnings')
    def test_inherit_warning_nested_inherit(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']

        Nested Inherit Test
        -------------------

        .. inherit:: after //section[@names=='tests']

        A paragraph in the nested inherit test.
        """
        app.builder.build_all()
        self.assertRegex(
            warning.getvalue(),
            "WARNING: nested inherits are not allowed")

    @with_basic_app('allow-warnings')
    def test_inherit_warning_no_node(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']
        """
        app.builder.build_all()
        self.assertRegex(
            warning.getvalue(),
            "WARNING: inherit requires a node to inherit")

    @with_basic_app('allow-warnings')
    def test_inherit_warning_has_content(self, app, status, warning):
        """
        .. inherit:: inside //section[@names=='tests']

            inherit directive content.
        """
        app.builder.build_all()
        self.assertRegex(
            warning.getvalue(),
            "(?ms)Error in \"inherit\" directive:\sno content permitted\.")
