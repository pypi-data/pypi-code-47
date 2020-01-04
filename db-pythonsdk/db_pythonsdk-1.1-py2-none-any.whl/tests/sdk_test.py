from db_pythonsdk.filter_operators import Eq, Gt, Gte, Lt, Lte 
from db_pythonsdk.logical_operators import And, Or, Not 
from db_pythonsdk.sdk import SDK 
import pytest



class MockTable(object):
    """Creates a simple, one row table for mock testing 
    
    Use this table representation in conjunction with mock
    request commands (Get, Post, etc) to simulate calls to 
    our actual Postgrest db.

    Attributes:
        name (string) : mock table name
        table (List[dict[str, Any]]): mock table data structure
        columns (List[string]): list of table column names

    """

    def __init__(self, name, table):
        self.name = name
        self.table = table
        self.columns = self.table[0].keys()
    
    def is_valid(self, row):
        """Check if a given row would be valid to insert 

        Verifies that all keys (column names) in the provided
        row match up with those in the table

        Args:
            row (List[dict]): New row to compare to the table
        
        Returns:
            bool: Whether or not the row is valid
        """
        if len(row.keys()) != len(self.columns):
            return False
        
        for key in row.keys():
            if key not in self.columns:
                return False
            else:
                if type(row[key]) != type(self.table[0][key]):
                    return False 
        return True

    def contains(self, row):
        """Checks if table contains row

        Compares each datapoint to those in the table and returns 
        false if a new value is found

        Args:
            row (List[dict]): New row to compare to the table
        
        Returns:
            bool: Whether or not table contains row
        """
        if row not in self.table:
            return False
        return True

    def select(self, columns):
        """Selects a subset of columns from the table

        """
        results = []
        datapoint = {}

        for col in columns:
            if col in self.columns:
                datapoint[col] = self.table[0][col]
                results.append(datapoint)
                break

        return results


class MockSDK(SDK):
    """Mocks request calls to Postgrest endpoints

    Uses the MockTable class as a fake target and mocks
    the result of GET, POST, PATCH and DELETE requests. 

    """

    FAILURE_STATUS = {"status_code":400, "message":"FAIL"}
    SUCCESS_STATUS = {"status_code":200, "message":"SUCCESS"}

    TABLE = [
                {
                    "id" : 1,
                    "name" : "judith",
                    "data" : 10, 
                },
                
                {
                    "id" : 2,
                    "name" : "judy",
                    "data" : 20, 
                },

            ]
    
    # The number of entries at initialization of the mock table
    STARTING_ENTRIES = len (TABLE)

    MT = MockTable(name="test",
                   table=TABLE)

    def get(self, target):
        """Mock get request

        Return failure if the requested table does not exist

        """
        if self.MT.name not in target:
            return target, [{}]
        print (target)

        if 'select=' in target:
            selected = target.split("select=")[1]
            selected_cols = selected.split(',')
            selected_data = self.MT.select(selected_cols)
            return target, selected_data

        return target, self.MT.table

    def post(self, target, data):
        """Mock post request 

        Return failure if data is already in database, if the dictionaries 
        in data do not all have the same key count or if there are keys 
        (a.k.a columns) that do not exist in the database already

        """
        if self.MT.name not in target:
            return False, self.FAILURE_STATUS

        for row in data:
            if self.MT.contains(row) or not self.MT.is_valid(row):
                return False, self.FAILURE_STATUS
            else:
                self.MT.table.append(row)

        return True, self.SUCCESS_STATUS

    def patch(self, target, attributes):
        """Mock patch request 

        Return failure if data is not in database, or if the attribute keys
        are not found in the database or if the table does not exist

        """
        if self.MT.name not in target:
            return False, self.FAILURE_STATUS

        if not attributes:
            return False, self.FAILURE_STATUS

        for key in attributes.keys():
            if key not in self.MT.columns:
                return False, self.FAILURE_STATUS
        
        return True, self.SUCCESS_STATUS

    def remove(self, target):
        """Mock delete request 

        Return failure if table does not exist. Removes last item 
        in the table otherwise 

        """
        if self.MT.name not in target:
            return False, self.FAILURE_STATUS
        
        self.MT.table.pop()
        return True, self.SUCCESS_STATUS


class TestSDK(object):
    """Test class for the SDK. Tests filter, insert, update 
    and delete commands on a mock database class. 

    """

    TABLE_NAME = "test"
    SDK_TESTER = MockSDK("www.example.com/", auth=None)

    def test_filter(self):
        # Test valid filter of al columns
        target, all_cols = self.SDK_TESTER.filter(self.TABLE_NAME, None)
        assert (len(all_cols[0].keys()) == len(self.SDK_TESTER.MT.columns))

        # Test valid filter of a subset of columns
        selected_cols = ['data']
        target, selected = self.SDK_TESTER.filter(self.TABLE_NAME, None, select=selected_cols)
        assert("select" in target)
        assert (len(selected) == len(selected_cols))

        # Test invalid filter of a column that does not exist in the db
        selected_cols = ['fake column']
        target, selected = self.SDK_TESTER.filter(self.TABLE_NAME, None, select=selected_cols)
        assert("select" in target)
        assert (len(selected) == 0)

        # Test valid filter of ordering
        target, ordered = self.SDK_TESTER.filter(self.TABLE_NAME, None, order=selected_cols)
        assert("order=" in target)

        # Test invalid filter of a table that does not exist. 
        target, fake_table = self.SDK_TESTER.filter("fake", None)
        assert (fake_table == [{}])
        
    def test_insert(self):
        # Test valid insert of one row with all columns existing in db
        new_entry= [{'id':3, 'name':'Vincent', 'data': 30}]
        success, status = self.SDK_TESTER.insert(self.TABLE_NAME, new_entry)
        assert (success == True)
        assert (len(self.SDK_TESTER.MT.table) == self.SDK_TESTER.STARTING_ENTRIES + 1)

        # Test invalid insert of the same row, attempting to make a duplicate insert
        duplicate_entry = new_entry
        success, status = self.SDK_TESTER.insert(self.TABLE_NAME, duplicate_entry)
        assert (success == False)
        assert (len(self.SDK_TESTER.MT.table) == self.SDK_TESTER.STARTING_ENTRIES + 1)

        # Test invalid insert of a row with mismatched columns to those in db
        false_entry = [{'id':1, 'fake stuff': ''}]
        success, status = self.SDK_TESTER.insert(self.TABLE_NAME, false_entry)
        assert (success == False)
        assert (len(self.SDK_TESTER.MT.table) == self.SDK_TESTER.STARTING_ENTRIES + 1)

        # Test invalid insert to a table that does not exist
        success, status = self.SDK_TESTER.insert("faketable", None)
        assert (success == False)

    def test_update(self):
        # Test valid update to an item that exists in db
        updates = {'name': 'something else', 'data':12}
        success, status = self.SDK_TESTER.update(self.TABLE_NAME, Eq('data', 10),  updates)
        
        # Test invalid update with column that does not exist in db
        false_updates = {'fake column': '', 'data':12}
        success, status = self.SDK_TESTER.update(self.TABLE_NAME, Eq('data', 10),  false_updates)
        assert (success == False)

        # Test invalid update to table that does not exist
        success, status = self.SDK_TESTER.update("faketable", Eq('data', 10),  None)
        assert (success == False)

        # Assert that we cannot pass an invalid query to update method
        with pytest.raises(ValueError):
            success, status = self.SDK_TESTER.update("faketable", None,  None)

    def test_delete(self):
        # Test valid delete to table 
        success, status = self.SDK_TESTER.delete(self.TABLE_NAME, Eq("id", 1))
        assert(len(self.SDK_TESTER.MT.table) == self.SDK_TESTER.STARTING_ENTRIES)
        assert (success== True)

        # Test invalid delete to table that does not exist
        success, status = self.SDK_TESTER.delete("faketable", Eq("id", 1))
        assert (success == False)
        assert(len(self.SDK_TESTER.MT.table) == self.SDK_TESTER.STARTING_ENTRIES)

        # Assert that we cannot pass an invalid query to delete method
        with pytest.raises(ValueError):
            success, status = self.SDK_TESTER.delete(self.TABLE_NAME, None)

        




        