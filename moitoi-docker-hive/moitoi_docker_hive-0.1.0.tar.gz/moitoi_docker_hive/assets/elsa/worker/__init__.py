import json
import logging.config
import os
import time

import docker
import crossplane

NGINX_CONFIG_FILE = "/data/etc/nginx/nginx.conf"
PROM_TARGET_FILE = "/data/prometheus/targets.json"
TARGETS_PATH = '/'.join(PROM_TARGET_FILE.split("/")[:-1])
DEFAULT_TARGETS = [
    {
        "labels": {
            "job": "mdh_backend"
        },
        "targets": [
            "mdh_backend1:9273"
        ]
    }
]

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d %(funcName)s - %(message)s'
        },
    },
    'handlers': {
        'log': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        '': {
            'handlers': ['log'],
            'level': 'DEBUG',
        }
    }
})


def write_targets_file(data):
    """ Prometheus targets.json writer

    Args:
        data (object): Object to write JSON file

    """
    with open(PROM_TARGET_FILE, "w") as outfile:
        json.dump(data, outfile)


def load_targets_file():
    """ Load prometheus targets.json file. On missing file new file will be created.

    Returns (object): JSON formatted object

    """
    if not os.path.exists(TARGETS_PATH):
        os.makedirs(TARGETS_PATH)
        write_targets_file(DEFAULT_TARGETS)

    with open(PROM_TARGET_FILE) as f:
        return json.load(f)


def get_all_prom_backends():
    """ Helper function to filter targets from prometheus targets.json file

    Returns (list): List of monitored instances

    """
    return load_targets_file()[0]["targets"]


def add_prom_target(backend):
    """ Adds backend instance for prometheus scraping

    Args:
        backend (str): Backend instance name to add

    Returns:

    """
    backends = list(map(lambda x: x.split(":")[0], get_all_prom_backends()))
    if backend not in backends:
        logging.info("Adding {} to {}".format(backend, PROM_TARGET_FILE))
        targets = load_targets_file()
        targets[0]["targets"].append("{}:9273".format(backend))
        write_targets_file(targets)
        logging.info(targets)


def remove_prom_target(backend):
    """ Removes backend instance from prometheus scraping

    Args:
        backend (str): backend name to remove

    Returns:

    """
    backends = list(map(lambda x: x.split(":")[0], get_all_prom_backends()))
    if backend in backends:
        logging.info("Removinf {} from {}".format(backend, PROM_TARGET_FILE))
        targets = load_targets_file()
        targets[0]["targets"].remove("{}:9273".format(backend))
        write_targets_file(targets)
        logging.info(targets)


def get_all_nginx_backends():
    """ Helper function to filter out from nginx.conf backend servers

    Returns (str): List of backned servers

    """
    parsed_conf = crossplane.parse(NGINX_CONFIG_FILE)
    config_backends = parsed_conf['config'][0]['parsed'][1]['block'][0]['block']
    return list(map(lambda x: x['args'], config_backends))


def add_backend_to_nginx_conf(mdh_backend):
    """ Add backend server to nginx.conf
    Args:
        mdh_backend (dict): Dictionary object  mdh_backend as backend name and mdh_backend_port as backend port

    Returns:

    """
    parsed_conf = crossplane.parse(NGINX_CONFIG_FILE)
    parsed_conf['config'][0]['parsed'][1]['block'][0]['block'].append(
        {'directive': 'server', 'args': ['{mdh_backend}:{mdh_backend_port}'.format(**mdh_backend)]}
    )

    config_str = crossplane.build(parsed_conf['config'][0]['parsed'])
    write_nging_conf(config_str)
    logging.info(config_str)


def write_nging_conf(config_str):
    """ Helper function to weite nginx.file

    Args:
        config_str (str): Raw nginx.conf string

    Returns:

    """

    with open(NGINX_CONFIG_FILE, 'w') as f:
        f.write(config_str)


def remove_backend_from_nginx_conf(mdh_backend):
    """ Remove backend server to nginx.conf
    Args:
        mdh_backend (dict): Dictionary object  where mdh_backend as backend name and mdh_backend_port as backend port

    Returns:

    """
    parsed_conf = crossplane.parse(NGINX_CONFIG_FILE)
    config_backend_names = list(map(lambda x: x[0].split(":")[0], get_all_nginx_backends()))
    logging.info(config_backend_names)
    backend_index = config_backend_names.index('{mdh_backend}'.format(**mdh_backend))
    del parsed_conf['config'][0]['parsed'][1]['block'][0]['block'][backend_index]
    config_str = crossplane.build(parsed_conf['config'][0]['parsed'])
    write_nging_conf(config_str)
    logging.info(config_str)


def handle_nginx_reload(cli, mdh_custer_id):
    lb_container = list(filter(lambda x: (x.labels.get('mdh_lb', "null") == "true" and
                                          x.labels.get('mdh_cluster_id', "null") == mdh_custer_id),
                               cli.containers.list()))[0]
    if lb_container:
        logging.info("Nginx reload")
        lb_container.exec_run("nginx -s reload")
        logging.info(lb_container.logs())


def elsa_docker_event_worker():
    logging.info("Elsa is alive!")
    logging.info("Cluster ID: {}".format(os.environ.get("MDH_CLUSTER_ID")))

    cli = docker.from_env()
    while True:
        try:
            for event in cli.events():
                event = json.loads(event.decode('utf-8'))
                config_backend_names = list(map(lambda x: x[0].split(":")[0], get_all_nginx_backends()))
                if event['Type'] == 'container':
                    mdh_cluster_id = event['Actor']['Attributes'].get('mdh_cluster_id', "no_cluster_id")
                    if os.environ.get("MDH_CLUSTER_ID", "ENV_NOT_SET") != mdh_cluster_id:
                        continue
                    backend_nr = event['Actor']['Attributes'].get('mdh_backend_member_nr')
                    backend_name = "mdh_backend{}".format(backend_nr)
                    if event['Action'] == 'start' and backend_nr:
                        logging.info(event['Actor']['Attributes'])
                        if backend_name in config_backend_names:
                            continue
                        add_backend_to_nginx_conf(dict(mdh_backend=backend_name,
                                                       mdh_backend_port=os.environ.get("MDH_BACKEND_PORT", 5000)))
                        add_prom_target(backend_name)
                        handle_nginx_reload(cli, mdh_cluster_id)
                    elif event['Action'] == 'kill' and backend_nr:
                        remove_backend_from_nginx_conf(dict(mdh_backend=backend_name,
                                                            mdh_backend_port=os.environ.get("MDH_BACKEND_PORT", 5000)))
                        remove_prom_target(backend_name)
                        handle_nginx_reload(cli, mdh_cluster_id)
        except Exception as e:
            logging.exception(e)


def elsa_health_check_worker():
    logging.info("Elsa health worker is  alive!")
    logging.info("Cluster ID: {}".format(os.environ.get("MDH_CLUSTER_ID")))
    statuses = ["exited", "killed"]

    cli = docker.from_env()
    while True:
        mdh_cluster_id = os.environ.get("MDH_CLUSTER_ID", "ENV_NOT_SET")
        containers = cli.containers.list(
            filters={"label": ["mdh_backend=true", "mdh_cluster_id={}".format(mdh_cluster_id)]})
        for container in containers:
            backend_nr = container.labels.get('mdh_backend_member_nr')
            backend_name = "mdh_backend{}".format(backend_nr)
            if container.status in statuses and backend_nr:
                remove_backend_from_nginx_conf(dict(mdh_backend=backend_name,
                                                    mdh_backend_port=os.environ.get("MDH_BACKEND_PORT", 5000)))
                remove_prom_target(backend_name)
        time.sleep(30)
