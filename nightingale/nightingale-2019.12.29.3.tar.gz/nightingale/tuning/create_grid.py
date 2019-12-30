from pandas import DataFrame


def multiply_dictionary(dictionary, key, values):
	"""
	:type dictionary: dict
	:type key: str
	:type values: list
	:rtype: list[dict]
	"""
	result = []
	if not isinstance(values, (list, tuple)):
		values = [values]

	for value in values:
		new_d = dictionary.copy()
		new_d[key] = value
		result.append(new_d)
	return result



def create_grid(dictionary):
	"""
	:param dict[str, list] dictionary: a dictionary of lists of parameter values
	:rtype: list[dict[str,]]
	"""
	result = [{}]
	for key, values in dictionary.items():
		new_result = []
		for dictionary in result:
			new_result += multiply_dictionary(dictionary=dictionary, key=key, values=values)
		result = new_result
	return result


def create_model_grid(model, dictionary, name=None):
	list_of_dictionaries = create_grid(dictionary=dictionary)
	models = {}
	parameters_list = []
	parameters_dictionary = {}
	for index, kwargs in enumerate(list_of_dictionaries):
		model_name = f'{name}_{index}'
		models[model_name] =  model(**kwargs)
		parameters = kwargs.copy()
		parameters['model'] = model_name
		parameters_list.append(parameters)
		parameters_dictionary[model_name] = kwargs.copy()
	return {'models': models, 'parameter_table': DataFrame.from_records(parameters_list), 'parameters': parameters_dictionary}


class ModelGrid:
	def __init__(self, models, grid_dictionaries):
		if not isinstance(models, list):
			models = [models]

		if not isinstance(grid_dictionaries, list):
			grid_dictionaries = [grid_dictionaries]

		num_models_per_type = {}
		out_models = {}
		records = []
		parameter_dictionary = {}
		for model, dictionary in zip(models, grid_dictionaries):
			list_of_dictionaries = create_grid(dictionary=dictionary)

			for index, kwargs in enumerate(list_of_dictionaries):
				try:
					model_type = model.__name__
				except AttributeError:
					model_type = 'model'

				if model_type not in num_models_per_type:
					num_models_per_type[model_type] = 1
				else:
					num_models_per_type[model_type] += 1

				model_name = f'{model_type}_{num_models_per_type[model_type]}'
				out_models[model_name] = model(**kwargs)
				parameters = kwargs.copy()
				parameters['model_name'] = model_name
				records.append(parameters)
				parameter_dictionary[model_name] = kwargs.copy()

		self.models = out_models
		self.num_models_per_type = num_models_per_type
		self.parameters = parameter_dictionary
		self.parameter_table = DataFrame.from_records(records)

