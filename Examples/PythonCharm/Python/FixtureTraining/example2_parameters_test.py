import pytest


def count(x):
    print('tested for value =', x)


# get parameters by mark.parameterize

@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*1", 6),
])
def test_eval(test_input, expected):
    print('\n start test ')
    count(5)
    assert eval(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    (8, 8),
    (6, 6),
    (5, 6),
])

def test_eval1(test_input, expected):
    print('\n noPom for equal')
    count(5)
    assert test_input == expected

# get parameters by fixture