from __future__ import absolute_import
from create_multi_langs.creater.base import CreaterBase
import os
from subprocess import call
from typing import NoReturn
from . import to_upper_without_underscore


class CreaterGo(CreaterBase):

    @staticmethod
    def from_csv_file(csv_file: str,
                      output_code_file: str,
                      naming_rule='ucc',
                      sep=','):
        assert output_code_file.endswith(".go"), \
            "go filename must ends with .go"
        if naming_rule != "ucc":
            print('[WARNING] the naming rule: `{}` might conflict to go format'.format(naming_rule))  # noqa: E501
        creater = CreaterGo(
            csv_file,
            output_code_file,
            template_path="data/go/template.tmpl",
            naming_rule=naming_rule,
            sep=sep,
        )
        return creater

    @property
    def lang_data_define(self) -> str:
        return self._templater.key_value_lines(
            self._reader.field_notes(),
            double_quote_key=False,
            double_quote_value=False,
            split_punctuation=" string // ",
            end_punctuation="",
            n_indent=1,
        )

    @property
    def lang_code_contents(self) -> str:
        data = {}
        for lang_code in self._reader.lang_codes():
            data[to_upper_without_underscore(lang_code)] = lang_code
        return self._templater.key_value_lines(
            data,
            double_quote_key=False,
            double_quote_value=True,
            split_punctuation=" LangCode = ",
            end_punctuation="",
            n_indent=1,
        )

    @property
    def init_contents(self) -> str:
        lines = []
        for lang_code in self._reader.lang_codes():
            head = '{spaces}table[{lang_code}] = LangData'.format(
                spaces=self._templater.spaces(1),
                lang_code=to_upper_without_underscore(lang_code),
            ) + '{'
            lines.append(head)
            data = self._templater.key_value_lines(
                self._reader.field_values(lang_code),
                double_quote_key=False,
                double_quote_value=True,
                split_punctuation=": ",
                end_punctuation=",",
                n_indent=2,
            )
            lines.append(data)
            lines.append(self._templater.spaces(1) + '}')
        return '\n'.join(lines)

    @property
    def package_name(self) -> str:
        return os.path.splitext(os.path.basename(self._output))[0]

    def __call__(self) -> NoReturn:
        super().__call__()
        return_code = call(["gofmt", "-w", self._output])
        assert return_code == 0
