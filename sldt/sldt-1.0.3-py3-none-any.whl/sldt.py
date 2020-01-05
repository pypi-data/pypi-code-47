__version__ = '1.0.3'

import os
import re
import pandas as pd
import datetime
import logging
import pickle


SUPPORTED_EXT = ['.pkl', '.csv', '.png', '.txt']

def sep_path_name_ext(path_name_ext):
	ext = [ext_test for ext_test in SUPPORTED_EXT if path_name_ext[-len(ext_test):] == ext_test]
	assert ext != [], 'please specify extension / extension not supported, currently support: {}'.format(SUPPORTED_EXT)
	ext = ext[0]
	path_name = path_name_ext[:-len(ext)]
	if '/' in path_name or '\\' in path_name:
		splitted = re.split(r'/|\\', path_name)
		path = '/'.join(splitted[:-1])
		name = splitted[-1]
	else:
		path = ''
		name = path_name
	return path, name, ext

def append_dt(path_name_ext, datetime_format):
	path, name, ext = sep_path_name_ext(path_name_ext)

	datetime_now = datetime.datetime.now().strftime(datetime_format)
	if path != '':
		path_name_dt_ext = path + '/' + name + '_' + datetime_now + ext
	else:
		path_name_dt_ext = name + '_' + datetime_now + ext

	return path_name_dt_ext, ext

def s(var, path_name_ext, datetime_format="%y%m%d%H%M", **kwargs):
	'''
	given 'path/path/filename.extension'
	save var to 'path/path/filename_datetime.entension'
	e.g., '../data/titanic.pkl'
	save var to '../data/titanic_201912091148.pkl'

	plt to '.png'

	for .txt
	var needs to be a list of string, each element is a line
	'''
	path_name_dt_ext, ext = append_dt(path_name_ext, datetime_format)

	if ext == '.pkl':
		with open(path_name_dt_ext, 'wb') as f:
			pickle.dump(var, f)

	elif ext == '.csv':
		if kwargs == {}: # default kwargs
			kwargs = {'index': False}

		assert isinstance(var, pd.DataFrame), 'not handled'
		var.to_csv(path_name_dt_ext, **kwargs)

	elif ext == '.png':
		if kwargs == {}: # default kwargs
			kwargs = {'dpi': 600, 'bbox_inches': 'tight'}

		var.savefig(path_name_dt_ext, **kwargs)
		
		try:
			var.close()
		except:
			# print("didn't close")
			pass

	elif ext == '.txt':
		with open(path_name_dt_ext, 'w+', encoding='utf-8', **kwargs) as f:
			f.writelines(var)

	else:
		assert False, 'currently can only handle' + str(SUPPORTED_EXT)

	logging.info(f'{path_name_dt_ext} saved')


def find_newest(path_name_ext):
	path, name, ext = sep_path_name_ext(path_name_ext)

	all_files = os.listdir(path)
	all_matches = [x for x in all_files if re.match(fr'{name}_\d{{10}}{ext}', x)]
	all_dt = [x[len(name)+1:-len(ext)] for x in all_matches]
	assert all_dt != [], 'cannot find any files'

	newest_dt = max(all_dt)
	if path != '':
		newest_path_name_ext = path + '/' + name + '_' + newest_dt + ext
	else:
		newest_path_name_ext = name + '_' + newest_dt + ext
	return newest_path_name_ext, ext

def l(path_name_ext, **kwargs):
	newest_path_name_ext, ext = find_newest(path_name_ext)
	if ext == '.pkl':
		with open(newest_path_name_ext, 'rb') as f:
			data = pickle.load(f)

	elif ext == '.csv':
		if kwargs == {}: # default kwargs
			kwargs = {'index': False}
			
		data = pd.read_csv(newest_path_name_ext, **kwargs)

	elif ext == '.txt':
		with open(newest_path_name_ext, 'r') as f:
			data = f.read()

	else:
		print('not handled')

	logging.info(f'{newest_path_name_ext} loaded')
	return data