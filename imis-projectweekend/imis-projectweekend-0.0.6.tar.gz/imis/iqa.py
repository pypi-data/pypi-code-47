import requests


ASI_GENERIC_PROPERTY_DATA_COLLECTION = 'Asi.Soa.Core.DataContracts.GenericPropertyDataCollection, Asi.Contracts'


def _generic_property_data_collection_to_dict(collection):
    if collection['$type'] != ASI_GENERIC_PROPERTY_DATA_COLLECTION:
        msg = 'Input must be: {0}'.format(ASI_GENERIC_PROPERTY_DATA_COLLECTION)
        raise ValueError(msg)
    output = {}
    for prop in collection['$values']:
        k = prop['Name']
        try:
            output[k] = prop['Value']['$value']
        except TypeError:
            output[k] = prop['Value']
        except KeyError:
            output[k] = None
    return output


def _raw_iqa_results(client, query_name, offset=0, *parameters):
    headers = {'Authorization': client.auth.authorization_header}
    url = client.url + f'/api/iqa?QueryName={query_name}&offset={offset}'
    for param in parameters:
        url += f'&parameter={param}'

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    yield data
    if data['HasNext']:
        yield from _raw_iqa_results(client, query_name, data['NextOffset'], *parameters)


def iter_items(client, query_name, offset=0, *parameters):
    for page in _raw_iqa_results(client, query_name, *parameters):
        for item in page['Items']['$values']:
            yield _generic_property_data_collection_to_dict(item['Properties'])
