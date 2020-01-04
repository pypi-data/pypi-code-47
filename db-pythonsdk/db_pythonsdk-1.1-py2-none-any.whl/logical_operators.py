from query_i import QueryI
from operators import LogicalOperator


class And(LogicalOperator):
    """Query represenation of the logical 'and' of two filters 
    
    See LogicalOperator class
    """

    def __init__(self, queries, cmd="and"):
        self.queries = queries
        self.cmd = cmd


class Or(LogicalOperator):
    """Query representation of logical 'or' of two filters
    
    See LogicalOperator class
    """

    def __init__(self, queries, cmd="or"):
        self.queries = queries
        self.cmd = cmd


class Not(LogicalOperator):
    """Query representation of logical 'not' of a logical operation or filter
    
    See LogicalOperator class
    """

    def __init__(self, query, cmd="not"):
        self.query = query
        self.cmd = cmd

    def evaluate(self, logical_query=True):       
        """Evaluates a query and generate for a logical 'not' operation.
        
        Determines if the command to be negated is a logical operation
        or a filter operation and places negation accordingly.

        Args:
            logical_query (bool) : whether the current piece being evaluated is
                                   a logical or filter query. Can be overridden
        
        Returns:
            query_str (string) : postgrest command
        """ 
        query_str = self.query.evaluate()
        simple_command = ""

        if query_str.find("(")  >= 0:
            op = "{}.{}"
            return op.format(self.cmd, query_str)
        else:
            op = query_str.split("=")
            op.insert(1, "={}.".format(self.cmd))
            return "".join(op)
            


