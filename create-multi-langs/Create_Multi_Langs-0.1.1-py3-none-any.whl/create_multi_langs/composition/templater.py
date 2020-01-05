from __future__ import absolute_import
import jinja2
from typing import List


class Templater:

    def __init__(self,
                 template_path: str,
                 n_spaces_per_indent: int = 4):
        self._template_content = open(template_path, 'r').read()
        self._spaces_per_indent = " " * n_spaces_per_indent

    def spaces(self, n_indent: int) -> str:
        return self._spaces_per_indent * n_indent

    def comment(self, contents: str, n_indent: int = 0) -> str:
        spaces = self.spaces(n_indent)
        out = ""
        out += spaces + self._comment_head_prefix + "\n"
        for content in contents.split("\n"):
            out += spaces + self._comment_mid_prefix + content + "\n"
        out += spaces + self._comment_tail_prefix + "\n"

        return out

    def key_value_lines(self,
                        key_values: dict,
                        double_quote_key: bool = False,
                        double_quote_value: bool = False,
                        split_punctuation: str = ": ",
                        end_punctuation: str = "",
                        n_indent: int = 0) -> str:
        spaces = self.spaces(n_indent)
        keys_double_quotes = '"' if double_quote_key else ''
        value_double_quotes = '"' if double_quote_value else ''
        lines: List[str] = []
        for key, value in key_values.items():
            line = '''{spaces}{keys_double_quotes}{key}{keys_double_quotes}{split_punctuation}{value_double_quotes}{value}{value_double_quotes}{end_punctuation}'''.format(  # noqa: E501
                spaces=spaces,
                keys_double_quotes=keys_double_quotes,
                key=key,
                split_punctuation=split_punctuation,
                value_double_quotes=value_double_quotes,
                value=value,
                end_punctuation=end_punctuation
            )
            lines.append(line)

        return '\n'.join(lines)

    def render(self, data: dict) -> str:
        t = jinja2.Template(self._template_content)
        return t.render(**data)
