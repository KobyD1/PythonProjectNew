




def test_pass():
      print('into test pass ')
      res = 5 - 5
      assert res == 0, 'result is not 0 as expected'

def test_failed():
    res=5-4
    assert res == 0, 'result is not 0 as expected'


def test_pass1():
    print ('into test pass1')
    res=5-5
    assert res == 2, 'result is not 0 as expected'

    assert 1 == 1, 'result is not 1 as expected'


def test_pass2():
    res=5-5
    assert res == 0, 'result is not 0 as expected'

def test_pass3():
    res=5-5
    assert res == 0, 'result is not 0 as expected'
