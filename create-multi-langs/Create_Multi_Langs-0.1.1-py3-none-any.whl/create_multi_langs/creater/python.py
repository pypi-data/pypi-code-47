from __future__ import absolute_import
from create_multi_langs.creater.base import CreaterBase
from . import to_upper


class CreaterPython(CreaterBase):

    @staticmethod
    def from_csv_file(csv_file: str,
                      output_code_file: str,
                      naming_rule='lower',
                      sep=','):
        assert output_code_file.endswith(".py"), \
            "python filename must ends with .py"
        creater = CreaterPython(
            csv_file,
            output_code_file,
            template_path="data/python/template.tmpl",
            naming_rule=naming_rule,
            sep=sep,
        )
        return creater

    @property
    def dict_contents(self) -> str:
        outs = []
        for lang_code in self._reader.lang_codes():
            out = ""
            out += self._templater.spaces(1) + '"' + lang_code + '"' + ': {\n'
            out += self._templater.key_value_lines(
                key_values=self._reader.field_values(lang_code),
                double_quote_key=True,
                double_quote_value=True,
                split_punctuation=": ",
                end_punctuation=",",
                n_indent=2,
            )
            out += "\n" + self._templater.spaces(1) + "},"
            outs.append(out)
        return '\n'.join(outs)

    @property
    def lang_code_constants(self) -> str:
        data = {}
        for lang_code in self._reader.lang_codes():
            data[to_upper(lang_code)] = lang_code
        return self._templater.key_value_lines(
            key_values=data,
            double_quote_key=False,
            double_quote_value=True,
            split_punctuation=" = ",
            end_punctuation="",
        )

    @property
    def valid_lang_codes(self) -> str:
        data = {}
        for lang_code in self._reader.lang_codes():
            data['- "{}"'.format(lang_code)] = ""
        return self._templater.key_value_lines(
            key_values=data,
            double_quote_key=False,
            double_quote_value=False,
            split_punctuation="",
            end_punctuation="",
            n_indent=2,
        )

    @property
    def properties(self) -> str:
        outs = []
        for field, note in self._reader.field_notes().items():
            out = ""
            out += self._templater.spaces(1) + "@property\n"
            out += self._templater.spaces(1) + "def {}(self):\n".format(field)
            out += self._templater.spaces(2) + '"' * 3 + note + '"' * 3 + '\n'
            out += self._templater.spaces(2) + \
                'return self._data["{}"]'.format(field)
            outs.append(out)
        return '\n\n'.join(outs) + '\n'
