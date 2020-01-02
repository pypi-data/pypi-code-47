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

import fnmatch
import http.cookiejar
import mimetypes
import mmap
import os
import re
import urllib
import urllib.error
import urllib.request

import gunicorn.app.base


class RailyardApplication(gunicorn.app.base.BaseApplication):
    def __init__(self, routes, services, working_directories, ports, options=None):
        # http://docs.gunicorn.org/en/stable/custom.html
        self.options = options or {}

        self._port_mappings = {}  # key: route, value: port
        self._url_handlers = (
            {}
        )  # key: route, value: dict (key: url, value: handler dict)
        self._working_directory_mappings = {}  # key: route, value: working directory

        # Build the port mapping and working directory dicts
        for route in routes:
            service_name = routes[route]

            self._port_mappings[route] = ports[service_name]
            self._working_directory_mappings[route] = working_directories[service_name]

            # Build the path handlers dict
            handlers_dict = {}  # key: url, value: handler dict

            if "handlers" in services[service_name]:
                for handler in services[service_name]["handlers"]:
                    handlers_dict[handler["url"]] = handler

            self._url_handlers[route] = handlers_dict

        super(RailyardApplication, self).__init__()

    def load_config(self):
        config = dict(
            [
                (key, value)
                for key, value in self.options.items()
                if key in self.cfg.settings and value is not None
            ]
        )
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self

    def __call__(self, environ, start_response):
        matching_route = None
        matching_url = None

        request_path = environ.get("PATH_INFO", "")

        for route in self._url_handlers:
            if _match_route(_build_request_url(environ), route):
                matching_route = route
                break

        # Fail early
        if matching_route is None:
            return _not_found(environ, start_response)

        for url in self._url_handlers[matching_route]:
            handler_dict = self._url_handlers[matching_route][url]

            if _match_url(request_path, url):
                # Static routes are prioritized to match AppEngine behavior
                if "static_dir" in handler_dict or "static_files" in handler_dict:
                    matching_url = url
                    break

                if matching_url is None:
                    matching_url = url

        if matching_url is not None:
            handler_dict = self._url_handlers[matching_route][matching_url]

            # Handle static files specially
            static_file_path = None

            if "static_dir" in handler_dict:
                static_file_path = _build_file_path(
                    request_path,
                    matching_url,
                    static_dir=handler_dict["static_dir"],
                    working_directory=self._working_directory_mappings[matching_route],
                )
            elif "static_files" in handler_dict:
                static_file_path = _build_file_path(
                    request_path,
                    matching_url,
                    static_files=handler_dict["static_files"],
                    working_directory=self._working_directory_mappings[matching_route],
                )

            if static_file_path is not None:
                if os.path.isfile(static_file_path) is True:
                    return _serve_static_file(environ, start_response, static_file_path)

                return _not_found(environ, start_response)

        # Proxy the request
        new_url = _build_proxy_url(
            _build_request_url(environ), self._port_mappings[matching_route]
        )
        return _proxy(environ, start_response, new_url)


class HTTPErrorPassthroughProcessor(urllib.request.HTTPErrorProcessor):
    # HTTPErrorProcessor that simply passes through the error response
    # https://stackoverflow.com/a/11744894
    def http_response(self, request, response):
        return response

    https_response = http_response


def _match_route(to_check, route_rule):
    return fnmatch.fnmatch(to_check, route_rule)


def _match_url(to_check, url_rule):
    path_regex = re.compile(url_rule, re.I)

    if path_regex.match(to_check) is None:
        return False

    return True


def _proxy(environ, start_response, path):
    proxy_cookiejar = http.cookiejar.CookieJar()

    proxy_opener = urllib.request.build_opener(
        HTTPErrorPassthroughProcessor,
        urllib.request.HTTPCookieProcessor(proxy_cookiejar),
    )

    # Convert the environ into headers
    request_headers = {}

    for environ_variable in environ:
        if environ_variable.startswith("HTTP_") is True:
            request_headers[
                environ_variable[len("HTTP_") :].replace("_", "-")
            ] = environ[environ_variable]
        elif environ_variable in ("CONTENT_TYPE", "CONTENT_LENGTH"):
            request_headers[environ_variable.replace("_", "-")] = environ[
                environ_variable
            ]

    request = urllib.request.Request(
        path,
        data=environ.get("wsgi.input"),
        headers=request_headers,
        method=environ.get("REQUEST_METHOD"),
    )

    try:
        response = proxy_opener.open(request)

    except urllib.error.HTTPError as error:
        response = error

    start_response(str(response.status) + " " + response.reason, response.getheaders())

    return iter([response.read()])


def _serve_static_file(environ, start_response, file_path):
    def file_wrapper(file_path, block_size=1024):
        # Makes a path into an iterable
        file_object = open(file_path, "rb")
        file_mmap = mmap.mmap(file_object.fileno(), 0, prot=mmap.PROT_READ)

        try:
            data = file_mmap.read(block_size)

            while data:
                yield data
                data = file_mmap.read(block_size)
        finally:
            file_mmap.close()
            file_object.close()

    static_file_mimetype = mimetypes.guess_type(file_path)

    headers = []

    if static_file_mimetype[0] is not None:
        headers.append(("Content-Type", static_file_mimetype[0]))

    if static_file_mimetype[1] is not None:
        headers.append(("Content-Encoding", static_file_mimetype[1]))

    start_response("200 OK", headers)

    if "wsgi.file_wrapper" in environ:
        return environ["wsgi.file_wrapper"](open(file_path, "rb"), 1024)

    # Use our crude memory map iterator instead
    return file_wrapper(file_path)


def _not_found(environ, start_response):
    data = b"Not Found"

    start_response(
        "404 Not Found",
        [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))],
    )

    return iter([data])


def _build_request_url(environ):
    # https://www.python.org/dev/peps/pep-3333/#url-reconstruction
    url = environ["wsgi.url_scheme"] + "://"

    if environ.get("HTTP_HOST"):
        url += environ["HTTP_HOST"]
    else:
        url += environ["SERVER_NAME"]

        if environ["wsgi.url_scheme"] == "https":
            if environ["SERVER_PORT"] != "443":
                url += ":" + environ["SERVER_PORT"]
        else:
            if environ["SERVER_PORT"] != "80":
                url += ":" + environ["SERVER_PORT"]

    url += urllib.parse.quote(environ.get("SCRIPT_NAME", ""))
    url += urllib.parse.quote(environ.get("PATH_INFO", ""))

    if environ.get("QUERY_STRING"):
        url += "?" + environ["QUERY_STRING"]

    return url


def _build_proxy_url(original_url, redirect_port):
    parsed_url = urllib.parse.urlparse(original_url)

    # Replace the original port with the redirect port
    return parsed_url._replace(
        netloc=parsed_url.hostname + ":" + str(redirect_port)
    ).geturl()


def _build_file_path(
    request_path,
    handler_url,
    static_dir=None,
    static_files=None,
    working_directory=None,
):
    if static_dir is not None:
        # Replace the handler_url of the path with static_dir, adding working dir if necessary
        static_file_path = request_path.replace(handler_url, static_dir)
    elif static_files is not None:
        # Map the handler_url regular expression to static_files
        static_file_path = re.sub(handler_url, static_files, request_path)

    else:
        raise ValueError("static_dir or static_files argument required.")

    if working_directory is None:
        return static_file_path

    return os.path.join(working_directory, static_file_path)
