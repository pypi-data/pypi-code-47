# This file is part of the sphinxcontrib-inherit extension.
# Please see the COPYRIGHT and README.rst files at the top level of this
# repository for full copyright notices, license terms and support information.
from sphinx_testing import with_app
from unittest import TestCase


def with_modular_app(confoverrides):
    confoverrides.update({'exclude_patterns': []})
    return with_app(
        confoverrides=confoverrides,
        srcdir='test/doc/modules/',
        warningiserror=True)


def inherit_modules(app, config):
    return ['module1', 'module2']


class TestInheritModules(TestCase):

    @with_modular_app({'inherit_modules': None})
    def test_config_none_modules(self, app, status, warning):
        "Test building with None modules."
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertNotRegex(
            source,
            '(?ms)<h3>Module One Test.*</h3>')
        self.assertNotRegex(
            source,
            '(?ms)<h3>Module Two Test.*</h3>')

    @with_modular_app({'inherit_modules': []})
    def test_config_no_modules(self, app, status, warning):
        "Test building without modules."
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertNotRegex(
            source,
            '(?ms)<h3>Module One Test.*</h3>')
        self.assertNotRegex(
            source,
            '(?ms)<h3>Module Two Test.*</h3>')

    @with_modular_app({'inherit_modules': ['module1']})
    def test_config_module1(self, app, status, warning):
        "Test building with only module1."
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<h3>Module One Test.*</h3>')
        self.assertNotRegex(
            source,
            '(?ms)<h3>Module Two Test.*</h3>')

    @with_modular_app({'inherit_modules': ['module2']})
    def test_config_module2(self, app, status, warning):
        "Test building with only module2."
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertNotRegex(
            source,
            '(?ms)<h3>Module One Test.*</h3>')
        self.assertRegex(
            source,
            '(?ms)<h3>Module Two Test.*</h3>')

    @with_modular_app({'inherit_modules': ['module1', 'module2']})
    def test_config_module1_and_module2(self, app, status, warning):
        "Test building with module1 and module2."
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<h3>Module One Test.*</h3>.*'
            '(?ms)<h3>Module Two Test.*</h3>')

    @with_modular_app({'inherit_modules': ['module2', 'module1']})
    def test_config_module2_and_module1(self, app, status, warning):
        "Test building with module2 and module1."
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<h3>Module Two Test.*</h3>.*'
            '(?ms)<h3>Module One Test.*</h3>')

    @with_modular_app({'inherit_modules': inherit_modules})
    def test_config_inherit_modules_function(self, app, status, warning):
        "Test using a function to define the modules to include."
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegex(
            source,
            '(?ms)<h3>Module One Test.*</h3>.*'
            '(?ms)<h3>Module Two Test.*</h3>')
