"""Console script for partial_s3_to_es."""
import click
from dateutil.parser import parse
import re
import sys

from partial_s3_to_es import partial_s3_to_es

DT_TYPE = click.DateTime([
    '%Y-%m-%d',
    '%Y-%m-%d %H',
    '%Y-%m-%dT%H',
    '%Y-%m-%d %H:%M',
    '%Y-%m-%dT%H:%M',
    '%Y-%m-%d %H:%M:%S',
    '%Y-%m-%dT%H:%M:%S'
])
DT_PATTERN = re.compile(r"(\d+-\d+-\d+T\d+:\d+:\d+).*")


@click.command()
@click.option('-s', '--start', default=None, type=DT_TYPE)
@click.option('-e', '--end', default=None, type=DT_TYPE)
def main(args=None, start=None, end=None):
    """Console script for partial_s3_to_es.

    See click documentation at https://click.palletsprojects.com/
    """
    if start:
        start = start.replace(tzinfo=None)
    if end:
        end = end.replace(tzinfo=None)
    if start and end and start > end:
        raise click.UsageError(f"Start date {start} cannot be after end date {end}.")

    config = partial_s3_to_es.load_config()
    s3 = partial_s3_to_es.S3Client(config)
    reader = partial_s3_to_es.Reader(config)
    es = partial_s3_to_es.ESClient(config)

    es_body = []
    for filename in s3.get_s3_files():
        click.echo(f"Download {filename}")
        content = s3.download_file(filename)
        for data in reader.read(content):
            line_date = parse(data["timestamp"])
            line_date = line_date.replace(tzinfo=None)
            if start and line_date < start:
                continue
            if end and end < line_date:
                continue
            es_body.append({"index": {"_index": data["index"].lower()}})
            es_body.append({"data": data})

    click.echo("Sending to elasticsearch")
    es.bulk(es_body)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
