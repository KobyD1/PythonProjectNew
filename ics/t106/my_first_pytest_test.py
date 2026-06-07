import unittest


class myFirstPytestTest(unittest.TestCase):

    def test_summery_numbers(self):

        num1=4
        num2=6
        summery = num1+num2
        assert summery ==10,"summery numbers should be 10"

    def test_failure_example(self):
        num1=4
        num2=6
        diff = num2-num1
        assert diff ==3,"the diff  numbers should be 3"