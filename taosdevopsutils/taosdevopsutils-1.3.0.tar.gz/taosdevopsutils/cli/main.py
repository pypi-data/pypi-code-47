import click
from taosdevopsutils.slack import Slack
from taosdevopsutils import config


@click.group()
@click.pass_context
def main(ctx):
    pass


@main.command("message")
@click.argument("target")
@click.argument("message")
@click.option(
    "--api-token",
    envvar=config.STRINGS.SLACK_API_TOKEN_ENV,
    default=config.SLACK_API_TOKEN,
)
def post_message(target, message, api_token):
    client = Slack(token=api_token)
    response = Slack(token=api_token).post_slack_message(target, message)
    click.echo(f"Response: {response['response']}")
    click.echo(f"StatusCode: {response['status_code']}")
