def setUp(self):
    print('into set up \n')


def test_1(self):
    print("into test1 \n")


def test_2(self):
    print("into test2 \n")
    assert 5 == 5


def test_3(self):
    print("into test3 \n")
    assert 5 == 5

def tearDown(self):
    print('into tear down')