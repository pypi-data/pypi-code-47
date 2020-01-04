
class SDKI(object):
    """SDK interface for accessing our Postgrest database

    """

    def filter(self, table_name, query, select=None, order=None):
        """Filters rows of data from the specified table based on query

        Args:
            table_name (string): Name of table to insert into
            rows (List[dict]): Data to insert into table. Keys 
                               in each dict must match. 
        
        Returns:
            tuple (bool, dict): Success of operation and status object
        
        """   
        raise NotImplementedError("SDK classes must implement "
                                "filter(self, table_name, query, select, order)") 

    def insert(self, table_name, rows):
        """Inserts rows of data into the specified table 

        Args:
            table_name (string): Name of table to insert into
            rows (List[dict]): Data to insert into table. Keys 
                               in each dict must match. 
        
        Returns:
            tuple (bool, dict): Success of operation and status object
        
        """
        raise NotImplementedError("SDK classes must implement " 
                                  "insert(table_name, rows)")

    
    def update(self, table_name, query, attributes):
        """Updates existing rows in the specified table
        
        Filters rows based on the provided query, then updates
        the filtered rows

        Args:
            table_name (string): Name of table to update
            query (Query): Query to filter rows with 
            attributes (dict): Column names mapped to values to update

        Returns:
            tuple (bool, dict): Success of operation and status object

        """
        raise NotImplementedError("SDK classes must implement "
                                  "update(table_name, query, rows)")
    
    def delete(self, table_name, query):
        """Deletes existing rows from the specified table
        
        Filters rows based on the provided query, then deletes
        the filtered rows

        Args:
            table_name (string): Name of table to update
            query (Query): Query to filter rows with 

        Returns:
            tuple (bool, dict): Success of operation and status object

        """
        raise NotImplementedError("SDK classes must implement "
                                  "delete(table_name, query)")
    
