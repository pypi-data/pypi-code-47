from query_i import QueryI
from operators import FilterOperator


class Eq(FilterOperator):
    """Query represenation of the 'equals' horizontal filter 
    
    See FilterOperator class
    """

    def __init__(self, col, arg, cmd="eq"):
        self.cmd = cmd
        self.col = col
        self.arg = arg
        

class Gt(FilterOperator):
    """Query represenation of the 'greater than' horizontal filter 
    
    See FilterOperator class
    """

    def __init__(self, col, arg, cmd="gt"):
        self.cmd = cmd
        self.col = col
        self.arg = arg
        

class Gte(FilterOperator):
    """Query represenation of the 'greater than or equal to' horizontal filter 
    
    See FilterOperator class
    """

    def __init__(self, col, arg, cmd="gte"):
        self.cmd = cmd
        self.col = col
        self.arg = arg


class Lt(FilterOperator):
    """Query represenation of the 'lesser than' horizontal filter 
    
    See FilterOperator class
    """

    def __init__(self, col, arg, cmd="lt"):
        self.cmd = cmd
        self.col = col
        self.arg = arg


class Lte(FilterOperator):
    """Query represenation of the 'lesser than or equal to' horizontal filter 
    
    See FilterOperator class
    """

    def __init__(self, col, arg, cmd="lte"):
        self.cmd = cmd
        self.col = col
        self.arg = arg

