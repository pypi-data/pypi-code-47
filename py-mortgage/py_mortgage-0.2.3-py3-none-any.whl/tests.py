import unittest
from mortgage import Mortgage

new_mortgage_io_false = Mortgage(rate = .04/12, loan = 400000, term = 360, interest_only=False)

class MyFirstTests(unittest.TestCase):
    def test_total_12_pmts_equals_1_pmt_times_12(self):
        self.assertEqual(new_mortgage_io_false.total_pmts(12), new_mortgage_io_false.get_pmt()*12)

    def test_cumulative_interest_pmt_of_new_mortgage_io_false(self):
        self.assertAlmostEqual(new_mortgage_io_false.get_pmt(), 1910, 0)

    def test_total_pmts_equals_sum_interest_and_principal(self):
        for i in range(1, 300, 12):
            sum_interest_and_principal = new_mortgage_io_false.cumulative_interest_pmt(i) + new_mortgage_io_false.cumulative_principal_pmt(i) 
            total_pmts = new_mortgage_io_false.total_pmts(i)
            self.assertEqual(sum_interest_and_principal, total_pmts)


if __name__ == '__main__':
    unittest.main()
