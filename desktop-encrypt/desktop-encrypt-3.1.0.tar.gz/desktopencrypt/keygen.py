from ecdsa import keys, curves
from ecies import encrypt
import hashlib, getpass, os

def keygen():
	dk_string1 = getpass.getpass(prompt="Decryption Key 1: ")
	if len(dk_string1) < 6:
		raise ValueError("For your own security each passphrase should be at least 6 characters")
	sk_int1 = int(hashlib.sha256(dk_string1.encode()).hexdigest(), 16)

	dk_string2 = getpass.getpass(prompt="Decryption Key 2: ")
	if len(dk_string2) < 6:
		raise ValueError("For your own security each passphrase should be at least 6 characters")
	sk_int2 = int(hashlib.sha256(dk_string2.encode()).hexdigest(), 16)

	sk_int = (sk_int1*sk_int2)%curves.SECP256k1.order

	sk = keys.SigningKey.from_secret_exponent(sk_int, curve=curves.SECP256k1, hashfunc=hashlib.sha256)
	pk = sk.verifying_key.pubkey

	pub = "04" + hex(pk.point.x())[2:] + hex(pk.point.y())[2:]
	try:
		c = encrypt(pub, b'abc')
	except:
		raise ValueError("Sorry: this passphrase combination does not work. Try again and change one passphrase!")

	print("Encryption Key:", pub)