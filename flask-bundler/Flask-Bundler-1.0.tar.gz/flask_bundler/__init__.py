"""
Flask-Bundler
-------------

This class will allow you to use the information generated from
Webpack BundleTrackerPlugin to serve your current assets. The last modification
date of the bundle data is checked before every request and the bundle data is
updated if it has been refreshed.
"""

import os
import typing
import json

import flask


__all__ = ["Bundler"]


class Bundler:
    """
    The main extension class. Allows for regular initialization and application
    factory-style initialization.
    """

    stats_file: str
    last_mtime: float
    bundles: typing.Dict[str, typing.List[str]]
    renderers: typing.Dict[str, str]
    strict: bool

    def __init__(self, app: flask.Flask = None, stats_file: str = None,
                 custom_renderers: typing.Dict[str, str] = None,
                 strict: bool = False):
        """Initializes the bundler.

        Arguments:

          :param app: The Flask application. Can be None if you're using
                      the application factory pattern.
          :param stats_file: Path to the webpack-stats.json. Defaults to
                             {app.static_folder}/webpack-stats.json.
          :param custom_renderers: A dictionary of custom renderers.
                                   str.format will be called on the given
                                   string with the public path of the asset as
                                   the only parameter. The default renderers
                                   are "css" and "js", but additional renderers
                                   can be passed if your application contains
                                   other types of outputs.
          :param strict: If True, an error will be raised in exceptional
                         situations. Otherwise, a warning will be issued and
                         the empty string will be returned.
        """
        self._stats_file: str = stats_file

        self.last_mtime = 0.0
        self.bundles = {}

        self.renderers = {
            "css": "<link rel=\"stylesheet\" type=\"text/css\" "
                   "href=\"{0}\" />",
            "js": "<script type=\"text/javascript\" src=\"{0}\"></script>"
        }

        if custom_renderers is not None:
            self.renderers.update(custom_renderers)

        self.strict = strict

        if app is not None:
            self.init_app(app)

    def init_app(self, app: flask.Flask) -> None:
        """Initializes the application for use with the bundler.

        Arguments:

          :param app: The Flask application.
        """
        if self._stats_file is not None:
            self.stats_file = self._stats_file
        else:
            self.stats_file = os.path.join(
                app.static_folder,
                "webpack-stats.json"
            )
        del self._stats_file

        # Check webpack-stats before every request
        app.before_request(self.try_update_bundle)
        # Provide bundle()
        app.context_processor(self.register_bundle)

    def _parse_bundles(self, f: typing.TextIO) -> dict:
        """Parse the webpack-stats.json file."""
        data: dict = json.load(f)

        if data["status"] != "done":
            msg = "The webpack manifest has errors or is still processing."
            if self.strict:
                raise RuntimeError(msg)
            else:
                flask.current_app.logger.warning(msg)

        output = {}
        for bundle, assets in data["chunks"].items():
            output[bundle] = []

            for asset in assets:
                output[bundle].append(asset["publicPath"])

        return output

    def update_bundle(self) -> None:
        """Update the bundle data."""
        try:
            with open(self.stats_file, "r") as bundle_file:
                self.bundles = self._parse_bundles(bundle_file)
        except FileNotFoundError:
            raise RuntimeError("The webpack manifest doesn't exist.")

    def try_update_bundle(self) -> None:
        """Request middleware to check whether to update the bundle data."""
        stat = os.stat(self.stats_file)
        if self.last_mtime < stat.st_mtime:
            self.update_bundle()
            self.last_mtime = stat.st_mtime

    def render_bundle(self, name: str) -> str:
        """Render a bundle.

        The bundle is rendered with the given renderers.

        Arguments:

          :param name: The name of the bundle.
        """
        if name not in self.bundles:
            if self.strict:
                raise ValueError("Bundle {0} does not exist!".format(name))
            else:
                flask.current_app.logger.warning(
                    "Unknown bundle {0}.".format(name)
                )
                return ""

        output = []
        for path in self.bundles[name]:
            ext = path.rsplit(".", 1)[1]

            if ext in self.renderers:
                output.append(self.renderers[ext].format(path))
            else:
                msg = "Unknown asset type {0} for {1}.".format(ext, path)
                if self.strict:
                    raise ValueError(msg)
                else:
                    flask.current_app.logger.warning(msg)

        return flask.Markup("\n".join(output))

    def register_bundle(self) -> dict:
        """Provide the bundle() function to templates."""
        return {
            "bundle": self.render_bundle
        }
