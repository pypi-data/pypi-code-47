from pathlib import Path
import json
from slugify import slugify

col_json = Path(__file__).parent / "colors.json"
col_css = Path(__file__).parent / "language-pills.css"

CSS_TEMPL = """
.badge-{language} {{
    color: {text_color};
    background-color: {pill_color};
}}
"""


def gen_color_css():
    with col_json.open("r") as f:
        col_data = json.load(f)
    css_snippets = []
    for language, data in col_data.items():
        language = slugify(language)

        pill_color = data.get("color") or "#ADB2CB"
        text_color = "#ffffff" if is_dark(pill_color) else "#111111"
        css_snippets.append(
            CSS_TEMPL.format(
                language=language, pill_color=pill_color, text_color=text_color
            )
        )
    col_css.write_text("\n".join(css_snippets))


def get_language_colors_css_path():
    if not col_css.is_file():
        gen_color_css()
    return col_css


def is_dark(color: str):
    """
    from https://github.com/ozh/github-colors/blob/master/github-colors.py
    """
    color = color.lstrip("#")
    brightness = (
        0.2126 * int(color[0:2], 16)
        + 0.7152 * int(color[2:4], 16)
        + 0.0722 * int(color[4:6], 16)
    )
    return False if brightness / 255 > 0.65 else True
