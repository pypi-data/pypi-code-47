import json
import os
from typing import Callable, Tuple

import click
from requests import exceptions, Response
from requests_toolbelt.sessions import BaseUrlSession


class BoilerSession(BaseUrlSession):

    page_size = 50

    def __init__(self, base_url):
        super(BoilerSession, self).__init__(base_url=base_url)
        self.headers.update(
            {
                'User-agent': 'boiler',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'X-Stumpf-Token': os.getenv('X_STUMPF_TOKEN'),
            }
        )


@click.group()
@click.option('--api-url', default='http://localhost:5000/api/diva/', envvar='STUMPF_API_URL')
@click.version_option()
@click.pass_context
def cli(ctx, api_url):
    session = BoilerSession(api_url)
    ctx.obj = {'session': session}


def handle_request_error(func: Callable) -> Tuple[dict, Response]:
    try:
        r = func()
        if not r.ok:
            error_text = r.text
            try:
                error_text = r.json()
            except ValueError:
                pass

            del r.request.headers['X-Stumpf-Token']
            return (
                {
                    'context': {
                        'url': r.url,
                        'method': r.request.method,
                        'status': r.status_code,
                        'body': str(r.request.body),
                        'headers': str(r.request.headers),
                    },
                    'error': error_text,
                },
                r,
            )
        return ({'response': r.json()}, r)
    except exceptions.ConnectionError as err:
        return ({'context': 'request to stumpf failed', 'error': str(err)}, r)


def exit_with(out: dict):
    click.echo(json.dumps(out))
    if out.get('error'):
        exit(1)
    exit(0)


from boiler.commands.kpf import kpf  # noqa: F401 E402
from boiler.commands.vendor import vendor  # noqa: F401 E402
from boiler.commands.video import video  # noqa: F401 E402
