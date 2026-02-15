import pytest

# cause to run the fixture once , per session or module
@pytest.fixture()
def my_fixture():
     print("\n I'm the fixture - setUp per session")
     print("I'm the fixture - tearDown per session")

@pytest.fixture()
def fixture_1(x=0):
    x==x+1
    print("\n I'm the fixture - fixture per module , only once will run ")
    print("\n x value = ",x)


# @pytest.fixture(scope="function")
# def fixture_1(moduleCntr=0):
#     moduleCntr+1
#     print("\n I'm the fixture - fixture1 per function ")
#     print('module Counter',moduleCntr  )


def test_1(fixture_1):
     print("\n I'm the  test1")

def test_2(my_fixture):
    print("\n I'm the  test2")

def test_3(my_fixture):
    print("\n I'm the  test3")

def test_4(fixture_1):
    print("\n I'm the  test4")

def test_5(fixture_1):
    print("\n I'm the  test5")
