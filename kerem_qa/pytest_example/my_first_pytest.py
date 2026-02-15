import unittest

from Examples.PythonCharm.Python.PythonTraining.IntegerTest import result


class myFirstPytest(unittest.TestCase):

    def setUp(self):
        print ("into setup")
        self.num1= 2
        self.num2=3

    def tearDown(self):
        print ("into test end ")


    def test_summery(self):

        summery = self.num1 + self.num2


        assert summery==9,"our code did not suport summery "
        result=summery*2
        print (result)

    def test_multiple(self):
        num3=5
        num4=9
        multiple = self.num1 * self.num2
        multiple2 = num3 * num4
        assert multiple==7,"our code did not suport multiple "


