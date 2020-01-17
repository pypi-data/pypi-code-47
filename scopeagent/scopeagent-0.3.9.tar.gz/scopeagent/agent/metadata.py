def parse_env_metadata(raw_metadata):
    if not raw_metadata:
        return {}

    metadata = {}

    for key_value in raw_metadata.split(','):
        key, value = key_value.split('=', 1)
        metadata[key] = value

    return metadata
