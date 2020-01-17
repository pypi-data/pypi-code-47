from distutils.version import StrictVersion
import sys

import click
import requests
from requests.exceptions import RequestException
from requests_toolbelt.sessions import BaseUrlSession

__version__ = '0.0.3'


class BoilerSession(BaseUrlSession):

    page_size = 50

    def __init__(self, base_url, token):
        super(BoilerSession, self).__init__(base_url=base_url)
        self.token = token
        self.headers.update(
            {
                'User-agent': f'boiler/{__version__}',
                'Accept': 'application/json',
                'X-Stumpf-Token': self.token,
            }
        )


def newer_version_available():
    r = requests.get('https://pypi.org/pypi/diva-boiler/json', timeout=(5, 5))
    r.raise_for_status()
    releases = list(r.json()['releases'])
    return any(StrictVersion(r) > StrictVersion(__version__) for r in releases)


@click.group()
@click.option(
    '--api-url',
    default='https://stumpf-the-younger.avidannotations.com/api/diva/',
    envvar='STUMPF_API_URL',
)
@click.option('--x-stumpf-token', envvar='X_STUMPF_TOKEN')
@click.option('--offline', is_flag=True)
@click.version_option()
@click.pass_context
def cli(ctx, api_url, x_stumpf_token, offline):
    if not offline:
        try:
            if newer_version_available():
                click.echo(
                    click.style(
                        """There is a newer version of boiler available.
You must upgrade to the latest version before continuing.
If you are using pip, then you can upgrade by running the following command:
""",
                        fg='yellow',
                    ),
                    err=True,
                )
                click.echo(click.style('pip install --upgrade diva-boiler', fg='green'), err=True)
                sys.exit(1)
        except RequestException:
            click.echo(
                click.style('Failed to check for newer version of boiler:', fg='red'), err=True
            )
            raise

    session = BoilerSession(api_url, x_stumpf_token)
    ctx.obj = {'session': session}


from boiler.commands import activity  # noqa: F401 E402
from boiler.commands.kpf import kpf  # noqa: F401 E402
from boiler.commands.kw18 import kw18  # noqa: F401 E402
from boiler.commands.vendor import vendor  # noqa: F401 E402
from boiler.commands.video import video  # noqa: F401 E402
