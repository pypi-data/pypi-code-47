# Copyright 2019 Typo
#
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
#
# you may not use this file except in compliance with the
#
# License.
#
#
#
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing, software
#
# distributed under the License is distributed on an "AS IS" BASIS,
#
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#
# implied. See the License for the specific language governing
#
# permissions and limitations under the License.
#
#
#
# This product includes software developed at
#
# or by Typo (https://www.typo.ai/).
#!/usr/bin/env python3
import os
import sys
import json
from datetime import datetime
import pkg_resources
import singer
from singer import utils, metadata
from tap_typo.typo import TypoTap


REQUIRED_CONFIG_KEYS = []
logger = singer.get_logger()

# State parameter
now = datetime.now().strftime('%Y%m%dT%H%M%S')


def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


def load_schemas():
    """
    Load schemas from schemas folder
    """

    schemas = {}

    for filename in os.listdir(get_abs_path('schemas')):
        path = get_abs_path('schemas') + '/' + filename
        file_raw = filename.replace('.json', '')
        with open(path) as file:
            schemas[file_raw] = json.load(file)

    return schemas


def discover(dataset):
    '''
    Construct catalog
    '''
    raw_schemas = load_schemas()
    streams = []

    for schema_name, schema in raw_schemas.items():

        stream_metadata = []
        stream_key_properties = []

        # create and add catalog entry
        catalog_entry = {
            'stream': dataset,
            'tap_stream_id': dataset,
            'schema': schema,
            'metadata': [],
            'key_properties': []
        }
        streams.append(catalog_entry)

    return {'streams': streams}


def get_selected_streams(catalog):
    '''
    Gets selected streams.  Checks schema's 'selected' first (legacy)
    and then checks metadata (current), looking for an empty breadcrumb
    and mdata with a 'selected' entry
    '''
    selected_streams = []
    # for stream in catalog.streams:
    for stream in catalog['streams']:
        # stream_metadata = metadata.to_map(stream.metadata)
        stream_metadata = metadata.to_map(stream['metadata'])
        # stream metadata will have an empty breadcrumb
        if metadata.get(stream_metadata, (), 'selected'):
            selected_streams.append(stream.tap_stream_id)

    return selected_streams


def sync(config, state, catalog):
    '''
    Process configuration, catalog and request dataset
    '''

    selected_stream_ids = get_selected_streams(catalog)

    # Loop over streams in catalog
    # for stream in catalog.streams:
    for stream in catalog['streams']:
        stream_id = stream['tap_stream_id']
        stream_schema = stream['schema']

        # Output tap_stream_id's schema
        singer.write_schema(stream_id, stream_schema, stream['key_properties'])

        # Typo session
        typo = TypoTap(
            api_key=config["api_key"],
            api_secret=config["api_secret"],
            cluster_api_endpoint=config["cluster_api_endpoint"],
            repository=config["repository"],
            dataset=config["dataset"],
            audit_id=config["audit_id"]
        )
        typo.token = typo.request_token()

        # GET dataset
        data_out = typo.get_dataset(config["dataset"])

        # Output data
        for data in data_out:
            singer.write_record(stream_id, data)


def validate_config(config, config_loc):
    '''
    Configuration file validation
    '''
    
    logger.debug(
        'validate_config - config=[%s], config_loc=[%s]', config, config_loc)
    logger.info('Input configuration parameters: {}'.format(config))
    missing_parameters = []
    if 'api_key' not in config:
        missing_parameters.append('api_key')
    if 'api_secret' not in config:
        missing_parameters.append('api_secret')
    if 'cluster_api_endpoint' not in config:
        missing_parameters.append('cluster_api_endpoint')
    if 'repository' not in config:
        missing_parameters.append('repository')
    if 'dataset' not in config:
        missing_parameters.append('dataset')
    if 'audit_id' not in config:
        missing_parameters.append('audit_id')

    # Output error message is there are missing parameters
    if len(missing_parameters) != 0:
        sep = ','
        logger.error('Configuration parameter missing. Please ' +
                     'set the [{0}] in the configuration file "{1}".'.format(
                         sep.join(missing_parameters), config_loc))
        sys.exit(1)

# @utils.handle_top_exception(LOGGER)
@utils.handle_top_exception(logger)
def main():
    logger.info('\'tap-typo:{}\' Starting...'.format(
        pkg_resources.get_distribution('tap_typo').version))
    # Parse command line arguments
    try:
        args = utils.parse_args(REQUIRED_CONFIG_KEYS)
    except Exception as e:
        logger.error('There is an issue with parsing the configuration files. Please validate your inputs.')
        logger.error(e)
        sys.exit(1)

    # Validate configuration for required parameters
    validate_config(args.config, args.config_path)

    # If discover flag was passed, run discovery mode and dump output to stdout
    if args.discover:
        catalog = discover(args.config['dataset'])
        print(json.dumps(catalog, indent=2))
    # Otherwise run in sync mode
    else:
        if args.catalog:
            #catalog = args.catalog
            catalog = {"streams": []}
            for stream in args.catalog.streams:
                stream = {
                    "stream": stream.stream,
                    "tap_stream_id": stream.tap_stream_id,
                    "schema": stream.schema,
                    "metadata": stream.metadata,
                    "key_properties": stream.key_properties
                }
                catalog["streams"].append(stream)
        else:
            catalog = discover(args.config['dataset'])

    sync(args.config, args.state, catalog)

    state = {
        "date": now,
        "dataset": args.config["dataset"]
    }
    singer.write_state(state)

    logger.info('\'tap-typo:{}\' Finished...'.format(
        pkg_resources.get_distribution('tap_typo').version))


if __name__ == '__main__':
    logger.error('__main__')
    main()
