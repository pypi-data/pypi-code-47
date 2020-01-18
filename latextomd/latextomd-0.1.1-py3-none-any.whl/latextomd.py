import re

def _remove_comments(latex_string):
    """Remove comments"""
    return re.sub('(?<!\\\\)%.*$', '', latex_string, flags=re.M)

def _process_preamble(latex_string):
    """Detect latex preamble"""
    if r"\begin{document}" in latex_string:
        preamble, content = latex_string.split(r"\begin{document}")
        if r"\end{document}" in content:
            content, draft = content.split(r"\end{document}")
    else:
        preamble = 'default header\n'
        content = latex_string
    return preamble, content


def to_markdown(latex_string, export_file_name=""):
    content = latex_string
    content = _remove_comments(content)
    preamble, content = _process_preamble(content)
    return content
