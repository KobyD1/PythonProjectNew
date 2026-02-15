import pytest


# @pytest.fixture
# def fixture1():
#     return fixture_input + 5


@pytest.mark.parametrize(
    'input,expected_output,desc',
    [
        (10, 20, 'positive numbers'),
        (0, 0, 'zero values'),
        (-5, -10, 'negative values'),
        (-5, -10, 'negative values'),
        (2,6, 'failed values'),

    ]
)
def test_Multiple(input,expected_output,desc):
    print('start test for', desc)
    assert input * 2 == expected_output,('Assert found in case of files',input,"output",expected_output)


def tearDown(self):

    print('into tear down')# def test_by_fixture1(fixture1):
#     fixture1 = fixture1 + 3
#     assert fixture1 == 13
