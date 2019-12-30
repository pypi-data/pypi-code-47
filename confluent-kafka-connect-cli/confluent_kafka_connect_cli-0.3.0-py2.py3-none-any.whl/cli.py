"""Console script for confluent_kafka_connect_cli."""
import confluent_kafka_connect_cli.call as call
import click
import json


def pprint(data):
    print(json.dumps(data, indent=4, sort_keys=True))


@click.group()
@click.version_option()
@click.option("--host", help="The kafka connector host.", default="localhost")
@click.option("--port", help="The kafka connector port.", default="8083")
@click.pass_context
def connector(ctx, host, port):
    ctx.obj['baseurl'] = 'http://{host}:{port}'.format(host=host, port=port)


@connector.command()
@click.pass_context
def status(ctx):
    pprint(call.status(ctx.obj['baseurl']))


@connector.command()
@click.pass_context
def config(ctx):
    pprint(call.config(ctx.obj['baseurl']))


@connector.command()
@click.option("--config", help="The kafka connector config file.")
@click.pass_context
def create(ctx, config):
    pprint(call.create(ctx.obj['baseurl'], config))


@connector.command()
@click.pass_context
def delete(ctx):
    pprint(call.delete(ctx.obj['baseurl']))


@connector.command()
@click.pass_context
def restart(ctx):
    pprint(call.restart(ctx.obj['baseurl']))


@connector.command()
@click.pass_context
def restart_tasks(ctx):
    pprint(call.restart_tasks(ctx.obj['baseurl']))


@connector.command()
@click.pass_context
def pause(ctx):
    pprint(call.pause(ctx.obj['baseurl']))


@connector.command()
@click.pass_context
def resume(ctx):
    pprint(call.resume(ctx.obj['baseurl']))


def main():
    return connector(obj={})


if __name__ == '__main__':
    connector(obj={})
