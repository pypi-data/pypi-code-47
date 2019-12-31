
import os, re, shutil, json

def json_to_params(path):
	
	# takes the path to a properly formatted .json file and returns a list of parameters for the read() function

	with open(path, 'r') as f:
		json_params = json.load(f)

	# json_params can be a list of dicts, a list of lists, or a dict of lists but will have to be converted to a list of dicts
	if type(json_params) == dict: # dict of lists
		tmp = [{k: v} for k in json_params.keys() for v in json_params[k]]
		n = int(len(tmp)/2)
		tmp = [{**a, **b} for a, b in zip(tmp[:n], tmp[n:])]
		json_params = tmp

	elif type(json_params[0]) is not dict: # list of lists
		pattern = [p[0] if type(p) == list else p for p in json_params]
		attrs = [p[1:] if type(p) == list else None for p in json_params]
		tmp = [{'pattern': p, 'attrs': a} for p, a in zip(pattern, attrs)]
		json_params = tmp

	# I've made these mistakes so others are bound to	
	for bad, good in zip(['patterns', 'attr'], ['pattern', 'attrs']):
		for idx in range(len(json_params)):
			if bad in json_params[idx].keys():
				json_params[idx][good] = json_params[idx][bad]

	read_params = [] # will be populated and returned
	for curr_json_param in json_params:
		curr_read_param = () # by default, the parameter will be an empty tuple
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

def read(path=None, params=None, master_dict={}):
	
	files = [] # That which will be returned

	# Preprocess parameters

	curr_param = params[0] # Shouldn't ever return an error, since params should always be a list
	if not curr_param:
		curr_param = '.' # Process all files

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
		if len(matches): # If this file/dir doesn't match the re pattern, go to the next file/dir in path
			if len(attrs_to_read) > 0: # Read attributes
				matches = matches[0]
				if type(matches) == str:
					matches = (matches,)
				for idx in range(len(matches)):
					curr_attrs[attrs_to_read[idx]] = matches[idx] # Add attributes
			curr_path = os.path.join(path, curr_path_head)
			if os.path.isdir(curr_path): # Recursion if we're currently on a folder
				files += read(curr_path, params[1:], master_dict=curr_attrs)
			else: # Bottom of file hierarchy
				files += [{
					'path': curr_path,
					'attrs': curr_attrs.copy()
				}]
	return files # List of dicts

def translate(files=None, translation=None, direction='forward'):
	
	if type(translation) == str: # Are we working with a JSON file?
		with open(translation, 'r') as f:
			translation = json.load(f)

	if direction != 'forward': # Swap values and keys
		translation = {attr: {new: old for old, new in entry.items()} for attr, entry in translation.items()}

	for attr in translation.keys():
		for fileidx in range(len(files)):
			curr_val = files[fileidx]['attrs'][attr]
			if curr_val in translation[attr]:
				new_val = translation[attr][curr_val]
				files[fileidx]['attrs'][attr] = new_val

	return files

def flatten(files=None, path_name='path'):
	
	flattened = [file['attrs'].copy() for file in files] # get just the attrs
	for idx in range(len(files)):
		flattened[idx][path_name] = files[idx]['path'] # add "path" or whatever as another key-value pair
	
	return flattened

def write(files=None, path=None, params=None, disp=False, key='c'):
	
	destinations = []

	for file in files:
		curr_destination = ''

		for param in params:
			if type(param) == str: # We are adding a static name to the path
				curr_path_head = param
			else: # We are adding a formatted name to the path
				curr_path_head = param[0] % tuple(file['attrs'][attr] for attr in param[1:])
			curr_destination = os.path.join(curr_destination, curr_path_head)

		curr_destination = os.path.join(path, curr_destination)
		destinations.append(curr_destination)
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
