import json

import click

from boiler import cli
from boiler.commands.video import video_from_string
from boiler.models import summarize_activities
from boiler.serialization import denseobj, kpf as serialization
from boiler.validate import validate_activities


@click.group(name='kpf', short_help='Ingest and validate kpf')
@click.pass_obj
def kpf(ctx):
    pass


@kpf.command(name='validate', help='locally validate kpf')
@click.option('--types', type=click.File(mode='r'), help='path to types.yml')
@click.option('--geom', type=click.File(mode='r'), help='path to geom.yml')
@click.option('--activities', type=click.File(mode='r'), help='path to activities.yml')
def validate(types, geom, activities):
    actor_map = {}
    activity_map = {}
    if types:
        serialization.deserialize_types(types, actor_map)
    if activities:
        serialization.deserialize_activities(activities, activity_map, actor_map)
    if geom:
        serialization.deserialize_geom(geom, actor_map)
    errors = validate_activities(activity_map.values())
    summary = summarize_activities(activity_map.values())
    click.echo(
        message=json.dumps(
            {'errors': denseobj.serialize_validation_errors(errors), 'summary': summary,}
        )
    )


@kpf.command(name='ingest', help='push kpf to stumpf')
@click.option('--types', type=click.File(mode='r'), help='path to types.yml', required=True)
@click.option('--geom', type=click.File(mode='r'), help='path to geom.yml', required=True)
@click.option(
    '--activities', type=click.File(mode='r'), help='path to activities.yml', required=True,
)
@click.option('--video-name', type=click.STRING, help='video name in stumpf', required=True)
@click.pass_obj
def loadkpf(ctx, types, geom, activities, video_name):
    actor_map = {}
    activity_map = {}

    try:
        video_from_string(video_name)
    except ValueError as err:
        click.echo(
            message=json.dumps(
                {
                    'error': [str(err)],
                    'context': 'encountered video name parse error. ingest aborted.',
                }
            )
        )
        exit(1)

    serialization.deserialize_types(types, actor_map)
    serialization.deserialize_activities(activities, activity_map, actor_map)
    serialization.deserialize_geom(geom, actor_map)
    errors = validate_activities(activity_map.values())

    if len(errors) > 0:
        click.echo(
            message=json.dumps(
                {
                    'error': denseobj.serialize_validation_errors(errors),
                    'context': 'encountered validation errors:  ingest aborted.',
                }
            )
        )
        exit(1)


cli.add_command(kpf)
