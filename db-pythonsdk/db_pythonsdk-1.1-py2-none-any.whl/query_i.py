
class QueryI(object):
    """Query interface for building logical and filter commands 
    
    Attributes:
        filter_cmd: (string) command representing a simple filter
        logic_cmd: (string) command representing a logical operation
    """

    filter_cmd = "{}={}.{}"
    logic_cmd = "{}.{}.{}"


    def evaluate(self, logical_query=False):
        """Translates the query object into a Postgrest request string

        Attributes:
            logical_query: (bool) Whether or not the command is being 
                            evaluated as one part of a logical query. 
                            Alters command generated if true. 

        Returns:
            query_str (string) String representing a request to db
        """
        raise NotImplementedError("Query classes must implement "
                                  "evaluate(self, complex_command)")