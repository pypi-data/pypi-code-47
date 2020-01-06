import click

from boiler import cli, exit_with, handle_request_error


@click.group(name='vendor', short_help='Manage annotation vendors')
@click.pass_obj
def vendor(ctx):
    pass


@vendor.command(name='search')
@click.pass_obj
def search(ctx, **kwargs):
    resp, _ = handle_request_error(lambda: ctx['session'].get('annotation-vendor'))
    exit_with(resp)


@vendor.command(name='dispatch')
@click.option('--name', type=click.STRING, required=True)
@click.option('--video-name', type=click.STRING, required=True)
@click.pass_obj
def dispatch(ctx, name, video_name):
    data = {'video_name': video_name, 'vendor_name': name}
    resp, _ = handle_request_error(
        lambda: ctx['session'].post('video-pipeline/annotate', json=data)
    )
    exit_with(resp)


cli.add_command(vendor)
