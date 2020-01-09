import sphinx

from . import version
from .generate_gallery import MetaSphinxCardsDirective, MetaSphinxTocDirective
from .generate_pages import generate_page_files
from .generate_hosting import generate_hosting
from .styles import add_bootstrap_styles, re_add_existing_styles
from slugify import slugify


def setup(app: sphinx.application.Sphinx):
    """Setup meta-sphinx"""
    add_bootstrap_styles(app)
    app.add_directive("meta_sphinx_gallery", MetaSphinxCardsDirective)
    app.add_directive("meta_sphinx_toc", MetaSphinxTocDirective)
    app.add_config_value("meta_sphinx_generate_stubs_from", [], "html")
    app.add_config_value("meta_sphinx_project_type", "Libraries", "html")
    app.connect("builder-inited", generate_page_files)
    app.connect("builder-inited", re_add_existing_styles)

    metadata = {
        "parallel_read_safe": True,
        "parallel_write_safe": False,
        "version": version,
    }

    return metadata
