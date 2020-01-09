from pathlib import Path

import sphinx

from .configuration import load_conf, parse_languages
from .jinja import env
from slugify import slugify

PAGE_TEMPLATE = env.get_template("page.jinja")


INDEX_TEMPLATE = env.get_template("index-page.jinja")


def generate_page_files(app: sphinx.application.Sphinx):
    # app.config.html_static_path.append(str(static_path()))
    pages_from_config(
        load_conf(app, *app.config.meta_sphinx_generate_stubs_from),
        app.config.meta_sphinx_project_type,
    )


def pages_from_config(conf, project_type="Libraries"):
    page_parent_dir = Path("project-index")
    page_parent_dir.mkdir(exist_ok=True)
    # clean the page directory
    for file_ in page_parent_dir.glob("*.rst"):
        file_.unlink()

    conf = parse_languages(conf)

    (page_parent_dir / "index.rst").write_text(
        INDEX_TEMPLATE.render(project_type=project_type)
    )

    for item in conf:
        page_content = PAGE_TEMPLATE.render(item=item)

        (
            page_parent_dir / f"{item['name'].lower().replace(' ', '-')}.rst"
        ).write_text(page_content)
