
import os, re, shutil, json

def json_to_params(path):
	
	# takes the path to a properly formatted .json file and returns a list of parameters for the read() function

	with open(path, 'r') as f:
		json_params = json.load(f)
	
	# I've made these mistakes so someone else is bound to:
	for bad, good in zip(['patterns', 'attr'], ['pattern', 'attrs']):
		if bad in json_params.keys():
			json_params[good] = json_params[bad]

	# json_params can be a list of dicts, a list of lists, or a dict of lists but will have to be converted to a list of dicts
	if type(json_params) == dict: # dict of lists
		json_params = [{
			'pattern': pattern,
			'attrs': attrs
		} for pattern, attrs in zip(json_params['pattern'], json_params['attrs'])]
	elif type(json_params[0]) is not dict: # list of lists
		tmp = []
		for param in json_params:
			if type(param) is list:
				curr_pattern = param[0]
				curr_attrs = param[1:]
			elif type(param) is str:
				curr_pattern = param
				curr_attrs = None
			if not curr_attrs:
				curr_attrs = None # just to standardize
			tmp.append({
				'pattern': curr_pattern, # a string
				'attrs': curr_attrs # a list
			})
		json_params = tmp


	read_params = [] # will be populated and returned
	for curr_json_param in json_params:
		curr_read_param = ()
		curr_pattern = curr_json_param['pattern']
		if curr_pattern: # is there a pattern at all?
			curr_read_param += (curr_pattern,)
			curr_attrs = curr_json_param['attrs']
			if curr_attrs: # are there attributes to read?
				if type(curr_attrs) == str:
					curr_attrs = (curr_attrs,)
				elif type(curr_attrs) == list:
					curr_attrs = tuple(curr_attrs)
				curr_read_param += curr_attrs
		read_params.append(curr_read_param)

	return read_params

def read(path, params, master_dict={}):
	
	all_files = [] # That which will be returned

	# Preprocess parameters
	if len(params) == 0:
		curr_param = '*' # Process all files
	else:
		curr_param = params[0] # Filter by regular expression

	for curr_path_head in os.listdir(path):
		curr_attrs = master_dict.copy()

		# Are we reading attributes?
		if type(curr_param) == tuple: # Yes
			pattern = curr_param[0]
			attrs_to_read = curr_param[1:]
		else: # No
			pattern = curr_param
			attrs_to_read = []
		matches = re.findall(pattern, curr_path_head)
		if len(matches) == 0:
			continue # This one doesn't match, go to the next file/dir in path
		else:
			if len(attrs_to_read) > 0: # Read attributes
				matches = matches[0]
				if type(matches) == str:
					matches = (matches,)
				for idx in range(len(matches)):
					curr_attrs[attrs_to_read[idx]] = matches[idx] # Add attributes
			curr_path = os.path.join(path, curr_path_head)
			if os.path.isdir(curr_path): # Recursion if we're currently on a folder
				all_files += read(curr_path, params[1:], master_dict=curr_attrs)
			else: # Bottom of file hierarchy
				all_files += [{
					'path': curr_path,
					'attrs': curr_attrs.copy()
				}]
	return all_files # List of dicts

def translate(all_files, translation, direction='forward'):
	
	if type(translation) == str: # Are we working with a JSON file?
		with open(translation, 'r') as f:
			translation = json.load(f)

	if direction != 'forward': # Swap values and keys
		translation = {attr: {new: old for old, new in entry.items()} for attr, entry in translation.items()}

	for attr in translation.keys():
		for fileidx in range(len(all_files)):
			curr_val = all_files[fileidx]['attrs'][attr]
			if curr_val in translation[attr]:
				new_val = translation[attr][curr_val]
				all_files[fileidx]['attrs'][attr] = new_val

	return all_files

def write(all_files, path, params, disp=False, key='c'):
	
	destinations = []

	for file in all_files:
		curr_destination = ''

		for param in params:
			if type(param) == str: # We are adding a static name to the path
				curr_path_head = param
			else: # We are adding a formatted name to the path
				curr_path_head = param[0] % tuple(file['attrs'][attr] for attr in param[1:])
			curr_destination = os.path.join(curr_destination, curr_path_head)

		curr_destination = os.path.join(path, curr_destination)
		if disp: # Let the user double check that the destination paths are ok
			print(curr_destination)
		if key != 'n': # We're actually commiting to creating new files
			os.makedirs(os.path.dirname(curr_destination), exist_ok=True)
			if key == 'c': # Copy and paste
				func = shutil.copy
			elif key == 'x': # Cut and paste
				func = shutil.move
			else: # Could also be a user-provided function
				func = key
			func(file['path'], curr_destination)

	return destinations
