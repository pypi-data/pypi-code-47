#!/usr/bin/env python3
#
# Convert RDS parameter group intom a TF parameter group.
#
# Usage:
#   aws rds describe-db-parameters --db-parameter-group-name your-parameter-group-name | python3 convert.py
#

import json
import sys
import subprocess
import click

VERSION = '1.2.1'

__version__ = VERSION
__author__ = 'Lev Kokotov <lev.kokotov@instacart.com>'

def main(body):
    if 'Parameters' not in body:
        print('Input is not valid AWS CLI response JSON object with "Parameters" key required.')
        exit(1)

    parameters = body['Parameters']

    print('resource "aws_db_parameter_group" "parameter_group_name" {')

    for parameter in parameters:
        if not parameter['IsModifiable']:
            continue
        if 'ParameterValue' not in parameter:
            continue
        apply_method = 'immediate' if parameter['ApplyType'] == 'dynamic' else 'pending-reboot'
        print('  parameter {')
        print('    apply_method = "{}"'.format(apply_method))
        print('    name         = "{}"'.format(parameter['ParameterName']))
        print('    value        = "{}" # {}'.format(parameter['ParameterValue'], parameter['Description'].replace('\n', ' ').strip()))
        print('  }')

    print('}')

@click.command()
@click.option('--name', required=False, help='The name of the parameter group in RDS.')
@click.option('--stdin', required=False, help='Get the JSON payload from stdin instead.')
def cli(name, stdin):
    if name:
        result = subprocess.check_output(['aws', 'rds', 'describe-db-parameters', '--db-parameter-group-name', name])
        body = json.loads(result)
        main(body)
    elif stdin:
        body = json.loads(sys.stdin.read())
        main(body)
    else:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()
