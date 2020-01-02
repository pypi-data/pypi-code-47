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
import unittest
from collections import namedtuple
from unittest.mock import Mock, call, mock_open, patch

import railyard
from railyard.entrypoint import (
    _get_port,
    _launch_services,
    _parse_app,
    _parse_dispatch,
    _parse_routes,
    main,
)


class TestInitFunctions(unittest.TestCase):
    def test_parse_routes(self):
        with open(
            os.path.join(os.path.dirname(__file__), "test_dispatch1.yaml"), "r"
        ) as yaml_contents:
            routes = _parse_routes(yaml_contents)

        self.assertEqual(
            routes, {"*/mobile/*": "mobile-frontend", "*/work/*": "static-backend"}
        )

    def test_get_port(self):
        mock_socket = Mock()
        mock_socket.getsockname.return_value = ["dummy", 1234]

        with patch.object(socket, "socket") as mock_socket_constructor:
            mock_socket_constructor.return_value = mock_socket

            result = _get_port()

        self.assertEqual(result, 1234)

    def test_parse_app(self):
        app_file_path = os.path.join(os.path.dirname(__file__), "test_app1.yaml")

        with open(app_file_path, "r") as yaml_contents:
            with patch("builtins.open") as mock_open_yaml:
                mock_open_yaml.side_effect = mock_open(read_data=yaml_contents.read())

                results = _parse_app(app_file_path)

        mock_open_yaml.assert_called_once_with(app_file_path, "r")

        self.assertEqual(
            results,
            (
                {"*": "default"},
                {
                    "default": {
                        "env_variables": {"BUCKET_NAME": "example-gcs-bucket"},
                        "handlers": [
                            {"static_dir": "static/images", "url": "/images"},
                            {
                                "redirect_http_response_code": 301,
                                "script": "auto",
                                "secure": "always",
                                "url": "/.*",
                            },
                        ],
                        "instance_class": "F2",
                        "runtime": "python37",
                    }
                },
                {"default": "."},
            ),
        )

    def test_parse_dispatch(self):
        # Test with default service
        dispatch_file_path = os.path.join(
            os.path.dirname(__file__), "test_dispatch2.yaml"
        )
        app1_file_path = os.path.join(os.path.dirname(__file__), "test_app1.yaml")

        with open(dispatch_file_path, "r") as yaml_contents:
            dispatch_file_contents = yaml_contents.read()

        with open(app1_file_path, "r") as yaml_contents:
            app1_file_contents = yaml_contents.read()

        with patch("builtins.open") as mock_open_yaml:
            mock_open_yaml.side_effect = (
                mock_open(read_data=dispatch_file_contents).return_value,
                mock_open(read_data=app1_file_contents).return_value,
            )

            results = _parse_dispatch(dispatch_file_path)

        self.assertEqual(
            mock_open_yaml.mock_calls,
            [call(dispatch_file_path, "r"), call("app.yaml", "r")],
        )

        self.assertEqual(
            results,
            (
                {"*": "default"},
                {
                    "default": {
                        "env_variables": {"BUCKET_NAME": "example-gcs-bucket"},
                        "handlers": [
                            {"static_dir": "static/images", "url": "/images"},
                            {
                                "redirect_http_response_code": 301,
                                "script": "auto",
                                "secure": "always",
                                "url": "/.*",
                            },
                        ],
                        "instance_class": "F2",
                        "runtime": "python37",
                    }
                },
                {"default": "."},
            ),
        )

        # Test with app files in dispatch folder
        dispatch_file_path = os.path.join(
            os.path.dirname(__file__), "test_dispatch3.yaml"
        )
        app2_file_path = os.path.join(os.path.dirname(__file__), "test_app2.yaml")
        app3_file_path = os.path.join(os.path.dirname(__file__), "test_app3.yaml")

        with open(dispatch_file_path, "r") as yaml_contents:
            dispatch_file_contents = yaml_contents.read()

        with open(app2_file_path, "r") as yaml_contents:
            app2_file_contents = yaml_contents.read()

        with open(app3_file_path, "r") as yaml_contents:
            app3_file_contents = yaml_contents.read()

        with patch("builtins.open") as mock_open_yaml:
            with patch.object(os.path, "isfile") as mock_os_path_isfile:
                mock_open_yaml.side_effect = (
                    mock_open(read_data=dispatch_file_contents).return_value,
                    mock_open(read_data=app2_file_contents).return_value,
                    mock_open(read_data=app3_file_contents).return_value,
                )
                mock_os_path_isfile.side_effect = (True, True)

                results = _parse_dispatch(dispatch_file_path)

        self.assertEqual(
            mock_open_yaml.mock_calls,
            [
                call(dispatch_file_path, "r"),
                call("test_app2.yaml", "r"),
                call("test_app3.yaml", "r"),
            ],
        )
        self.assertEqual(
            mock_os_path_isfile.mock_calls,
            [call("test_app2.yaml"), call("test_app3.yaml")],
        )

        self.assertEqual(
            results,
            (
                {"*/app2/*": "test_app2", "*/app3/*": "test_app3"},
                {
                    "test_app2": {
                        "entrypoint": "gunicorn -b :$PORT main:app",
                        "handlers": [{"static_dir": "static/", "url": "/app2/static"}],
                        "runtime": "python37",
                    },
                    "test_app3": {
                        "entrypoint": "gunicorn -b :$PORT main:app",
                        "handlers": [
                            {
                                "static_files": "static/\\1",
                                "url": "/app3/(.*\\.(gif|png|jpg))$",
                            }
                        ],
                        "runtime": "python37",
                    },
                },
                {"test_app2": ".", "test_app3": "."},
            ),
        )

        # Test with app files in separate folder
        with patch("builtins.open") as mock_open_yaml:
            with patch.object(os.path, "isfile") as mock_os_path_isfile:
                mock_open_yaml.side_effect = (
                    mock_open(read_data=dispatch_file_contents).return_value,
                    mock_open(read_data=app2_file_contents).return_value,
                    mock_open(read_data=app3_file_contents).return_value,
                )
                mock_os_path_isfile.side_effect = (False, True, False, True)

                results = _parse_dispatch(dispatch_file_path)

        self.assertEqual(
            mock_open_yaml.mock_calls,
            [
                call(dispatch_file_path, "r"),
                call(os.path.join("test_app2", "test_app2.yaml"), "r"),
                call(os.path.join("test_app3", "test_app3.yaml"), "r"),
            ],
        )
        self.assertEqual(
            mock_os_path_isfile.mock_calls,
            [
                call("test_app2.yaml"),
                call(os.path.join("test_app2", "test_app2.yaml")),
                call("test_app3.yaml"),
                call(os.path.join("test_app3", "test_app3.yaml")),
            ],
        )

        self.assertEqual(
            results,
            (
                {"*/app2/*": "test_app2", "*/app3/*": "test_app3"},
                {
                    "test_app2": {
                        "entrypoint": "gunicorn -b :$PORT main:app",
                        "handlers": [{"static_dir": "static/", "url": "/app2/static"}],
                        "runtime": "python37",
                    },
                    "test_app3": {
                        "entrypoint": "gunicorn -b :$PORT main:app",
                        "handlers": [
                            {
                                "static_files": "static/\\1",
                                "url": "/app3/(.*\\.(gif|png|jpg))$",
                            }
                        ],
                        "runtime": "python37",
                    },
                },
                {"test_app2": "test_app2", "test_app3": "test_app3"},
            ),
        )

        # Test missing dispatch
        with patch("builtins.open") as mock_open_yaml:
            with patch.object(os.path, "isfile") as mock_os_path_isfile:
                mock_open_yaml.side_effect = (
                    mock_open(read_data=dispatch_file_contents).return_value,
                    mock_open(read_data=app2_file_contents).return_value,
                    mock_open(read_data=app3_file_contents).return_value,
                )
                mock_os_path_isfile.side_effect = (False, False)

                with self.assertRaises(RuntimeError):
                    _parse_dispatch(dispatch_file_path)

        self.assertEqual(
            mock_open_yaml.mock_calls, [call(dispatch_file_path, "r"),],
        )
        self.assertEqual(
            mock_os_path_isfile.mock_calls,
            [
                call("test_app2.yaml"),
                call(os.path.join("test_app2", "test_app2.yaml")),
            ],
        )

    def test_launch_services(self):
        test_services = {"service1": {}, "service2": {"entrypoint": "service2 $PORT"}}
        test_working_directories = {"service1": ".", "service2": "service2"}

        with patch.object(railyard.entrypoint, "_get_port") as mock_get_port:
            with patch.object(os.environ, "copy") as mock_environ_copy:
                with patch.object(subprocess, "Popen") as mock_popen:
                    mock_get_port.side_effect = (1111, 2222)
                    mock_environ_copy.side_effect = (
                        {"test": "environment"},
                        {"test": "environment"},
                    )

                    result_ports = _launch_services(
                        test_services, test_working_directories
                    )

        self.assertEqual(
            mock_popen.mock_calls,
            [
                call(
                    "gunicorn -b :$PORT main:app",
                    shell=True,
                    cwd=".",
                    env={"test": "environment", "PORT": "1111"},
                ),
                call(
                    "service2 $PORT",
                    shell=True,
                    cwd="service2",
                    env={"test": "environment", "PORT": "2222"},
                ),
            ],
        )

        self.assertEqual(result_ports, {"service1": 1111, "service2": 2222})

    def test_main(self):
        # Test with app.yaml
        mock_argument_parser = Mock()
        mock_argument_parser.parse_args.return_value = _dict_to_argument_parser_result(
            {"input": "app.yaml", "entrypoint": None}
        )

        mock_railyard_application = Mock()

        with patch.object(
            argparse, "ArgumentParser"
        ) as mock_argument_parser_constructor:
            with patch.object(railyard.entrypoint, "_parse_app") as mock_parse_app:
                with patch.object(
                    railyard.entrypoint, "_launch_services"
                ) as mock_launch_services:
                    with patch.object(
                        railyard.entrypoint, "RailyardApplication"
                    ) as mock_railyard_application_constructor:
                        mock_argument_parser_constructor.return_value = (
                            mock_argument_parser
                        )
                        mock_parse_app.return_value = (
                            {"routes": "routes data"},
                            {"services": "services data"},
                            {"working_directories": "working directories data"},
                        )
                        mock_launch_services.return_value = {"ports": "ports data"}
                        mock_railyard_application_constructor.return_value = (
                            mock_railyard_application
                        )

                        main()

        # Make sure the arg parser is correctly constructed
        self.assertEqual(
            mock_argument_parser.add_argument.mock_calls,
            [
                call(
                    "input",
                    type=str,
                    choices=["app.yaml", "dispatch.yaml"],
                    help="the app.yaml or dispatch.yaml file to run",
                ),
                call(
                    "-e",
                    "--entrypoint",
                    action="append",
                    help="Override for defined entrypoint in input file(s), number of provided overrides must match number of entrypoints defined in input file(s)",
                ),
            ],
        )

        mock_parse_app.assert_called_once_with("app.yaml")
        mock_launch_services.assert_called_once_with(
            {"services": "services data"},
            {"working_directories": "working directories data"},
        )
        mock_railyard_application_constructor.assert_called_once_with(
            {"routes": "routes data"},
            {"services": "services data"},
            {"working_directories": "working directories data"},
            {"ports": "ports data"},
            {"bind": ":8000"},
        )
        mock_railyard_application.run.assert_called_once_with()

        # Test with dispatch.yaml
        mock_argument_parser = Mock()
        mock_argument_parser.parse_args.return_value = _dict_to_argument_parser_result(
            {"input": "dispatch.yaml", "entrypoint": None}
        )

        mock_railyard_application = Mock()

        with patch.object(
            argparse, "ArgumentParser"
        ) as mock_argument_parser_constructor:
            with patch.object(
                railyard.entrypoint, "_parse_dispatch"
            ) as mock_parse_dispatch:
                with patch.object(
                    railyard.entrypoint, "_launch_services"
                ) as mock_launch_services:
                    with patch.object(
                        railyard.entrypoint, "RailyardApplication"
                    ) as mock_railyard_application_constructor:
                        mock_argument_parser_constructor.return_value = (
                            mock_argument_parser
                        )
                        mock_parse_dispatch.return_value = (
                            {"routes": "routes data"},
                            {"services": "services data"},
                            {"working_directories": "working directories data"},
                        )
                        mock_launch_services.return_value = {"ports": "ports data"}
                        mock_railyard_application_constructor.return_value = (
                            mock_railyard_application
                        )

                        main()

        mock_parse_dispatch.assert_called_once_with("dispatch.yaml")
        mock_launch_services.assert_called_once_with(
            {"services": "services data"},
            {"working_directories": "working directories data"},
        )
        mock_railyard_application_constructor.assert_called_once_with(
            {"routes": "routes data"},
            {"services": "services data"},
            {"working_directories": "working directories data"},
            {"ports": "ports data"},
            {"bind": ":8000"},
        )
        mock_railyard_application.run.assert_called_once_with()

        # Test entrypoint override
        mock_argument_parser = Mock()
        mock_argument_parser.parse_args.return_value = _dict_to_argument_parser_result(
            {"input": "dispatch.yaml", "entrypoint": ["entrypoint override"]}
        )

        mock_railyard_application = Mock()

        with patch.object(
            argparse, "ArgumentParser"
        ) as mock_argument_parser_constructor:
            with patch.object(
                railyard.entrypoint, "_parse_dispatch"
            ) as mock_parse_dispatch:
                with patch.object(
                    railyard.entrypoint, "_launch_services"
                ) as mock_launch_services:
                    with patch.object(
                        railyard.entrypoint, "RailyardApplication"
                    ) as mock_railyard_application_constructor:
                        mock_argument_parser_constructor.return_value = (
                            mock_argument_parser
                        )
                        mock_parse_dispatch.return_value = (
                            {"routes": "routes data"},
                            {"test": {"entrypoint": "original entrypoint"}},
                            {"working_directories": "working directories data"},
                        )
                        mock_launch_services.return_value = {"ports": "ports data"}
                        mock_railyard_application_constructor.return_value = (
                            mock_railyard_application
                        )

                        main()

        mock_parse_dispatch.assert_called_once_with("dispatch.yaml")
        mock_launch_services.assert_called_once_with(
            {"test": {"entrypoint": "entrypoint override"}},
            {"working_directories": "working directories data"},
        )
        mock_railyard_application_constructor.assert_called_once_with(
            {"routes": "routes data"},
            {"test": {"entrypoint": "entrypoint override"}},
            {"working_directories": "working directories data"},
            {"ports": "ports data"},
            {"bind": ":8000"},
        )
        mock_railyard_application.run.assert_called_once_with()

        # Test with invalid input
        mock_argument_parser = Mock()
        mock_argument_parser.parse_args.return_value = _dict_to_argument_parser_result(
            {"input": "bad.yaml", "entrypoint": None}
        )

        with patch.object(
            argparse, "ArgumentParser"
        ) as mock_argument_parser_constructor:
            mock_argument_parser_constructor.return_value = mock_argument_parser

            with self.assertRaises(RuntimeError):
                main()

        # Test mismatched endpoint override
        mock_argument_parser = Mock()
        mock_argument_parser.parse_args.return_value = _dict_to_argument_parser_result(
            {"input": "dispatch.yaml", "entrypoint": ["entrypoint override"]}
        )

        mock_railyard_application = Mock()

        with patch.object(
            argparse, "ArgumentParser"
        ) as mock_argument_parser_constructor:
            with patch.object(
                railyard.entrypoint, "_parse_dispatch"
            ) as mock_parse_dispatch:
                with patch.object(
                    railyard.entrypoint, "_launch_services"
                ) as mock_launch_services:
                    with patch.object(
                        railyard.entrypoint, "RailyardApplication"
                    ) as mock_railyard_application_constructor:
                        mock_argument_parser_constructor.return_value = (
                            mock_argument_parser
                        )
                        mock_parse_dispatch.return_value = (
                            {"routes": "routes data"},
                            {
                                "test1": {"entrypoint": "original entrypoint 1"},
                                "test2": {"entrypoint": "original entrypoint 2"},
                            },
                            {"working_directories": "working directories data"},
                        )
                        mock_launch_services.return_value = {"ports": "ports data"}
                        mock_railyard_application_constructor.return_value = (
                            mock_railyard_application
                        )

                        with self.assertRaises(RuntimeError):
                            main()


def _dict_to_argument_parser_result(args_dict):
    return namedtuple("Args", args_dict.keys())(*args_dict.values())
