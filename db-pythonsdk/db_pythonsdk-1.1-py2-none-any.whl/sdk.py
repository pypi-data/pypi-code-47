from filter_operators import Eq, Gt, Gte, Lt, Lte 
from logical_operators import And, Or, Not 
from sdk_i import SDKI
import requests
import json
import os


class SDK(SDKI):
    """SDK to abstract calls to our Postgrest database endpoints 

    Wraps commands performing commands on database by submitting 
    a request to an endpoint.
    
    Attributes:
        db_uri: (string) Location the database is hosted at
        auth: (JWTAuth) Jwt authentication object for database
    
    """
    def __init__(self, db_uri, auth):
        self.db_uri = db_uri
        self.auth = auth

    def get_status(self, response):
        """Creates a dict status to show if last command was successful

        Args:
            response (requests.response): Response object from last call to 
                                          Postgrest api. 
        Returns:
            dict : status

        """
        try:
            status = json.loads(response.text)

        # Catch error upon successful POST or PATCH if response.text is empty
        except ValueError as e:
            status = {}
            code = response.status_code

            if code >= 200 and code < 300:
                status['message'] = "Success"
            else:
                status['message'] = "Failure, refer to status code"

        status['status_code'] = response.status_code
        return status

    def post(self, target, data):
        """Wrapper function for requests.post

        Args:
            target (string): Request endpoint with filter argument appended
            data (List[dict]): Data to insert into table. Keys 
                               in each dict must match. 
        
        Returns:
            tuple (bool, dict): Success of operation and status object
        
        """
        response = requests.post(target, json=data, auth=self.auth)
        success = True if response else False
        status = self.get_status(response)
        return success, status

    def get(self, target):
        """Wrapper function for requests.get

        Args:
            target (string): Request endpoint with filter argument appended
            attributes (dict): Column names mapped to values to update 
        
        Returns:
            tuple (bool, dict): Success of operation and status object
        
        """
        response = requests.get(target, auth=self.auth)
        success = True if response else False
        return success, response.text

    def patch(self, target, attributes):
        """Wrapper function for requests.patch

        Args:
            target (string): Request endpoint with filter argument appended
            attributes (dict): Column names mapped to values to update 
        
        Returns:
            tuple (bool, dict): Success of operation and status object
        
        """
        response = requests.patch(target, data=attributes, auth=self.auth)
        success = True if response else False
        status = self.get_status(response)
        return success, status

    def remove(self, target):
        """Wrapper function for requests.delete

        Args:
            target (string): Request endpoint with filter argument appended
        
        Returns:
            tuple (bool, dict): Success of operation and status object
        
        """
        response = requests.delete(target, auth=self.auth)
        success = True if response else False
        status = self.get_status(response)
        return success, status

    def filter(self, table_name, query, select=None, order=None):
        """See SDKI interface
        
        """      
        query_str = "" if query is None else query.evaluate()
        table_path = os.path.join(self.db_uri, table_name)
        target = "{}?{}".format(table_path, query_str)

        if order is not None:
            order_str = "&order={}".format(",".join(order))
            target += order_str 
        
        if select is not None:
            select_str = "&select={}".format((",".join(select))) 
            target += select_str

        return self.get(target)

    def insert(self, table_name, rows):
        """See SDKI interface
        
        """
        target = os.path.join(self.db_uri, table_name)
        return self.post(target, rows)
                
    def update(self, table_name, query, attributes):
        """See SDKI interface

        """
        if query is None:
            raise ValueError("Error: 'query' argument cannot be None")
        
        if query.evaluate() == "":
            raise ValueError("Error: invalid query")
        
        table_path = os.path.join(self.db_uri, table_name)
        target = "{}?{}".format(table_path, query.evaluate())
        return self.patch(target, attributes)
    
    def delete(self, table_name, query):
        """See SDI interface

        """
        if query is None:
            raise ValueError("Error: 'query' argument cannot be None")

        if query.evaluate() == "":
            raise ValueError("Error: invalid query")
        
        table_path = os.path.join(self.db_uri, table_name)
        target = "{}?{}".format(table_path, query.evaluate())
        return self.remove(target)
