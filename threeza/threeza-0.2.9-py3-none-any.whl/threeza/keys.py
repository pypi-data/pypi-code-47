import uuid

def keyhash(key):
	return str(uuid.uuid5(uuid.NAMESPACE_DNS, key))

