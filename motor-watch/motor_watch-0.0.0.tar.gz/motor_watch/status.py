def process(status):
    status_info = {}
    status_info['name'] = status.pos.name
    status_info['target'] = status.target
    return status_info
