import os
import json
import requests
import time


def call(method, baseurl, uri, data=None):
    response = getattr(requests, method)(
        url=os.path.join(baseurl, uri),
        data=data,
        headers={'content-type': 'application/json'}
    ).content.decode('utf-8')
    return json.loads(response) if response else None


def list_connectors(baseurl):
    return call('get', baseurl, 'connectors')


def call_all_connectors(method, baseurl, uri):
    responses = {'connectors': []}
    for name in list_connectors(baseurl):
        connector_name = os.path.join('connectors', name)
        response = call(method, baseurl, os.path.join(connector_name, uri)) or call('get', baseurl, os.path.join(connector_name, 'status'))
        responses['connectors'].append(response)
    return responses


def status(baseurl):
    return call_all_connectors('get', baseurl, 'status')


def config(baseurl):
    return call_all_connectors('get', baseurl, 'config')


def create(baseurl, config):
    data = {}
    try:
        data = json.loads(config)
    except ValueError as _:
        if os.path.isfile(config):
            with open(config, "r") as f:
                data = json.load(f)
        else:
            return '["{config} was not found."]'
    return call('post', baseurl, 'connectors', data=json.dumps(data))


def delete(baseurl):
    call_all_connectors('delete', baseurl, '')
    return call_all_connectors('get', baseurl, 'status')


def restart(baseurl):
    return call_all_connectors('post', baseurl, 'restart')


def restart_tasks(baseurl, failed_only=True):
    for connector in status(baseurl)['connectors']:
        for task in connector['tasks']:
            call('post', baseurl, os.path.join('connectors', connector['name'], 'tasks', str(task['id']), 'restart'))
    return status(baseurl)['connectors']


def pause(baseurl):
    return call_all_connectors('put', baseurl, 'pause')


def resume(baseurl):
    return call_all_connectors('put', baseurl, 'resume')


def handle_missing_connector(baseurl, name):
    connectors = call('get', baseurl, 'connectors')
    invalid = not name in connectors
    while invalid:
        print(connectors)
        input_name = input("Enter a connector name: ")
        invalid = not input_name in connectors
    return name