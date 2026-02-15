import unittest


class PythonOrgSearch(unittest.TestCase):


    def setUp(self):
        print(' into set up')


    def tearDown(self):
        print('teat down')


    def test_summery(self):

        num1= 1
        num2 =2
        summery = num1+num2
        assert summery ==3, "The summery of numbers is not equal to 3"
        print ("summery test end")

    def test_multiple(self):
        num1= 4
        num2= 2
        result = num1 * num2
        assert result == 8, "The result is not equal to 6"
        print ("multiple test end")
