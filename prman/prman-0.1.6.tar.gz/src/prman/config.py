# pylint: disable=unused-wildcard-import
import os
import jstyleson
import sys
from .cli.colorized_print import *


def read_json_file(file_path):
  with open(file_path, 'r') as file:
    file_content = file.read()
  return jstyleson.loads(file_content)


def write_json_file(file_path, config):
  with open(file_path, 'w') as file:
    file.write(config)


def get_config_pathes():
  script_dir = os.path.dirname(os.path.abspath(__file__))
  config_base_path = os.path.join(script_dir, 'config.base.jsonc')

  # because of __main__ hack
  if not os.path.exists(config_base_path):
    script_dir = os.path.dirname(script_dir)
    config_base_path = os.path.join(script_dir, 'config.base.jsonc')

  app_config_dir = os.path.expanduser('~/.config/prman')
  if not os.path.exists(app_config_dir):
    os.mkdir(app_config_dir)
  config_path = os.path.join(app_config_dir, 'config.json')

  return (config_base_path, config_path)


def add_config_kvp(key, value):
  config_base_path, config_path = get_config_pathes()
  config_base = read_json_file(config_base_path)
  if not key in config_base.keys() and key != 'gitlab.token':
    print_red(f'Unknown config key \'{key}\'.')
    sys.exit(1)
  config = read_json_file(config_path) if os.path.exists(config_path) else { }
  config[key] = value
  config_json = jstyleson.dumps(config, indent=2)

  write_json_file(config_path, config_json)


def read_config():
  config_base_path, config_path = get_config_pathes()
  config_base = read_json_file(config_base_path)
  config = read_json_file(config_path) if os.path.exists(config_path) else { }

  for key in config_base.keys():
    config[key] = config.get(key, config_base[key])

  if config.get('gitlab.token', None) is None:
    print_red('Config gitlab.token is not specified. You can create one here https://gitlab.com/profile/personal_access_tokens')
    sys.exit(1)

  return config
