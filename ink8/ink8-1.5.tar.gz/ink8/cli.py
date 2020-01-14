import click
import random
import git
import os
import json
import subprocess
import yaml
import shutil
import coloredlogs
import logging
from os import makedirs
from os.path import join, dirname, abspath, exists, expanduser
from jinja2 import Environment, FileSystemLoader

log = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=log)


def _generateImageTag(ctx, service):
    cwd = dirname(os.getcwd())
    repo = git.Repo(join(cwd, service))
    sha = repo.head.object.hexsha
    pepper = '-' + str(random.randint(10000, 99999)
                       ) if ctx.obj['namespace'] == "local" else ""
    imageTag = '{}{}'.format(sha[:7], pepper)
    log.info("Generated image tag: {}".format(imageTag))
    return imageTag


def _buildImage(imageTag, service):
    log.info("Building image for service: {}".format(service))
    exitCode = subprocess.call('docker build -t {}:{} {}'.format(
        service,
        imageTag,
        join(dirname(os.getcwd()), service)
    ), shell=True)
    if exitCode > 0:
        exit(exitCode)


def _renderTemplate(ctx, deploymenttemplate, service, groupConfig, imageTag=""):
    log.info("Rendering with template {} for service: {}".format(
        deploymenttemplate, service))
    env = Environment(loader=FileSystemLoader(ctx.obj['kubedir']))
    template = env.get_template('{}.yml.j2'.format(deploymenttemplate))
    rendered = template.render(
        name_space=ctx.obj['namespace'],
        service_name=service,
        image_tag=imageTag,
        services=groupConfig.get('services', [])
    )
    renderedFileName = join(ctx.obj['distPath'], '{}.yml'.format(service))
    with open(renderedFileName, 'w+') as f:
        f.write(rendered)
    return renderedFileName


def _deployServices(ctx, deployOrder):
    for file in deployOrder:
        log.info("Deploying File: {}".format(file))
        exitCode = subprocess.call(
            'kubectl apply -f {}'.format(file), shell=True)


@click.group()
@click.pass_context
def main(ctx):
    ctx.obj = {}


@main.command()
@click.argument('groupfilepath')
@click.option('--namespace', '-n', default='local', help='Namespace to deploy to')
@click.option('--kubedir', '-k', default='kubernetes', help='Directory where the K8S configs are stored')
@click.pass_context
def deploy(ctx, groupfilepath, namespace, kubedir):
    os.system(
        'kubectl config set-context --current --namespace {}'.format(namespace))
    ctx.obj['namespace'] = namespace
    ctx.obj['kubedir'] = kubedir
    ctx.obj['distPath'] = join(kubedir, 'dist')
    if exists(ctx.obj['distPath']):
        shutil.rmtree(ctx.obj['distPath'])
    makedirs(ctx.obj['distPath'], exist_ok=True)
    deployOrder = []
    with open(groupfilepath) as f:
        for group in json.loads(f.read()):
            if group.get('build'):
                if group.get('services'):
                    for service in group['services']:
                        imageTag = _generateImageTag(ctx, service)
                        _buildImage(imageTag, service)
                        deployOrder.append(_renderTemplate(
                            ctx, group['template'], service, group, imageTag))
            else:
                deployOrder.append(_renderTemplate(
                    ctx, group['template'], group['template'], group))
    _deployServices(ctx, deployOrder)


@main.command()
@click.pass_context
def start(ctx):
    os.system('eval $(minikube docker-env); minikube start --cpus=4 --memory=4096')


@main.command()
@click.pass_context
def stop(ctx):
    os.system('minikube stop')


if __name__ == '__main__':
    main()
