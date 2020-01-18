import unittest

import liebres as lb


class SQLiteDataFrameTestCase(unittest.TestCase):

    def test_columns(self):
        observed = lb.DataFrame({
            'a': [1, 2, 3],
            'b': [3, 2, 1],
        })
        self.assertEqual(observed.columns, {'a': int, 'b': int})

    def test_len(self):
        observed = lb.DataFrame({
            'a': [1, 2, 3],
            'b': [3, 2, 1],
        })
        self.assertEqual(len(observed), 3)

    def test_shape(self):
        observed = lb.DataFrame({
            'a': [1, 2, 3],
            'b': [3, 2, 1],
        })
        self.assertEqual(observed.shape, (len(observed), len(observed.columns)))

    def test_head(self):
        n = 10
        data = {'a': list(range(100)), 'b': list(range(100, 200))}
        df = lb.DataFrame(data)

        observed_df = df.head(n=n)
        self.assertIsInstance(observed_df, lb.DataFrame)

        observed_data = observed_df.to_dict('list')
        self.assertEqual(len(observed_data), len(data))
        for key in observed_data:
            self.assertEqual(len(observed_data[key]), n)

    def test_sum(self):
        data = {'a': list(range(100)), 'b': list(range(100, 200))}
        df = lb.DataFrame(data)

        observed_data = df.sum()

        self.assertEqual(len(observed_data), len(data))
        for key in observed_data:
            observed_cell = observed_data[key]
            expected_cell = sum(data[key])
            self.assertEqual(observed_cell, expected_cell)

    def test_add(self):
        other = 10
        data = {'a': list(range(10)), 'b': list(range(10, 20))}
        df = lb.DataFrame(data)

        observed_df = df.add(other)
        self.assertIsInstance(observed_df, lb.DataFrame)
        observed_data = observed_df.to_dict('list')
        self.assertEqual(len(observed_data), len(data))
        for key in observed_data:
            for observed_cell, expected_cell in zip(observed_data[key], map(lambda x: x + other, data[key])):
                self.assertEqual(observed_cell, expected_cell)

    def test_inline_add(self):
        other = 10
        data = {'a': list(range(10)), 'b': list(range(10, 20))}
        observed = lb.DataFrame(data)
        self.assertEqual((observed + other).to_dict(), observed.add(other).to_dict())

    def test_subtract(self):
        other = 10
        data = {'a': list(range(10)), 'b': list(range(10, 20))}
        df = lb.DataFrame(data)

        observed_df = df.subtract(other)
        self.assertIsInstance(observed_df, lb.DataFrame)
        observed_data = observed_df.to_dict('list')
        self.assertEqual(len(observed_data), len(data))
        for key in observed_data:
            for observed_cell, expected_cell in zip(observed_data[key], map(lambda x: x - other, data[key])):
                self.assertEqual(observed_cell, expected_cell)

    def test_inline_subtract(self):
        other = 10
        data = {'a': list(range(10)), 'b': list(range(10, 20))}
        observed = lb.DataFrame(data)
        self.assertEqual((observed - other).to_dict(), observed.subtract(other).to_dict())

    def test_invalid_subtract(self):
        other = 10
        data = {'a': list(map(str, range(10))), 'b': list(range(10, 20))}
        observed = lb.DataFrame(data)
        self.assertRaises(TypeError, lambda: observed - other)

    def test_scalar_get_item(self):
        expected = lb.DataFrame({
            'a': list(map(str, range(10))),
        })
        data = {'a': list(map(str, range(10))), 'b': list(range(10, 20))}
        observed_df = lb.DataFrame(data)
        observed = observed_df['a']
        self.assertTrue(observed.equals(expected))

    def test_list_get_item(self):
        expected = lb.DataFrame({
            'a': list(map(str, range(10))),
            'c': list(range(20, 30))
        })
        observed_df = lb.DataFrame({
            'a': list(map(str, range(10))),
            'b': list(range(10, 20)),
            'c': list(range(20, 30))
        })
        observed = observed_df[['a', 'c']]
        self.assertTrue(observed.equals(expected))

    def test_invalid_get_item(self):
        data = {'a': list(map(str, range(10))), 'b': list(range(10, 20))}
        observed_df = lb.DataFrame(data)
        self.assertRaises(KeyError, lambda: observed_df[1])

    def test_equal_true(self):
        a = lb.DataFrame({
            'a': list(range(10)),
            'b': list(range(10, 20)),
        })
        b = lb.DataFrame({
            'a': list(range(10)),
            'b': list(range(10, 20)),
        })
        self.assertTrue(a.equals(b))
        self.assertTrue(b.equals(a))

    def test_equal_false(self):
        a = lb.DataFrame({
            'a': list(range(10)),
            'b': list(range(10, 20)),
        })
        b = lb.DataFrame({
            'a': list(range(10)),
            'b': list(range(20, 30)),
        })
        self.assertFalse(a.equals(b))
        self.assertFalse(b.equals(a))

    def test_scalar_eq(self):
        expected = lb.DataFrame({
            'a': [False, False, True],
            'b': [True, False, False],
        })
        observed_df = lb.DataFrame({
            'a': [1, 2, 3],
            'b': [3, 2, 1],
        })
        observed = observed_df.eq(3)
        self.assertTrue(observed, expected)


if __name__ == '__main__':
    unittest.main()
