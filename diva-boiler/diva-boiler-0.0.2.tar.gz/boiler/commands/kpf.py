import click

from boiler import cli
from boiler.commands.utils import (
    activity_types_from_file,
    exit_with,
    handle_request_error,
    sha1,
    summarize_activities,
)
from boiler.definitions import AnnotationVendors
from boiler.serialization import denseobj, kpf as serialization, serializers
from boiler.validate import validate_activities


@click.group(name='kpf', short_help='Ingest and validate kpf')
@click.pass_obj
def kpf(ctx):
    pass


@kpf.command(name='load', help='interact locally with the KPF format')
@click.option('--types', type=click.File(mode='rb'), help='path to types.yml')
@click.option('--geom', type=click.File(mode='rb'), help='path to geom.yml')
@click.option('--activities', type=click.File(mode='rb'), help='path to activities.yml')
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
def load(types, geom, activities, validate, prune, convert):
    actor_map = {}
    activity_map = {}
    if types:
        serialization.deserialize_types(types, actor_map)
    if activities:
        serialization.deserialize_activities(activities, activity_map, actor_map)
    if geom:
        serialization.deserialize_geom(geom, actor_map)
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


@kpf.command(name='ingest', help='push kpf to stumpf')
@click.option('--types', type=click.File(mode='rb'), help='path to types.yml', required=True)
@click.option('--geom', type=click.File(mode='rb'), help='path to geom.yml', required=True)
@click.option(
    '--activities', type=click.File(mode='rb'), help='path to activities.yml', required=True
)
@click.option('--video-name', type=click.STRING, help='video name in stumpf', required=True)
@click.option(
    '--vendor-name',
    type=click.Choice([e.value for e in AnnotationVendors]),
    help='vendor name in stumpf',
    required=True,
)
@click.option('--activity-type-list', type=click.File(mode='r'), required=True)
@click.pass_obj
def ingest(ctx, types, geom, activities, video_name, vendor_name, activity_type_list):
    actor_map = {}
    activity_map = {}
    activity_types = activity_types_from_file(activity_type_list)
    serialization.deserialize_types(types, actor_map)
    serialization.deserialize_activities(activities, activity_map, actor_map)
    serialization.deserialize_geom(geom, actor_map)
    errors = validate_activities(activity_map.values())

    if len(errors) > 0:
        exit_with(
            {
                'validation_errors': denseobj.serialize_validation_errors(errors),
                'context': 'encountered validation errors:  ingest aborted.',
            }
        )

    files = {
        'geom': {'file': geom, 'model': None},
        'types': {'file': types, 'model': None},
        'activities': {'file': activities, 'model': None},
    }

    for f in files.values():
        f['file'].seek(0, 0)  # reset reader position after local deserialization
        payload = {'file': f['file']}
        r = ctx['session'].post('upload', files=payload)
        resp = handle_request_error(r)
        if r.status_code == 201:
            f['model'] = resp['response']
        elif r.status_code == 409:
            payload = {'sha1': sha1(f['file'])}
            r = ctx['session'].get('upload', params=payload)
            resp = handle_request_error(r)
            if r.ok:
                f['model'] = resp['response']
            else:
                exit_with(resp)
        else:
            exit_with(resp)

    data = {
        'video_name': video_name,
        'vendor_name': vendor_name,
        'kpf_geom_id': files['geom']['model']['id'],
        'kpf_types_id': files['types']['model']['id'],
        'kpf_activities_id': files['activities']['model']['id'],
        'activity_types': activity_types,
    }
    r = ctx['session'].post('video-pipeline/audit', json=data)
    exit_with(handle_request_error(r))


cli.add_command(kpf)
