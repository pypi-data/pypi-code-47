from pathlib import Path

import sphinx

from . import static_path


def add_bootstrap_styles(app: sphinx.application.Sphinx):
    app.config.html_static_path.append(str(static_path()))
    app.add_css_file("bs4-no-fonts.css")
    app.add_css_file("embedded.css")
    app.add_css_file("language-pills.css")
    # then, add the theme styles to override the bootstrap style


def re_add_existing_styles(app):
    for theme_path in app.builder.theme.get_theme_dirs():
        for css in (Path(theme_path) / "static").glob("**/*.css"):
            app.add_css_file(str(css))
    app.config.html_static_path.append(str(static_path()))
