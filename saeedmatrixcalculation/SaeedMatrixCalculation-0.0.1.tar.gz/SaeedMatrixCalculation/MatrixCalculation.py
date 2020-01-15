import numpy as np

class Matrix:
	""" Matrix class for adding, subtracting,
		multiplying and dividing.

	Attributes:
		column_count (int) representing the number of columns in the matrix
		row_count    (int) representing the number of rows in the matrix
		data_list    (list of lists) a list of lists inputed from the user
	"""

	def __init__(self, column_count, row_count, data_list):
		self.column_count = column_count
		self.row_count = row_count
		self.data_list = data_list

	def __add__(self, other):
		
		"""Function to add together two matrices together
		
		Args:
			other (Matrix): Matrix instance
			
		Returns:
			Matrix: Matrix instance
		"""

		try:
			assert self.column_count == other.column_count, 'column_count values are not equal'
			assert self.row_count == other.row_count, 'row_count values are not equal'
		except AssertionError as error:
			raise
            
		result = Matrix(self.column_count, self.row_count, [[]])
		result.data_list = [[]]

		matrix_one = np.array(self.data_list)
		matrix_two = np.array(other.data_list)
        
		result.data_list = matrix_one + matrix_two
		return result
    
	def __sub__(self, other):
		""" Function to subtract two matrices from each other
		
			Args:
				other (Matrix): Matrix instance

			Returns:
				Matrix: Matrix instance
		"""

		try:
			assert self.column_count == other.column_count, 'column_count values are not equal'
			assert self.row_count == other.row_count, 'row_count values are not equal'
		except AssertionError as error:
			raise
            
		result = Matrix(self.column_count, self.row_count, [[]])
		result.data_list = [[]]

		matrix_one = np.array(self.data_list)
		matrix_two = np.array(other.data_list)
        
		result.data_list = matrix_one + matrix_two
		return result
    
	def __mul__(self, other):
		""" Function to multiply two matrices together
		
			Args:
				other (Matrix): Matrix instance

			Returns:
				Matrix: Matrix instance
		"""

		try:
			assert self.column_count == other.column_count, 'column_count values are not equal'
			assert self.row_count == other.row_count, 'row_count values are not equal'
		except AssertionError as error:
			raise
            
		result = Matrix(self.column_count, self.row_count, [[]])
		result.data_list = [[]]

		matrix_one = np.array(self.data_list)
		matrix_two = np.array(other.data_list)
        
		result.data_list = matrix_one.dot(matrix_two)
		return result
    
	def invert_matrix(self):
		"""Function to invert a matrix instance
		
		Args:
			None
		
		Returns:
			matrix: matrix instance
		"""

		return Matrix(self.column_count, self.row_count, np.linalg.inv(self.data_list))
    
	def __repr__(self):
		"""Function to output the characteristics of the Matrix instance
		
		Args:
			None
		
		Returns:
			string: characteristics of the matrix
		"""
		return "coulumn {}, row {}, data {}".format(self.column_count, self.row_count, self.data_list)
