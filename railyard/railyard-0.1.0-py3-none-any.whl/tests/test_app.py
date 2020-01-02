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

import mimetypes
import os
import unittest
import urllib.error
import urllib.request
from unittest.mock import ANY, Mock, patch

from railyard.app import (
    HTTPErrorPassthroughProcessor,
    RailyardApplication,
    _build_file_path,
    _build_proxy_url,
    _build_request_url,
    _match_route,
    _match_url,
    _not_found,
    _proxy,
    _serve_static_file,
)


class TestRailyardApplication(unittest.TestCase):
    def test_init(self):
        test_routes = {"*/route1/*": "service1", "*/route2/*": "service2"}
        test_services = {
            "service1": {},
            "service2": {
                "handlers": [
                    {"url": "/service2/static", "static_dir": "static/"},
                    {"url": "/service2/app", "script": "auto"},
                ]
            },
        }
        test_working_directories = {"service1": ".", "service2": "service2/"}
        test_ports = {"service1": 4000, "service2": 5000}

        result_application = RailyardApplication(
            test_routes, test_services, test_working_directories, test_ports
        )

        self.assertEqual(
            result_application._port_mappings, {"*/route1/*": 4000, "*/route2/*": 5000}
        )
        self.assertEqual(
            result_application._url_handlers,
            {
                "*/route1/*": {},
                "*/route2/*": {
                    "/service2/static": {
                        "url": "/service2/static",
                        "static_dir": "static/",
                    },
                    "/service2/app": {"url": "/service2/app", "script": "auto"},
                },
            },
        )
        self.assertEqual(
            result_application._working_directory_mappings,
            {"*/route1/*": ".", "*/route2/*": "service2/"},
        )

    def test_load_config(self):
        result_application = RailyardApplication(
            {}, {}, {}, {}, options={"reload": True, "loglevel": "debug"}
        )

        self.assertEqual(result_application.cfg.reload, True)
        self.assertEqual(result_application.cfg.loglevel, "debug")

    def test_load(self):
        result_application = RailyardApplication({}, {}, {}, {})

        self.assertEqual(result_application.load(), result_application)

    def test_call(self):
        # Test with static_dir
        test_routes = {"*/service/*": "service"}
        test_services = {
            "service": {"handlers": [{"url": "/service/static", "static_dir": "./"}]}
        }
        test_working_directories = {"service": os.path.dirname(__file__)}
        test_ports = {"service": 4000}

        test_application = RailyardApplication(
            test_routes, test_services, test_working_directories, test_ports
        )

        # Bad route
        response_body = test_application.__call__(
            {
                "wsgi.url_scheme": "http",
                "HTTP_HOST": "localhost",
                "PATH_INFO": "/badroute",
            },
            Mock(),
        )

        self.assertEqual(list(response_body), [b"Not Found"])

        # Good route, file exists
        response_body = test_application.__call__(
            {
                "wsgi.url_scheme": "http",
                "HTTP_HOST": "localhost",
                "PATH_INFO": "/service/static/test_static_file",
            },
            Mock(),
        )

        self.assertEqual(list(response_body), [b"test static file content\n"])

        # Good route, file doesn't exist
        response_body = test_application.__call__(
            {
                "wsgi.url_scheme": "http",
                "HTTP_HOST": "localhost",
                "PATH_INFO": "/service/static/bad_file",
            },
            Mock(),
        )

        self.assertEqual(list(response_body), [b"Not Found"])

        # Test with static_files
        test_routes = {"*/service/*": "service"}
        test_services = {
            "service": {
                "handlers": [{"url": "/service/(.*)$", "static_files": "./\\1"}]
            }
        }
        test_working_directories = {"service": os.path.dirname(__file__)}
        test_ports = {"service": 4000}

        test_application = RailyardApplication(
            test_routes, test_services, test_working_directories, test_ports
        )

        # Good route, file exists
        response_body = test_application.__call__(
            {
                "wsgi.url_scheme": "http",
                "HTTP_HOST": "localhost",
                "PATH_INFO": "/service/test_static_file",
            },
            Mock(),
        )

        self.assertEqual(list(response_body), [b"test static file content\n"])

        # Good route, file doesn't exist
        response_body = test_application.__call__(
            {
                "wsgi.url_scheme": "http",
                "HTTP_HOST": "localhost",
                "PATH_INFO": "/service/bad_file",
            },
            Mock(),
        )

        self.assertEqual(list(response_body), [b"Not Found"])

        # Test no match, default to proxy, for coverage reasons
        test_routes = {"*/service/*": "service"}
        test_services = {
            "service": {
                "handlers": [
                    {"url": "/images", "static_dir": "static/images"},
                    {"url": "/pdfs", "static_dir": "static/pdfs"},
                ]
            }
        }
        test_working_directories = {"service": "./"}
        test_ports = {"service": 4000}

        test_application = RailyardApplication(
            test_routes, test_services, test_working_directories, test_ports
        )

        mock_open_response = Mock()
        mock_open_response.status = 200
        mock_open_response.reason = "OK"
        mock_open_response.getheaders.return_value = {"Proxy": "Headers"}
        mock_open_response.read.return_value = b"mock proxied content"

        mock_opener = Mock()
        mock_opener.open.return_value = mock_open_response

        with patch.object(urllib.request, "Request") as mock_request:
            with patch.object(urllib.request, "build_opener") as mock_build_opener:
                mock_request.return_value = Mock()
                mock_build_opener.return_value = mock_opener

                response_body = test_application.__call__(
                    {
                        "wsgi.url_scheme": "http",
                        "HTTP_HOST": "localhost",
                        "PATH_INFO": "/service/test",
                    },
                    Mock(),
                )

        self.assertEqual(list(response_body), [b"mock proxied content"])

        # Test a proxied URL
        test_routes = {"*/service/*": "service"}
        test_services = {"service": {"handlers": [{"url": "/.*", "script": "auto"},]}}
        test_working_directories = {"service": "./"}
        test_ports = {"service": 4000}

        test_application = RailyardApplication(
            test_routes, test_services, test_working_directories, test_ports
        )

        mock_open_response = Mock()
        mock_open_response.status = 200
        mock_open_response.reason = "OK"
        mock_open_response.getheaders.return_value = {"Proxy": "Headers"}
        mock_open_response.read.return_value = b"mock proxied content"

        mock_opener = Mock()
        mock_opener.open.return_value = mock_open_response

        with patch.object(urllib.request, "Request") as mock_request:
            with patch.object(urllib.request, "build_opener") as mock_build_opener:
                mock_request.return_value = Mock()
                mock_build_opener.return_value = mock_opener

                response_body = test_application.__call__(
                    {
                        "wsgi.url_scheme": "http",
                        "HTTP_HOST": "localhost",
                        "PATH_INFO": "/service/test",
                    },
                    Mock(),
                )

        self.assertEqual(list(response_body), [b"mock proxied content"])

        # Test static priority over application URLs
        test_routes = {"*": "default"}
        test_services = {
            "default": {
                "handlers": [
                    {"url": "/", "script": "auto"},
                    {"url": "/static", "static_dir": "./"},
                ]
            }
        }
        test_working_directories = {"default": os.path.dirname(__file__)}
        test_ports = {"default": 4000}

        test_application = RailyardApplication(
            test_routes, test_services, test_working_directories, test_ports
        )

        response_body = test_application.__call__(
            {
                "wsgi.url_scheme": "http",
                "HTTP_HOST": "localhost",
                "PATH_INFO": "/static/test_static_file",
            },
            Mock(),
        )

        self.assertEqual(list(response_body), [b"test static file content\n"])

        # Test multiple matching route, priority to first match
        test_routes = {"*": "default"}
        test_services = {
            "default": {
                "handlers": [
                    {"url": "/match", "script": "auto",},
                    {"url": "/match/longer", "script": "auto"},
                ]
            }
        }
        test_working_directories = {"default": "./"}
        test_ports = {"default": 4000}

        test_application = RailyardApplication(
            test_routes, test_services, test_working_directories, test_ports
        )

        mock_open_response = Mock()
        mock_open_response.status = 200
        mock_open_response.reason = "OK"
        mock_open_response.getheaders.return_value = {"Proxy": "Headers"}
        mock_open_response.read.return_value = b"mock proxied content"

        mock_opener = Mock()
        mock_opener.open.return_value = mock_open_response

        with patch.object(urllib.request, "Request") as mock_request:
            with patch.object(urllib.request, "build_opener") as mock_build_opener:
                mock_request.return_value = Mock()
                mock_build_opener.return_value = mock_opener

                response_body = test_application.__call__(
                    {
                        "wsgi.url_scheme": "http",
                        "HTTP_HOST": "localhost",
                        "PATH_INFO": "/match/longer",
                    },
                    Mock(),
                )

        self.assertEqual(list(response_body), [b"mock proxied content"])


class TestHTTPErrorPassthroughProcessor(unittest.TestCase):
    def test_init(self):
        self.assertIsInstance(
            HTTPErrorPassthroughProcessor(), urllib.request.HTTPErrorProcessor
        )

    def test_http_response(self):
        mock_response = Mock()

        self.assertEqual(
            HTTPErrorPassthroughProcessor().http_response(Mock(), mock_response),
            mock_response,
        )

    def test_https_response(self):
        self.assertEqual(
            HTTPErrorPassthroughProcessor.http_response,
            HTTPErrorPassthroughProcessor.https_response,
        )


class TestAppFunctions(unittest.TestCase):
    def test_match_route(self):
        self.assertTrue(_match_route("http://www.test.com/mobile/", "*/mobile/*"))
        self.assertTrue(
            _match_route("http://www.test.com/mobile/index.html", "*/mobile/*")
        )
        self.assertTrue(
            _match_route("http://www.test.com/mobile/sub/index.html", "*/mobile/*")
        )
        self.assertTrue(_match_route("https://www.test.com/mobile/", "*/mobile/*"))
        self.assertTrue(
            _match_route("https://www.test.com/mobile/index.html", "*/mobile/*")
        )
        self.assertTrue(
            _match_route("https://www.test.com/mobile/sub/index.html", "*/mobile/*")
        )
        self.assertTrue(_match_route("http://localhost:8000/mobile/", "*/mobile/*"))
        self.assertTrue(
            _match_route("http://localhost:8000/mobile/index.html", "*/mobile/*")
        )
        self.assertTrue(
            _match_route("http://localhost:8000/mobile/sub/index.html", "*/mobile/*")
        )

        self.assertFalse(_match_route("http://www.test.com/mobile/", "*/work/*"))
        self.assertFalse(
            _match_route("http://www.test.com/mobile/index.html", "*/work/*")
        )
        self.assertFalse(
            _match_route("http://www.test.com/mobile/sub/index.html", "*/work/*")
        )
        self.assertFalse(_match_route("https://www.test.com/mobile/", "*/work/*"))
        self.assertFalse(
            _match_route("https://www.test.com/mobile/index.html", "*/work/*")
        )
        self.assertFalse(
            _match_route("https://www.test.com/mobile/sub/index.html", "*/work/*")
        )
        self.assertFalse(_match_route("http://localhost:8000/mobile/", "*/work/*"))
        self.assertFalse(
            _match_route("http://localhost:8000/mobile/index.html", "*/work/*")
        )
        self.assertFalse(
            _match_route("http://localhost:8000/mobile/sub/index.html", "*/work/*")
        )

    def test_match_url(self):
        self.assertTrue(_match_url("/app/static", "/app/static"))
        self.assertTrue(_match_url("/app/static/test.ext", "/app/static"))
        self.assertTrue(_match_url("/app/static/test/test.ext", "/app/static"))

        self.assertFalse(_match_url("/app/path", "/app/static"))
        self.assertFalse(_match_url("/app/path/test.ext", "/app/static"))
        self.assertFalse(_match_url("/app/path/test/test.ext", "/app/static"))

        self.assertTrue(_match_url("/profile/edit/manager", "/profile/(.*)/(.*)"))
        self.assertFalse(_match_url("/profile/edit", "/profile/(.*)/(.*)"))

    def test_proxy(self):
        mock_start_response = Mock()

        mock_request_object = Mock()

        mock_open_response = Mock()
        mock_open_response.status = 200
        mock_open_response.reason = "OK"
        mock_open_response.getheaders.return_value = {"Proxy": "Headers"}
        mock_open_response.read.return_value = b"mock proxied content"

        mock_opener = Mock()
        mock_opener.open.return_value = mock_open_response

        with patch.object(urllib.request, "Request") as mock_request:
            with patch.object(urllib.request, "build_opener") as mock_build_opener:
                mock_request.return_value = mock_request_object
                mock_build_opener.return_value = mock_opener

                proxied_response_body = _proxy(
                    {
                        "wsgi.input": "test wsgi input",
                        "REQUEST_METHOD": "GET",
                        "HTTP_test_header": "test http header",
                        "CONTENT_TYPE": "test-content/type",
                        "CONTENT_LENGTH": 1234,
                    },
                    mock_start_response,
                    "/test/path",
                )

        mock_request.assert_called_once_with(
            "/test/path",
            data="test wsgi input",
            headers={
                "test-header": "test http header",
                "CONTENT-TYPE": "test-content/type",
                "CONTENT-LENGTH": 1234,
            },
            method="GET",
        )
        mock_opener.open.assert_called_once_with(mock_request_object)
        mock_start_response.assert_called_once_with("200 OK", {"Proxy": "Headers"})

        self.assertEqual(list(proxied_response_body), [b"mock proxied content"])

        # Test an error
        mock_start_response = Mock()

        mock_request_object = Mock()

        mock_http_error = Mock()
        mock_http_error.status = 404
        mock_http_error.getheaders.return_value = {"Proxy": "Headers"}
        mock_http_error.read.return_value = b"mock error content"

        mock_opener = Mock()

        with patch.object(urllib.request, "Request") as mock_request:
            with patch.object(urllib.request, "build_opener") as mock_build_opener:
                mock_request.return_value = mock_request_object
                mock_build_opener.return_value = mock_opener

                mock_opener.open.side_effect = urllib.error.HTTPError(
                    "/test/path",
                    404,
                    "Not Found",
                    {"Proxy": "Headers"},
                    mock_http_error,
                )

                proxied_response_body = _proxy(
                    {
                        "wsgi.input": "test wsgi input",
                        "REQUEST_METHOD": "GET",
                        "HTTP_test_header": "test http header",
                        "CONTENT_TYPE": "test-content/type",
                        "CONTENT_LENGTH": 1234,
                    },
                    mock_start_response,
                    "/test/path",
                )

        mock_request.assert_called_once_with(
            "/test/path",
            data="test wsgi input",
            headers={
                "test-header": "test http header",
                "CONTENT-TYPE": "test-content/type",
                "CONTENT-LENGTH": 1234,
            },
            method="GET",
        )
        mock_opener.open.assert_called_once_with(mock_request_object)
        mock_start_response.assert_called_once_with(
            "404 Not Found", {"Proxy": "Headers"}
        )

        self.assertEqual(list(proxied_response_body), [b"mock error content"])

    def test_serve_static_file(self):
        def test_file_wrapper(file_object, block_size):
            file_content = file_object.read()

            file_object.close()

            return [file_content]

        test_file_path = os.path.join(os.path.dirname(__file__), "test_static_file")

        mock_start_response = Mock()

        with patch.object(mimetypes, "guess_type") as mock_guess_type:
            mock_guess_type.return_value = (None, None)

            response_content = _serve_static_file(
                {}, mock_start_response, test_file_path
            )

        mock_guess_type.assert_called_once_with(test_file_path)
        mock_start_response.assert_called_once_with("200 OK", [])

        self.assertEqual(list(response_content), [b"test static file content\n"])

        # Try again with a mimetype
        mock_start_response = Mock()

        with patch.object(mimetypes, "guess_type") as mock_guess_type:
            mock_guess_type.return_value = ("text/plain", "deflate, gzip")

            response_content = _serve_static_file(
                {}, mock_start_response, test_file_path
            )

        mock_guess_type.assert_called_once_with(test_file_path)
        mock_start_response.assert_called_once_with(
            "200 OK",
            [("Content-Type", "text/plain"), ("Content-Encoding", "deflate, gzip")],
        )

        self.assertEqual(list(response_content), [b"test static file content\n"])

        # Try again with wsgi.file_wrapper
        mock_start_response = Mock()
        mock_file_wrapper = Mock(wraps=test_file_wrapper)

        with patch.object(mimetypes, "guess_type") as mock_guess_type:
            mock_guess_type.return_value = ("text/plain", "deflate, gzip")

            response_content = _serve_static_file(
                {"wsgi.file_wrapper": mock_file_wrapper},
                mock_start_response,
                test_file_path,
            )

        mock_guess_type.assert_called_once_with(test_file_path)
        mock_start_response.assert_called_once_with(
            "200 OK",
            [("Content-Type", "text/plain"), ("Content-Encoding", "deflate, gzip")],
        )
        mock_file_wrapper.assert_called_once_with(ANY, 1024)

        self.assertEqual(list(response_content), [b"test static file content\n"])

    def test_not_found(self):
        mock_start_response = Mock()

        response_body = _not_found(None, mock_start_response)

        mock_start_response.assert_called_once_with(
            "404 Not Found", [("Content-Type", "text/plain"), ("Content-Length", "9")]
        )

        self.assertEqual(list(response_body), [b"Not Found"])

    def test_build_request_url(self):
        self.assertEqual(
            _build_request_url({"wsgi.url_scheme": "http", "HTTP_HOST": "localhost"}),
            "http://localhost",
        )
        self.assertEqual(
            _build_request_url(
                {
                    "wsgi.url_scheme": "https",
                    "SERVER_NAME": "test.com",
                    "SERVER_PORT": "443",
                }
            ),
            "https://test.com",
        )
        self.assertEqual(
            _build_request_url(
                {
                    "wsgi.url_scheme": "https",
                    "SERVER_NAME": "test.com",
                    "SERVER_PORT": "4430",
                }
            ),
            "https://test.com:4430",
        )
        self.assertEqual(
            _build_request_url(
                {
                    "wsgi.url_scheme": "http",
                    "SERVER_NAME": "test.com",
                    "SERVER_PORT": "80",
                }
            ),
            "http://test.com",
        )
        self.assertEqual(
            _build_request_url(
                {
                    "wsgi.url_scheme": "http",
                    "SERVER_NAME": "test.com",
                    "SERVER_PORT": "8000",
                }
            ),
            "http://test.com:8000",
        )
        self.assertEqual(
            _build_request_url(
                {
                    "wsgi.url_scheme": "http",
                    "HTTP_HOST": "localhost",
                    "SCRIPT_NAME": "/script",
                }
            ),
            "http://localhost/script",
        )
        self.assertEqual(
            _build_request_url(
                {
                    "wsgi.url_scheme": "http",
                    "HTTP_HOST": "localhost",
                    "PATH_INFO": "/path_info",
                }
            ),
            "http://localhost/path_info",
        )
        self.assertEqual(
            _build_request_url(
                {
                    "wsgi.url_scheme": "http",
                    "HTTP_HOST": "localhost",
                    "QUERY_STRING": "query1=value1&query2=value2",
                }
            ),
            "http://localhost?query1=value1&query2=value2",
        )

    def test_build_proxy_url(self):
        self.assertEqual(
            _build_proxy_url("http://www.test.com/", 8080), "http://www.test.com:8080/"
        )
        self.assertEqual(
            _build_proxy_url("http://localhost:80/", 8080), "http://localhost:8080/"
        )
        self.assertEqual(
            _build_proxy_url("http://www.test.com/app/path", 8080),
            "http://www.test.com:8080/app/path",
        )
        self.assertEqual(
            _build_proxy_url("http://localhost:80/app/path", 8080),
            "http://localhost:8080/app/path",
        )

    def test_build_file_path(self):
        self.assertEqual(
            _build_file_path(
                "/stylesheets/style.css", "/stylesheets", static_dir="stylesheets"
            ),
            "stylesheets/style.css",
        )
        self.assertEqual(
            _build_file_path(
                "/stylesheets/style.css", "/stylesheets", static_dir="dist/css"
            ),
            "dist/css/style.css",
        )
        self.assertEqual(
            _build_file_path(
                "/stylesheets/style.css",
                "/stylesheets",
                static_dir="stylesheets",
                working_directory="app",
            ),
            "app/stylesheets/style.css",
        )
        self.assertEqual(
            _build_file_path(
                "/stylesheets/style.css",
                "/stylesheets",
                static_dir="dist/css",
                working_directory="app",
            ),
            "app/dist/css/style.css",
        )

        self.assertEqual(
            _build_file_path(
                "/test.gif", r"/(.*\.(gif|png|jpg))$", static_files=r"static/\1"
            ),
            "static/test.gif",
        )
        self.assertEqual(
            _build_file_path(
                "/test.png", r"/(.*\.(gif|png|jpg))$", static_files=r"static/\1"
            ),
            "static/test.png",
        )
        self.assertEqual(
            _build_file_path(
                "/test.jpg", r"/(.*\.(gif|png|jpg))$", static_files=r"static/\1"
            ),
            "static/test.jpg",
        )
        self.assertEqual(
            _build_file_path(
                "/test/test.gif", r"/(.*\.(gif|png|jpg))$", static_files=r"static/\1"
            ),
            "static/test/test.gif",
        )
        self.assertEqual(
            _build_file_path(
                "/test/test.png", r"/(.*\.(gif|png|jpg))$", static_files=r"static/\1"
            ),
            "static/test/test.png",
        )
        self.assertEqual(
            _build_file_path(
                "/test/test.jpg", r"/(.*\.(gif|png|jpg))$", static_files=r"static/\1"
            ),
            "static/test/test.jpg",
        )

        self.assertEqual(
            _build_file_path(
                "/test.gif",
                r"/(.*\.(gif|png|jpg))$",
                static_files=r"static/\1",
                working_directory="app",
            ),
            "app/static/test.gif",
        )
        self.assertEqual(
            _build_file_path(
                "/test.png",
                r"/(.*\.(gif|png|jpg))$",
                static_files=r"static/\1",
                working_directory="app",
            ),
            "app/static/test.png",
        )
        self.assertEqual(
            _build_file_path(
                "/test.jpg",
                r"/(.*\.(gif|png|jpg))$",
                static_files=r"static/\1",
                working_directory="app",
            ),
            "app/static/test.jpg",
        )
        self.assertEqual(
            _build_file_path(
                "/test/test.gif",
                r"/(.*\.(gif|png|jpg))$",
                static_files=r"static/\1",
                working_directory="app",
            ),
            "app/static/test/test.gif",
        )
        self.assertEqual(
            _build_file_path(
                "/test/test.png",
                r"/(.*\.(gif|png|jpg))$",
                static_files=r"static/\1",
                working_directory="app",
            ),
            "app/static/test/test.png",
        )
        self.assertEqual(
            _build_file_path(
                "/test/test.jpg",
                r"/(.*\.(gif|png|jpg))$",
                static_files=r"static/\1",
                working_directory="app",
            ),
            "app/static/test/test.jpg",
        )

        with self.assertRaises(ValueError):
            _build_file_path("/stylesheets/style.css", "/stylesheets")
