import os
import subprocess
import webbrowser
import click
import ast


class PythonLiteralOption(click.Option):

    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except:
            raise click.BadParameter(value)


def get_user_dir():
    return subprocess.check_output(['pwd'], shell=True).decode().rstrip()


def get_project_name():
    return os.path.basename(get_user_dir())


def open_window(port):
    path = f'http://localhost:{port}'
    webbrowser.open(path, new=2)


def init_environment(environment_init_path, version):
    write_path = os.path.join(get_user_dir(), 'environment.yml')

    if os.path.exists(write_path):
        click.echo('Environment already exists.')
    else:
        with open(environment_init_path, 'r') as r:
            data = r.read()

        data = data.replace('{{name}}', get_project_name())
        data = data.replace('{{version}}', version)

        with open(write_path, 'w') as w:
            w.write(data)


def check_output(args):
    return subprocess.check_output(args).decode().rstrip()


def call(args):
    subprocess.call(args)
