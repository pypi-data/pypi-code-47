"""Make a sphinx directive"""


def make_directive(
    directive_type, *directive_arguments, content="", **directive_options
):
    """Generate a sphinx RST directive with correctly formatted arguments"""
    first_line = f".. {directive_type}:: {' '.join(directive_arguments)}"
    option_lines = [
        "    " + (f":{key}: {val}" if val is not None else f":{key}:")
        for key, val in directive_options.items()
    ]
    if isinstance(content, str):
        content = content.split("\n")
    content = ["    " + line for line in content]

    text = "\n".join([first_line, *option_lines, "", *content])
    return text
