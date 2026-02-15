import unittest


class multipleExample(unittest.TestCase):

    def setUp(self):
        print ("into set up ")
        self.num1=1
        self.num2= 2


    def test_add(self):
        print ("testing summery ")


        assert self.num1+self.num2 ==3 ,"The summery of 1 and 2 in not 3 "

    def test_minus(self):
        print ("testing diff")

        assert self.num1-self.num2 ==-1 , "The diff of 4 and 1 in not 3 "

    def test_multiple_with_error(self):

        assert self.num1*self.num2 ==5, "The result of multiple action is not as expected"