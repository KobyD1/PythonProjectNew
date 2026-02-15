import PythonCharm.Python.Pytest1.utils as utils


def setUp(self):
    a = 4
    a = a + a
    print('into set up ')


def test_twice_1():
    assert utils.twice(10) == 20, f"twice(10) != 20"


def test_twice_2():
    assert utils.twice(0) == 0, f"twice(0) != 0"


def test_twice_3():
    assert utils.twice(-5) == -10, f"twice(-5) != -10"


def test_thrice_1():
    assert utils.thrice(10) == 30, f"thrice(10) != 30"


def test_thrice_2():
    assert utils.thrice(0) == 0, f"thrice(0) != 0"


def test_thrice_3():
    assert utils.thrice(-5) == -15, f"thrice(-5) != -15"
