import pytest


@pytest.fixture()
def my_fixture():
    print("\n I'm the fixture - setUp")



@pytest.fixture()
def fixture_1():
    print("\n I'm the fixture - fixture1")


def test_1(fixture_1):
    print("I'm the first test")


def test_2(my_fixture):
    print("I'm the second test")


def test_3(my_fixture):
    print("I'm the third test")


def test_4():
    print("I'm  test without fixture")
    assert 4 == 4


@pytest.mark.skip

def test_5():
    print("I'm  test No5 ")
