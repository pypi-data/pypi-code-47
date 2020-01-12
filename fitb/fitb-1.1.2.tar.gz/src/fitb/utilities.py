import logging

log = logging.getLogger()


def merge(dest, src):
    """Merge two config dicts.

    `dest` is updated in-place with the contents of `src`.
    """
    for src_name, src_val in src.items():
        if isinstance(src_val, dict):
            dest_val = dest.setdefault(src_name, {})
            if not isinstance(dest_val, dict):
                raise ValueError('Incompatible config structures')

            merge(dest_val, src_val)
        else:
            dest[src_name] = src_val

    return dest


def default_config(*extension_points):
    config = {}
    for point in extension_points:
        merge(
            config,
            {point.name: point.default_config()}
        )
    return config