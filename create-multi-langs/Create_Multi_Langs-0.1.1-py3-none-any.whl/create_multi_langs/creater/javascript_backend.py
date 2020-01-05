from __future__ import absolute_import
from create_multi_langs.creater.javascript_frontend import CreaterJavaScriptFrontEnd  # noqa: E501


class CreaterJavaScriptBackEnd(CreaterJavaScriptFrontEnd):

    @staticmethod
    def from_csv_file(csv_file: str,
                      output_code_file: str,
                      naming_rule='lcc',
                      sep=','):
        assert output_code_file.endswith((".js", ".mjs")), \
            "javascript filename must ends with .js or .mjs"
        creater = CreaterJavaScriptBackEnd(
            csv_file,
            output_code_file,
            template_path="data/javascript/template_backend.tmpl",
            naming_rule=naming_rule,
            sep=sep,
        )
        return creater

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
            out += self._templater.spaces(2) + 'return this.data.{}\n'.format(
                field)
            out += self._templater.spaces(1) + '}'
            outs.append(out)
        return '\n'.join(outs)
