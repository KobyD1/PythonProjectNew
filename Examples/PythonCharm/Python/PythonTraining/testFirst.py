def is_anagram(a_word, b_word):
    return sorted(a_word) == sorted(b_word)

def test_first_angram1():
    assert is_anagram("abc", "acb")
    assert is_anagram("silent", "listen")
    assert not is_anagram("one", "two")
    print('## Running test first1 ##')
    assert 4==4

def test_first_angram2():
    assert is_anagram("abc", "acb")
    assert is_anagram("silent", "listen")
    assert not is_anagram("one", "two")
    print('## Running test first2 ##')
    assert 'ab'=='ab'

def test_first_angram3():
    assert is_anagram("abc", "acb")
    assert is_anagram("silent", "listen")
    assert not is_anagram("one", "two")
    print('## Running test first2 - fail##')
    assert 'ab'=='abc' , "failre found at test_first_angram3 "




