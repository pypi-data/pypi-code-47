# This file is part of the sphinxcontrib-inherit extension.
# Please see the COPYRIGHT and README.rst files at the top level of this
# repository for full copyright notices, license terms and support information.
from sphinx_testing import with_app
from unittest import TestCase


def with_builder_app(buildername):
    return with_app(
        buildername=buildername,
        srcdir='test/doc/basic/',
        warningiserror=True)


class TestInheritBuilders(TestCase):

    @with_builder_app('epub')
    def test_builder_epub(self, app, status, warning):
        "Test building epub documentation."
        app.builder.build_all()

    @with_builder_app('html')
    def test_builder_html(self, app, status, warning):
        "Test building html documentation."
        app.builder.build_all()

    @with_builder_app('latex')
    def test_builder_latex(self, app, status, warning):
        "Test building latex documentation."
        app.builder.build_all()

    @with_builder_app('man')
    def test_builder_man(self, app, status, warning):
        "Test building man documentation."
        app.builder.build_all()

    @with_builder_app('singlehtml')
    def test_builder_singlehtml(self, app, status, warning):
        "Test building singlehtml documentation."
        app.builder.build_all()

    @with_builder_app('texinfo')
    def test_builder_texinfo(self, app, status, warning):
        "Test building texinfo documentation."
        app.builder.build_all()

    @with_builder_app('text')
    def test_builder_text(self, app, status, warning):
        "Test building text documentation."
        app.builder.build_all()
