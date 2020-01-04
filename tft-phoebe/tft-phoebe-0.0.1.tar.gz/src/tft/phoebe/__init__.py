import argparse
import sys
import traceback

from prometheus_client import CollectorRegistry, generate_latest
from prometheus_client.metrics import MetricWrapperBase as Metric
import ruamel.yaml

from typing import Any, Dict, Iterator

SettingsType = Dict[str, Any]


class Exporter:
    def create_args_parser(self) -> argparse.ArgumentParser:
        """
        Create and return a parser for command-line options. The parser is already set to accept
        common, shared options ``--config`` and ``--export``.
        """

        args_parser = argparse.ArgumentParser()

        args_parser.add_argument(
            "--config", "-c",
            required=True,
            metavar="FILE",
            help="Path to plugin's YAML config file."
        )

        args_parser.add_argument(
            "--export", "-e",
            required=True,
            metavar="FILE",
            help="Path to the output file. Use '-' for standard output instead of a file."
        )

        return args_parser

    def parse_args(self) -> argparse.Namespace:
        """
        Parse command-line arguments.

        Common options ``--config`` and ``--export`` are consumed immediately.
        """

        parser = self.create_args_parser()

        options = parser.parse_args()

        self.config_filepath = options.config
        self.export_filepath = options.export

        with open(options.config) as f:
            self.config = ruamel.yaml.YAML().load(f)

        return options

    def fetch_data(self) -> None:
        """
        This method is responsible for acquiring data the exporter needs to emit metrics.
        """

        pass

    def create_metric(self) -> Iterator[Metric]:
        """
        This method is expected to yield one metric every time is called, or return when exporter
        runs out of metrics to export.
        """

        # This method is supposed to be a generator, overriden by child classes. We want to provide a default
        # behavior, which would be an "empty" iterator - when called, this method should yield no entries,
        # iteration over it should end immediately. This is achieved by doing nothing and calling `return`
        # right away.
        #
        # But `return` alone is not enough - this function must be a generator, and generator must have `yield`.
        # So, adding `yield` - and the order is important, `return` must go first. Othwerwise, `yield` would
        # actually yielded an item, `None`, but as said above, this generator is supposed to be empty.
        #
        # So, `return` to quit the generator, and `yield` to "trick" Python to treating this method as
        # a generator. The `yield` is never used, all calls end with `return`, but it's present.
        return
        yield

    def export_prometheus_data(self) -> None:
        """
        Main workhorse: calls ``create_metric`` as long as necessary, adds gained metrics to a registry,
        and emits the output.
        """

        registry = CollectorRegistry()

        for metric in self.create_metric():
            registry.register(metric)

        exported = generate_latest(registry)

        if self.export_filepath == '-':
            sys.stdout.write(exported.decode('utf-8'))

        else:
            with open(self.export_filepath, 'w') as f:
                f.write(exported.decode('utf-8'))

    def run(self) -> None:
        self.parse_args()

        try:
            self.fetch_data()

        except Exception as exc:
            print('Failed to fetch data: {}'.format(exc), file=sys.stderr)
            print(file=sys.stderr)
            traceback.print_exc(file=sys.stderr)

            sys.exit(1)

        try:
            self.export_prometheus_data()

        except Exception as exc:
            print('Failed export metrics: {}'.format(exc), file=sys.stderr)
            print(file=sys.stderr)
            traceback.print_exc(file=sys.stderr)

            sys.exit(1)
