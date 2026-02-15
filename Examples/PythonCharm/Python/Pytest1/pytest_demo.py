def setUp(self):
    a = 4
    print('into set up , before each test')


def test_pass():
    print('into test pass ')
    res=5-5
    assert res==0,'result is is not 0 as expected '

def test_fail():
    print('\ninto test fail \n')

    res=5-5
    print('after math action')
    assert res==1,'Results is not 1 as expected'


