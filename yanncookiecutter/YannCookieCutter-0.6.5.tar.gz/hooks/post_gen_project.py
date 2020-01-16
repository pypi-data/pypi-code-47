import os
import shutil


print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}

def remove(filepath):
    if not os.path.exists(filepath):
        return

    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

command_line_interface = 'y' in '{{cookiecutter.command_line_interface}}'

if not command_line_interface:
    # remove relative file nested inside the generated folder
    remove(os.path.join('{{cookiecutter.project_name}}', 'cli.py'))
    