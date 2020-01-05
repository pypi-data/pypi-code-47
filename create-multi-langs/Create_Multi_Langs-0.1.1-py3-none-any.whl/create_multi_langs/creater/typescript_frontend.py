from __future__ import absolute_import
from create_multi_langs.creater.base import CreaterBase


class CreaterTypeScriptFrontEnd(CreaterBase):

    @staticmethod
    def from_csv_file(csv_file: str,
                      output_code_file: str,
                      naming_rule='lcc',
                      sep=','):
        assert output_code_file.endswith(".ts"), \
            "typescript filename must ends with .ts"
        creater = CreaterTypeScriptFrontEnd(
            csv_file,
            output_code_file,
            template_path="data/typescript/template_frontend.tmpl",
            naming_rule=naming_rule,
            sep=sep,
        )
        return creater

    @property
    def lang_data_define(self) -> str:
        data = {}
        for field in self._reader.fields():
            data[field] = "string"
        return self._templater.key_value_lines(
            key_values=data,
            double_quote_key=False,
            double_quote_value=False,
            split_punctuation=": ",
            end_punctuation="",
            n_indent=1,
        )

    @property
    def lang_code_define(self) -> str:
        return ' | '.join(
            ['"' + code + '"' for code in self._reader.lang_codes()])

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
                field) + ': string {\n'
            out += self._templater.spaces(2) + 'return target.{}\n'.format(
                field)
            out += self._templater.spaces(1) + '}'
            outs.append(out)
        return '\n'.join(outs)
