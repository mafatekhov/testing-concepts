import unittest

from main import sum_of_many


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum_of_many(data)
        self.assertEqual(result, 6)
