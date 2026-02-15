import unittest
import pytest
from PythonCharm.Python.FixtureTraining.uttils import utils_pytest

demo_utils = utils_pytest()
class PythonOrgSearch(unittest.TestCase):


    # def setUp(self):
    #     print('\n set up')


    def test1(self):
         print ('into test1')
         demo_utils.check_equals(2,2)

    def test2(self):
         print ('into test1')
         demo_utils.check_equals(3,2)

    @pytest.mark.parametrize("test_input,expected", [
        (8, 8),
        (4, 6),
        (6, 6),
    ])

    def test_eval1(test_input, expected):
        print('\n noPom for equal')
        assert test_input == expected

    def test_parmeter(self,x = 1):
        x = x *10
        y = int('20')
        y = y +30
        print('xxxx='+str(x))