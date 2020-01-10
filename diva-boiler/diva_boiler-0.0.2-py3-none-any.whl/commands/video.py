import csv
import datetime
import inspect
import re

import click

from boiler import BoilerSession, cli
from boiler.commands.utils import exit_with, handle_request_error
from boiler.definitions import CameraLocation, CameraTypes, DataCollects, ReleaseBatches


def video_from_string(string: str):
    pattern = ''.join(
        [
            r'(?P<date>\d{4}-\d{2}-\d{2})',
            r'[._]+(?P<begin>\d{2}-\d{2}-\d{2})',
            r'[._]+(?P<end>\d{2}-\d{2}-\d{2})',
            '[._]+(?P<location>({}))'.format('|'.join([l.value for l in CameraLocation])),
            r'[._]+(?P<gtag>[g]\d{3})',
        ]
    )
    result = re.search(pattern, string, re.IGNORECASE)
    if result is None:
        raise ValueError(f'{string} is not a valid Video name')
    return {
        'gtag': result.group('gtag').lower(),
        'location': result.group('location').lower(),
        'start_time': result.group('begin'),
        'end_time': result.group('end'),
        'date': result.group('date'),
    }


# This function should take exactly the arguments collected from the user
# and no others.  Its method signature will be used to generate a header template
# for bulk video ingestion.
def make_video_payload(
    name=None,
    local_path=None,
    s3_path=None,
    frame_rate=None,
    duration=None,
    width=None,
    height=None,
    date=None,
    start_time=None,
    end_time=None,
    gtag=None,
    location=None,
    data_collect=None,
    set_name=None,
    release_batch=None,
    camera_type=None,
    scenario=None,
) -> dict:
    if bool(local_path) == bool(s3_path):
        raise ValueError('either local_path XOR s3_path should be specified')

    if s3_path and any([not v for v in [frame_rate, duration, width, height]]):
        raise ValueError(
            (
                'if s3_path is specified, all post-transcoding fields'
                '(width, height, frame_rate, duration) must be set'
            )
        )

    try:
        parsed_meta = video_from_string(local_path or s3_path)
    except (ValueError, TypeError):
        try:
            parsed_meta = video_from_string(name)
        except (ValueError, TypeError):
            parsed_meta = {}

    date = date or parsed_meta.get('date')
    start_time = start_time or parsed_meta.get('start_time')
    end_time = end_time or parsed_meta.get('end_time')
    gtag = gtag or parsed_meta.get('gtag')
    location = location or parsed_meta.get('location')
    if not date:
        raise ValueError('date is required')
    if not start_time:
        raise ValueError('start_time is required')
    if not end_time:
        raise ValueError('end_time is required')

    time_format = r'%Y-%m-%d %H-%M-%S'
    start_datetime = datetime.datetime.strptime(f'{date} {start_time}', time_format)
    end_datetime = datetime.datetime.strptime(f'{date} {end_time}', time_format)
    name = name or f'{date}.{start_time}.{end_time}.{location}.{gtag}'.lower()
    if any([ext in name for ext in ['.mp4', '.avi', '.mov', '.webm', '.wmv']]):
        raise ValueError(f'{name} should not contain file extension')

    return {
        'name': name.lower(),
        'path': s3_path,
        'gtag': gtag.lower(),
        'location': location,
        'start_time': str(start_datetime),
        'end_time': str(end_datetime),
        'frame_rate': frame_rate,
        'duration': duration,
        'width': width,
        'height': height,
        'data_collect': data_collect,
        'set_name': set_name,
        'release_batch': release_batch,
        'camera_type': camera_type,
        'scenario': scenario,
    }


def ingest_video(payload: dict, session: BoilerSession):
    p = payload
    local_path = p.get('local_path')
    r = session.post('video', json=p)
    out = handle_request_error(r)

    if r.ok:
        v = out['response']
        click.echo(f'id={v["id"]} created for id={p["name"]}', err=True)

        if local_path:
            click.echo(f'sending name={p["name"]} id={v["id"]} to S3')
            # TODO: upload to s3
            return out
        else:
            return out

    elif r.status_code == 409:
        query = {'name': p['name']}
        existing_r = session.get('video', params=query)
        existing_video = handle_request_error(existing_r)
        if existing_r.ok:
            v = existing_video['response'][0]  # there should be 1 result
            click.echo(f'id={v["id"]} already exists for name={p["name"]}', err=True)

            if local_path:
                click.echo(f'sending name={p["name"]} id={v["id"]} to S3')
                # TODO: upload to s3
                return out
            else:
                # return object that will match POST 201 response
                return {'response': v}
        else:
            click.echo(f'name={p["name"]} creation failed', err=True)
            return existing_video
    else:
        click.echo(f'name={p["name"]} creation failed', err=True)
        return out


@click.group(name='video', short_help='ingest and query video')
@click.pass_obj
def video(ctx):
    pass


@video.command(name='get-bulk-csv-header')
def make_header():
    click.echo(','.join(inspect.getfullargspec(make_video_payload).args))


@video.command(name='bulk-ingest', help='ingest videos from CSV file')
@click.option('--file', type=click.File(mode='r'), required=True, help='csv file')
@click.pass_obj
def bulk_ingest(ctx, file):
    reader = csv.DictReader(file)
    payloads = []
    successes = []
    failures = []
    for row in reader:
        try:
            payloads.append(make_video_payload(**row))
        except ValueError as err:
            failures.append(
                {'error': str(err), 'context': f'Failed to construct valid payload for video',}
            )
            click.echo(str(err), err=True)
    for p in payloads:
        result = ingest_video(p, ctx['session'])
        if 'error' in result:
            failures.append(result)
        else:
            successes.append(result)

    exit_with({'error': failures, 'response': successes})


@video.command(name='search', help='search for video')
@click.option('--name', type=click.STRING)
@click.option('--gtag', type=click.STRING)
@click.option('--location', type=click.Choice([e.value for e in CameraLocation]))
@click.option('--frame-rate', type=click.FLOAT, default=29.99)
@click.option('--duration', type=click.FLOAT, default=300.0)
@click.option('--width', type=click.INT, default=1920)
@click.option('--height', type=click.INT, default=1080)
@click.pass_obj
def search(ctx, **kwargs):
    data = {}
    for key, value in kwargs.items():
        if value is not None:
            data[key] = value
    r = ctx['session'].get('video', params=data)
    exit_with(handle_request_error(r))


@video.command(name='add', help='ingest video into stumpf from file')
@click.option(
    '--local-path', type=click.Path(exists=True, dir_okay=False, resolve_path=True),
)
@click.option('--s3-path', type=click.STRING)
@click.option('--name', type=click.STRING)
@click.option('--gtag', type=click.STRING)
@click.option('--location', type=click.Choice([e.value for e in CameraLocation]))
@click.option('--start-time', type=click.STRING)
@click.option('--end-time', type=click.STRING)
@click.option('--date', type=click.STRING)
@click.option('--frame-rate', type=click.FLOAT)
@click.option('--duration', type=click.FLOAT)
@click.option('--width', type=click.INT)
@click.option('--height', type=click.INT)
@click.option('--data-collect', type=click.Choice([e.value for e in DataCollects]))
@click.option('--set-name', type=click.STRING, default='')
@click.option('--release-batch', type=click.Choice([e.value for e in ReleaseBatches]))
@click.option('--camera-type', type=click.Choice([e.value for e in CameraTypes]))
@click.option('--scenario', type=click.STRING, default='')
@click.pass_obj
def add(ctx, **kwargs):
    try:
        data = make_video_payload(**kwargs)
    except ValueError as err:
        exit_with(
            {'error': str(err), 'context': 'failed to construct valid payload for video',}
        )
    exit_with(ingest_video(data, ctx['session']))


cli.add_command(video)
