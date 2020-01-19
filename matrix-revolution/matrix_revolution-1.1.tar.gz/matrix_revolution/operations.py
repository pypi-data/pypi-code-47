from .matrix_format import Matrix
import numpy as np

class Operations(Matrix):
    """
    Performs simple addition and dot product on the two input arrays/matrices.
    
    """
    def __init__(self, matrix1, matrix2):
        Matrix.__init__(self, matrix1, matrix2)
        self.A, self.B = Matrix.convert_type(self)

        
    def add_operation(self):
        """
        Adds two numpy arrays to produce a scalar sum.
        """
        return np.sum([self.A,self.B])
    
    
    def dot_operation(self):
        """
        Dot product on two numpy arrays.
        """
        return self.A.dot(self.B)
        