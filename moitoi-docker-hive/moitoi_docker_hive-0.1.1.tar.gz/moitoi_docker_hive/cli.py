"""Console script for moitoi_docker_hive."""
import argparse
import os
import sys

import yaml

from moitoi_docker_hive import DEFAULT_CONFIG_DIR, DEFAULT_MDH_PASSWORD, \
    DEFAULT_MDH_CLUSTER_ID, DEFAULT_CONFIG, DEFAULT_CONFIG_FILE
from .main import ClusterHandler


def parse_args():
    """Console script for moitoi_docker_hive."""
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', nargs='*', choices=["init", "show", "+", "-"], help='Cluster commands')
    parser.add_argument('--private-key', default="{}/id_rsa".format(DEFAULT_CONFIG_DIR),
                        help='ssh private key location')
    parser.add_argument('--public-key', default="{}/id_rsa.pub".format(DEFAULT_CONFIG_DIR),
                        help='ssh public key location')
    parser.add_argument('--hive-password', default=os.environ.get("MDH_PASSWORD", DEFAULT_MDH_PASSWORD),
                        help='hive password for keys/user')
    parser.add_argument('--cluster-id', default=os.environ.get("MDH_CLUSTER_ID", DEFAULT_MDH_CLUSTER_ID),
                        help='Uniq cluster id')
    parser.add_argument('--node-name', help='Docker container on append/remove to cluster')
    return parser.parse_args()


def prepare_env():
    if not os.path.isdir(DEFAULT_CONFIG_DIR):
        os.mkdir(DEFAULT_CONFIG_DIR, 0o750)

    if not os.path.isfile(DEFAULT_CONFIG_FILE):
        with open(DEFAULT_CONFIG_FILE, 'w') as file:
            yaml.dump(DEFAULT_CONFIG, file)

    with open(DEFAULT_CONFIG_FILE) as file:
        documents = yaml.full_load(file)[0]
        for item, doc in documents.items():
            if isinstance(doc, dict):
                for _i, _d in doc.items():
                    os.environ["MDH_{}_{}".format(item.upper(), _i.upper())] = _d
            else:
                os.environ["MDH_{}".format(item.upper())] = doc


def worker(args):
    cli = ClusterHandler(args)
    cli.load_ssh_keys()
    cli.invoke()


def main():
    prepare_env()
    worker(parse_args())
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
