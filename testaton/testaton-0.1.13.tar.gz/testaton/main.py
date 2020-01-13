import json
from dtest import Dtest
from .tests_processor import process_connections, process_datasets, process_tests


def testaton(config=None, config_file=None):
    assert config is not None or config_file is not None, "test configuration must be provided by 'config' as an object or 'config_file' as a path"

    definition = None
    if config is not None:
        definition = config
    elif config_file is not None:
        with open(config_file, 'r') as read_file:
            definition = json.load(read_file)

    dt = Dtest(definition['connection-config'],
               definition['test-suite-metadata'])
    connection_dict = process_connections(definition['connections'])
    datasets_dict = process_datasets(
        connection_dict, definition['data-definitions'])
    tests_dict = process_tests(
        datasets_dict, definition['tests'], definition['spark-config'], dt)

    for t in tests_dict:
        tests_dict[t].execute()

    dt.publish()
