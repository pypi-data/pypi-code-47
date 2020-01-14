# -*- coding: utf-8 -*-
import pkg_resources

"""
This is the class to represent loading package data

Input to get file name
----------------------
file name : str
	file to be loaded
"""

class LoadPackageData():

	def __init__(self):
		super(LoadPackageData, self).__init__()


	def getFileName(self, filename):
		data_path = pkg_resources.resource_filename(__name__, 'data')
		return data_path+'/'+filename

