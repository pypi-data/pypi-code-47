import click
from requests_toolbelt.sessions import BaseUrlSession


class BoilerSession(BaseUrlSession):

    page_size = 50

    def __init__(self, base_url, token):
        super(BoilerSession, self).__init__(base_url=base_url)
        self.token = token
        self.headers.update(
            {'User-agent': 'boiler', 'Accept': 'application/json', 'X-Stumpf-Token': self.token,}
        )


@click.group()
@click.option(
    '--api-url',
    default='https://stumpf-the-younger.avidannotations.com/api/diva/',
    envvar='STUMPF_API_URL',
)
@click.option('--x-stumpf-token', envvar='X_STUMPF_TOKEN')
@click.version_option()
@click.pass_context
def cli(ctx, api_url, x_stumpf_token):
    session = BoilerSession(api_url, x_stumpf_token)
    ctx.obj = {'session': session}


from boiler.commands import activity  # noqa: F401 E402
from boiler.commands.kpf import kpf  # noqa: F401 E402
from boiler.commands.kw18 import kw18  # noqa: F401 E402
from boiler.commands.vendor import vendor  # noqa: F401 E402
from boiler.commands.video import video  # noqa: F401 E402
