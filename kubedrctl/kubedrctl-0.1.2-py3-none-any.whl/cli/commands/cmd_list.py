
import click
import logging
import subprocess

from kubedrctl.cli import context

def replace_secret_values(d):
    d["accesskey"] = "***"
    d["secretkey"] = "***"
    d["repopwd"] = "***"

@click.group()
@context.pass_context
def cli(ctx):
    """List backups.

    """

    pass

@cli.command()
@context.pass_context
@click.option('--accesskey', help='Access Key. ')
@click.option('--secretkey', help='Secret Key. ')
@click.option('--repopwd', help='Repo Password. ')
@click.option('--endpoint', help='S3 endpoint. ')
@click.option('--bucket', help='S3 Bucket name. ')
def backups(ctx, accesskey, secretkey, repopwd, endpoint, bucket):
    """List backups.

    """

    if not accesskey or not secretkey or not repopwd or not endpoint or not bucket:
        raise Exception('One of the required parameters (accesskey, secretkey, repopwd, endpoint, bucket) is missing. ')

    params = {
        "accesskey": accesskey, "secretkey": secretkey, "repopwd": repopwd,
        "endpoint": endpoint, "bucket": bucket
    }

    cmdfmt = "docker run --rm -it -e AWS_ACCESS_KEY_ID={accesskey} -e AWS_SECRET_ACCESS_KEY={secretkey} -e RESTIC_PASSWORD={repopwd} restic/restic -r s3:{endpoint}/{bucket} snapshots"

    cmd = cmdfmt.format(**params)
    replace_secret_values(params)

    display_cmd = cmdfmt.format(**params)
    logging.critical("\nRunning the command: {}".format(display_cmd))

    print()
    subprocess.call(cmd, shell=True)



