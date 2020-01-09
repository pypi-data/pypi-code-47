from pathlib import Path

import sphinx
from docutils.nodes import raw
from sphinx.util.docutils import SphinxDirective

from .configuration import load_conf, parse_languages, read_configuration_file
from .jinja import env
from .rst_generators import make_directive
from slugify import slugify


CARDS_TEMPLATE = env.get_template("cards.jinja")


def generate_cards_file(app: sphinx.application.Sphinx):

    cards_file = Path("meta-sphinx.rst")
    if cards_file.is_file():
        cards_file.unlink()
    conf = load_conf(app)

    cards_directive = directive_from_config(conf)

    cards_file.write_text(cards_directive)


def directive_from_config(conf):
    content = content_from_config(conf)
    cards_directive = make_directive("raw", "html", content=content)

    return cards_directive


def content_from_config(conf):
    conf = parse_languages(conf)
    return CARDS_TEMPLATE.render(items=conf)  # actually create the html


class MetaSphinxCardsDirective(SphinxDirective):
    name = "meta_sphinx_gallery"
    has_content = False
    optional_arguments = 1
    final_argument_whitespace = True

    def run(self):
        file = self.arguments[0] if self.arguments else "libraries.yaml"
        # check if the configuration for this file has been generated:

        config = _get_and_parse_config_file(self, file)

        # config = self.env.meta_sphinx_configs[yaml_file]
        content = content_from_config(config)

        return [raw("", content, format="html")]


class MetaSphinxTocDirective(sphinx.directives.TocTree):
    name = "meta_sphinx_toc"
    has_content = False
    optional_arguments = 1
    final_argument_whitespace = True

    def parse_content(self, toctree):

        for docname in Path("project-index/").glob("*.rst"):
            if docname.stem == "index":
                continue
            toctree["entries"].append((None, str(docname.with_suffix(""))))
            toctree["includefiles"].append(str(docname.with_suffix("")))

        return []


def _get_and_parse_config_file(directive, file):
    if not hasattr(directive.env, "meta_sphinx_configs"):
        directive.env.meta_sphinx_configs = {}

    if file not in directive.env.meta_sphinx_configs:
        directive.env.meta_sphinx_configs[file] = read_configuration_file(
            file, download_meta=False
        )

    return directive.env.meta_sphinx_configs[file]
