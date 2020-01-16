import os
import re
import pathlib
import json


class PyFinder():
	'''
	This object is a tool for searching archives with their related formats.
	'''

	def __init__(self, folder, formats=[], deep=False):
		
		# Stores formats for search
		self.formats = formats
		
		# Stores each format of organized way
		new_formats = {}
		
		# loop throug of each format
		for f in self.formats:
			# Default formats in one dictionary
			new_formats[f] = []

		# Tell for PyFinder search in hidden directories
		self.deep = deep
		# Stores the start of search
		self.initial_folder = folder
		# Listing of all files in this folder
		data_base = os.listdir('.')
		# Searching data base of application
		if 'pyfinder.json' not in data_base:
			# Data base format
			self.data = {'status': 0, 'archives': new_formats}
			# Function for save data
			self.save()

		else:
			# Load all data
			self.load()


	def init(self):
		# Start file search
		self.find(self.initial_folder)
		# Save results
		self.save()

	
	def change_folder(salf, folder):
		'''
		this function change default folder to search
		'''

		self.initial_folder = folder


	def save(self):
		'''
		Stores all data in one file
		'''
		self.storer = open('pyfinder.json', 'w')
		self.storer.write(json.dumps(self.data))
		self.storer.close()


	def load(self):
		'''
		Load all data in pyfinder.json
		'''

		with open('pyfinder.json', 'r') as archive:

			self.data = json.loads(archive.read())
			archive.close()

	def find(self, folder):

		try:
			
			# Instace of PosixPath
			p = pathlib.Path(folder)
			
			# Loop throug of each sub file and sub archive
			for element in p.iterdir():
				# If True, searching in hidden folders
				if self.deep:
					# Check if this is a directorie
					if element.is_dir():

						self.find(str(element))
					# Check if this is a file
					elif element.is_file():						

						# Call this function for find the format of this archive.
						# If this archive has one format that is in self.formats, True will be returned.
						found = self.verify_archive(str(element))

						if found[0]:
							# stores path to file
							self.data['archives'][found[1]].append(str(element))

				else:
					# Check if is not hidden file or folder
					if not re.findall('\..*', str(element).split('/')[len(str(element).split('/')) - 1]) or not re.findall('[Gg]ames', str(element).split('/')[len(str(element).split('/')) - 1]):
						
						# Check if this is directorie
						if element.is_dir():

							self.find(str(element))
						# Check if this is file
						elif element.is_file():

							# Call this function for find the format of this archive.
							# If this archive has one format that is in self.formats, True will be returned
							found = self.verify_archive(str(element))

							if found[0]:
								# Stores path in data
								self.data['archives'][found[1]].append(str(element))

		except (PermissionError, OSError):

			self.generate_log(f'permission deneid-{p}')

		except KeyboardInterrupt:

			self.save()

			raise BaseException('search canceled')

	def generate_log(self, log):
		'''
		generate a log file
		'''

		self.log = open('pyfinder_log.txt', 'w')
		self.log.write('\n')
		self.log.write(log)
		self.log.close()

	def verify_archive(self, archive:str) -> list:
		'''
		Check if this file is not hidden
		'''

		for f in self.formats:

			if re.findall(f'.\.{f}', archive):
				
				# Data found
				data = [True, f]

				return data

		return [False, f]


