import pytest


def contains_digit_7(n: int) -> bool:
    """Return True if digit '7' appears in the decimal representation of integer n."""
    return '7' in str(abs(int(n)))


@pytest.mark.parametrize("value,expected", [
    (7, True),
    (17, True),
    (70, True),
    (123, False),
    (-271, True),
    (0, False),
    (777, True),
])
def test_contains_digit_7(value, expected):
    assert contains_digit_7(value) is expected
