import json

from flask import Flask, request

from .addon import BasicAddon, RepositoryAddon
from .common import logger
from .context import Context
from .router import create_blueprint
from .test import test_addons
from .views import render


def _parse(args):
    req = {}
    for arg in args:
        key, value = arg.split('=', 1)
        try:
            value = json.loads(value)
            value = str(value)
        except Exception:
            pass
        req[key] = value
    return req


def _start(addons, *args):
    app = Flask(__name__)

    blueprints = {}

    @app.route('/', methods=['GET'])
    def root():
        if request.args.get('wtchDiscover'):
            response = {
                'watched': 'index',
                'addons': [addon.id for addon in addons]
            }
            return json.dumps(response), 200, {'content-type': 'application/json'}

        return render(addons)

    @app.route('/health', methods=['GET'])
    def health():
        return 'OK'

    for addon in addons:
        path = f'/{addon.id}'
        logger.info('Mounting %s (%s) on %s',
                    addon.id, addon.type, path)
        if addon.id not in blueprints:
            blueprints[addon.id] = create_blueprint(addon)
        app.register_blueprint(blueprints[addon.id], url_prefix=path)

    app.run('0.0.0.0', 3000, debug=True if 'debug' in args else False)


def _call(addons, *args):
    data = _parse(args)

    addon_id = data.pop('addon_id', None)
    if addon_id:
        addons = [a for a in addons if a.id == addon_id]
    if not addons:
        raise ValueError(f'Addon "{addon_id}" not found')
    addon = addons[0]

    action = data.pop('action', 'addon')
    ctx = Context(addon, action)
    response = ctx.run(data)
    print(json.dumps(response, indent=2))


def main(addons, *args):
    """The main function of the WATCHED SDK.
    - `call`: Test your addon on the command line.
    - `test`: Run automatic tests on your addons.
    - `start`: Starts a HTTP server on port 3000.
    - `start debug`: Starts a HTTP server on port
      3000 with debug options enabled (automatic
      reloading etc.)
    """
    try:
        cmd = args[0]
    except IndexError:
        cmd = None

    if cmd == 'start':
        _start(addons, *args[1:])
    elif cmd == 'call':
        _call(addons, *args[1:])
    elif cmd == 'test':
        test_addons(addons, *args[1:])
    else:
        raise ValueError('Usage: watched_sdk <start|call|test> [...]')
