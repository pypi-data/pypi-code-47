import hashlib
import re

def sha256sum(filename):
    with open(filename, 'rb', buffering=0) as f:
        return sha256(f)

def sha256(file):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    for n in iter(lambda : file.readinto(mv), 0):
        h.update(mv[:n])
    return h.hexdigest()

def full_uuid(uuid):
	if (re.search(r"^[0-9a-fA-F]{8}\Z",uuid)):
		return '{0}-0000-1000-8000-00805F9B34FB'.format(uuid).lower()
	elif(re.search(r"^[0-9a-fA-F]{4}\Z",uuid)):
		return '{0}0000-0000-1000-8000-00805F9B34FB'.format(uuid).lower()
	elif(re.search(r"^[0-9a-fA-F]{8}-?[0-9a-fA-F]{4}-?4[0-9a-fA-F]{3}-?[89ab][0-9a-fA-F]{3}-?[0-9a-fA-F]{12}\Z",uuid)):
		return uuid.lower()
	else:
		return ""

	
