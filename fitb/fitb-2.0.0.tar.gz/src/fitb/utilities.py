import copy
import logging

log = logging.getLogger()


def merge(dest, src):
    """Merge two config dicts.

    Merging can't happen if the dictionaries are incompatible. This happens when the same path in `src` exists in `dest`
    and one points to a `dict` while another points to a non-`dict`.

    Returns: A new `dict` with the contents of `src` merged into `dest`.

    Raises: 
        ValueError: If the two dicts are incompatible.
    """
    dest = copy.deepcopy(dest)

    for src_name, src_val in src.items():
        if isinstance(src_val, dict):
            dest_val = dest.get(src_name, {})
            if not isinstance(dest_val, dict):
                raise ValueError('Incompatible config structures')

            dest[src_name] = merge(dest_val, src_val)
        else:
            try:
                if isinstance(dest[src_name], dict):
                    raise ValueError('Incompatible config structures')
            except KeyError:
                pass
            dest[src_name] = src_val

    return dest


def default_config(*extension_points):
    config = {}
    for point in extension_points:
        config = merge(
            config,
            {point.name: point.default_config()}
        )
    return config