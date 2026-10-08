import unittest


class examplePytestTest(unittest.TestCase):

    def test_1_calc_multiple(self):
        num1 = 4
        num2 = 5
        multiple = num1 * num2
        assert multiple== 20, f"Expected {multiple} to be 20"

    def test_2_calc_add(self):

        num1 = 4
        num2 = 5
        add = num1 + num2
        assert add == 9, f"Expected {add} to be 9"

    def test_3_calc_diff(self):
        num1 = 4
        num2 = 5
        diff = num1 - num2
        assert diff == -1, f"Expected {diff} to be -1"

    def test_error_example(self):
        num1 = 4
        num2 = 5
        diff = num1 - num2
        assert diff == 3, f"Expected {diff} to be -1"