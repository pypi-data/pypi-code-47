import logging
import mimetypes
from pathlib import Path
from typing import Any, Dict

import boto3
from botocore.exceptions import ClientError

from nefelibata.publishers import Publisher

_logger = logging.getLogger("nefelibata")


class S3Publisher(Publisher):

    """A publisher that uploads the weblog to S3.

    You need a user with this policy:

        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "VisualEditor0",
                    "Effect": "Allow",
                    "Action": [
                        "s3:GetBucketWebsite",
                        "s3:PutBucketWebsite",
                        "route53:ChangeResourceRecordSets",
                        "s3:PutBucketAcl",
                        "s3:CreateBucket"
                    ],
                    "Resource": [
                        "arn:aws:route53:::hostedzone/taoetc.org",
                        "arn:aws:s3:::blog.taoetc.org"
                    ]
                },
                {
                    "Sid": "VisualEditor1",
                    "Effect": "Allow",
                    "Action": [
                        "s3:PutObject",
                        "s3:GetObject",
                        "s3:PutObjectAcl"
                    ],
                    "Resource": "arn:aws:s3:::blog.taoetc.org/*"
                },
                {
                    "Sid": "VisualEditor2",
                    "Effect": "Allow",
                    "Action": "route53:ListHostedZones",
                    "Resource": "*"
                }
            ]
        }

    """

    def __init__(
        self,
        bucket: str,
        AWS_ACCESS_KEY_ID: str,
        AWS_SECRET_ACCESS_KEY: str,
        configure_website: bool = False,
        configure_route53: str = None,
        region: str = "us-east-1",
    ):
        self.bucket = bucket
        self.aws_access_key_id = AWS_ACCESS_KEY_ID
        self.aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        self.configure_website = configure_website
        self.configure_route53 = configure_route53
        self.region = region

    def publish(self, root: Path, force: bool = False) -> None:
        self._create_bucket()

        # store file with the last time weblog was published
        last_published_file = root / "last_published"
        if last_published_file.exists():
            last_published = last_published_file.stat().st_mtime
        else:
            last_published = 0

        build = root / "build"
        queue = [build]
        # manually walk, since `glob("**/*")` doesn't follow symlinks
        while queue:
            current = queue.pop()
            for path in current.glob("*"):
                if not path.exists():
                    # broken symlink
                    continue
                if path.is_dir():
                    queue.append(path)
                elif force or path.stat().st_mtime > last_published:
                    key = str(path.relative_to(build))
                    self._upload_file(path, key)

        if self.configure_website:
            self._configure_website()

        if self.configure_route53:
            self._configure_route53()

        # update last published
        with open(last_published_file, "w") as fp:
            pass

    def _get_client(self, service: str):
        return boto3.client(
            service,
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.region,
        )

    def _create_bucket(self) -> bool:
        client = self._get_client("s3")
        _logger.info(f"Creating bucket {self.bucket}")
        try:
            if self.region is None:
                client.create_bucket(Bucket=self.bucket, ACL="public-read")
            else:
                location = {"LocationConstraint": self.region}
                client.create_bucket(
                    Bucket=self.bucket,
                    CreateBucketConfiguration=location,
                    ACL="public-read",
                )
        except ClientError as e:
            _logger.error(e)
            return False
        return True

    def _upload_file(self, path: Path, key: str) -> bool:
        client = self._get_client("s3")
        _logger.info(f"Uploading {path}")
        extra_args = {"ACL": "public-read"}
        mimetype = mimetypes.guess_type(str(path))[0]
        if mimetype:
            extra_args["ContentType"] = mimetype
        try:
            client.upload_file(str(path), self.bucket, key, ExtraArgs=extra_args)
        except ClientError as e:
            _logger.error(e)
            return False
        return True

    def _configure_website(self) -> None:
        client = self._get_client("s3")
        _logger.info("Configuring website")
        website_configuration = {
            "IndexDocument": {"Suffix": "index.html"},
        }
        client.put_bucket_website(
            Bucket=self.bucket, WebsiteConfiguration=website_configuration
        )

    def _configure_route53(self) -> None:
        client = self._get_client("route53")
        _logger.info("Configuring route53")

        # CNAME value
        value = f"{self.bucket}.s3-website-{self.region}.amazonaws.com"

        for zone in client.list_hosted_zones()["HostedZones"]:
            if self.configure_route53.endswith(zone["Name"]):
                zone_id = zone["Id"]
                break
        else:
            _logger.error("No zone found!")
            return

        payload = {
            "Changes": [
                {
                    "Action": "UPSERT",
                    "ResourceRecordSet": {
                        "Name": self.configure_route53.rstrip("."),
                        "Type": "CNAME",
                        "SetIdentifier": "nefelibata",
                        "Region": self.region,
                        "TTL": 600,
                        "ResourceRecords": [{"Value": value}],
                    },
                },
            ]
        }
        response = client.change_resource_record_sets(
            HostedZoneId=zone_id, ChangeBatch=payload
        )
