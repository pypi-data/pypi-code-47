from query_i import QueryI


class FilterOperator(QueryI):
    """Query represenation of the horizontal filter specified by 'cmd' 

    Wraps a query filtering rows of a database by adding a condition 
    to a column.
    
    Attributes:
        col: (string) column name to conduct filtering on
        arg: (string) value to compare as a threshold for filtering
        cmd: (string) name of filter command this class implements
    """

    def __init__(self, col, arg, cmd):
        self.col = col
        self.arg = arg
        self.cmd = cmd
    
    def evaluate(self, logical_query=False):
        """Evaluates a filter query

        Returns string form of a query performing a filter operation
        on rows in postgrest format

        Args:
            logical_query (bool) : whether the current piece being evaluated is
                                   a logical or filter query. Can be overridden

        Returns: 
            op (string) : final postgrest command 
        """ 
        if logical_query:
            return self.logic_cmd.format(self.col, self.cmd, self.arg)
        else:
            return self.filter_cmd.format(self.col, self.cmd, self.arg)


class LogicalOperator(QueryI):
    """Query represenation of a logical operation represented by 'cmd'
    
    Wraps a logical operation to combine two filtering operations acting 
    upon rows in a database. 
    
    Attributes:
        queries: (List[Query]) List of query objects to operate on
        cmd: (string) name of command this class implements
    """

    def __init__(self, queries, cmd):
        self.queries = queries
        self.cmd = cmd

    def handle_nested(self, query_str):
        """Handles nested queries

        Prunes nested logical statements to match postgrest requirement
        - nested logical statements need to omit the '=' character

        Args:
            query_str (string) : represents unpruned string query.
        
        Returns:
            query_str (string) : postgrest command
        """
        if "(" in query_str:
            return "".join(query_str.split("="))
        else:
            return query_str

    def evaluate(self, logical_query=True):
        """Evaluates a logical query

        Returns string form of a query performing a logical operation
        on rows in postgrest format

        Args:
            logical_query (bool) : whether the current piece being evaluated is
                                   a logical or filter query. Can be overridden

        Returns: 
            op (string) : final postgrest command 
        """ 
        conditions = ""
        
        for index, query in enumerate(self.queries):
            query_str = query.evaluate(logical_query=True)
            query_str = self.handle_nested(query_str)
            conditions += ", " + query_str if index !=0 else query_str
        
        op = "{}=({})".format(self.cmd, conditions)
        return op
        
