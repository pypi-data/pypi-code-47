from __future__ import absolute_import
from create_multi_langs.creater.base import CreaterBase


class CreaterJavaScriptFrontEnd(CreaterBase):

    @staticmethod
    def from_csv_file(csv_file: str,
                      output_code_file: str,
                      naming_rule='lcc',
                      sep=','):
        assert output_code_file.endswith((".js", ".mjs")), \
            "javascript filename must ends with .js or .mjs"
        creater = CreaterJavaScriptFrontEnd(
            csv_file,
            output_code_file,
            template_path="data/javascript/template_frontend.tmpl",
            naming_rule=naming_rule,
            sep=sep,
        )
        return creater

    @property
    def lang_table_contents(self) -> str:
        outs = []
        for lang_code in self._reader.lang_codes():
            out = ''
            out += self._templater.spaces(1) + '"' + lang_code + '"' + ': {\n'
            out += self._templater.key_value_lines(
                key_values=self._reader.field_values(lang_code),
                double_quote_key=False,
                double_quote_value=True,
                split_punctuation=": ",
                end_punctuation=",",
                n_indent=2,
            ) + '\n'
            out += self._templater.spaces(1) + '},'
            outs.append(out)
        return '\n'.join(outs)

    @property
    def default_lang(self) -> str:
        return '"' + self._reader.default_lang_code() + '"'

    @property
    def multi_langs_properties(self) -> str:
        outs = []
        for field, note in self._reader.field_notes().items():
            out = ''
            out += self._templater.spaces(1) + '/**\n'
            out += self._templater.spaces(1) + ' * {}\n'.format(
                note
            )
            out += self._templater.spaces(1) + ' */\n'
            out += self._templater.spaces(1) + 'get {}()'.format(
                field) + ' {\n'
            out += self._templater.spaces(2) + 'return target.{}\n'.format(
                field)
            out += self._templater.spaces(1) + '}'
            outs.append(out)
        return '\n'.join(outs)
