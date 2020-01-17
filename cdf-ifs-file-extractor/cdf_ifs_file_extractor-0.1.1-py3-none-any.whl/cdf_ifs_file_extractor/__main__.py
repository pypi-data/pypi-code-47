#!/usr/bin/env python
"""
An IFS file extractor for Cognite Data Fusion (CDF).

Example usage: python -m cdf_ifs_file_extractor -h
"""
import argparse
import logging
import os
import glob
import sys
from pathlib import Path

from cognite.client import CogniteClient
from cognite.client.exceptions import CogniteAPIError

from .helper import configure_logger
from .monitoring import Monitor
from .utils import read_yaml
from .file_uploader import FileUploader


def create_cli_parser() -> argparse.ArgumentParser:
    """Returns ArgumentParser for command line interface."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--conf", default="config/default.yml", help="Path to configuration yaml file, default: config/default.yml",
    )
    return parser


def main():
    """
    Main functions which parses arguments and kicks off the app.
    """
    args = create_cli_parser().parse_args()

    try:
        config = read_yaml(args.conf)
    except OSError as exc:
        logging.error("Failed to load yaml config: {}. {}".format(args.conf, exc))
        sys.exit(1)

    try:
        configure_logger(config.get("log_level", logging.INFO), Path(config.get("log_path", "log")))
        client = CogniteClient(
            api_key=os.environ.get(config.get("api_key_name")),
            project=config.get("project"),
            base_url=config.get("base_url"),
            client_name=config.get("client_name"),
            timeout=config.get("client_timeout"),
        )
        login_status = client.login.status()
        logging.info(login_status)
        if not login_status.logged_in:
            logging.error("Not logged in to CDF API")
            sys.exit(2)
    except CogniteAPIError as exc:
        logging.error("Failed to create CDF client: {!s}".format(exc))
        sys.exit(2)

    path = config.get("path")
    path_csvs = os.path.join(path, r'*.csv')
    mapping_files = glob.glob(path_csvs)
    mapping_files.sort(key=os.path.getmtime)
    print(mapping_files)
    monitor = Monitor(namespace="cdf_ifs_file_extractor", project_name=login_status.project)
    monitor.push()
    for mapping_file in mapping_files:
        # mapping_file = config.get("mapping_file")
        logging.info(
            "Start uploading files from path: %s \n using the mapping file: %s", path, mapping_file,
        )
        fileUploader = FileUploader(monitor=monitor, client=client, path=path,
                                    mapping_file=os.path.basename(mapping_file))
        fileUploader.process_csv()


if __name__ == "__main__":
    # if len(sys.argv) == 1 and sys.argv[1] == "install":
    #     from .winservice import install
    #     install()
    # else:
    #     main()
    main()
