# Copyright 2019 Okera Inc. All Rights Reserved.
#
# Integration authorization tests
#

import time
import unittest

from okera import context

TEST_DB = 'auth_test_db'
TEST_ROLE = 'auth_test_role'
TEST_USER = 'auth_test_user'

class AuthorizationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Initializes one time state that is shared across test cases. This is used
            to speed up the tests. State that can be shared across (but still stable)
            should be here instead of __cleanup()."""
        super(AuthorizationTest, cls).setUpClass()

    @staticmethod
    def __cleanup(conn):
        """ Cleanups all the test state used in this test to "reset" the catalog.
            dbs can be specified to do the initialize over multiple databases.
            This can be used for tests that use multiple dbs (but makes the test
            take longer). By default, only load TEST_DB.
        """
        conn.execute_ddl("DROP ROLE IF EXISTS %s" % TEST_ROLE)
        conn.execute_ddl("CREATE ROLE %s" % TEST_ROLE)
        conn.execute_ddl("GRANT ROLE %s to GROUP %s" % (TEST_ROLE, TEST_USER))

    @staticmethod
    def __collect_grant_objects(conn):
        grants = conn.execute_ddl('SHOW GRANT ROLE %s' % (TEST_ROLE))
        result = []
        for grant in grants:
            path = ''
            if grant[1]:
                path = grant[1]
                if grant[2]:
                    path += '.' + grant[2]
                    if grant[3]:
                        path += '.' + grant[3]
                else:
                    path += '.*'
            else:
                path = '*'
            result.append(path)
        return result

    # Tests that revokes to a db does not cascade to the table or columns
    def test_revoke_db_no_cascade(self):
        ctx = context()
        with ctx.connect() as conn:
            self.__cleanup(conn)

            # Grant on db, table and column
            conn.execute_ddl(
                'GRANT SELECT ON DATABASE okera_sample TO ROLE %s' % (TEST_ROLE))
            conn.execute_ddl(
                'GRANT SELECT ON TABLE okera_sample.sample TO ROLE %s' % (TEST_ROLE))
            conn.execute_ddl(
                'GRANT SELECT(record) ON TABLE okera_sample.sample TO ROLE %s' %\
                (TEST_ROLE))

            objs = self.__collect_grant_objects(conn)
            print(objs)
            self.assertTrue('okera_sample.*' in objs)
            self.assertTrue('okera_sample.sample' in objs)
            self.assertTrue('okera_sample.sample.record' in objs)
            self.assertTrue(len(objs) == 3)

            # Revoke on db, should not cascade, this cascade can take a while so sleep
            # first. In the test setup, the refresh is 5 seconds.
            conn.execute_ddl(
                'REVOKE SELECT ON DATABASE okera_sample FROM ROLE %s' % (TEST_ROLE))
            time.sleep(7)
            objs = self.__collect_grant_objects(conn)
            print(objs)
            self.assertTrue('okera_sample.sample' in objs)
            self.assertTrue('okera_sample.sample.record' in objs)
            self.assertTrue(len(objs) == 2)

            # Revoke on table, should not cascade.
            conn.execute_ddl(
                'REVOKE SELECT ON TABLE okera_sample.sample FROM ROLE %s' % (TEST_ROLE))
            time.sleep(7)
            objs = self.__collect_grant_objects(conn)
            print(objs)
            self.assertTrue('okera_sample.sample.record' in objs)
            self.assertTrue(len(objs) == 1)

            # Revoke on column.
            conn.execute_ddl(
                'REVOKE SELECT(record) ON TABLE okera_sample.sample FROM ROLE %s' %\
                (TEST_ROLE))
            objs = self.__collect_grant_objects(conn)
            self.assertTrue(len(objs) == 0)

if __name__ == "__main__":
    unittest.main()
