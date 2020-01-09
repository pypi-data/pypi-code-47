from pathlib import Path
import sphinx

import click
from .jinja import env
from .configuration import read_configuration_file
from slugify import slugify


def generate_hosting(app: sphinx, exception: Exception):
    if exception is None:
        hosting_outdir = Path(app.outdir) / "hosting_info"
        hosting_outdir.mkdir(exist_ok=True)
        generate_kubernetes_volumes(app, hosting_outdir)


@click.command(
    "interpolate_kubernetes_volumes",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
    help="Interpolate INPUTFILE with values, and write to OUTPUTFILE",
)
@click.argument("inputfile", type=click.File("r"))
@click.argument("outputfile", type=click.File("w"), default="-")
@click.option(
    "--library-config",
    type=click.Path(exists=True),
    default="libraries.yaml",
    help="The config file defining the projects.",
)
@click.option("--interpolate", type=str, multiple=True)
@click.pass_context
def generate_kubernetes_volumes(
    ctx, inputfile, outputfile, interpolate, library_config
):
    extra_interps = dict(var.split("=", 2) for var in interpolate)
    config = read_configuration_file(library_config, download_meta=False)
    volume_mounts = env.get_template("kubernetes_volume_mounts.jinja").render(
        items=config
    )
    volumes = env.get_template("kubernetes_volumes.jinja").render(items=config)
    k8s_template = env.from_string(inputfile.read())
    k8s_output = k8s_template.render(
        META_SPHINX_VOLUME_MOUNTS=volume_mounts,
        META_SPHINX_VOLUMES=volumes,
        **extra_interps
    )
    outputfile.write(k8s_output)
