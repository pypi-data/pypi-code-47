from __future__ import print_function

import os.path
import sys

from flake8.options import config
from flake8.utils import parse_comma_separated_list
from six import iteritems, string_types


class ProfileError(Exception):
    """Error loading a profile."""


class ProfilePlugin(object):

    name = "flake8-profiles"
    version = "0.1.0"

    @classmethod
    def add_options(cls, parser):
        parser.add_option(
            "--profile",
            help="Enable a flake8 profile",
            comma_separated_list=False,
            parse_from_config=True,
        )

    @classmethod
    def parse_options(cls, parser, options, args):
        profile = options.profile
        if not profile:
            return
        profile_dir = os.environ.get("FLAKE8_PROFILE_DIR")
        if not profile_dir:
            raise ProfileError("No FLAKE8_PROFILE_DIR set")
        profile_file = os.path.join(profile_dir, "{}.conf".format(profile))
        conf, filenames = config.ConfigFileFinder._read_config([profile_file])
        if not filenames:
            raise ProfileError(
                "Profile file {} not found".format(profile_file)
            )
        print("Loaded profile from", filenames[0], file=sys.stderr)
        profile_options = dict(conf.items("flake8"))
        for k, v in iteritems(profile_options):
            try:
                old_v = getattr(options, k)
            except AttributeError:
                setattr(options, k, v)
            else:
                # Don't overwrite local config options which aren't lists
                if not isinstance(old_v, string_types):
                    if isinstance(v, string_types):
                        new_v = list(old_v) + parse_comma_separated_list(v)
                    else:
                        new_v = list(old_v) + v
                    setattr(options, k, new_v)
