

class PytestExampleTest():

    def test_summery(self):
        print("test_login")
        a= 2
        b= 3
        assert a+b==5 ,"The summery of A and B is not as expected "

    def test_multiple(self):
        print ("test_login_incorrect")
        a = 2
        b = 3
        assert a * b == 5, "The multiple  of A and B is not as expected "