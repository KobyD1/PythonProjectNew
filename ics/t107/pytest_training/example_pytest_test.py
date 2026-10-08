import unittest


class examplePytestTest(unittest.TestCase):

    def test_1_calc_multiple(self):
        num1 = 4
        num2 = 5
        multiple = num1 * num2
        assert multiple== 20, f"Expected {multiple} to be 20"