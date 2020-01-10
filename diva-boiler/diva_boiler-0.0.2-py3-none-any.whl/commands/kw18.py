import click

from boiler import cli
from boiler.commands.utils import exit_with, summarize_activities
from boiler.serialization import denseobj, kw18 as serialization, serializers
from boiler.validate import validate_activities


@click.group(name='kw18', short_help='Ingest and validate kw18')
@click.pass_obj
def kw18(ctx):
    pass


@kw18.command(name='load', help='interact locally with the kw18 format')
@click.option('--types', type=click.File(mode='r'), help='path to .kw18.types file')
@click.option('--kw18', type=click.File(mode='r'), help='path to .kw18 geometry file')
@click.option('--txt', type=click.File(mode='r'), help='path to .txt activity definitions')
@click.option('--validate', is_flag=True, help='run static integrity checks')
@click.option('--prune', is_flag=True, help='prune interpolated detections before validation')
@click.option(
    '--convert',
    nargs=2,
    type=click.Tuple(
        [
            click.Choice(serializers.keys()),
            click.Path(
                exists=False, file_okay=True, dir_okay=False, writable=True, resolve_path=True
            ),
        ]
    ),
    default=(None, None),
    help='convert to another serialization',
)
def load(types, kw18, txt, validate, prune, convert):
    actor_map = {}
    activity_map = {}

    if types:
        serialization.deserialize_types(types, actor_map)
    if txt:
        serialization.deserialize_activities(txt, activity_map, actor_map)
    if kw18:
        serialization.deserialize_geom(kw18, actor_map)

    if prune:
        [a.prune() for a in activity_map.values()]

    output = {'summary': summarize_activities(activity_map.values())}

    if validate:
        errors = validate_activities(activity_map.values())
        output['error'] = denseobj.serialize_validation_errors(errors)

    serialization_type = convert[0]
    base_path = convert[1]
    if serialization_type and base_path:
        serializer = serializers.get(serialization_type)
        serializer.serialize_to_files(
            base_path, activity_map.values(), actor_map.values(), keyframes_only=prune
        )

    exit_with(output)


cli.add_command(kw18)
