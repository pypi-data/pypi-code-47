import unittest


class TestMysql(unittest.TestCase):

    def setUp(self):
        super().setUp()
        db = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': 'password',
            'db': 'arbhac'
        }
        from sakura.mysql import connect
        self.sakura = connect(**db)

    def test_get_model(self):
        Test = self.sakura.getModel('test')
        print(Test.__mappings__)
        self.assertEqual(1, 1)


class TestSqlUtil(unittest.TestCase):
    def test_field_value(self):
        from sakura.util import SqlUtil
        _field_value = {
            'a': 1,
            'b': 2,
            'c': 'c'
        }
        field_value, args = SqlUtil.get_field_value(_field_value)
        self.assertEqual(field_value, '`a` = %s, `b` = %s, `c` = %s')
        self.assertEqual(args, [1, 2, 'c'])


if __name__ == '__main__':
    unittest.main()
