import logging

import pkg_resources
from stevedore import ExtensionManager

from .extension_point import ExtensionPoint

log = logging.getLogger()


def load_from_pkg_resources(namespace):
    """Populate an dict of ExtensionPoints using pkg_resources.

    This uses pkg_resources to scan the entry-points for `namespace`. Each dotted entrypoint name should have two parts.
    The first will be `namespace` and the second will be assumed to be the name of the entry point to which it belongs.

    Each discovered entry point should be a callable that takes a single argument of an ExtensionPoint. The extension
    should populate the ExtensionPoint appropriately, e.g. by calling `ExtensionPoint.add()`.

    Args:
        namespace: The pkg_resources namespace to scan.

    Returns: A dict mapping extension point names to ExtensionPoint objects.
    """
    points = {}

    for entry_point_name in pkg_resources.get_entry_map(namespace):
        toks = entry_point_name.split('.')
        if len(toks) == 1:
            # This happens for e.g. console_scripts
            continue

        # TODO: Do we need to extend for the case of an entry_point_name with more than two tokens? We could return a
        # tree of ExtensionPoint instead of just a flat mapping.

        assert toks[0] == namespace

        extension_point = points.setdefault(toks[1], ExtensionPoint(toks[1]))

        manager = ExtensionManager(
            '.'.join(toks),
            on_load_failure_callback=_log_extension_loading_failure)

        for extension in manager:
            extension.plugin(extension_point)

    return points


def _log_extension_loading_failure(_mgr, extension_point, err):
    # We have to log at the `error` level here as opposed to, say, `info`
    # because logging isn't configure when we reach here. We need this infor to
    # print with the default logging settings.
    log.error('Plugin load failure: extension-point="%s", err="%s"',
              extension_point, err)
