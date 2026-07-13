class TestMyFirstPytest():


    def test_add_numbers(self):
        num1=2
        num2=3
        assert num1+num2 == 5 , "Summery of num1 and num2 should be equal to 5"

    def test_multiple_numbers(self):
        num1=2
        num2=3
        assert num1*num2 == 6 , "Multip[le of num1 and num2 should be equal to 6"

    def test_diff_numbers(self):
        num1=2
        num2=3
        assert num1-num2 == 6 , "Diff of num1 and num2 should be equal to 6"





