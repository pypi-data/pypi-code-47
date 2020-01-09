import jinja2
import markdown
from docutils.core import publish_parts

from . import static_path

md = markdown.Markdown(extensions=["meta"])


def md_to_html(text):
    return jinja2.Markup(md.convert(text))


def rst_to_html(text):
    return jinja2.Markup(
        publish_parts(
            source=text,
            writer_name="html",
            settings_overrides={"report_level": 5},
        )["html_body"]
    )


def prefix_lines(text, prefix, first=False):
    lines = text.split("\n")
    new_lines = []
    if first:
        new_lines.append(prefix + lines.pop(0))
    else:
        new_lines.append(lines.pop(0))
    new_lines.extend(prefix + line for line in lines)
    return "\n".join(new_lines)


def indent(text, width=4, first=False):
    prefix = " " * width
    return prefix_lines(text, prefix=prefix, first=first)


env = jinja2.Environment(undefined=jinja2.DebugUndefined)
env.loader = jinja2.FileSystemLoader(str(static_path()))
env.filters["markdown"] = md_to_html
env.filters["rst"] = rst_to_html
env.filters["indent"] = indent
env.filters["prefix"] = prefix_lines
env.globals.update(zip=zip)
