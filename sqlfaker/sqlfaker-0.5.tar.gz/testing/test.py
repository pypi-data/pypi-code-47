import unittest
import anybadge

# set temporary app path to reach files for import
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sqlfaker.database as db
import sqlfaker.table as tbl
import sqlfaker.column as clmn
from sqlfaker.database import Database


class FunctionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.my_db = Database(db_name="campusdb", dbs_type="mysql")

        # add tables
        cls.my_db.add_table(table_name="studiengang", n_rows=10)
        cls.my_db.add_table(table_name="student", n_rows=150)
        
        # add columns to studiengang table
        cls.my_db.tables["studiengang"].add_primary_key(
            column_name="studiengang_id"
        )

        cls.my_db.tables["studiengang"].add_column(
            column_name="bezeichnung",
            data_type="varchar(50)",
            data_target="name"
        )

        cls.my_db.tables["studiengang"].add_column(
            column_name="start_datum", 
            data_type="date",
            data_target="date"
        )

        # add columns to student table
        cls.my_db.tables["student"].add_primary_key(
            column_name="student_id"
        )
        
        cls.my_db.tables["student"].add_column(
            column_name="firstname",
            data_type="varchar(50)",
            data_target="first_name"
        )
        
        cls.my_db.tables["student"].add_column(
            column_name="lastname",
            data_type="varchar(50)",
            data_target="last_name"
        )
        
        cls.my_db.tables["student"].add_foreign_key(
            column_name="studiengang_id",
            target_table="studiengang",
            target_column="studiengang_id"
        )

        # generate data
        cls.my_db.generate_data()
        cls.my_db.export_sql("test_1.sql")

        # add recursive db
        cls.hr = Database(db_name="hr", dbs_type="mysql")
        cls.hr.add_table(table_name="employee", n_rows=10)

        cls.hr.tables["employee"].add_primary_key(column_name="emp_id")
        cls.hr.tables["employee"].add_column(column_name="firstname", data_type="varchar(50)", data_target="first_name")
        cls.hr.tables["employee"].add_column(column_name="lastname", data_type="varchar(50)", data_target="last_name")
        cls.hr.tables["employee"].add_foreign_key(column_name="boss_id", target_table="employee", target_column="emp_id")
        cls.hr.generate_data(recursive = True)
        cls.hr.export_sql("test_2.sql")


        # create test badge
        if os.path.exists('badges/dbsetup.svg'):
            os.remove('badges/dbsetup.svg')
            
        thresholds = {
            0.2: 'red',
            0.4: 'orange',
            0.6: 'yellow',
            1: 'green'
        }

        badge_runs = anybadge.Badge(
            'Database Setup',
            round(1, 2),
            thresholds=thresholds
        )

        badge_runs.write_badge('badges/dbsetup.svg')

    def test_get_fake_data(self):
        self.assertEqual(
            len(clmn.get_fake_data("name", n_rows=5)),
            5,
            msg="Number of generated data items was not correct."
        )
        with self.assertRaises(
            AttributeError,
            msg="Function cannot generate on this type."
        ):
            clmn.get_fake_data("hallo welt daten tag", n_rows=5)

    def test_data_generation(self):
        
        pk_column_a = self.my_db.tables["studiengang"].columns["studiengang_id"]
        pk_column_b = self.my_db.tables["student"].columns["student_id"]

        self.assertEqual(
            len(pk_column_a.data),
            10,
            msg="Length of data column is not correct."
        )

        self.assertEqual(
            len(pk_column_b.data),
            150,
            msg="Length of data column is not correct."
        )

    def test_primary_key(self):

        tab = self.my_db.tables["studiengang"]
        col = tab.columns["studiengang_id"]
        
        self.assertEqual(
            col._column_name,
            "studiengang_id",
            msg="Primary key column name not correctly set."
        )

        self.assertEqual(
            col._data_type,
            "int",
            msg="Primary key data type is not int."
        )

        self.assertEqual(
            col._ai,
            True,
            msg="Primary key column is not correctly set to auto increment"
        )

        self.assertEqual(
            col._not_null,
            True,
            msg="Primary key column should not be nullable."
        )

        self.assertEqual(
            col._n_rows,
            tab._n_rows,
            msg="Number of not rows not correctly taken from table."
        )

        self.assertEqual(
            col._data_target,
            None,
            msg="Data target of primary key should be none but is not."
        )

        self.assertTrue(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == col.data,
            msg="Primary key values are not correctly set (AI)."
        )

    def test_foreign_key(self):

        tab = self.my_db.tables["student"]
        col = tab.columns["studiengang_id"]
        data = self.my_db.tables["studiengang"].columns["studiengang_id"].data

        self.assertEqual(
            len(data),
            10,
            msg="n rows is not correct."
        )

        self.assertEqual(
            col._column_name,
            "studiengang_id",
            msg="Column name has not been correctly set."
        )

        self.assertEqual(
            col._data_type,
            "int",
            msg="Foreign key data type should be int but is not."
        )

        self.assertEqual(
            col._ai,
            False,
            msg="Foreign key is not auto increment."
        )

        self.assertEqual(
            col._not_null,
            False,
            msg="Foreign key is nullable."
        )

        self.assertEqual(
            col._n_rows,
            tab._n_rows,
            msg="n rows not correctly taken from table."
        )

        self.assertEqual(
            col._data_target,
            None,
            msg="Data target should be none."
        )
        
        for row in col.data:
            self.assertTrue(
                row in data,
                msg="Foreign key value not in set of primary key values"
            )

    def test_ddl_return(self):
        pass

    def test_dml_return(self):
        pass
        

# Define test suit
def suite():
    suite = unittest.TestSuite()

    # Add all test cases
    suite.addTest(FunctionTest('test_get_fake_data'))
    suite.addTest(FunctionTest('test_data_generation'))
    suite.addTest(FunctionTest('test_primary_key'))
    suite.addTest(FunctionTest('test_foreign_key'))
    suite.addTest(FunctionTest('test_ddl_return'))
    suite.addTest(FunctionTest('test_dml_return'))
    
    # suite.addTest(FunctionTest(''))
    
    return suite

# Run test suit
if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    test_result = runner.run(suite())

    number_of_errors = len(test_result.errors)
    number_of_failures = len(test_result.failures)
    number_of_tests = test_result.testsRun

    if os.path.exists('badges/errors.svg'):
        os.remove('badges/errors.svg')
    if os.path.exists('badges/failures.svg'):
        os.remove('badges/failures.svg')
    if os.path.exists('badges/tests.svg'):
        os.remove('badges/tests.svg')
    if os.path.exists('badges/total.svg'):
        os.remove('badges/total.svg')

    thresholds = {
        1: 'green',
        2: "orange",
        3: "red"
    }
    badge_errors = anybadge.Badge('Test errors', number_of_errors, thresholds=thresholds)
    badge_errors.write_badge('badges/errors.svg')

    thresholds = {
        1: 'green',
        2: "orange",
        3: "red"
    }
    badge_failures = anybadge.Badge('Tests failed', number_of_failures, thresholds=thresholds)
    badge_failures.write_badge('badges/failures.svg')

    thresholds = {
        0: 'green'
    }
    badge_runs = anybadge.Badge('Tests run', number_of_tests, thresholds=thresholds)
    badge_runs.write_badge('badges/tests.svg')

    thresholds = {
        0.2: 'red',
        0.4: 'orange',
        0.6: 'yellow',
        1: 'green'
    }
    badge_runs = anybadge.Badge(
        'Success ratio',
        number_of_tests/(number_of_tests+number_of_errors+number_of_failures),
        thresholds=thresholds
    )
    badge_runs.write_badge('badges/total.svg')
