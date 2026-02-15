import pytest


def string_analyze(pattern):
    max_loops = int(len(pattern) / 2)
    for position_begin in range(max_loops):
        l1 = len(pattern) - position_begin - 1
        s1 = pattern[l1]
        s2 = pattern[position_begin]
        if (s1 == s2):
            print('match found')
        else:
            assert False ,'test failed'
            break

@pytest.mark.parametrize("pattern_to_test", [
    ("aabbaa"),
    ("aabbcecbbaa"),
    ("asersa"),
    ("adsersra"),
    ("asbfbsa"),

])
def test_string(pattern_to_test):
    string_to_test = "abccba"
    string_analyze(pattern_to_test)


def test_string_failure():
    string_to_test = "awbccba"
    string_analyze(string_to_test)

