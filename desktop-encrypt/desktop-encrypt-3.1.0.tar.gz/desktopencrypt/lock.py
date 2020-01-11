from ecies import encrypt
from zipfile import ZipFile
import sys, shutil, base64, os

def zipDir(dirPath, zipPath):
	with ZipFile(zipPath , mode='w') as zipf:
		lenDirPath = len(dirPath)
		for root, _ , files in os.walk(dirPath):
			for file in files:
				filePath = os.path.join(root, file)
				zipf.write(filePath , filePath[lenDirPath :])

def lock():
	dirname=sys.argv[1]
	desktop = os.path.join(os.path.expanduser("~"), "Desktop/")
	path_arg = os.path.join(desktop, dirname)
	zip_path = os.path.join(desktop, dirname+".zip")
	pub = input("Encryption Key: ")

	zipDir(path_arg, zip_path)

	with open(zip_path, 'rb') as f:
		data = f.read()

	try:
		c = encrypt(pub, data)
	except:
		raise ValueError("Encrpytion failed. Are you sure the encryption key provided is valid?")

	shutil.rmtree(path_arg)
	with open(os.path.join(desktop, dirname), "w") as f:
		f.write(base64.b64encode(c).decode('utf-8'))
	os.remove(zip_path)

