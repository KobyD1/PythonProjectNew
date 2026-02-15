import unittest



class pytestBefore(unittest.TestCase):

    def setUp(self):
        a=4
        a=a+a
        print ('/n')

        print ('a=',a)




    def test1(self):
        print ('into test1')


    def test2(self):
        print ('into test2')

    def test3(self):
        print ('into test3')



    def tearDown(self):
        print ('into tear down')


