"""Main module."""

import boto3
from config import config
from elasticsearch import Elasticsearch
import gzip
import logging
import re
import tempfile


log = logging.getLogger(__name__)


def load_config(filename=None):
    configurations = (
        ("env", "S3_TO_ES"),
        ("ini", "s3_to_es.ini", True),
        ("yaml", "s3_to_es.yaml", True),
        ("yaml", "s3_to_es.yml", True),
        ("toml", "s3_to_es.toml", True),
    )
    default_config = {
        "s3.service_name": "s3",
        "s3.region_name": None,
        "s3.endpoint_url": None,
        "s3.aws_access_key_id": None,
        "s3.aws_secret_access_key": None,
        "s3.bucket": None,
        "log.pattern": r"(?P<timestamp>[^\t]+)\t(?P<index>[^\t]+)\t(?P<data>[^\s]+)",
    }
    if filename is None:
        cfg = config(
            *configurations,
            default_config,
            ignore_missing_paths=True,
            lowercase_keys=True
        )
    else:
        cfg = config(filename, default_config, lowercase_keys=True)
    return cfg.as_dict()


class S3Client:
    def __init__(self, cfg=None):
        if cfg is None:
            cfg = load_config()
        self.config = cfg
        self.session = boto3.session.Session()

    @property
    def client(self):
        return self.get_client()

    def get_client(self):
        return self.session.client(
            service_name=self.config["s3.service_name"],
            region_name=self.config["s3.region_name"],
            endpoint_url=self.config["s3.endpoint_url"],
            aws_access_key_id=self.config["s3.aws_access_key_id"],
            aws_secret_access_key=self.config["s3.aws_secret_access_key"],
        )

    def download_file(self, filename):
        with tempfile.TemporaryFile() as fp:
            self.client.download_fileobj(self.config["s3.bucket"], filename, fp)
            fp.seek(0)
            data = fp.read()
        if filename.endswith(".gz"):
            data = gzip.decompress(data)
        return data.decode()

    def get_s3_files(self):
        resp = self.list_objects()
        return [content["Key"] for content in resp["Contents"]]

    def list_objects(self):
        return self.client.list_objects(Bucket=self.config["s3.bucket"])


class Reader:
    def __init__(self, config=None):
        if config is None:
            config = load_config()
        self.config = config
        self.pattern = re.compile(config['log.pattern'])

    def read(self, content):
        for line in content.split('\n'):
            if not line:
                continue
            matches = self.pattern.match(line)
            if not matches:
                continue
            yield matches.groupdict()


class ESClient:
    def __init__(self, config=None):
        if config is None:
            config = load_config()
        self.config = config
        kwargs = {'hosts': config.get("es.hosts")}
        self.client = Elasticsearch(**kwargs)

    def bulk(self, *args, **kwargs):
        return self.client.bulk(*args, **kwargs)
