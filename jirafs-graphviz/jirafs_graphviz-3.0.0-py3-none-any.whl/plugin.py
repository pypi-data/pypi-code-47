import subprocess
import tempfile

from jirafs.plugin import (
    ImageMacroPlugin,
    PluginValidationError,
    PluginOperationError
)
from jirafs.types import JirafsMacroAttributes


class GraphvizMixin(object):
    def _get_command_args(
        self,
        input_filename,
        output_filename,
        command: str = 'dot',
        format: str = 'png'
    ):
        command = [
            command,
            '-T%s' % format,
            input_filename,
            '-o',
            output_filename,
        ]

        return command

    def _build_output(
        self,
        input_filename: str,
        output_filename: str,
        command: str = 'dot',
        format: str = 'png',
    ):
        proc = subprocess.Popen(
            self._get_command_args(
                input_filename,
                output_filename,
                command=command,
                format=format,
            ),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = proc.communicate()

        if proc.returncode:
            raise PluginOperationError(
                "%s encountered an error while compiling from %s to %s: %s" % (
                    self.entrypoint_name,
                    input_filename,
                    output_filename,
                    stderr.decode('utf-8'),
                )
            )

    def validate(self):
        try:
            subprocess.check_call(
                [
                    'dot',
                    '-V',
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except (subprocess.CalledProcessError, IOError, OSError):
            raise PluginValidationError(
                "%s requires graphviz (dot) to be installed." % (
                    self.plugin_name,
                )
            )


class Graphviz(GraphvizMixin, ImageMacroPlugin):
    """ Converts .dot files into PNG images using Graphviz for JIRA."""
    MIN_VERSION = '2.0.0'
    MAX_VERSION = '3.0.0'
    TAG_NAME = 'graphviz'

    def get_extension_and_image_data(self, data: str, attrs: JirafsMacroAttributes):
        command = attrs.get('command', 'dot')
        format = attrs.get('format', 'png')

        with tempfile.NamedTemporaryFile('w') as inf:
            inf.write(data)
            inf.flush()

            with tempfile.NamedTemporaryFile('wb+') as outf:
                self._build_output(
                    inf.name,
                    outf.name,
                    command=command,
                    format=format,
                )

                outf.seek(0)
                return format, outf.read()
