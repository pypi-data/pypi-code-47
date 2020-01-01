import json_store_client, base64

class _Client(object):
	def __init__(self, secret, sendk, recvk):
		self.client = json_store_client.Client(
			(secret*64)[:64])
		self.sendk = sendk
		self.recvk = recvk
	def send(self, raw):
		if not type(raw) == bytes:
			raise ValueError("Expected bytes as argument")
		raw = base64.b64encode(raw).decode()
		old = self.client.retrieve(self.sendk) or []
		while not old == []:
			old = self.client.retrieve(self.sendk) or []
		self.client.store(self.sendk, [raw])
	def recv(self):
		res = self.client.retrieve(self.recvk) or []
		while res == []:
			res = self.client.retrieve(self.recvk) or []
		d = base64.b64decode(res[0])
		self.client.store(self.recvk, [])
		return d

def Client(secret):
	return _Client(secret, "recv", "send")
def Server(secret):
	return _Client(secret, "send", "recv")
def Pair(secret):
	return Server(secret), Client(secret)