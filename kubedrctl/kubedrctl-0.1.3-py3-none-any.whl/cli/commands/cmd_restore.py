
import click
import logging
import os
import subprocess

from kubedrctl.cli import context

def replace_secret_values(d):
    d["accesskey"] = "***"
    d["secretkey"] = "***"
    d["repopwd"] = "***"

@click.command()
@context.pass_context
@click.option('--accesskey', help='Access Key. ')
@click.option('--secretkey', help='Secret Key. ')
@click.option('--repopwd', help='Repo Password. ')
@click.option('--endpoint', help='S3 endpoint. ')
@click.option('--bucket', help='S3 Bucket name. ')
@click.option('--targetdir', help='Restore target directory. ')
@click.argument('snapid')
def cli(ctx, accesskey, secretkey, repopwd, endpoint, bucket, targetdir, snapid):
    """Restore from backups.

    """

    if not accesskey or not secretkey or not repopwd or not endpoint or not bucket or not targetdir:
        raise Exception('One of the required parameters (accesskey, secretkey, repopwd, endpoint, bucket, targetdir) is missing. ')

    params = {
        "accesskey": accesskey, "secretkey": secretkey, "repopwd": repopwd,
        "targetdir": targetdir, "endpoint": endpoint, "bucket": bucket, "snapid": snapid
    }

    cmdfmt = "docker run --rm -it -e AWS_ACCESS_KEY_ID={accesskey} -e AWS_SECRET_ACCESS_KEY={secretkey} -e RESTIC_PASSWORD={repopwd} -v {targetdir}:{targetdir} restic/restic -r s3:{endpoint}/{bucket} restore --target {targetdir} {snapid}"

    cmd = cmdfmt.format(**params)
    replace_secret_values(params)

    display_cmd = cmdfmt.format(**params)
    logging.critical("\nRunning the command: {}".format(display_cmd))

    print()
    subprocess.call(cmd, shell=True)
