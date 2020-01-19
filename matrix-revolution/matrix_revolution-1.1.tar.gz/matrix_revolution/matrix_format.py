import numpy as np

class Matrix:
    """
    Converts the input matrices/arrays into numpy arrays.
    Args:
        matrix1(list): first input matrix
        matrix2(list): second input matrix
    Returns:
        A(numpy array)
        B(numpy array)
    """
    def __init__(self, matrix1, matrix2):
        self.A = matrix1
        self.B = matrix2
        
    
    def convert_type(self):
        A = np.array(self.A)
        B = np.array(self.B)
        self.A = A
        self.B = B
        
        return A, B
        
        