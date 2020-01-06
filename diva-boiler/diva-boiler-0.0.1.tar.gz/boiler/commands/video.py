import csv
import datetime
import json
import re

import click

from boiler import cli, handle_request_error
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
    return (
        result.group('gtag').lower(),
        result.group('location').lower(),
        result.group('begin'),
        result.group('end'),
        result.group('date'),
    )


def make_video_payload(**kwargs) -> dict:
    local_path = kwargs.get('local_path')
    s3_path = kwargs.get('s3_path')
    if bool(local_path) == bool(s3_path):
        raise ValueError('either local_path XOR s3_path should be specified')

    frame_rate = kwargs.get('frame_rate')
    duration = kwargs.get('duration')
    width = kwargs.get('width')
    height = kwargs.get('height')
    if s3_path and any([not v for v in [frame_rate, duration, width, height]]):
        raise ValueError(
            (
                'if s3_path is specified, all post-transcoding fields'
                '(width, height, frame_rate, duration) must be set'
            )
        )

    try:
        gtag, location, start_time, end_time, date = video_from_string(local_path or s3_path)
    except (ValueError, TypeError):
        try:
            gtag, location, start_time, end_time, date = video_from_string(kwargs.get('name'))
        except (ValueError, TypeError):
            gtag, location, start_time, end_time, date = (None, None, None, None, None)

    date = kwargs.get('date') or date
    start_time = kwargs.get('start_time') or start_time
    end_time = kwargs.get('end_time') or end_time
    gtag = kwargs.get('gtag') or gtag
    location = kwargs.get('location') or location
    if not date:
        raise ValueError('date is required')
    if not start_time:
        raise ValueError('start_time is required')
    if not end_time:
        raise ValueError('end_time is required')

    time_format = r'%Y-%m-%d %H-%M-%S'
    start_datetime = datetime.datetime.strptime(f'{date} {start_time}', time_format)
    end_datetime = datetime.datetime.strptime(f'{date} {end_time}', time_format)
    name = kwargs.get('name') or f'{date}.{start_time}.{end_time}.{location}.{gtag}'.lower()
    if any([ext in name for ext in ['.mp4', '.avi', '.mov', '.webm', '.wmv']]):
        raise ValueError(f'{name} should not contain file extension')
    return {
        'name': name,
        'path': kwargs.get('s3_path'),
        'gtag': gtag.lower(),
        'location': location,
        'start_time': str(start_datetime),
        'end_time': str(end_datetime),
        'frame_rate': kwargs.get('frame_rate'),
        'duration': kwargs.get('duration'),
        'width': kwargs.get('width'),
        'height': kwargs.get('height'),
        'data_collect': kwargs.get('data_collect'),
        'set_name': kwargs.get('set_name'),
        'release_batch': kwargs.get('release_batch'),
        'camera_type': kwargs.get('camera_type'),
        'scenario': kwargs.get('scenario'),
    }


@click.group(name='video', short_help='ingest and query video')
@click.pass_obj
def video(ctx):
    pass


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
        local_path = p.get('local_path')

        out, r = handle_request_error(lambda: ctx['session'].post('video', json=p))

        if r.ok:
            v = out['response']
            successes.append(v)
            click.echo(f'id={v["id"]} created for id={p["name"]}', err=True)

            if local_path:
                click.echo(f'sending name{p["name"]} id={v["id"]} to S3')
                # TODO: upload to s3
        else:
            failures.append(out)
            click.echo(f'name={p["name"]} creation failed', err=True)

    click.echo(json.dumps({'failures': failures, 'successes': successes}))
    if len(failures):
        exit(1)


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
    out, _ = handle_request_error(lambda: ctx['session'].get('video', params=data))
    click.echo(json.dumps(out))
    if out.get('error'):
        exit(1)


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
@click.option('--date', type=click.STRING, default=datetime.date.today().strftime(r'%Y-%m-%d'))
@click.option('--frame-rate', type=click.FLOAT)
@click.option('--duration', type=click.FLOAT)
@click.option('--width', type=click.INT)
@click.option('--height', type=click.INT)
@click.option(
    '--data-collect',
    type=click.Choice([e.value for e in DataCollects]),
    default=DataCollects.M1.value,
)
@click.option('--set-name', type=click.STRING, default='')
@click.option(
    '--release-batch',
    type=click.Choice([e.value for e in ReleaseBatches]),
    default=ReleaseBatches.TESTING.value,
)
@click.option(
    '--camera-type',
    type=click.Choice([e.value for e in CameraTypes]),
    default=CameraTypes.VISIBLE.value,
)
@click.option('--scenario', type=click.STRING, default='')
@click.pass_obj
def add(ctx, **kwargs):
    try:
        data = make_video_payload(**kwargs)
    except ValueError as err:
        click.echo(
            json.dumps(
                {'error': str(err), 'context': 'failed to construct valid payload for video',}
            )
        )
        exit(1)
    out, _ = handle_request_error(lambda: ctx['session'].post('video', json=data))
    # TODO: send to S3
    click.echo(json.dumps(out))
    if out.get('error'):
        exit(1)


cli.add_command(video)
