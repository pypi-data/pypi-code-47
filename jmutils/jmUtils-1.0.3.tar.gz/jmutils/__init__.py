from jmutils.show import show, niceprint
from jmutils.times import *
import random
import unicodedata
import re
import hashlib

def sorte(n_in = 100000, n_out = 1000000):
	return random.randrange( n_in, n_out )

def remove_acentos(string):
	nfkd = unicodedata.normalize('NFKD', string)
	string_sem_acento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
	return re.sub('[^a-zA-Z0-9_ \\\]', '', string_sem_acento)	

def hash_md5(var = None):
	if var == None:
		var = timestamp()
	return hashlib.md5(str(var).encode('utf-8')).hexdigest()

def hash_sha256(var = None):
	if var == None:
		var = timestamp()
	return hashlib.sha256(str(var).encode('utf-8')).hexdigest()


