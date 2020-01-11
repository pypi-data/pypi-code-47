from ecies import decrypt
from ecdsa import curves
import sys, hashlib, getpass, os, base64

def unlock():
	fname = sys.argv[1]
	dk_string1 = getpass.getpass(prompt="Decryption Key 1: ")
	sk_int1 = int(hashlib.sha256(dk_string1.encode()).hexdigest(), 16)

	dk_string2 = getpass.getpass(prompt="Decryption Key 2: ")
	sk_int2 = int(hashlib.sha256(dk_string2.encode()).hexdigest(), 16)

	sk = hex((sk_int1*sk_int2)%curves.SECP256k1.order)[2:]

	fpath = os.path.join(os.path.join(os.path.expanduser("~"), "Desktop"), fname)

	with open(fpath, "rb") as f:
		data = f.read()
	c = base64.b64decode(data)
	try:
		data = decrypt(sk, c)
	except:
		raise ValueError("Decryption failed. Are you sure the passphrases entered were correct?")
	zipname = os.path.join(os.path.join(os.path.expanduser("~"), "Desktop"), fname+".zip")
	with open(zipname, "wb") as f:
		f.write(data)

	os.remove(os.path.join(os.path.join(os.path.expanduser("~"), "Desktop"), fname))