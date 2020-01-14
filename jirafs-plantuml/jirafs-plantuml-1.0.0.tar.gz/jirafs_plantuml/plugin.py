import os
import subprocess

from jirafs.plugin import (
    ImageMacroPlugin,
    PluginValidationError,
    PluginOperationError
)
from jirafs.types import JirafsMacroAttributes


class PlantUMLMixin(object):
    def _get_command_args(self):
        config = self.get_configuration()

        command = [
            'java',
            '-jar',
            config['bin'],
            '-pipe'
        ]

        return command

    def _build_output(self, data: str):
        proc = subprocess.Popen(
            self._get_command_args(),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = proc.communicate(data.encode('utf-8'))

        if proc.returncode:
            raise PluginOperationError(
                "%s encountered an error while compiling plantuml diagram: %s" % (
                    self.entrypoint_name,
                    stderr.decode('utf-8'),
                )
            )

        return stdout

    def validate(self):
        config = self.get_configuration()

        if 'bin' not in config:
            raise PluginValidationError(
                "Path to plantuml.jar must be set; please set your path "
                "to plantuml.jar by running `jirafs config --global --set "
                "plantuml.bin /path/to/plantuml.jar"
            )

        if not os.path.exists(config['bin']):
            raise PluginValidationError(
                "%s requires plantuml.jar to be installed." % (
                    self.entrypoint_name,
                )
            )


class PlantUML(PlantUMLMixin, ImageMacroPlugin):
    """ Converts .dot files into PNG images using Graphviz for JIRA."""
    MIN_VERSION = '2.0.0'
    MAX_VERSION = '3.0.0'
    TAG_NAME = 'plantuml'

    def get_extension_and_image_data(self, data: str, attrs: JirafsMacroAttributes):
        result = self._build_output(data)

        return 'png', result
