def get_coefficients(model, columns, raise_error, **kwargs):
	try:
		coefficients = list(model.coef_.flatten())
	except AttributeError:
		coefficients = None

	if coefficients is None:
		return None

	else:
		if len(columns) != len(coefficients):
			if raise_error:
				raise RuntimeError(f'number of columns: {len(columns)}, number of coefficients: {len(coefficients)}')
			else:
				return None
		else:
			coefficient_dictionary = {column: coefficient for coefficient, column in zip(coefficients, columns)}

			for key, value in kwargs.items():
				coefficient_dictionary[key] = value

			return coefficient_dictionary
