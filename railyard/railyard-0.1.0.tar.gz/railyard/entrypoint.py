# -*- coding: utf-8 -*-

# Copyright (c) 2020, Brandon Nielsen
#
# This file is part of Railyard.
#
# Railyard is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Railyard is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Railyard.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import os
import socket
import subprocess

import yaml

from railyard.app import RailyardApplication


def _parse_routes(dispatch_yaml):
    routes = {}

    dispatch_dict = yaml.safe_load(dispatch_yaml)

    for route in dispatch_dict["dispatch"]:
        routes[route["url"]] = route["service"]

    return routes


def _get_port():
    # Bind a socket on the first open port provided by the OS
    net_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    net_socket.bind(("", 0))

    port = net_socket.getsockname()[1]

    net_socket.close()

    return port


def _parse_app(app_file_path):
    routes = {"*": "default"}
    services = {}  # Key: service name, value: service yaml as dict
    working_directories = {}  # Key: service name, value: working directory for service

    with open(app_file_path, "r") as app_yaml:
        services["default"] = yaml.safe_load(app_yaml)
        working_directories["default"] = "."

    return routes, services, working_directories


def _parse_dispatch(dispatch_file_path):
    routes = {}  # Key: route, value: service name
    services = {}  # Key: service name, value: service yaml as dict
    working_directories = {}  # Key: service name, value: working directory for service

    # Read the dispatch file
    with open(dispatch_file_path, "r") as dispatch_yaml:
        routes = _parse_routes(dispatch_yaml)

    for route in routes:
        service = routes[route]

        if service == "default":
            with open("app.yaml", "r") as app_yaml:
                services["default"] = yaml.safe_load(app_yaml)
                working_directories["default"] = "."
        else:
            # Check for '$SERVICE.yaml' first, than '$SERVICE/$SERVICE.yaml'
            service_filename = service + ".yaml"
            service_file_path = os.path.join(service, service_filename)

            if os.path.isfile(service_filename) is True:
                with open(service_filename, "r") as app_yaml:
                    services[service] = yaml.safe_load(app_yaml)
                    working_directories[service] = "."
            elif os.path.isfile(service_file_path) is True:
                with open(service_file_path, "r") as app_yaml:
                    services[service] = yaml.safe_load(app_yaml)
                    working_directories[service] = service
            else:
                raise RuntimeError("Unable to find {}".format(service_filename))

    return routes, services, working_directories


def _launch_services(services, working_directories):
    ports = {}  # Key: service name, value: port for service

    for service in services:
        service_dict = services[service]
        port = _get_port()

        # Determine how to launch the service
        if "entrypoint" in service_dict:
            popen_args = service_dict["entrypoint"]
        else:
            popen_args = "gunicorn -b :$PORT main:app"

        # Set environment variables
        popen_env = os.environ.copy()
        popen_env["PORT"] = str(port)

        # Launch the service
        subprocess.Popen(
            popen_args, shell=True, cwd=working_directories[service], env=popen_env
        )

        ports[service] = port

    return ports


def main():
    parser = argparse.ArgumentParser(
        description="Runner for local development of standard environment App Engine applications."
    )

    parser.add_argument(
        "input",
        type=str,
        choices=["app.yaml", "dispatch.yaml"],
        help="the app.yaml or dispatch.yaml file to run",
    )

    parser.add_argument(
        "-e",
        "--entrypoint",
        action="append",
        help="Override for defined entrypoint in input file(s), number of provided overrides must match number of entrypoints defined in input file(s)",
    )

    args = parser.parse_args()

    if args.input == "app.yaml":
        routes, services, working_directories = _parse_app(args.input)
    elif args.input == "dispatch.yaml":
        routes, services, working_directories = _parse_dispatch(args.input)
    else:
        raise RuntimeError("Unrecognized input file {}".format(args.input))

    if args.entrypoint is not None and len(args.entrypoint) != len(services):
        raise RuntimeError(
            "Number of entrypoint overrides ({0}) must match number of entrypoints defined in input file(s) ({1})".format(
                len(args.entrypoint), len(routes)
            )
        )
    elif args.entrypoint is not None:
        for entrypoint_index, entrypoint_override in enumerate(args.entrypoint):
            services[list(services)[entrypoint_index]][
                "entrypoint"
            ] = entrypoint_override

    ports = _launch_services(services, working_directories)

    # Spawn the proxy
    RailyardApplication(
        routes, services, working_directories, ports, {"bind": ":8000"}
    ).run()
